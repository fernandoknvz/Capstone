from fase3_common import *  # noqa: F401,F403
from fase3_docx_lib import Doc


def tbl(d: Doc, *headers: str):
    for t in d.doc.tables:
        cells = [c.text.strip() for c in t.rows[0].cells]
        if len(cells) >= len(headers) and all(cells[i].startswith(h) for i, h in enumerate(headers)):
            return t
    raise KeyError(headers)


DOC_TABLE = [
    ["Presentación: problema", "Obligatoria (informada por el equipo)", "D03 §1 y §3; Informe §2", "Cubierto"],
    ["Presentación: solución y arquitectura", "Obligatoria (informada por el equipo)", "D01; Informe §6", "Cubierto"],
    ["Presentación: demostración funcional completa", "Obligatoria (informada por el equipo)", "D06 (puesta en marcha) y D05 §10; guion de demostración del Informe", "Pendiente de ensayo sobre main"],
    ["Requerimientos IEEE 830 o historias de usuario", "Referencia, por validar", "D03 §4 a §6 (12 RF, 10 RNF + RNF-11, 8 HU)", "Cubierto; estados actualizados al 17-nov"],
    ["Casos de uso", "Referencia, por validar", "D03 §11", "Cubierto con UC-01 a UC-11; UP-1 a UP-4 pendientes"],
    ["Diagrama de clases", "Referencia, por validar", "D01 §10.3", "Cubierto como módulos y clases reales; el código es mayormente funcional"],
    ["Diagramas de actividad", "Referencia, por validar", "D01 §10.2", "Cubierto (actividad del worker)"],
    ["Modelo de datos", "Referencia, por validar", "D01 §10.5", "Declarado: no existe base de datos; se documenta el almacenamiento real"],
    ["Mockups", "Referencia, por validar", "D05 §10 (capturas del producto)", "No existen mockups previos al desarrollo; se muestran capturas reales, sin presentarlas como mockups"],
    ["Plan de pruebas, casos y resultados", "Referencia, por validar", "D05", "Cubierto; certificación del 17-nov"],
    ["Backlogs y actas", "Referencia, por validar", "—", "[PENDIENTE] no están en los repositorios (CoreStream/actas)"],
    ["Estados de avance, stakeholders y plan de proyecto", "Referencia, por validar", "D04; D03 §2.3; Fase 1 (plan de trabajo)", "Cubierto parcialmente; backlogs y actas pendientes"],
]


def build() -> Path:
    d = Doc(ORIG / "D03_Levantamiento_de_Requerimientos.docx")
    d.capture_templates("1. Propósito", "2.1 Fuentes de información", "Este documento reúne", "Entrevista / reunión",
                        "Cadena esperada", "1. ¿Cuándo")
    # la plantilla de "caption" no existe en D03: usamos un párrafo de figura propio
    caption_template(d)
    cover(d, "D03")
    control_row(d, change=(
        "Actualización de Fase 3 sobre una copia completa de la v1.0 (30-oct). Se actualizaron los estados de implementación al corte 77ff85c (PR #16, #17, #19 y #20 fusionados), "
        "se añadieron fuentes F-08 a F-10, RNF-11 (CI), cambios de requerimientos, preguntas abiertas, la sección 11 (casos de uso), la sección 12 (documentación de Fase 3) y la matriz de trazabilidad ampliada. "
        "Los identificadores RF/RNF/HU se mantienen. La v1.0 se conserva sin cambios en Fase 2."))

    # --- fuentes
    t = tbl(d, "ID", "Fuente", "Fecha")
    d.add_row(t, ["F-08", "Estado integrado del repositorio técnico y CI", "17-nov-2026", "Estado de implementación de cada RF/RNF contrastado con origin/main (77ff85c, PR #1 a #17, #19, #20).", "Repositorio técnico y run de CI 42435613596 [CONFIRMADO]"])
    d.add_row(t, ["F-09", "Evidencia E2E de la clínica dental", "31-oct-2026", "Primera sesión con log del worker archivado desde la Web Demo (5 turnos E2E).", "Logs sanitizados con SHA-256 en Fase 3/07_Evidencias [CONFIRMADO]"])
    d.add_row(t, ["F-10", "Instrucciones del docente para Fase 3", "Informadas por el equipo", "La presentación debe incluir problema, solución y arquitectura y demostración funcional completa; la documentación de referencia incluye requerimientos, casos de uso, diagramas, modelo de datos, mockups, plan y resultados de pruebas, backlogs, actas, avances, stakeholders y plan de proyecto. Evaluación: jueves 19-nov-2026.", "[REPORTADO POR EL EQUIPO] sin pauta oficial adjunta"])

    # --- contexto AS-IS / TO-BE
    t = tbl(d, "", "Situación actual")
    d.cell_set(t, "Latencia", 2, "Medición actual: mediana 2,59 s en el navegador (E01, n=13) y 2,74 s en el E2E del 31-oct (n=5); no cumple 1 s (D05).")

    # --- RF
    d.rep("Estado al 30-oct", "Estado al 17-nov (main 77ff85c)")
    t = tbl(d, "ID", "Requerimiento", "Origen", "Prio.")
    d.cell_set(t, "RF-01", 6, "Implementado e integrado (PR #7); validado en navegador (E01 30-oct; E2E clínica dental 31-oct)")
    d.cell_set(t, "RF-08", 6, "Implementado e integrado (PR #9); 40 pruebas")
    d.cell_set(t, "RF-09", 6, "Implementado e integrado (PR #11 a #16); Netlify y Vercel")
    d.cell_set(t, "RF-10", 6, "Implementado e integrado (PR #16, 30-oct); solo la persona clínica dental tiene E2E archivado")
    d.cell_set(t, "RF-11", 6, "Implementado e integrado (PR #16); verificación real de micrófono y silencio pendiente (TC-12, TC-13)")
    # --- RNF
    t = tbl(d, "ID", "Requerimiento", "Origen", "Clasificación")
    d.cell_set(t, "RNF-01", 4, "No se cumple. E01 (30-oct): mediana de 2,59 s (n=13), mínimo 0,48 s, máximo 4,08 s. E2E 31-oct: mediana de 2,74 s (n=5), rango 1,19 a 3,35 s. Muestras no combinables.")
    d.cell_set(t, "RNF-08", 4, "214 pruebas de Python y 91 de la web ejecutadas el 17-nov sobre main (D05 §2.4); CI desde el PR #19.")
    d.cell_set(t, "RNF-09", 4, "El worker corre en un computador del equipo; el nombre del agente es configurable (PR #17) pero el hosting persistente sigue [PENDIENTE].")
    d.add_row(t, ["RNF-11", "Integración continua: cada PR y push a main ejecuta pruebas y controles de calidad sin secretos.", "Equipo", "[PROPUESTA]", "Implementado (PR #19, #20); run 42435613596 (success) sobre 77ff85c."])

    # --- restricciones
    d.rep("; hoy corresponde la semana 12.", "; la evaluación de Fase 3 está programada para el jueves 19 de noviembre de 2026 (informada por el equipo).")

    # --- cambios
    t = tbl(d, "Fecha", "Cambio", "Motivo")
    d.cell_set(t, "30-oct-2026", 4, "[PROPUESTA] (PR #16 fusionado el 30-oct; sin aprobación del cliente)")
    d.add_row(t, ["31-oct-2026", "El nombre del agente LiveKit pasa a ser configurable.", "Evitar despachos cruzados entre workers de desarrollo.", "Sin cambio funcional; mejora la operación.", "[PROPUESTA] (PR #17 fusionado)"])
    d.add_row(t, ["4-nov-2026", "El PR #18 propone nuevos LLM, STT seleccionable y optimizaciones.", "Reducir la latencia.", "No integrado; no modifica los requisitos vigentes.", "[PENDIENTE DE VALIDACIÓN] PR abierto sin revisión"])
    d.add_row(t, ["7-nov-2026", "Se incorpora integración continua con GitHub Actions.", "Automatizar el control de calidad.", "Cada PR y push ejecuta pruebas y build.", "[PROPUESTA] (PR #19, #20 fusionados)"])
    d.add_row(t, ["17-nov-2026", "Se menciona una evolución del alcance (cobranza para pymes, «DART»).", "Idea de Fase 3 (ver matriz de trazabilidad, fila EV-01).", "Ninguno: no se cambia el nombre ni el alcance del proyecto.", "[PENDIENTE DE VALIDACIÓN] sin autorización académica"])

    # --- preguntas abiertas
    d.at(d.par("11. ¿Dónde debe alojarse"))
    d.para("12. [PENDIENTE] (al docente) ¿Cuál es la pauta oficial de Fase 3 y qué documentos de la lista de referencia son obligatorios?")
    d.para("13. [PENDIENTE] (al docente) ¿Se aceptan capturas de la Web Demo como evidencia de interfaz, dado que no existen mockups previos al desarrollo?")
    d.para("14. [PENDIENTE] (al docente y a Alloxentric) ¿Puede presentarse la cobranza para pymes como evolución futura sin modificar el alcance acordado?")

    # --- matriz de trazabilidad
    t = tbl(d, "Requerimiento", "Implementación", "Prueba", "Evidencia")
    d.cell_set(t, "RF-01", 3, "PR #7; validación 26-oct; métricas 30-oct (E01); E2E 31-oct")
    d.cell_set(t, "RF-09", 3, "PR #11 a #16; despliegues; runs de CI")
    d.cell_set(t, "RF-10", 3, "PR #16 (fusionado); E2E 31-oct (solo clínica dental)")
    d.cell_set(t, "RF-10", 4, "Implementado e integrado; 6 personas sin E2E")
    d.cell_set(t, "RF-11", 3, "PR #16 (fusionado)")
    d.cell_set(t, "RF-11", 4, "Implementado e integrado; TC-12/TC-13 reales pendientes")
    d.cell_set(t, "RNF-01", 3, "E01; E2E 31-oct; D05")
    d.add_row(t, ["RF-06 Interrupciones", "Sesión de LiveKit (VAD y turnos)", "TC-15 (pendiente)", "E01: 10 de 22 turnos marcados como interrumpidos", "Implementado; eco y falsas interrupciones sin probar"])
    d.add_row(t, ["RNF-04 Seguridad", "session.ts, http.ts, livekit.ts, CSP", "login, session, origin, livekit-token y csp-headers (30 pruebas); TC-06 a TC-10", "PR #11 a #17; D01 §5", "Cumplido (controles verificados por prueba)"])
    d.add_row(t, ["RNF-05 Privacidad", "record=False; localStorage", "history.test.ts (8); client-secrets.test.ts (1); TC-18", "D01 §5 y §10.5", "Cumplido"])
    d.add_row(t, ["RNF-08 Mantenibilidad", "Módulos por proveedor; CI", "214 + 91 pruebas (17-nov); CI", "D05 §2.4; run 42435613596", "Cumplido"])
    d.add_row(t, ["RNF-09 Disponibilidad", "Worker local; LIVEKIT_AGENT_NAME", "test_agent_name.py (14)", "D06", "Parcial: sin hosting persistente"])
    d.add_row(t, ["RNF-11 Integración continua", ".github/workflows/ci.yml", "Runs 42433340255, 42433603292, 42435613596", "PR #19, #20", "Cumplido"])

    # ------------------------------------------------------------------ nuevas secciones al final
    d.at_end()
    d.h1("11. Casos de uso")
    d.para("Los casos de uso se derivaron de los requerimientos (RF) y de las historias de usuario (HU) de este documento y del código integrado en main (77ff85c). UC-01 a UC-11 están implementados y cuentan con verificación automática o manual; UP-1 a UP-4 no existen en el código y se muestran fuera del límite del sistema. No se añadieron casos sin respaldo en el código o en D03.")
    use_case_tables(d)
    landscape_figure(d, FIG / "fig_casos_uso.png", "Figura 1. Diagrama de casos de uso. Fuente: elaboración propia a partir de D03 y del repositorio técnico (77ff85c).")
    d.h1("12. Documentación de Fase 3: obligatoria y de referencia")
    d.para("El equipo informó que la evaluación del 19 de noviembre de 2026 exige presentar el problema, la solución con su arquitectura y una demostración funcional completa, y que la documentación de referencia incluye los elementos de la tabla. No se dispone de la pauta oficial, por lo que la clasificación de cada elemento como obligatorio o de referencia debe validarse. [REPORTADO POR EL EQUIPO]")
    d.table_new(["Elemento", "Clasificación", "Dónde se cubre", "Estado al 17-nov"], DOC_TABLE, [4.6, 3.2, 4.4, 4.6])
    d.h1("13. Conclusiones")
    d.para("Los requerimientos funcionales centrales (conversación de voz, STT, LLM, TTS, métricas, Web Demo, escenarios y controles de interfaz) están implementados e integrados en main y cuentan con pruebas automáticas y una sesión E2E archivada. Siguen pendientes los requisitos que dependen del cliente o de entornos externos: guion oficial y reconocimiento de intenciones (RF-05), telefonía Asterisk (RF-07), comparación de costo y efectividad (RF-12) y el cumplimiento del umbral de 1 s (RNF-01). "
           "La trazabilidad requerimiento → implementación → prueba → evidencia se mantiene en la sección 10 y se amplió con los RNF verificables. [CONFIRMADO]")
    d.h1("14. Referencias")
    for x in ["D01 v1.1 (arquitectura y diseño), D05 v1.1 (pruebas y resultados) y D06 v1.1 (operación), en Fase 3/Entregables.",
              "Repositorio técnico fernandoknvz/alloxentric-real-time-agent en el corte 77ff85c (PR #1 a #17, #19 y #20).",
              "Informe de definición del proyecto APT (Fase 1) y guía 2.4 de avance (Fase 2).",
              "Evidencia E2E del 31-oct-2026 y matriz de trazabilidad de Fase 3 (Fase 3/07_Evidencias y Fase 3/MATRIZ_TRAZABILIDAD_PRELIMINAR.md).",
              "Instrucciones del docente para Fase 3 informadas por el equipo (sin documento adjunto)."]:
        d.bullet(x)
    out = OUT / "D03_Levantamiento_de_Requerimientos_v1.1_Fase3.docx"
    d.save(out)
    return out


if __name__ == "__main__":
    print(build())
