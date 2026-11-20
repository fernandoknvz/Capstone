"""Genera los entregables vigentes de la Etapa 2 (D01 v1.2, D02 v1.2, D03 v1.2, D04 v1.2, D05 v1.3, D06 v1.2 e Informe v1.2).

Requisito: las versiones anteriores están en Fase 3/Entregables/_historico.
Uso (desde esta carpeta): py build_etapa2.py [carpeta_pdf]
Con carpeta_pdf, además actualiza índices con Word y exporta un PDF de revisión de cada documento.
"""
import sys
from pathlib import Path

import build_d01_d02_v12, build_d03_v12, build_d04_v12, build_d05_v13, build_d06_v12, build_informe

outs = [build_d01_d02_v12.build_d01(), build_d01_d02_v12.build_d02()] + [m.build() for m in (build_d03_v12, build_d04_v12, build_d05_v13, build_d06_v12, build_informe)]
for o in outs:
    print(o.name)
if len(sys.argv) > 1:
    from word_finalize import finalize
    for o in outs:
        print(o.name, "páginas:", finalize(o, Path(sys.argv[1])))
