"""Utilidades para actualizar los DOCX históricos D01-D06 sin perder su formato.

Se parte de una COPIA del documento original (nunca se modifica el original):
se reemplaza texto de forma estricta, se agregan filas/tablas/figuras con el mismo
formato del documento y se insertan secciones nuevas en posiciones concretas.
"""
from __future__ import annotations

import copy
import re
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from docx.table import Table
from docx.text.paragraph import Paragraph

TAG_COLORS = {
    "CONFIRMADO": "1B7F4C",
    "PENDIENTE": "B3261E",
    "PENDIENTE DE VALIDACIÓN": "B3261E",
    "PROPUESTA": "1F5FA8",
    "INFERENCIA": "9A6700",
    "REPORTADO POR EL EQUIPO": "555555",
}
TAG_RE = re.compile(r"\[(CONFIRMADO|PENDIENTE DE VALIDACIÓN|PENDIENTE|PROPUESTA|INFERENCIA|REPORTADO POR EL EQUIPO)([^\]]*)\]")
HEADER_FILL = "0A7D69"
TOTAL_DXA = 9070


def _txt(el) -> str:
    return "".join(t.text or "" for t in el.iter(qn("w:t")))


class Doc:
    def __init__(self, src: Path):
        self.doc = Document(str(src))
        self.body = self.doc.element.body
        self.cursor = None
        # Plantillas clonables (se capturan del propio documento)
        self.tpl = {}

    # ---------------------------------------------------------------- búsqueda
    def par(self, startswith: str, nth: int = 0) -> Paragraph:
        found = [p for p in self.doc.paragraphs if p.text.strip().startswith(startswith)]
        if len(found) <= nth:
            raise KeyError(f"Párrafo no encontrado: {startswith!r}")
        return found[nth]

    def table(self, first_cell: str, nth: int = 0) -> Table:
        found = [t for t in self.doc.tables if t.rows and t.rows[0].cells[0].text.strip().startswith(first_cell)]
        if len(found) <= nth:
            raise KeyError(f"Tabla no encontrada: {first_cell!r}")
        return found[nth]

    # ---------------------------------------------------------------- reemplazos
    def rep(self, old: str, new: str, scope=None, count_min: int = 1) -> int:
        """Reemplaza `old` por `new` dentro de UN run (estricto). Aplica a todo el documento."""
        n = 0
        for p in self._all_paragraphs(scope):
            for r in p.runs:
                if old in r.text:
                    r.text = r.text.replace(old, new)
                    n += 1
        if n < count_min:
            raise KeyError(f"Texto no encontrado en un único run: {old!r}")
        return n

    def _all_paragraphs(self, scope=None):
        if scope is None:
            for p in self.doc.paragraphs:
                yield p
            for t in self.doc.tables:
                for row in t.rows:
                    seen = set()
                    for c in row.cells:
                        if id(c._tc) in seen:
                            continue
                        seen.add(id(c._tc))
                        for p in c.paragraphs:
                            yield p
        elif isinstance(scope, Table):
            for row in scope.rows:
                seen = set()
                for c in row.cells:
                    if id(c._tc) in seen:
                        continue
                    seen.add(id(c._tc))
                    for p in c.paragraphs:
                        yield p
        else:
            yield scope

    def set_par(self, p: Paragraph, text: str) -> None:
        """Reescribe un párrafo conservando el formato del primer run 'normal' y coloreando las etiquetas."""
        runs = p.runs
        base = None
        for r in runs:
            if not TAG_RE.fullmatch(r.text.strip() or "x"):
                base = r
                break
        base_rpr = copy.deepcopy(base._r.rPr) if base is not None and base._r.rPr is not None else None
        for r in runs:
            r._r.getparent().remove(r._r)
        self._fill(p, text, base_rpr)

    def _fill(self, p: Paragraph, text: str, base_rpr=None, size_pt: float | None = None) -> None:
        pos = 0
        for m in TAG_RE.finditer(text):
            if m.start() > pos:
                self._run(p, text[pos:m.start()], base_rpr, size_pt)
            tag = m.group(1)
            r = p.add_run(m.group(0))
            r.bold = True
            r.font.color.rgb = RGBColor.from_string(TAG_COLORS[tag])
            if size_pt:
                r.font.size = Pt(size_pt)
            pos = m.end()
        if pos < len(text):
            self._run(p, text[pos:], base_rpr, size_pt)

    def _run(self, p, text, base_rpr, size_pt):
        r = p.add_run(text)
        if base_rpr is not None:
            old = r._r.rPr
            if old is not None:
                r._r.remove(old)
            r._r.insert(0, copy.deepcopy(base_rpr))
        if size_pt:
            r.font.size = Pt(size_pt)
        return r

    # ---------------------------------------------------------------- celdas y filas
    def cell_set(self, table: Table, row_key: str, col: int, text: str, key_col: int = 0) -> None:
        for row in table.rows[1:]:
            if row.cells[key_col].text.strip().startswith(row_key):
                self._set_cell(row.cells[col], text)
                return
        raise KeyError(f"Fila no encontrada: {row_key!r}")

    def _set_cell(self, cell, text: str) -> None:
        p = cell.paragraphs[0]
        base_size = None
        for r in p.runs:
            if r.font.size:
                base_size = r.font.size.pt
                break
        for extra in cell.paragraphs[1:]:
            extra._p.getparent().remove(extra._p)
        for r in list(p.runs):
            r._r.getparent().remove(r._r)
        self._fill(p, text, None, base_size or 9)
        for r in p.runs:
            if r.font.size is None:
                r.font.size = Pt(9)
            if not TAG_RE.fullmatch(r.text.strip() or "x"):
                r.bold = False

    def add_row(self, table: Table, values: list[str]) -> None:
        last = table.rows[-1]._tr
        new = copy.deepcopy(last)
        last.addnext(new)
        from docx.table import _Row
        row = _Row(new, table)
        for cell, v in zip(row.cells, values):
            self._set_cell(cell, v)

    # ---------------------------------------------------------------- cursor / inserción
    def at(self, element_or_par) -> "Doc":
        self.cursor = element_or_par._p if hasattr(element_or_par, "_p") else (element_or_par._tbl if hasattr(element_or_par, "_tbl") else element_or_par)
        return self

    def at_end(self) -> "Doc":
        children = [c for c in self.body if c.tag != qn("w:sectPr")]
        self.cursor = children[-1]
        return self

    def _place(self, el):
        self.cursor.addnext(el)
        self.cursor = el
        return el

    def capture_templates(self, h1: str, h2: str | None, body_start: str, bullet_start: str, caption_start: str, step_start: str | None = None):
        def clone(prefix):
            return copy.deepcopy(self.par(prefix)._p)
        self.tpl["h1"] = clone(h1)
        if h2:
            self.tpl["h2"] = clone(h2)
        self.tpl["body"] = clone(body_start)
        self.tpl["bullet"] = clone(bullet_start)
        self.tpl["caption"] = clone(caption_start)
        if step_start:
            self.tpl["step"] = clone(step_start)

    def _from_tpl(self, key: str, text: str, size_pt=None) -> Paragraph:
        el = copy.deepcopy(self.tpl[key])
        p = Paragraph(el, self.doc._body)
        base = None
        for r in p.runs:
            if not r.bold or key in ("h1", "h2", "caption"):
                base = r
                break
        if key == "body":
            for r in p.runs:
                if r.text.strip() and not TAG_RE.fullmatch(r.text.strip()):
                    base = r
        base_rpr = copy.deepcopy(base._r.rPr) if base is not None and base._r.rPr is not None else None
        for r in list(p.runs):
            r._r.getparent().remove(r._r)
        for br in el.findall(qn("w:bookmarkStart")) + el.findall(qn("w:bookmarkEnd")):
            el.remove(br)
        self._fill(p, text, base_rpr, size_pt)
        self._place(el)
        return p

    def h1(self, text): return self._from_tpl("h1", text)
    def h2(self, text): return self._from_tpl("h2", text)
    def para(self, text): return self._from_tpl("body", text)
    def bullet(self, text): return self._from_tpl("bullet", text)
    def caption(self, text): return self._from_tpl("caption", text)

    def step(self, num: str, text: str):
        el = copy.deepcopy(self.tpl["step"])
        p = Paragraph(el, self.doc._body)
        first, rest = p.runs[0], None
        rest_rpr = copy.deepcopy(p.runs[1]._r.rPr) if len(p.runs) > 1 and p.runs[1]._r.rPr is not None else None
        first_rpr = copy.deepcopy(first._r.rPr)
        for r in list(p.runs):
            r._r.getparent().remove(r._r)
        r = p.add_run(num + " ")
        if first_rpr is not None:
            r._r.insert(0, first_rpr)
        self._fill(p, text, rest_rpr)
        self._place(el)
        return p

    def spacer(self):
        p = self.doc.add_paragraph()
        self._place(p._p)

    def figure(self, image: Path, caption: str, width_cm: float = 16.2):
        p = self.doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.keep_with_next = True
        p.add_run().add_picture(str(image), width=Cm(width_cm))
        self._place(p._p)
        self.caption(caption)

    def table_new(self, header: list[str], rows: list[list[str]], widths: list[float]):
        """Tabla con el mismo aspecto que las del documento (cabecera verde, 9 pt)."""
        total = sum(widths)
        dxa = [int(TOTAL_DXA * w / total) for w in widths]
        t = self.doc.add_table(rows=1 + len(rows), cols=len(header))
        tbl = t._tbl
        tbl_pr = tbl.tblPr
        for child in list(tbl_pr):
            tbl_pr.remove(child)
        for xml in (
            '<w:tblStyle xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" w:val="TableGrid"/>',
            '<w:tblW xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" w:type="auto" w:w="0"/>',
            '<w:jc xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" w:val="center"/>',
            '<w:tblLayout xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" w:type="fixed"/>',
            '<w:tblLook xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" w:firstColumn="1" w:firstRow="1" w:lastColumn="0" w:lastRow="0" w:noHBand="0" w:noVBand="1" w:val="04A0"/>',
            '<w:tblCellMar xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:top w:w="60" w:type="dxa"/><w:left w:w="90" w:type="dxa"/><w:bottom w:w="60" w:type="dxa"/><w:right w:w="90" w:type="dxa"/></w:tblCellMar>',
        ):
            from docx.oxml import parse_xml
            tbl_pr.append(parse_xml(xml))
        grid = tbl.tblGrid
        for gc, w in zip(grid.findall(qn("w:gridCol")), dxa):
            gc.set(qn("w:w"), str(w))
        for ri, row in enumerate(t.rows):
            tr = row._tr
            trpr = tr.get_or_add_trPr()
            if ri == 0:
                trpr.append(OxmlElement("w:tblHeader"))
            else:
                trpr.append(OxmlElement("w:cantSplit"))
            for ci, cell in enumerate(row.cells):
                tcpr = cell._tc.get_or_add_tcPr()
                for old in tcpr.findall(qn("w:tcW")):
                    tcpr.remove(old)
                tcw = OxmlElement("w:tcW")
                tcw.set(qn("w:type"), "dxa")
                tcw.set(qn("w:w"), str(dxa[ci]))
                tcpr.insert(0, tcw)
                p = cell.paragraphs[0]
                p.paragraph_format.space_after = Pt(1 if ri else 0)
                if ri <= 1:
                    p.paragraph_format.keep_with_next = True
                if ri == 0:
                    shd = OxmlElement("w:shd")
                    shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), HEADER_FILL)
                    tcpr.append(shd)
                    r = p.add_run(header[ci]); r.bold = True; r.font.size = Pt(9); r.font.color.rgb = RGBColor(255, 255, 255)
                else:
                    self._fill(p, rows[ri - 1][ci], None, 9)
                    for r in p.runs:
                        if not TAG_RE.fullmatch(r.text.strip() or "x"):
                            r.bold = False
        self._place(tbl)
        sp = self.doc.add_paragraph()
        self._place(sp._p)
        return t

    # ---------------------------------------------------------------- portada
    def retitle_cover(self, date_text: str, code_text: str, status_text: str):
        self.set_par(self.par("30 de octubre de 2026"), date_text)
        self.set_par(self.par("Código del documento:"), code_text)
        self.set_par(self.par("Estado: Borrador"), status_text)

    def save(self, out: Path):
        out.parent.mkdir(parents=True, exist_ok=True)
        self.doc.save(str(out))
