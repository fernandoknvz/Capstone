from fase3_common import *  # noqa: F401,F403
from fase3_docx_lib import Doc
from build_d03 import tbl


def build() -> Path:
    d = Doc(ORIG / "D05_Plan_de_Pruebas_y_Resultados.docx")
    d.capture_templates("1. Propósito y estrategia", "2.1 Resultado", "Define cómo se comprueba", "Requisito de 1 s", "Figura 1.", None)
    cover(d, "D05")
    control_row(d, change=(
        "Actualización de Fase 3 sobre una copia completa de la v1.0 (30-oct). Se corrigió la afirmación «no hay CI», se añadió la certificación del 17-nov sobre main (77ff85c), "
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

    # --- 5 catálogo
    t = tbl(d, "ID", "Caso", "Resultado esperado")
    d.cell_set(t, "TC-01", 4, "Sesiones del 30-oct (E01) y E2E del 31-oct (clínica dental); latencia sobre el requisito")
    d.cell_set(t, "TC-14", 4, "Mediana 2,59 s (n=13, 30-oct) y 2,74 s (n=5, 31-oct)")
    d.add_row(t, ["TC-19", "Un worker de desarrollo con otro nombre no atiende los despachos de la demo.", "Aislamiento por LIVEKIT_AGENT_NAME.", "Auto + OK", "test_agent_name.py (14); E2E del 31-oct con worker aislado"])
    d.add_row(t, ["TC-20", "La integración continua ejecuta pytest, Vitest, ESLint, TypeScript y build en cada PR y push a main.", "Workflow en verde.", "OK", "Runs 42433340255, 42433603292 y 42435613596 (success)"])
    d.add_row(t, ["TC-21", "Certificación local de las suites sobre main (77ff85c).", "214 Python y 91 web aprobadas; lint, tipos y build sin errores.", "OK", "Sección 2.4; certificación del 17-nov"])
    d.add_row(t, ["TC-22", "Conversación E2E desde la Web Demo con la persona clínica dental.", "Sesión sin errores con métricas por turno.", "OK*", "5 turnos E2E; 0 errores; latencia sobre el requisito"])

    # --- 7 defectos
    t = tbl(d, "Hallazgo", "Cómo se detectó", "Corrección")
    d.add_row(t, ["Un worker de desarrollo podía atender los despachos de la demo publicada", "Pruebas del 30-31-oct", "PR #17: nombre configurable (LIVEKIT_AGENT_NAME) y prueba automática", "Corregido"])
    d.add_row(t, ["Vitest no arranca en el equipo de la certificación (Node 22 y layout por defecto de pnpm)", "Certificación local del 17-nov", "Node 24.15.0 e instalación hoisted; el CI de Ubuntu pasó en verde", "Resuelto (solo local)"])

    # --- 8 limitaciones
    d.rep("No hay integración continua ni informe automático de cobertura.", "Hay integración continua desde el PR #19, pero no un informe automático de cobertura.")
    d.at(d.par("Las pruebas de cobranza usan datos ficticios"))
    d.bullet("Las mediciones de latencia disponibles son dos muestras pequeñas (E01, n=13; E2E 31-oct, n=5) y de una sola ubicación de red; no hay protocolo acordado con el cliente (sección 6).")
    d.bullet("La certificación del 17-nov se hizo en un solo equipo y no incluyó proveedores reales ni E2E; las capturas de la sección 10 provienen de un servidor local con valores ficticios.")

    # --- 9 evidencias
    t = tbl(d, "Código", "Archivo", "Contenido")
    d.add_row(t, ["E02", "Fase 3/07_Evidencias/E2E-2026-10-31-clinica-dental/worker-AJ_vzjEF7rJwWqB.sanitizado.log", "Log del worker del 31-oct, sanitizado. SHA-256 844E3492283B2EB9F40F5D97ACCFAE7B28694B64880726588D3B58A49B797B41 (verificado el 17-nov)."])
    d.add_row(t, ["E03", "Fase 3/07_Evidencias/E2E-2026-10-31-clinica-dental/netlify-cli.sanitizado.log", "Log de Netlify CLI del 31-oct, sanitizado. SHA-256 A5FE4E40B3553D3B664AE153CAF8B8930C3B38DBFA511675E7B6FCCF754FD6C3 (verificado el 17-nov)."])
    d.add_row(t, ["E04", "Fase 3/07_Evidencias/capturas-web-demo-2026-11-17/", "Cuatro capturas de la Web Demo (acceso, acceso rechazado, selección de agente e historial) del 17-nov, sin credenciales ni datos personales."])
    d.add_row(t, ["E05", "Fase 3/07_Evidencias/CERTIFICACION_PRUEBAS_2026-11-17.md", "Resultados de la certificación del 17-nov sobre main (77ff85c)."])
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
    d.para("[PENDIENTE] Faltan capturas de la conversación y la transcripción en vivo: requieren el worker en ejecución con credenciales reales de LiveKit, Google, el LLM y ElevenLabs, y consumen servicios de pago. Deben tomarse durante el ensayo de la demostración (guía D06) con un navegador, sin mostrar variables de entorno ni el código de acceso, y archivarse en Fase 3/07_Evidencias/capturas-web-demo-2026-11-17/.")
    d.h1("11. Conclusiones")
    d.para("Las pruebas automáticas están en verde sobre main: 214 de Python y 91 de la web, con lint, tipos, build y CSP verificados, además de la CI. El flujo de voz a voz funciona desde el navegador según dos sesiones reales (E01 y E2E del 31-oct), pero la latencia (mediana ≈2,6 a 2,7 s) no cumple el requisito de 1 s, no hay prueba con Asterisk ni validación con el guion oficial, y las verificaciones con proveedores y las mediciones no se repitieron el 17-nov. "
           "Antes de la presentación se recomienda ensayar la demostración completa, archivar sus logs y capturas y, si se dispone de tiempo, ampliar la muestra de latencia según el protocolo de la sección 6. [CONFIRMADO]")
    d.h1("12. Referencias")
    for x in ["D01 v1.1 (arquitectura y diseño), D03 v1.1 (requerimientos y casos de uso) y D06 v1.1 (operación), en Fase 3/Entregables.",
              "Repositorio técnico en el corte 77ff85c; workflow .github/workflows/ci.yml; ejecuciones 42433340255, 42433603292 y 42435613596.",
              "Fase 3/07_Evidencias: E01 (en Fase 2), logs E2E del 31-oct, capturas y certificación del 17-nov."]:
        d.bullet(x)
    out = OUT / "D05_Plan_de_Pruebas_y_Resultados_v1.1_Fase3.docx"
    d.save(out)
    return out


if __name__ == "__main__":
    print(build())
