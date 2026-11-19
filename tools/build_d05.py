from fase3_common import *  # noqa: F401,F403
from fase3_docx_lib import Doc
from build_d03 import tbl


def build() -> Path:
    d = Doc(ORIG / "D05_Plan_de_Pruebas_y_Resultados.docx")
    d.capture_templates("1. Propósito y estrategia", "2.1 Resultado", "Define cómo se comprueba", "Requisito de 1 s", "Figura 1.", None)
    cover(d, "D05", version="1.2", date=DATE_DS)
    control_row(d, version="1.2", date=DATE_DS, change=(
        "Versión 1.2: consolida la v1.1 (17-nov) y agrega la sesión E2E del 17-nov con DeepSeek (caso TC-23, sección 4.7, evidencias E06 a E09 y capturas de la conversación en la sección 10). Se parte de una copia completa de la v1.0 (30-oct); la v1.1 se conserva sin cambios. Contenido de la v1.1: Se corrigió la afirmación «no hay CI», se añadió la certificación del 17-nov sobre main (77ff85c), "
        "la sesión E2E del 31-oct, las pruebas test_agent_name.py (214), los casos TC-19 a TC-22, hallazgos nuevos, evidencias E02 a E05 y la sección de evidencias visuales de la Web Demo. "
        "Los resultados históricos del 30-oct se conservan y se distinguen de las ejecuciones nuevas. La v1.0 se conserva sin cambios en Fase 2."))

    # --- 2.1
    r = d.par("Ejecutadas el 30 de octubre de 2026")
    d.set_par(r, "Resultado histórico del 30 de octubre de 2026 sobre la rama del PR #16: 200 pruebas de Python y 91 de la web, todas aprobadas (uv run pytest y pnpm test), además de tsc, ESLint y el build de producción sin errores. [CONFIRMADO] "
                 "En esa fecha no había integración continua: los resultados se obtuvieron en el equipo del autor sin registro de CI. [CONFIRMADO] La CI se incorporó el 7-nov (PR #19 y #20) y el 17-nov se ejecutó una certificación nueva sobre main (sección 2.4). [CONFIRMADO]")
    d.rep("Inventario Python (200)", "Inventario Python (214 al 17-nov; 200 al 30-oct)")
    t = tbl(d, "Archivo", "Pruebas", "Qué cubre")
    d.add_row(t, ["tests/test_agent_name.py", "14", "Nombre del agente LiveKit configurable y aislamiento de workers de desarrollo (PR #17; no existía el 30-oct)."])

    # --- 2.4 certificación (antes de «3. Verificaciones manuales»)
    h3 = d.par("3. Verificaciones manuales")
    d.at(h3._p.getprevious())
    d.h2("2.4 Certificación del 17 de noviembre de 2026 sobre main (nueva ejecución)")
    d.para("[CONFIRMADO] Se ejecutaron las suites y los controles de calidad sobre una copia limpia de origin/main en el commit 77ff85c (git archive), sin modificar el repositorio técnico y sin credenciales ni proveedores reales. No se repitieron E2E ni verificaciones manuales con proveedores; los resultados de las secciones 3 y 4 siguen siendo históricos. Entorno: Windows 11, Python 3.12.6 con uv 0.12.23 (uv.lock), Node 24.15.0 y pnpm 9.15.9 (lockfile).")
    d.table_new(["Verificación", "Resultado del 17-nov", "Entorno / fuente"], CERT_TABLE, [4.6, 8.4, 3.8])
    d.para("[CONFIRMADO] Incidencia de entorno: Vitest no arrancó con Node 22.20.0 (el proyecto exige 24.x) ni con el layout por defecto de pnpm en este equipo (ERR_PACKAGE_IMPORT_NOT_DEFINED); con Node 24.15.0 y la instalación --node-linker=hoisted las 91 pruebas pasaron. ESLint, TypeScript y el build pasaron en todas las configuraciones y el CI de Ubuntu concluyó en verde. La causa es probablemente del entorno local. [INFERENCIA] El detalle por archivo está en Fase 3/07_Evidencias/CERTIFICACION_PRUEBAS_2026-11-17.md.")
    d.table_new(["Corte", "Python", "Web", "Naturaleza del resultado"], [
        ["PR #16 (30-oct)", "200", "91", "Histórico, ejecutado por el autor; sin CI"],
        ["PR #17 (31-oct)", "214", "No informado", "Histórico declarado en el PR"],
        ["PR #18 (4-nov, abierto)", "281", "103", "Rama NO integrada; no comparable con main"],
        ["main 77ff85c (17-nov)", "214", "91", "Nueva ejecución local y CI en verde (run 42435613596)"],
    ], [4.2, 2.2, 2.2, 8.2])

    # --- 3: nota
    d.at(d.table("Script"))
    d.para("[CONFIRMADO] Las verificaciones de esta sección son históricas (octubre). El 17-nov no se repitieron porque consumen servicios de pago y requieren credenciales del equipo.")

    # --- 4.6 E2E 31-oct (antes de «5. Catálogo»)
    h5 = d.par("5. Catálogo de casos de prueba")
    d.at(h5._p.getprevious())
    d.h2("4.6 Sesión E2E del 31 de octubre (clínica dental)")
    d.para("[CONFIRMADO] Fuente: log del worker y log de Netlify CLI sanitizados (SHA-256 en la sección 9). Conversación desde la Web Demo local con voz humana de un hablante, worker de desarrollo aislado por nombre (PR #17), commit d80c419, record=False. Es una sesión independiente de E01: sus cifras no se combinan con las del 30-oct.")
    d.table_new(["Indicador", "Resultado"], E2E_TABLE, [5.2, 11.4])
    d.figure(FIG / "fig_latencia_actualizada.png", "Figura 2. Latencia de voz a voz (E01 y E2E del 31-oct) frente al requisito de 1 s. Las muestras no se combinan. Fuente: E01 y log del worker del 31-oct.", 16.2)
    d.bullet("Requisito de 1 s: ninguno de los 5 turnos con E2E lo cumple (mínimo 1,191 s). No se cumple.")
    d.bullet("Riesgo de corte (> 3 s): 1 de 5 turnos (3,352 s).")
    d.bullet("Etapas (medianas): espera de la transcripción final 1,126 s, primer token del LLM 1,093 s y primer audio 0,318 s; coinciden en orden de magnitud con E01 (1,21 s, 0,93 s y 0,31 s).")
    d.bullet("Alcance: una sesión, una persona, un hablante, 5 muestras E2E y sin reloj externo; no sirve como validación estadística ni cubre las otras seis personas ni telefonía.")

    # --- 4.7 E2E 17-nov DeepSeek
    d.h2("4.7 Sesión E2E del 17 de noviembre (clínica dental, DeepSeek)")
    d.para("[CONFIRMADO] Fuente: log del worker y log de Netlify CLI sanitizados, registro de evidencias y capturas del video (carpeta " + EV_DS + "). Conversación desde la Web Demo local con voz humana de un hablante y worker local de desarrollo. Dictamen: APROBADO CON OBSERVACIONES. Es una sesión independiente de E01 y de la del 31-oct (que usó Gemini): sus cifras no se combinan. Dos intentos previos del mismo día con Gemini fallaron por API_KEY_INVALID (jobs AJ_85xF2YcY3Thz y AJ_FfgnQQhpXcrz, sin respuestas del LLM); el cambio de proveedor a DeepSeek es una decisión PROPUESTA del equipo, sin acta de aprobación del cliente.")
    d.table_new(["Indicador", "Resultado"], E2E_DS_TABLE, [5.2, 11.4])
    d.bullet("Requisito de 1 s: NO CUMPLIDO. Solo 2 de 8 turnos medidos lo alcanzan y ambos coinciden con transcripción disponible antes del cierre del turno (transcription_delay_s = 0), no con un LLM más rápido. [INFERENCIA]")
    d.bullet("Latencia dominada por el primer token del LLM (0,94 a 2,48 s) y la espera de la transcripción final (≈1,2 a 1,5 s); 771 de 1.050 tokens de salida son de razonamiento (73 %). [INFERENCIA: su aporte al TTFT no se aisló]")
    d.bullet("Verificado en log: conexión LiveKit, STT, detección de fin de turno, LLM, TTS y cierre limpio. Verificado en capturas del video: transcripción en vivo y continuidad de hasta 15 mensajes (sección 10). No verificable en logs: audio audible e historial de esta sesión en el navegador. [REPORTADO]")
    d.bullet("Alcance: una sesión, n=8 turnos con E2E, voz no controlada y sin reloj externo. El agendamiento es simulado: no hay reservas reales ni integración con Asterisk ni persistencia empresarial.")

    # --- 5 catálogo
    t = tbl(d, "ID", "Caso", "Resultado esperado")
    d.cell_set(t, "TC-01", 4, "Sesiones del 30-oct (E01) y E2E del 31-oct (clínica dental); latencia sobre el requisito")
    d.cell_set(t, "TC-14", 4, "Mediana 2,59 s (n=13, 30-oct), 2,74 s (n=5, 31-oct) y 3,26 s (n=8, 17-nov)")
    d.add_row(t, ["TC-19", "Un worker de desarrollo con otro nombre no atiende los despachos de la demo.", "Aislamiento por LIVEKIT_AGENT_NAME.", "Auto + OK", "test_agent_name.py (14); E2E del 31-oct con worker aislado"])
    d.add_row(t, ["TC-20", "La integración continua ejecuta pytest, Vitest, ESLint, TypeScript y build en cada PR y push a main.", "Workflow en verde.", "OK", "Runs 42433340255, 42433603292 y 42435613596 (success)"])
    d.add_row(t, ["TC-21", "Certificación local de las suites sobre main (77ff85c).", "214 Python y 91 web aprobadas; lint, tipos y build sin errores.", "OK", "Sección 2.4; certificación del 17-nov"])
    d.add_row(t, ["TC-22", "Conversación E2E desde la Web Demo con la persona clínica dental.", "Sesión sin errores con métricas por turno.", "OK*", "5 turnos E2E; 0 errores; latencia sobre el requisito"])
    d.add_row(t, ["TC-23", "Conversación E2E con DeepSeek: persona clínica dental, Web Demo local y worker local (17-nov).", "Conversación E2E completa (saludo y respuestas generadas) sin errores de sesión. El cumplimiento temporal (≤ 1 s) se evalúa aparte en TC-14.", "OK*", "Sección 4.7; E06 a E08; 10 turnos del agente (1 saludo estático + 9 respuestas), errors {}; agendamiento simulado. Latencia: ver TC-14 (NO CUMPLIDA: media 2,96 s, mediana 3,26 s, 2 de 8 turnos ≤ 1 s)"])

    # --- 7 defectos
    t = tbl(d, "Hallazgo", "Cómo se detectó", "Corrección")
    d.add_row(t, ["Un worker de desarrollo podía atender los despachos de la demo publicada", "Pruebas del 30-31-oct", "PR #17: nombre configurable (LIVEKIT_AGENT_NAME) y prueba automática", "Corregido"])
    d.add_row(t, ["Dos intentos previos del 17-nov con Gemini fallaron por API_KEY_INVALID (sin respuestas del LLM)", "Logs del worker del 17-nov (jobs AJ_85xF2YcY3Thz y AJ_FfgnQQhpXcrz)", "Cambio de proveedor a DeepSeek (decisión PROPUESTA del equipo, sin acta del cliente)", "Resuelto para la demostración"])
    d.add_row(t, ["Dos solicitudes POST /api/livekit-token (201) por un único job; también el 31-oct", "Log de Netlify CLI del 17-nov", "Sin investigar", "Pendiente"])
    d.add_row(t, ["Aviso «transcript arrives after turn has been committed» en el turno 2 (interrumpido)", "Log del worker del 17-nov", "El SDK sugiere subir min_delay del endpointing; no se aplicó", "Pendiente"])
    d.add_row(t, ["Vitest no arranca en el equipo de la certificación (Node 22 y layout por defecto de pnpm)", "Certificación local del 17-nov", "Node 24.15.0 e instalación hoisted; el CI de Ubuntu pasó en verde", "Resuelto (solo local)"])

    # --- 8 limitaciones
    d.rep("No hay integración continua ni informe automático de cobertura.", "Hay integración continua desde el PR #19, pero no un informe automático de cobertura.")
    d.at(d.par("Las pruebas de cobranza usan datos ficticios"))
    d.bullet("Las mediciones de latencia disponibles son tres muestras pequeñas (E01, n=13; E2E 31-oct, n=5; E2E 17-nov, n=8) y de una sola ubicación de red; no hay protocolo acordado con el cliente (sección 6).")
    d.bullet("La sesión del 17-nov usó voz humana no controlada, worker local de desarrollo y un solo proveedor de LLM (DeepSeek); el agendamiento es simulado (sin reservas reales, Asterisk ni persistencia empresarial) y el worker persistente sigue pendiente.")
    d.bullet("La certificación del 17-nov se hizo en un solo equipo y no incluyó proveedores reales ni E2E; las capturas de la sección 10 provienen de un servidor local con valores ficticios.")

    # --- 9 evidencias
    t = tbl(d, "Código", "Archivo", "Contenido")
    d.add_row(t, ["E02", "Fase 3/07_Evidencias/E2E-2026-10-31-clinica-dental/worker-AJ_vzjEF7rJwWqB.sanitizado.log", "Log del worker del 31-oct, sanitizado. SHA-256 844E3492283B2EB9F40F5D97ACCFAE7B28694B64880726588D3B58A49B797B41 (verificado el 17-nov)."])
    d.add_row(t, ["E03", "Fase 3/07_Evidencias/E2E-2026-10-31-clinica-dental/netlify-cli.sanitizado.log", "Log de Netlify CLI del 31-oct, sanitizado. SHA-256 A5FE4E40B3553D3B664AE153CAF8B8930C3B38DBFA511675E7B6FCCF754FD6C3 (verificado el 17-nov)."])
    d.add_row(t, ["E04", "Fase 3/07_Evidencias/capturas-web-demo-2026-11-17/", "Cuatro capturas de la Web Demo (acceso, acceso rechazado, selección de agente e historial) del 17-nov, sin credenciales ni datos personales."])
    d.add_row(t, ["E05", "Fase 3/07_Evidencias/CERTIFICACION_PRUEBAS_2026-11-17.md", "Resultados de la certificación del 17-nov sobre main (77ff85c)."])
    d.add_row(t, ["E06", EV_DS + "README.md", "Registro de evidencias E2E del 17-nov con DeepSeek (dictamen, métricas, hallazgos, capturas y verificación cruzada). SHA-256 en SHA256SUMS.txt de esa carpeta."])
    d.add_row(t, ["E07", EV_DS + "worker-AJ_zm9g5TDNqgG5.sanitizado.log y netlify-cli.sanitizado.log", "Logs sanitizados del 17-nov. SHA-256 D7525A212FBC4DD467980021D4A895E04F54B2ED8B4FED33C9A9078557016649 (worker) y 00DDF21D1DBC350639C05F494431DD21DB08F46D33D3846961F4F3AC175BCA6C (Netlify)."])
    d.add_row(t, ["E08", EV_DS + "capturas/", "Cinco capturas recortadas del video de la sesión del 17-nov, sin credenciales ni datos personales."])
    d.add_row(t, ["E09", "Video original (fuera de Git)", "Grabación de pantalla de la sesión (173,2 s). SHA-256 D6FE9270F86BACAB76231FC8EA103DAD0B88E8BDC486BBFDE3AB7457ED5CABFA. No se incorpora al repositorio porque expone datos del equipo."])
    d.cell_set(t, "E01", 2, "5 sesiones y 22 turnos del worker, solo valores numéricos de latencia y uso; sin texto de conversaciones, audio ni secretos. SHA-256 69AF78CA176BDFB944D95D3A02B61F63EEC8280DED2362644BA525FED4A71C7A (verificado el 17-nov).")

    # --- nuevas secciones al final
    d.at_end()
    d.h1("10. Evidencias visuales de la Web Demo")
    d.para("[CONFIRMADO] Las capturas son del producto en funcionamiento (no mockups previos al desarrollo). Se tomaron el 17-nov-2026 sirviendo la exportación estática de main (77ff85c) con las funciones reales de login y sesión y secretos ficticios generados para la captura; no se usaron credenciales del equipo ni datos personales reales. "
           "El historial de la Figura 6 se pobló con dos conversaciones sintéticas de texto marcado [Texto sintético de captura] para mostrar la interfaz. Los escenarios de cobranza muestran nombres y montos ficticios definidos en el propio producto.")
    d.figure(SHOT / "01_acceso.png", "Figura 3. Pantalla de acceso con código temporal. Fuente: captura del 17-nov-2026 (main 77ff85c).", 14.5)
    d.figure(SHOT / "02_acceso_rechazado.png", "Figura 4. Acceso con un código incorrecto: el servidor responde 401 y la interfaz muestra el error. Fuente: captura del 17-nov-2026.", 14.5)
    d.figure(SHOT / "03_seleccion_agente.png", "Figura 5. Selección de agente (7 personas) e historial vacío. Fuente: captura del 17-nov-2026 (nombre del deudor ficticio de una tarjeta omitido).", 12.0)
    d.figure(SHOT / "04_historial.png", "Figura 6. Historial local con dos conversaciones sintéticas. Fuente: captura del 17-nov-2026.", 12.0)
    d.h2("10.1 Conversación E2E del 17 de noviembre (DeepSeek)")
    d.para("[CONFIRMADO] Las figuras 7 a 11 son fotogramas del video de la sesión AJ_zm9g5TDNqgG5, recortados al área de la aplicación para excluir el navegador y el escritorio del equipo; no se retocó su interior. Muestran la pantalla del cliente: no prueban el audio ni la latencia (que constan en el log). La grabación contiene nombres pronunciados durante la demostración. No se dispone de evidencia suficiente para verificar su carácter ficticio. El agendamiento es simulado: la frase «queda reservada» es conversacional y no corresponde a una reserva real.")
    d.figure(SHOT_DS / "captura-01-interfaz-inicial-t000s.png", "Figura 7. Interfaz inicial con el campo de código de acceso vacío (video, 0:00). Fuente: sesión del 17-nov-2026.", 12.5)
    d.figure(SHOT_DS / "captura-02-conversacion-saludo-t030s.png", "Figura 8. Llamada activa con la persona clínica dental: el saludo del agente aparece parcial por la transcripción en streaming (video, 0:30). Fuente: sesión del 17-nov-2026.", 12.5)
    d.figure(SHOT_DS / "captura-03-respuestas-generadas-t060s.png", "Figura 9. Transcripción en vivo con cinco mensajes y una respuesta sobre horarios; el mensaje «Hola, Juan,» truncado es coherente con el turno 2 interrumpido (video, 1:00). Fuente: sesión del 17-nov-2026.", 12.5)
    d.figure(SHOT_DS / "captura-04-continuidad-turnos-9-mensajes-t090s.png", "Figura 10. Continuidad con nueve mensajes: el agente declara que no tiene la agenda de un profesional y repite los horarios (video, 1:30). Fuente: sesión del 17-nov-2026.", 12.5)
    d.figure(SHOT_DS / "captura-05-continuidad-turnos-15-mensajes-t140s.png", "Figura 11. Continuidad con quince mensajes: restricción de horario, oferta de alternativas y agendamiento simulado (video, 2:20). Fuente: sesión del 17-nov-2026.", 12.5)
    d.para("[PENDIENTE] No hay capturas del cierre de la llamada ni del historial de esta sesión: el tramo final del video muestra un nombre completo pronunciado durante la demostración y requeriría enmascararlo. Las capturas de las figuras 3 a 6 provienen de un servidor local con valores ficticios.")
    d.h1("11. Conclusiones")
    d.para("Las pruebas automáticas están en verde sobre main: 214 de Python y 91 de la web, con lint, tipos, build y CSP verificados, además de la CI. El flujo de voz a voz funciona desde el navegador según tres fuentes de medición (E01, E2E del 31-oct con Gemini y E2E del 17-nov con DeepSeek, esta última aprobada con observaciones, con 9 respuestas generadas y sin errores), pero la latencia (medianas ≈2,6 a 3,3 s) no cumple el requisito de 1 s (2 de 8 turnos en la última sesión). "
           "El agendamiento es simulado: no hay reservas reales, integración con Asterisk, persistencia empresarial ni worker persistente, y tampoco validación con el guion oficial. Antes de la presentación se recomienda ensayar la demostración completa, archivar sus logs y capturas y, si se dispone de tiempo, ampliar la muestra de latencia según el protocolo de la sección 6. [CONFIRMADO]")
    d.h1("12. Referencias")
    for x in ["D01 v1.1 (arquitectura y diseño), D03 v1.1 (requerimientos y casos de uso) y D06 v1.1 (operación), en Fase 3/Entregables.",
              "Repositorio técnico en el corte 77ff85c; workflow .github/workflows/ci.yml; ejecuciones 42433340255, 42433603292 y 42435613596.",
              "Fase 3/07_Evidencias: E01 (en Fase 2), logs E2E del 31-oct, capturas y certificación del 17-nov, y evidencias E2E DeepSeek del 17-nov (carpeta E2E-2026-11-17-clinica-dental-deepseek)."]:
        d.bullet(x)
    out = OUT / "D05_Plan_de_Pruebas_y_Resultados_v1.2_Fase3.docx"
    d.save(out)
    return out


if __name__ == "__main__":
    print(build())
