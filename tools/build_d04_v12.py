"""D04 v1.2: separa estado histórico (corte 30-oct) y estado final (19-nov), actualiza PR, E2E y CoreStream (Etapa 2).

Base: D04 v1.1 (Fase 3/Entregables/_historico).
"""
from fase3_v2 import *  # noqa: F401,F403


def build() -> Path:
    d = Doc(HIST / "D04_Estado_de_Avance_del_Proyecto_v1.1_Fase3.docx")
    d.capture_templates("1. Resumen ejecutivo", None, "A la fecha de corte del informe grupal 2.4", "Disponibles:", "Disponibles:")
    cover_v2(d, "17 de noviembre de 2026", "D04", "1.2")
    d.set_par(P(d, "Qué se ha hecho hasta el 30 de octubre"),
              "Qué se hizo hasta el 30 de octubre de 2026 (corte histórico original) y estado final actualizado al 19 de noviembre de 2026")
    control_row(d, version="1.2", date=DATE_V2, change=(
        "Versión 1.2 (saneamiento tras la auditoría del 19-nov, AUD-12): se distingue el estado histórico (secciones 1 a 8, corte del 30-oct) del estado final (sección 9, 19-nov); "
        "se corrigieron las referencias al PR #16 como abierto, la nota «DeepSeek real solo reportado» y las evidencias disponibles; se incorporó la evidencia E2E del 17-nov, DART-14-2.5, EV-20 y EV-21; "
        "Scrum se describe como adaptación parcial y se explica el alcance de CoreStream; se actualizaron nombres de portada. La v1.1 se conserva en Fase 3/Entregables/_historico."))

    # --- aviso histórico / final
    p = P(d, "[CONFIRMADO] Actualización del 17-nov-2026")
    d.set_par(p, "[CONFIRMADO] Estado histórico y estado final. Las secciones 1 a 8 describen el corte original del 30-oct-2026 y conservan su redacción de entonces (por ejemplo, el PR #16 estaba abierto al redactarse, aunque se fusionó ese mismo día). "
                 "La sección 9 recoge el estado final verificado al 19-nov-2026, con el PR #16 fusionado y la evidencia E2E del 17-nov.")

    # --- referencias históricas a PR #16 y conteos
    t = tbl(d, "Indicador", "Corte 10-oct", "Corte 30-oct")
    d.cell_set(t, "Pull Requests fusionados", 2, "15 (#1 a #15); el #16 estaba abierto al corte del 30-oct")
    d.cell_set(t, "Pruebas automatizadas", 2, "200 de Python y 91 de la web ejecutadas el 30-oct sobre la rama del PR #16")
    t = tbl(d, "Fecha", "Hito", "PR / ticket", "Evidencia")
    d.cell_set(t, "30-oct", 2, "PR #16 (abierto al corte del 30-oct; fusionado ese día) · DART-14-5.1 [PROPUESTA]")
    d.cell_set(t, "2-sep", 3, "Transcripción citada en el informe de Fase 1; no archivada (evidencia indirecta)")
    d.cell_set(t, "2-sep", 1, "Reunión inicial con Max Kreimerman (reportada; sin acta ni transcripción archivada).")
    t = tbl(d, "Componente", "Responsable", "Impl.", "Prob.", "Fus.", "Integ.")
    d.cell_set(t, "Agentes por persona", 6, "PR #16 (abierto al corte del 30-oct; fusionado ese día); 200 + 91 pruebas; despliegue de prueba verificado.")
    t = tbl(d, "Indicador", "Corte 30-oct", "Corte 17-nov")
    d.cell_set(t, "Pruebas automatizadas", 1, "200 Python y 91 web (rama del PR #16 al corte del 30-oct)")
    d.cell_set(t, "Escenarios y Web Demo", 1, "7 personas; Netlify y Vercel (PR #16, abierto al corte del 30-oct)")
    d.cell_set(t, "Medición de latencia", 2, "Mediana 2,59 s (E01, n=13), 2,74 s (E2E 31-oct, n=5) y 3,26 s (E2E 17-nov con DeepSeek, n=8; 2 de 8 turnos ≤ 1 s); no cumple 1 s")
    d.cell_set(t, "Evidencia E2E archivada", 2, "E01 + logs del worker y de Netlify CLI del 31-oct y del 17-nov (DeepSeek) con SHA-256 verificados; capturas del 17-nov (EV-17, EV-21); DART-14-2.5 del 19-oct (sanitizada); reporte agregado de CoreStream (EV-20)")

    t = tbl(d, "Evidencia", "Ubicación", "Estado")
    d.cell_set(t, "Código y pruebas automáticas", 1, "https://github.com/fernandoknvz/alloxentric-real-time-agent (rama del PR #16 al corte del 30-oct)")

    # --- 9.2 línea de tiempo
    t = tbl(d, "Fecha", "Hito", "PR / evidencia")
    d.add_row(t, ["17 y 18-nov", "E2E de la clínica dental con DeepSeek (aprobado con observaciones: latencia no cumplida, agendamiento simulado) y consolidación de sus evidencias.", "EV-14 a EV-19; D05 (v1.2 en esa fecha)"])
    d.add_row(t, ["19-nov", "Reporte agregado de CoreStream, expediente histórico de reuniones, capturas derivadas de la demo, evidencia DART-14-2.5 sanitizada y saneamiento de D03, D04, D05, D06 e Informe tras la auditoría.", "PR #7 del repositorio académico (fusionado); rama docs/fase3-saneamiento-entregables-finales (sin fusionar)"])

    # --- 9.3 componentes
    t = tbl(d, "Componente", "Responsable (verificable)", "Implementado")
    d.cell_set(t, "STT Google Chirp 3", 5, "PR #6; 14 pruebas; operativo en E01, E2E y E10; exactitud no medida (TC-03 parcial)")
    d.cell_set(t, "LLM DeepSeek y Gemini", 5, "Gemini operativo en el E2E del 31-oct; DeepSeek verificado en el E2E del 17-nov (9 respuestas, errors {}); sin aprobación formal del cliente; coherencia no verificada (TC-04)")

    # --- 9.4 objetivos
    t = tbl(d, "Objetivo específico", "Estado 30-oct", "Estado 17-nov")
    d.cell_set(t, "1. Guion", 3, "D03 v1.2 actualizado; faltan guion oficial, intenciones y protocolo comparativo.")
    d.cell_set(t, "2. Dise", 3, "D01 v1.2 con casos de uso, actividad, módulos y almacenamiento; falta Asterisk.")
    d.cell_set(t, "4. Planificar", 2, "Parcial (adaptación de Scrum)")
    d.cell_set(t, "4. Planificar", 3, "Ramas por ticket, PR por revisión de otro integrante y CI; no hay backlog, sprints ni retrospectivas exportados. CoreStream (herramienta de Alloxentric) solo aporta un reporte agregado (EV-20).")
    d.cell_set(t, "5. Pruebas", 3, "214 + 91 pruebas verificadas el 17-nov, CI y E2E del 31-oct y 17-nov; latencia sin cumplir 1 s; TC-03, TC-04 y TC-17 con respaldo parcial (D05 v1.3).")

    # --- 9.5 plan
    p = P(d, "9.5 Plan hasta la evaluación", nth=1)
    d.set_par(p, "9.5 Plan hasta la entrega (estado al 19-nov)")
    t = tbl(d, "Actividad", "Estado al 17-nov", "Responsable sugerido")
    d.cell_set(t, "Obtener la pauta oficial", 1, "Guías 3.1 y 3.3 incorporadas (Fase 3/Pautas_Oficiales/); planillas de evaluación pendientes")
    d.cell_set(t, "Capturar la conversación", 1, "Hecho el 17-nov (EV-17, EV-21); cierre e historial de la sesión pendientes")
    d.cell_set(t, "Reunir backlog", 1, "Reporte agregado de CoreStream archivado (EV-20); backlog, tickets y actas pendientes")

    # --- 9.6 evidencias
    p = P(d, "Disponibles: D01 a D06 v1.1")
    d.set_par(p, "Disponibles: D01, D02, D03 y D06 v1.2, D05 v1.3, E01, logs E2E del 31-oct y del 17-nov con hash verificado, certificación del 17-nov, capturas de la Web Demo y de la conversación, DART-14-2.5 sanitizada (E10), reporte agregado de CoreStream (EV-20) y registro consolidado de evidencias. "
                 "Pendientes: planillas de evaluación de Fase 3, tickets y actas de CoreStream, transcripción del 2-sep y especificación atribuida a Max, guion y flujo de Hites, capturas del cierre de la llamada y pruebas con Asterisk. [CONFIRMADO]")
    d.at(p)
    d.para("Scrum. El equipo declaró Scrum en Fase 1 y lo aplicó de forma parcial: flujo Git por ticket con revisión de otro integrante y CI. No hay backlog, sprints, revisiones ni retrospectivas exportados, por lo que se describe como una adaptación parcial y no como una aplicación completa. [CONFIRMADO]")
    d.para("CoreStream. " + CORESTREAM_NOTE)
    d.para("Hitos. Los hitos comunicados en el expediente histórico (REG-04: MVP con base de datos, proyecto en Docker y entrega documentada) son planificación reconstruida (E2/P). En el repositorio técnico en 77ff85c no se encontró base de datos de negocio ni Dockerfile; el cumplimiento de los hitos no está acreditado. [CONFIRMADO]")

    # --- 10 referencias
    p = P(d, "Referencias: repositorio técnico en 77ff85c")
    d.set_par(p, "Referencias: repositorio técnico en 77ff85c (PR #1 a #17, #19 y #20; PR #18 abierto), D01, D02, D03 y D06 v1.2, D05 v1.3, Fase 3/07_Evidencias y Fase 3/MATRIZ_TRAZABILIDAD_PRELIMINAR.md.")

    out = OUT / "D04_Estado_de_Avance_del_Proyecto_v1.2_Fase3.docx"
    d.save(out)
    return out


if __name__ == "__main__":
    print(build())
