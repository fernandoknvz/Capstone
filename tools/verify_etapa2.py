"""Verificaciones de coherencia de la Etapa 2 (solo lectura): identidad, versiones citadas, rutas de evidencia,
estados de prueba, CoreStream, hashes y secretos en los entregables vigentes y en la evidencia nueva."""
import hashlib, re, subprocess
from pathlib import Path
import docx
from docx.table import Table
from docx.text.paragraph import Paragraph

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "Fase 3" / "Entregables"
CURRENT = {"D01": "1.2", "D02": "1.2", "D03": "1.2", "D04": "1.2", "D05": "1.3", "D06": "1.2", "Informe": "1.2"}
SECRETS = [r"AIza[0-9A-Za-z_\-]{20,}", r"sk-[A-Za-z0-9]{20,}", r"eyJ[A-Za-z0-9_\-]{15,}\.[A-Za-z0-9_\-]{10,}", r"Bearer\s+[A-Za-z0-9._\-]{20,}",
           r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}", r"[A-Za-z]:[\/]Users[\/]", r"[\w.+-]+@[\w-]+\.[\w.]+", r"(?i)xi-api-key", r"-----BEGIN", r"\b\d{1,3}(\.\d{1,3}){3}\b"]


def text_of(d):
    parts = []
    for el in d.element.body.iterchildren():
        if el.tag.endswith("}p"):
            parts.append(Paragraph(el, d).text)
        elif el.tag.endswith("}tbl"):
            for r in Table(el, d).rows:
                seen = []
                for c in r.cells:
                    if c.text not in seen:
                        seen.append(c.text)
                parts.append(" | ".join(seen))
    return "\n".join(parts)


docs = {f.name: text_of(docx.Document(str(f))) for f in sorted(OUT.glob("*_Fase3.docx"))}
problems = []
print("== Entregables vigentes:", ", ".join(docs))

print("\n== 1. Identidad")
for n, t in docs.items():
    head = "\n".join(t.splitlines()[:25])
    cover = {k: (k in head) for k in ("Juan Díaz (", "Fernando Patricio Olguea González (", "David Sepúlveda (")}
    full = [v for v in ("David Alexis Sepúlveda Manque", "Fernando Olguea (") if v in t]
    bad = "Fernando Díaz" in t
    print(f"{n[:46]:46s} portada={'OK' if all(cover.values()) else cover} variantes_largas={full or '-'} 'Fernando Díaz'={'SÍ' if bad else 'no'}")
    if bad: problems.append((n, "Fernando Díaz"))

print("\n== 2. Versiones citadas (esperadas: " + ", ".join(f"{k} v{v}" for k, v in CURRENT.items()) + ")")
for n, t in docs.items():
    own = re.match(r"(D0\d|Informe)", n).group(1)
    t_chk = t.replace("D01 a D06 v1.1", "")  # cita histórica legítima
    for m in sorted(set(re.findall(r"\b(D0[1-6]|Informe)(?: acad[ée]mico)?(?: consolidado)? v(\d\.\d)\b", t_chk))):
        k, v = m
        if k in CURRENT and v != CURRENT[k]:
            print(f"{n[:46]:46s} cita {k} v{v} (vigente v{CURRENT[k]})")
            problems.append((n, f"{k} v{v}"))

print("\n== 3. Rutas de evidencia citadas")
miss = set()
for n, t in docs.items():
    for m in re.findall(r"Fase [123]/[A-Za-z0-9_./\-ÁÉÍÓÚáéíóú ]+", t):
        cand = re.split(r" y | v\d\.\d| en ", m)[0].rstrip(" .,;:)")
        while cand and not (ROOT / cand).exists() and "/" in cand:
            cand2 = cand.rsplit(" ", 1)[0] if " " in cand.split("/")[-1] else None
            if not cand2 or cand2 == cand: break
            cand = cand2
        if not (ROOT / cand).exists():
            miss.add((n[:30], m.strip()[:90]))
for x in sorted(miss): print("no existe:", x)
print("(sin faltantes)" if not miss else "")

print("== 4. Estados de TC en D05 v1.3")
t5 = docs["D05_Plan_de_Pruebas_y_Resultados_v1.3_Fase3.docx"]
for tc in ("TC-02", "TC-03", "TC-04", "TC-07", "TC-08", "TC-09", "TC-10", "TC-14", "TC-17", "TC-24"):
    row = [l for l in t5.splitlines() if l.startswith(tc + " |")][0].split(" | ")
    print(tc, "->", row[3])

print("\n== 5. CoreStream / Javier Cerna / 4 %")
for n, t in docs.items():
    for l in t.splitlines():
        if "Javier Cerna" in l:
            ok = "no forma parte" in l or "no pertenece" in l
            print(f"{n[:30]:30s} Javier Cerna {'(aclarado)' if ok else '(REVISAR)'}")
            if not ok: problems.append((n, "Javier"))
        if re.search(r"4 ?%", l) and "eficiencia" in l.lower() and not re.search(r"no (debe )?interpret|no es un porcentaje|no acredita|no permite", l):
            print(f"{n[:30]:30s} 4 % sin aclaración: {l[:100]}"); problems.append((n, "4%"))

print("\n== 6. Manifiestos SHA-256")
for man in ROOT.glob("Fase 3/07_Evidencias/**/SHA256SUMS.txt"):
    rc = subprocess.run(["sha256sum", "-c", "SHA256SUMS.txt"], cwd=man.parent, capture_output=True, text=True)
    print(man.parent.name, "OK" if rc.returncode == 0 else "FALLA: " + rc.stdout[-200:])
    if rc.returncode: problems.append((man.parent.name, "hash"))
for f in [ROOT / "Fase 2/Evidencias Proyecto/Evidencias Documentacion/E01_Evidencia_Metricas_Latencia_2026-10-30.txt"]:
    print(f.name, hashlib.sha256(f.read_bytes()).hexdigest().upper() == "69AF78CA176BDFB944D95D3A02B61F63EEC8280DED2362644BA525FED4A71C7A")

print("\n== 7. Secretos / datos personales en evidencia nueva y documentos")
new_md = list((ROOT / "Fase 3/07_Evidencias/DART-14-2.5_E2E-2026-10-19").glob("*.md"))
for name, txt in [(f.name, f.read_text(encoding="utf-8")) for f in new_md] + list(docs.items()):
    hits = {p: re.findall(p, txt)[:2] for p in SECRETS if re.findall(p, txt)}
    hits.pop(r"\b\d{1,3}(\.\d{1,3}){3}\b", None) if name.startswith("D0") or name.startswith("Informe") else None
    print(f"{name[:46]:46s}", hits or "ninguno")
    if hits: problems.append((name, "secretos"))
print("\nRESULTADO:", "OK" if not problems else f"REVISAR {problems}")
