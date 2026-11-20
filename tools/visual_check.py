"""Comprobaciones automáticas sobre los PDF exportados con Word (solo lectura).
Uso: py visual_check.py <carpeta_pdf>  (requiere PyMuPDF)"""
import re, sys, glob, collections
import fitz

TOL = 28  # pt de margen mínimo aceptable (≈1 cm)
tot = 0
for f in sorted(glob.glob(sys.argv[1] + "/*.pdf")):
    d = fitz.open(f); name = f.replace("\\", "/").split("/")[-1][:44]
    issues, fonts = [], collections.Counter()
    for i, pg in enumerate(d, 1):
        W, H = pg.rect.width, pg.rect.height
        words = pg.get_text("words")
        imgs = pg.get_images(full=True)
        if not words and not imgs:
            issues.append(f"p{i}: página en blanco")
        elif len(words) < 12 and not imgs and i > 1:
            issues.append(f"p{i}: casi vacía ({len(words)} palabras)")
        for b in pg.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                for s in l["spans"]:
                    fonts[s["font"]] += len(s["text"])
        xs0 = [w[0] for w in words]; xs1 = [w[2] for w in words]
        if words and (min(xs0) < TOL or max(xs1) > W - TOL):
            issues.append(f"p{i}: texto fuera de margen (x {min(xs0):.0f}–{max(xs1):.0f} de {W:.0f})")
        for dr in pg.get_drawings():
            r = dr["rect"]
            if r.width > 5 and (r.x0 < TOL - 12 or r.x1 > W - (TOL - 12)):
                issues.append(f"p{i}: tabla/forma fuera de margen ({r.x0:.0f}–{r.x1:.0f} de {W:.0f})"); break
        for im in imgs:
            for r in pg.get_image_rects(im[0]):
                pix_w, pix_h = im[2], im[3]
                if pix_w and pix_h and abs((r.width / r.height) / (pix_w / pix_h) - 1) > 0.03:
                    issues.append(f"p{i}: imagen deformada ({r.width/r.height:.2f} vs {pix_w/pix_h:.2f})")
                if r.x1 > W + 1 or r.y1 > H + 1 or r.x0 < -1:
                    issues.append(f"p{i}: imagen fuera de página")
    # índice: entradas «título ..... n» frente a la página real del encabezado
    toc_bad, n_toc = [], 0
    page_lines = [[l.strip() for l in pg.get_text().split(chr(10))] for pg in d]
    pat = re.compile(r'^(.+?)' + chr(92) + 's*' + chr(92) + '.{3,}' + chr(92) + 's*(' + chr(92) + 'd{1,3})$')
    for k in range(min(4, len(d))):
        for l in page_lines[k]:
            m = pat.match(l)
            if not m:
                continue
            n_toc += 1
            title, pgno = m.group(1).strip(), int(m.group(2))
            pages = [q + 1 for q, PL in enumerate(page_lines) if title in PL]
            if not pages:
                toc_bad.append(f'«{title[:40]}» no se encontró el encabezado')
            elif pgno not in pages:
                toc_bad.append(f'«{title[:40]}» índice p{pgno}, real p{pages[0]}')
    print(f"\n{name}: {len(d)} págs; índice {n_toc} entradas; fuentes {dict(fonts.most_common(3))}")
    for x in issues + [("ÍNDICE " + t) for t in toc_bad]:
        print("  -", x); tot += 1
print("\nTOTAL de observaciones automáticas:", tot)
