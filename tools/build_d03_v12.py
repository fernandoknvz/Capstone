"""D03 v1.2: RF-02/RF-03, trazabilidad de pruebas, resultados del 17-nov y F-10 alineado con la guía 3.3 (Etapa 2, 19-nov-2026).

Base: D03 v1.1 (Fase 3/Entregables/_historico).
"""
from fase3_v2 import *  # noqa: F401,F403


def replace_table(d: Doc, first_cell: str, header: list[str], rows: list[list[str]], widths: list[float]) -> None:
    old = d.table(first_cell)
    d.at(old._tbl.getprevious())
    d.table_new(header, rows, widths)
    old._tbl.getparent().remove(old._tbl)


def build() -> Path:
    d = Doc(HIST / "D03_Levantamiento_de_Requerimientos_v1.1_Fase3.docx")
    d.capture_templates("1. Propósito", "2.1 Fuentes de información", "Este documento reúne", "Entrevista / reunión", "Cadena esperada", "1. ¿Cuándo")
    caption_template(d)
    cover_v2(d, "17 de noviembre de 2026", "D03", "1.2")
    control_row(d, version="1.2", date=DATE_V2, change=(
        "Versión 1.2 (saneamiento tras la auditoría del 19-nov): se rebajó la fuente F-01 a evidencia indirecta y se registró la contradicción sobre el uso de un LLM; "
        "se actualizaron RF-01 a RF-03 y RF-10, RNF-01 y RNF-02 con los resultados del 17-nov; se corrigió la trazabilidad de pruebas (TC-03, TC-04 y TC-07 a TC-10 dejaron de figurar como cumplidos plenos); "
        "se alineó F-10 con las guías oficiales 3.1 y 3.3; se agregaron las fuentes F-11 y F-12 y un cambio de proveedor del 17-nov; se actualizaron los nombres de portada. "
        "Los identificadores RF/RNF/HU se mantienen. La v1.1 se conserva en Fase 3/Entregables/_historico y la v1.0 en Fase 2."))

    # --- 2.1 fuentes
    t = tbl(d, "ID", "Fuente", "Fecha", "Qué aportó")
    d.cell_set(t, "F-01", 3, "Problema de costos poco elásticos; tecnologías (LiveKit, STT, ElevenLabs, Asterisk); caso de cobranza; latencia ≤ 1 s y riesgo de corte sobre 3 s; voz adecuada al contexto chileno; y, según Fase 1, evitar un LLM al inicio (contradicho por la especificación v0.1 descrita en el informe DART 14 1.1; ver nota siguiente). Todo atribuido a Max [REPORTADO POR EL EQUIPO]")
    d.cell_set(t, "F-01", 4, "Evidencia indirecta: el informe de Fase 1 cita una transcripción de la intervención de Max que no está archivada (localización pendiente); ACTA-01 es una reconstrucción sin convocatoria ni asistentes [REPORTADO POR EL EQUIPO]")
    d.cell_set(t, "F-05", 4, "Mensaje del líder citando a Max; sin acta. Se trata como decisión técnica del equipo con indicación atribuida al cliente [PENDIENTE DE VALIDACIÓN]")
    d.cell_set(t, "F-10", 1, "Guías oficiales de Fase 3: 3.3 «Presentación Proyecto APT» y 3.1 «Diario de reflexión»")
    d.cell_set(t, "F-10", 2, "Guías disponibles al 19-nov")
    d.cell_set(t, "F-10", 3, "3.3: la presentación describe los aspectos relevantes y fundamenta las decisiones; dura máximo 20 minutos incluidas las preguntas; usa como estructura los campos del Informe Final; se acompaña de las evidencias del proyecto; incorpora ajustes a partir de la última retroalimentación del docente sobre el informe final; la comisión (docentes y Dirección de Carrera) evalúa individualmente y pondera el 30 % de la nota final. 3.1: reflexión individual sobre intereses, fortalezas, proyecciones y trabajo en grupo. "
                         "El equipo había informado además una lista de documentación de referencia (requerimientos, casos de uso, diagramas, modelo de datos, mockups, plan y resultados de pruebas, backlogs, actas, avances, stakeholders y plan de proyecto) y una evaluación el jueves 19-nov; la fecha de entrega indicada por el equipo es el sábado 21-nov-2026 [REPORTADO POR EL EQUIPO]")
    d.cell_set(t, "F-10", 4, "Guías 3.1 y 3.3 [CONFIRMADO] (copias sin modificar en Fase 3/Pautas_Oficiales/). Planillas de evaluación de Fase 3: [PENDIENTE]; no se declara completa la cobertura de evaluación")
    d.add_row(t, ["F-11", "Reporte de rendimiento de CoreStream (EV-20)", "19-nov-2026", "Reporte agregado del período «year»: eficiencia 4 %, bloqueo 0 %, redirección 0 % y 16 tareas completadas; sin tickets. CoreStream es una herramienta proporcionada por Alloxentric; Javier Cerna figura en el reporte pero no pertenece al equipo Capstone.", "PDF original sin alteraciones (SHA-256 CBDADA1B...EE869) [CONFIRMADO]; no acredita avance, hitos ni rendimiento individual"])
    d.add_row(t, ["F-12", "Informe E2E DART-14-2.5 (E10 de D05)", "19-oct-2026", "Primera validación E2E con una frase desde Agent Console.", "Versión sanitizada en Fase 3/07_Evidencias/DART-14-2.5_E2E-2026-10-19/ [CONFIRMADO]; original fuera de Git"])
    d.at(t)
    para_sb(d, "[REPORTADO POR EL EQUIPO] " + REUNION_NOTE)
    d.para("[PENDIENTE DE VALIDACIÓN] " + CONTRADICCION_LLM)
    # --- 4: requerimientos
    t = tbl(d, "ID", "Requerimiento", "Origen", "Prio.")
    d.cell_set(t, "RF-01", 6, "Implementado e integrado (PR #7); validado en navegador (E01 30-oct; E2E clínica dental 31-oct y 17-nov; una frase el 19-oct)")
    d.cell_set(t, "RF-02", 6, "Implementado (PR #6) con es-US [PROPUESTA]; funcionamiento confirmado en E2E (31-oct y 17-nov) y en la prueba del 19-oct; exactitud NO medida (TC-03 parcial); idioma definitivo [PENDIENTE]")
    d.cell_set(t, "RF-03", 6, "Implementado (PR #3, #5); respuestas generadas verificadas en E2E (Gemini 31-oct; DeepSeek 17-nov: 9 respuestas, errors {}); coherencia y conducta no verificables con la evidencia archivada (TC-04 parcial)")
    d.cell_set(t, "RF-10", 6, "Implementado e integrado (PR #16, 30-oct); solo la persona clínica dental tiene E2E archivado (31-oct y 17-nov); las dos de cobranza no tienen E2E")
    t = tbl(d, "ID", "Requerimiento", "Origen", "Clasificación", "Estado y evidencia")
    d.cell_set(t, "RNF-01", 4, "No se cumple. E01 (30-oct): mediana de 2,59 s (n=13), mínimo 0,48 s, máximo 4,08 s. E2E 31-oct: mediana de 2,74 s (n=5), rango 1,19 a 3,35 s. E2E 17-nov (DeepSeek): mediana de 3,26 s (n=8), rango 0,56 a 5,50 s; 2 de 8 turnos ≤ 1 s. Muestras no combinables; método de percentiles en D05 §4.4.")
    d.cell_set(t, "RNF-02", 4, "3 de 13 turnos superaron 3 s en E01; 1 de 5 el 31-oct; 4 de 8 el 17-nov.")
    # --- 8: cambios
    t = tbl(d, "Fecha", "Cambio", "Motivo", "Impacto", "Aprobación")
    d.cell_set(t, "Mediados oct-2026", 4, "Indicación atribuida a Max y transmitida por el líder; sin acta ni aprobación formal verificable. Decisión técnica del equipo [PENDIENTE DE VALIDACIÓN]")
    d.add_row(t, ["17-nov-2026", "En la demostración E2E se usa DeepSeek en lugar de Gemini.", "Dos intentos con Gemini fallaron por API_KEY_INVALID (sin respuestas del LLM).", "Misma cadena de voz; solo cambia el proveedor del LLM (LLM_PROVIDER).", "[PROPUESTA] del equipo; sin aprobación del cliente"])
    # --- 9: preguntas abiertas
    p = P(d, "12. [PENDIENTE] (al docente)")
    d.set_par(p, "12. [PENDIENTE] (al docente) ¿Existen planillas o pautas de evaluación de Fase 3 (evidencia individual y grupal), además de las guías 3.1 y 3.3, y cómo se incorpora la retroalimentación del informe final de Fase 2?")
    # --- 10: trazabilidad
    t = tbl(d, "Requerimiento", "Implementación", "Prueba", "Evidencia")
    d.cell_set(t, "RF-01", 3, "PR #7; validación 26-oct (reportada, sin logs); métricas 30-oct (E01); E2E 31-oct y 17-nov; E10")
    d.cell_set(t, "RF-02", 2, "tests/test_stt.py (14); TC-03 (parcial)")
    d.cell_set(t, "RF-02", 3, "PR #6; E2E 31-oct y 17-nov; E10; prueba real del 16-oct [REPORTADO POR EL EQUIPO]")
    d.cell_set(t, "RF-02", 4, "Funcional en navegador; exactitud no medida")
    d.cell_set(t, "RF-03", 2, "test_llm*.py (24); TC-04 (parcial / no verificable)")
    d.cell_set(t, "RF-03", 3, "PR #3, #5; E2E 31-oct (Gemini) y 17-nov (DeepSeek); medición de modelos [REPORTADO POR EL EQUIPO]")
    d.cell_set(t, "RF-03", 4, "Funcional; coherencia y conducta no verificadas")
    d.cell_set(t, "RF-09", 3, "PR #11 a #16; despliegues y pruebas en producción [REPORTADO POR EL EQUIPO]; runs de CI")
    d.cell_set(t, "RF-09", 4, "Cumplido por pruebas automáticas; verificación en producción reportada (TC-07 a TC-10)")
    d.cell_set(t, "RF-10", 3, "PR #16 (fusionado); E2E 31-oct y 17-nov (solo clínica dental)")
    d.cell_set(t, "RNF-01", 3, "E01; E2E 31-oct y 17-nov; D05 v1.3")
    d.cell_set(t, "RNF-04", 4, "Cumplido en pruebas automáticas; verificación en producción reportada")
    # --- 12: documentación de Fase 3
    p = P(d, "El equipo informó que la evaluación del 19 de noviembre")
    d.set_par(p, GUIA_33 + " " + PAUTAS_PENDIENTES + " La lista de documentación de referencia fue informada por el equipo y debe validarse. [REPORTADO POR EL EQUIPO]")
    replace_table(d, "Elemento", ["Elemento", "Clasificación", "Dónde se cubre", "Estado al 19-nov"], DOC_TABLE_V12, [4.6, 3.2, 4.4, 4.6])
    # --- 13 y 14
    p = P(d, "Los requerimientos funcionales centrales")
    d.set_par(p, p.text + " Tras la auditoría del 19-nov, la conversación de voz, el STT, el LLM y el TTS figuran como funcionales y medidos, pero no verificados en exactitud, coherencia ni conducta de cobranza; la fuente F-01 es evidencia indirecta y las decisiones atribuidas al cliente no tienen aprobación confirmada. [CONFIRMADO]")
    p = P(d, "D01 v1.1 (arquitectura y diseño), D05 v1.1")
    d.set_par(p, "D01 v1.2 (arquitectura y diseño), D05 v1.3 (pruebas y resultados) y D06 v1.2 (operación), en Fase 3/Entregables.")
    p = P(d, "Instrucciones del docente para Fase 3 informadas")
    d.set_par(p, "Guías oficiales 3.1 y 3.3 de Fase 3 (copias sin modificar en Fase 3/Pautas_Oficiales/); las planillas de evaluación de Fase 3 siguen pendientes.")
    d.at(p)
    d.bullet("Reporte de CoreStream (EV-20) y expediente histórico de reuniones (Fase 3/07_Evidencias/CoreStream y Reuniones_Cliente); evidencia DART-14-2.5 sanitizada (Fase 3/07_Evidencias/DART-14-2.5_E2E-2026-10-19).")

    out = OUT / "D03_Levantamiento_de_Requerimientos_v1.2_Fase3.docx"
    d.save(out)
    return out


if __name__ == "__main__":
    print(build())
