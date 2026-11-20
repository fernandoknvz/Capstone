"""Verifica enlaces Markdown relativos y rutas `Fase N/...` citadas en los .md de Fase 3 (solo lectura)."""
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
bad, n = [], 0
for md in ROOT.glob("Fase 3/**/*.md"):
    t = md.read_text(encoding="utf-8")
    for m in re.finditer(r"\[[^\]]*\]\(([^)#\s]+)(?:#[^)]*)?\)", t):
        tgt = m.group(1)
        if re.match(r"[a-z]+:", tgt): continue
        n += 1
        if not (md.parent / tgt).exists(): bad.append((md.relative_to(ROOT).as_posix(), tgt))
    for m in re.finditer(r"`(Fase [123]/[^`]+)`", t):
        n += 1
        if not (ROOT / m.group(1).rstrip("/")).exists(): bad.append((md.relative_to(ROOT).as_posix(), m.group(1)))
print("enlaces/rutas comprobados:", n)
for b in bad: print("ROTO:", b)
print("RESULTADO:", "OK" if not bad else f"{len(bad)} rotos")
