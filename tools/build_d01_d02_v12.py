"""D01 v1.2 y D02 v1.2: solo portada, identificación del equipo y referencias cruzadas (Etapa 3, 20-nov-2026).

Bases: D01 v1.1 y D02 v1.1 (Fase 3/Entregables/_historico). No se reescriben requisitos ni decisiones técnicas.
"""
from fase3_v2 import *  # noqa: F401,F403

NOTE = ("Versión 1.2 (coherencia documental, Etapa 3): se normalizaron la portada y la identificación del equipo y se actualizaron las referencias cruzadas "
        "a las versiones vigentes (D03 v1.2, D04 v1.2, D05 v1.3, D06 v1.2, Informe v1.2). No se modificaron requisitos, decisiones ni resultados. "
        "La v1.1 se conserva en Fase 3/Entregables/_historico y la v1.0 en Fase 2.")


def build_d01() -> Path:
    d = Doc(HIST / "D01_Arquitectura_de_la_Solucion_v1.1_Fase3.docx")
    d.capture_templates("1. Propósito y alcance", "1.1 Qué problema resuelve", "Este documento describe", "Telefonía. No hay", "Figura 1.", "1. La persona elige")
    cover_v2(d, "17 de noviembre de 2026", "D01", "1.2")
    control_row(d, version="1.2", date=DATE_V2, change=NOTE)
    p = P(d, "Diagramas fuente en Fase 3/03_Diseno/diagramas/")
    d.set_par(p, p.text.replace("D03 v1.1 (casos de uso), D05 v1.1 (pruebas) y D06 v1.1 (operación)", "D03 v1.2 (casos de uso), D05 v1.3 (pruebas) y D06 v1.2 (operación)"))
    out = OUT / "D01_Arquitectura_de_la_Solucion_v1.2_Fase3.docx"
    d.save(out)
    return out


def build_d02() -> Path:
    d = Doc(HIST / "D02_Plan_de_Respuesta_a_Riesgos_v1.1_Fase3.docx")
    d.capture_templates("1. Propósito y método", None, "Se registran 20", "R-01 · Latencia", "Figura 1.", None)
    cover_v2(d, "17 de noviembre de 2026", "D02", "1.2")
    control_row(d, version="1.2", date=DATE_V2, change=NOTE)
    p = P(d, "Referencias: D01, D03, D05 y D06 v1.1")
    d.set_par(p, p.text.replace("D01, D03, D05 y D06 v1.1", "D01 v1.2, D03 v1.2, D05 v1.3 y D06 v1.2"))
    out = OUT / "D02_Plan_de_Respuesta_a_Riesgos_v1.2_Fase3.docx"
    d.save(out)
    return out


if __name__ == "__main__":
    print(build_d01())
    print(build_d02())
