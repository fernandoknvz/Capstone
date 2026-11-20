"""Archiva una versión sanitizada del informe DART-14-2.5 (E2E del 19-oct-2026).

Entrada (fuera de Git, solo lectura): el DOCX original. Salida: carpeta de evidencias con
- el texto del informe extraído sin cambios de contenido (Markdown),
- la captura de Agent Console recortada al área de la consola (se excluyen pestañas, URL con
  identificadores de proyecto, favoritos, avatar y el panel lateral con el nombre de la cuenta),
- manifiesto SHA-256.
Uso: py -I archive_dart25.py <ruta_docx_original>
"""
import hashlib, io, sys, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET
from PIL import Image

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
BOX = (310, 125, 1345, 545)  # (izq, sup, der, inf) sobre la captura original de 1361x710
OUT = Path(__file__).resolve().parents[1] / "Fase 3" / "07_Evidencias" / "DART-14-2.5_E2E-2026-10-19"
PIPE = chr(92) + "|"


def txt(e):
    return "".join(t.text or "" for t in e.iter(W + "t"))


def paragraphs(xml: bytes):
    body = ET.fromstring(xml).find(W + "body")
    for c in body:
        if c.tag == W + "p":
            t = txt(c)
            if t.strip():
                yield ("p", t)
        elif c.tag == W + "tbl":
            for tr in c.iter(W + "tr"):
                cells = [" / ".join(txt(p) for p in tc.iter(W + "p") if txt(p).strip()) for tc in tr.findall(W + "tc")]
                yield ("r", cells)


def main(src: Path):
    OUT.mkdir(parents=True, exist_ok=True)
    z = zipfile.ZipFile(src)
    lines, in_table = [], False
    for kind, v in paragraphs(z.read("word/document.xml")):
        if kind == "r":
            if not in_table:
                lines.append("")
                in_table = True
            lines.append("| " + " | ".join(c.replace("|", PIPE) for c in v) + " |")
        else:
            if in_table:
                lines.append("")
                in_table = False
            lines.append(v)
            lines.append("")
    body = "\n".join(lines)
    NL = chr(10)
    intro = ("# Informe DART-14-2.5 (transcripción sanitizada)" + NL*2 +
             "> Transcripción textual del informe original del 19-oct-2026; ver README.md para procedencia y transformaciones. "
             "La Figura 1 se reemplazó por la captura recortada `captura_agent_console_recortada.png`." + NL*2)
    with open(OUT / "DART-14-2.5_informe_sanitizado.md", "w", encoding="utf-8", newline=NL) as fh:
        fh.write(intro + body + NL)
    img = Image.open(io.BytesIO(z.read("word/media/image1.png"))).convert("RGB")
    img.crop(BOX).save(OUT / "captura_agent_console_recortada.png")
    sums = []
    for f in sorted(OUT.glob("*")):
        if f.name not in ("SHA256SUMS.txt", "README.md"):
            sums.append(f"{hashlib.sha256(f.read_bytes()).hexdigest().upper()}  {f.name}")
    with open(OUT / "SHA256SUMS.txt", "w", encoding="utf-8", newline=NL) as fh:
        fh.write(NL.join(sums) + NL)
    print("\n".join(sums), "\noriginal:", hashlib.sha256(src.read_bytes()).hexdigest().upper(), "imagen original:", img.size)


if __name__ == "__main__":
    main(Path(sys.argv[1]))
