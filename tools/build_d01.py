from fase3_common import *  # noqa: F401,F403
from fase3_docx_lib import Doc


def build() -> Path:
    d = Doc(ORIG / "D01_Arquitectura_de_la_Solucion.docx")
    d.capture_templates("1. Propósito y alcance", "1.1 Qué problema resuelve", "Este documento describe",
                        "Telefonía. No hay", "Figura 1.", "1. La persona elige")
    cover(d, "D01")
    control_row(d, change=(
        "Actualización de Fase 3 sobre una copia completa de la v1.0 (30-oct). Corte técnico: origin/main 77ff85c (PR #1 a #17, #19 y #20). "
        "Se actualizaron estados de AD-10 a AD-13 (PR #16 fusionado), se añadieron AD-14 a AD-16, la CI, la certificación del 17-nov, "
        "los resultados E2E del 31-oct y la vista de diseño verificable (casos de uso, actividad, módulos y clases, almacenamiento). "
        "La v1.0 se conserva sin cambios en Fase 2."))

    # ------------------------------------------------------------------ §1.2 alcance
    t = d.table("Elemento")
    d.cell_set(t, "Escenarios de práctica", 1, "Implementados e integrados en main (PR #16, fusionado el 30-oct); 7 personas, una con E2E archivado (clínica dental)")
    d.cell_set(t, "Escenarios de práctica", 2, "[CONFIRMADO]")
    d.at(d.par("[CONFIRMADO] En la reunión inicial"))
    d.para("[CONFIRMADO] Actualización del 17-nov-2026: el estado descrito en este documento corresponde a origin/main en el commit 77ff85c (PR #1 a #17, #19 y #20 fusionados). "
           "El PR #18 sigue abierto, sin revisión registrada, y NO forma parte de esta arquitectura (sección 11).")

    # ------------------------------------------------------------------ §2
    d.rep("Fuente: elaboración propia a partir del repositorio técnico (rama del PR #16).",
          "Fuente: elaboración propia a partir del repositorio técnico. Figura original del 30-oct; sigue representando la arquitectura integrada en main (77ff85c).")
    t = d.table("Componente")
    d.cell_set(t, "Worker del agente", 2, "Recibe el job, arma la sesión de voz, aplica la persona y mide la latencia. El nombre del agente es configurable con LIVEKIT_AGENT_NAME (PR #17).")
    d.add_row(t, ["Integración continua", "GitHub Actions (ubuntu-24.04, uv 0.12.23, pnpm 9.15.9, Node 24.15.0)", "pytest, Vitest, ESLint, TypeScript, build de Next.js y verificación de la CSP en cada PR y push a main. Sin secretos ni despliegue.", ".github/workflows/ci.yml"])

    # ------------------------------------------------------------------ §3
    d.at(d.par("6. El audio de respuesta"))
    d.para("[CONFIRMADO] Desde el PR #17 el nombre del agente se resuelve con LIVEKIT_AGENT_NAME (por defecto, el de la demo publicada). Un worker de desarrollo con otro nombre no atiende los despachos de la demo y viceversa, lo que evita sesiones cruzadas entre integrantes.")

    # ------------------------------------------------------------------ §4 decisiones
    t = d.table("ID")
    for ad, est in (("AD-10", "[CONFIRMADO] fusionada (PR #16, 30-oct)"), ("AD-11", "[CONFIRMADO] fusionada (PR #16, 30-oct); sin aprobación del cliente"),
                    ("AD-12", "[CONFIRMADO] fusionada (PR #16, 30-oct)"), ("AD-13", "[CONFIRMADO] fusionada (PR #16, 30-oct)")):
        d.cell_set(t, ad, 4, est)
    d.add_row(t, ["AD-14", "31-oct (PR #17)", "Nombre del agente LiveKit configurable con LIVEKIT_AGENT_NAME.", "Evita que un worker de desarrollo atienda los despachos de la demo o reciba sesiones ajenas. Prueba: test_agent_name.py (14).", "[CONFIRMADO] fusionada"])
    d.add_row(t, ["AD-15", "7-nov (PR #19, #20)", "Integración continua con GitHub Actions (jobs python-tests y web-quality), sin secretos, despliegue ni proveedores.", "Automatizar el control de calidad exigido por el flujo Git (AD-01). Documentado en docs/validation/DART-14-5.6-CI-github-actions.md.", "[CONFIRMADO] fusionadas; PR #19 sin aprobación independiente"])
    d.add_row(t, ["AD-16", "4-nov (PR #18)", "Alternativas de LLM (Anthropic, LiveKit Inference) y STT seleccionable (Deepgram, Speechmatics) con muletillas y calentamiento.", "Reducir la latencia (cuello de botella: transcripción final). 281 pruebas Python y 103 web declaradas en la rama; medición con audio sintético.", "[PROPUESTA] PR abierto, sin revisión; NO integrada"])

    # ------------------------------------------------------------------ §5 seguridad
    t = d.table("Control")
    d.cell_set(t, "Persona validada", 2, "[CONFIRMADO] (PR #16 fusionado)")
    d.cell_set(t, "Origen de la petición", 2, "[CONFIRMADO] (PR #16 fusionado)")
    d.add_row(t, ["Pipeline de CI sin privilegios", "El workflow solo tiene permissions: contents: read, checkout sin credenciales persistentes, acciones fijadas por SHA y ninguna variable secreta.", "[CONFIRMADO]"])

    # ------------------------------------------------------------------ §6 latencia
    d.at(d.table("Las etapas se solapan"))
    d.para("[CONFIRMADO] Actualización del 17-nov: la sesión E2E del 31 de octubre (clínica dental, voz humana, un hablante, commit d80c419) registró 5 turnos con e2e_latency_s: media 2,330 s, mediana 2,741 s, rango 1,191 a 3,352 s y 0 errores. "
           "Es una muestra aún menor que E01 y de un solo agente; confirma el orden de magnitud (≈2,6 a 2,7 s) pero no demuestra cumplimiento del requisito de 1 s ni constituye validación estadística. No se mezclan las muestras de E01 y del 31-oct.")
    d.table_new(["Fuente", "Fecha", "n (turnos E2E)", "Mediana", "Rango", "Observación"], [
        ["E01 (5 sesiones, 22 turnos)", "30-oct", "13", "2,5941 s", "0,4775 a 4,0839 s", "Mezcla voz humana y sintética; 3 turnos sobre 3 s"],
        ["E2E clínica dental", "31-oct", "5", "2,7411 s", "1,1912 a 3,3519 s", "Una sesión; sin reloj externo ni grabación"],
        ["Requisito de Alloxentric", "2-sep", "—", "≤ 1 s", "—", "Sobre 3 s la persona puede cortar"],
    ], [3.6, 1.6, 2.2, 2.0, 3.0, 5.4])
    d.figure(FIG / "fig_latencia_actualizada.png", "Figura 4. Latencia de voz a voz medida (E01 y E2E del 31-oct) frente al requisito. Las muestras no se combinan. Fuente: E01 y log del worker del 31-oct (SHA-256 en D05).", 16.2)

    # ------------------------------------------------------------------ §7 despliegue
    t = d.table("Entorno")
    d.cell_set(t, "Demo en Vercel", 2, "Juan. [CONFIRMADO] desplegado el 30-oct; código fusionado en main (PR #16)")
    d.add_row(t, ["CI en GitHub Actions", "Pruebas Python y calidad web en cada PR y push a main; sin despliegue.", "Fernando. [CONFIRMADO] run 42435613596 (success) sobre 77ff85c"])

    # ------------------------------------------------------------------ §8 calidad
    t = d.table("Atributo")
    d.cell_set(t, "Mantenibilidad", 1, "Módulos pequeños, tipado y pruebas automatizadas: 214 de Python y 91 de la web, ejecutadas el 17-nov sobre main (77ff85c), además de la CI desde el PR #19.")
    d.cell_set(t, "Mantenibilidad", 2, "D05 §2.4; run de CI 42435613596")

    # ------------------------------------------------------------------ §9 limitaciones
    d.at(d.par("Cumplimiento."))
    d.bullet("Persistencia. No existe base de datos ni persistencia de negocio: el historial vive en localStorage y las métricas en logs (sección 10.5). [PENDIENTE]")
    d.bullet("Trabajo no integrado. Anthropic, LiveKit Inference y el STT seleccionable (PR #18) siguen en un PR abierto y no se consideran parte de la arquitectura vigente. [PENDIENTE DE VALIDACIÓN]")
    d.bullet("Latencia. Las dos muestras disponibles (E01 y E2E del 31-oct) rondan 2,6 a 2,7 s de mediana; falta un protocolo de medición acordado y una muestra mayor. [PROPUESTA]")

    # ------------------------------------------------------------------ nuevas secciones (antes de Referencias)
    ref = d.par("10. Referencias")
    d.at(ref._p.getprevious())
    d.h1("10. Vista de diseño verificable en main")
    d.para("Esta sección documenta el diseño tal como existe en origin/main (77ff85c). Cada elemento se derivó del código y de las pruebas; no se añadieron entidades, tablas, relaciones ni endpoints que el código no tenga. Lo que no existe se declara expresamente.")
    d.h2("10.1 Casos de uso")
    d.para("Los casos de uso UC-01 a UC-11 están implementados y se detallan, con su trazabilidad a requisitos y pruebas, en D03 (sección 11). La Figura 5 los resume; los casos UP-1 a UP-4 se muestran fuera del límite del sistema porque no tienen implementación.")
    landscape_figure(d, FIG / "fig_casos_uso.png", "Figura 5. Casos de uso del sistema implementado en main y casos pendientes. Fuente: elaboración propia a partir de D03 (RF, HU) y del código.")
    d.h2("10.2 Diagrama de actividad del agente")
    d.para("La Figura 6 describe la actividad del worker desde que recibe el job de LiveKit hasta el cierre. Está basada en agent.py (entrypoint), pipeline.py (build_agent_session, TURN_HANDLING, attach_observability) y metrics.py. Los puntos de decisión corresponden a validaciones reales del código: persona dentro de la lista cerrada (si no, agente de prueba), configuración completa (MissingConfigurationError) y detección de fin de turno/interrupción por la sesión de LiveKit.")
    landscape_figure(d, FIG / "fig_actividad_agente.png", "Figura 6. Diagrama de actividad del worker del agente. Fuente: agent.py, pipeline.py y metrics.py (77ff85c).")
    d.h2("10.3 Módulos y clases del worker (Python)")
    d.para("El código es principalmente funcional. Las clases existentes son cinco dataclasses de configuración (LiveKitSettings, DeepSeekSettings, ElevenLabsSettings, GeminiSettings, GoogleSTTSettings), Persona (dataclass inmutable con siete instancias), SessionMetrics y tres excepciones (MissingConfigurationError, InvalidConfigurationError, MissingCredentialsError). No hay entidades de dominio de cobranza.")
    d.table_new(["Módulo", "Responsabilidad", "Pruebas automáticas"], [
        ["agent.py", "Punto de entrada: AgentServer, setup_process (ADC y VAD) y entrypoint(ctx); aplica la persona y reproduce el saludo.", "test_project_bootstrap.py (3), test_agent_name.py (14)"],
        ["pipeline.py", "Compone STT, LLM y TTS en una AgentSession; TURN_HANDLING; observabilidad sin datos sensibles.", "test_pipeline.py (32), test_latency_settings.py (13)"],
        ["config.py", "Carga y valida variables de entorno; resuelve proveedor LLM y nombre del agente.", "test_config.py (6), test_agent_name.py"],
        ["personas.py", "Siete personas (guion, saludo y voz) y su construcción de instrucciones.", "test_personas.py (26), test_voices.py (28)"],
        ["stt.py", "Google Cloud Speech-to-Text v2 (Chirp 3) con ADC.", "test_stt.py (14)"],
        ["tts.py · llm.py · llm_gemini.py", "Construyen ElevenLabs, DeepSeek y Gemini con los plugins oficiales.", "test_tts.py (14), test_llm.py (9), test_llm_gemini.py (15)"],
        ["voice_warmup.py", "Precalienta las voces al iniciar el worker.", "test_voices.py"],
        ["metrics.py", "SessionMetrics: métricas numéricas por turno y resumen de uso por sesión.", "test_metrics.py (40)"],
    ], [3.4, 8.0, 5.0])
    landscape_figure(d, FIG / "fig_clases_python.png", "Figura 7. Módulos y clases del paquete alloxentric_real_time_agent. Fuente: src/alloxentric_real_time_agent/ (77ff85c).")
    d.h2("10.4 Módulos de la Web Demo")
    d.para("La Web Demo es una exportación estática de Next.js; el acceso, la sesión y el token se resuelven en cuatro funciones serverless (login, session, logout y livekit-token), con dos adaptadores equivalentes (Netlify y Vercel) que comparten lib/server/. Ninguna función aloja el worker.")
    landscape_figure(d, FIG / "fig_modulos_web.png", "Figura 8. Módulos de la Web Demo y funciones serverless. Fuente: web-demo/ (77ff85c).")
    d.h2("10.5 Modelo del almacenamiento actual")
    d.para("[CONFIRMADO] El sistema no tiene base de datos ni persistencia de negocio. Los únicos datos que se conservan son: (1) el historial de conversaciones en localStorage del navegador (HistoryEntry con hasta 400 HistoryMessage; límites de 30 conversaciones y 2.000 caracteres por mensaje), (2) la cookie de sesión firmada y (3) los logs de métricas del worker, que contienen solo valores numéricos. Los montos y deudores de los escenarios de cobranza son texto ficticio dentro de las instrucciones de cada Persona.")
    d.table_new(["Almacenamiento", "Ubicación", "Contenido", "Retención"], [
        ["localStorage 'alloxentric-demo-history-v1'", "Navegador del evaluador", "HistoryEntry { id, personaId, startedAt, messages[] } y HistoryMessage { id, role, text, timestamp }", "Hasta 30 conversaciones; el usuario puede borrarlas. Nunca se envía a un servidor."],
        ["Cookie __Host-alloxentric-demo", "Navegador", "JWT firmado (sin identidad ni datos personales)", "DEMO_SESSION_TTL_SECONDS (1.800 s por defecto); HttpOnly, Secure, SameSite=Strict"],
        ["Logs de métricas", "Proceso del worker", "Campos numéricos *_s por turno y resumen de uso (tokens, caracteres, segundos)", "Logger local; E01 y E2E 31-oct son extractos archivados"],
    ], [4.2, 3.0, 6.0, 4.4])
    landscape_figure(d, FIG / "fig_almacenamiento.png", "Figura 9. Modelo del almacenamiento actual y elementos ausentes. Fuente: web-demo/lib/history.ts, web-demo/lib/server/session.ts y metrics.py (77ff85c).")
    d.h2("10.6 Integración continua")
    d.para("El workflow .github/workflows/ci.yml define dos jobs independientes que se ejecutan en pull_request hacia main, en push a main y manualmente. Las ejecuciones 42433340255 (PR #19) y 42433603292 (main tras PR #19) y 42435613596 (main, 77ff85c) concluyeron con éxito. El alcance es solo estático/unitario: no ejecuta E2E, proveedores de IA ni despliegues.")
    d.figure(FIG / "fig_ci.png", "Figura 10. Flujo de integración continua. Fuente: .github/workflows/ci.yml (77ff85c).", 16.2)

    d.h1("11. Trabajo no integrado: PR #18")
    d.para("[PROPUESTA] El PR #18 (feat DART-14-5.2, abierto desde el 4-nov, sin revisiones registradas, un commit) agrega los LLM Anthropic y LiveKit Inference, un STT seleccionable (Deepgram Flux y Speechmatics Linden además de Chirp 3), un selector web de STT, muletillas habladas y calentamiento del LLM. Sus conteos (281 pruebas de Python y 103 de la web) y su medición con audio sintético describen la rama del PR y no el estado de main. "
           "Hasta que se revise y se fusione no debe presentarse como parte de la solución ni como evidencia de cumplimiento de latencia. [PENDIENTE DE VALIDACIÓN]")

    d.h1("12. Conclusiones")
    d.para("La arquitectura integrada en main cumple su objetivo técnico de demostrar una conversación de voz en tiempo real desde el navegador con proveedores intercambiables, controles de acceso y métricas, y ahora cuenta con CI. Las brechas relevantes siguen abiertas: la latencia (≈2,6 a 2,7 s de mediana frente a 1 s), la telefonía con Asterisk, el guion oficial y el protocolo de costo y efectividad, la persistencia y un worker alojado de forma persistente. "
           "El diseño verificable (sección 10) muestra que el código es compacto y modular, y que cualquier evolución (por ejemplo, PR #18 o telefonía) debe incorporarse como un cambio explícito y no presentarse como parte del sistema vigente. [CONFIRMADO]")

    ref_heading = d.par("10. Referencias")
    d.set_par(ref_heading, "13. Referencias")
    d.at(d.par("Documentación oficial de LiveKit Agents"))
    d.bullet("Repositorio técnico en el corte 77ff85c (PR #1 a #17, #19 y #20): pyproject.toml, uv.lock, web-demo/package.json y .github/workflows/ci.yml.")
    d.bullet("docs/validation/DART-14-5.6-CI-github-actions.md del repositorio técnico y ejecuciones de GitHub Actions 42433340255, 42433603292 y 42435613596.")
    d.bullet("Evidencia E2E del 31-oct-2026 (log del worker y log de Netlify CLI sanitizados) en Fase 3/07_Evidencias/E2E-2026-10-31-clinica-dental/.")
    d.bullet("Diagramas fuente en Fase 3/03_Diseno/diagramas/ (PNG y SVG) y D03 v1.1 (casos de uso), D05 v1.1 (pruebas) y D06 v1.1 (operación).")

    out = OUT / "D01_Arquitectura_de_la_Solucion_v1.1_Fase3.docx"
    d.save(out)
    return out


if __name__ == "__main__":
    print(build())
