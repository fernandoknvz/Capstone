"""Verificación de integridad y consistencia de los DOCX de Fase 3 (solo lectura)."""
import re, sys, zipfile
from pathlib import Path
import docx
from docx.table import Table
from docx.text.paragraph import Paragraph

OUT = Path(__file__).resolve().parents[1] / "Fase 3" / "Entregables"
SECRETS = [r"AIza[0-9A-Za-z_\-]{20,}", r"sk-[A-Za-z0-9]{20,}", r"eyJ[A-Za-z0-9_\-]{15,}\.[A-Za-z0-9_\-]{10,}", r"Bearer\s+[A-Za-z0-9._\-]{20,}",
           r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}", r"[A-Za-z]:[\\/]Users[\\/]", r"[\w.+-]+@[\w-]+\.[\w.]+", r"(?i)xi-api-key", r"-----BEGIN"]
STALE = ["no hay integración continua", "PR #16 abierto", "PR #16 en revisión", "en la rama del PR #16", "200 pruebas de Python y 91", "(rama del PR #16)", "hoy corresponde la semana 12"]


def text_of(d):
    parts = []
    for el in d.element.body.iterchildren():
        if el.tag.endswith('}p'):
            parts.append(Paragraph(el, d).text)
        elif el.tag.endswith('}tbl'):
            t = Table(el, d)
            for r in t.rows:
                seen = []
                for c in r.cells:
                    if c.text not in seen: seen.append(c.text)
                parts.append(" | ".join(seen))
    for s in d.sections:
        for p in s.footer.paragraphs: parts.append(p.text)
    return "\n".join(parts)


ok = True
for f in sorted(OUT.glob("*_Fase3.docx")):
    z = zipfile.ZipFile(f)
    bad = z.testzip()
    d = docx.Document(str(f))
    t = text_of(d)
    figs = [int(m) for m in re.findall(r"(?m)^Figura (\d+)\.", t)]
    media = len([n for n in z.namelist() if n.startswith("word/media/")])
    inl = len(d.inline_shapes)
    hits = {p: re.findall(p, t) for p in SECRETS}
    hits = {k: v[:3] for k, v in hits.items() if v}
    stale = [s for s in STALE if s in t]
    seq_ok = figs == sorted(figs) and len(set(figs)) == len(figs)
    heads = [p.text for p in d.paragraphs if p.style.name.startswith("Heading 1")]
    nums = [int(m.group(1)) for h in heads if (m := re.match(r"(\d+)\. ", h))]
    num_ok = nums == sorted(nums) and all(b - a == 1 for a, b in zip(nums, nums[1:]))
    print(f"{f.name}\n  zip={'OK' if bad is None else bad} · párrafos={len(d.paragraphs)} · tablas={len(d.tables)} · imágenes={inl}/{media} · figuras={figs} secuencia={'OK' if seq_ok else 'REVISAR'}"
          f"\n  numeración de secciones: {nums} {'OK' if num_ok else 'REVISAR'}\n  secretos/PII: {hits or 'ninguno'} · texto obsoleto: {stale or 'ninguno'}")
    if bad or hits or not seq_ok or not num_ok:
        ok = False
print("RESULTADO:", "OK" if ok else "REVISAR")
