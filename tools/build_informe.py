import zipfile
from copy import deepcopy

from docx.oxml.ns import qn

from fase3_v2 import *  # noqa: F401,F403
from fase3_docx_lib import Doc

ORIG_IMG = FIG / "originales_fase2"


def extract_original_images() -> None:
    ORIG_IMG.mkdir(parents=True, exist_ok=True)
    z = zipfile.ZipFile(ORIG / "D01_Arquitectura_de_la_Solucion.docx")
    names = {"word/media/image1.png": "D01_fig1_componentes.png", "word/media/image2.png": "D01_fig2_secuencia.png", "word/media/image3.png": "D01_fig3_latencia_30oct.png"}
    for src, dst in names.items():
        (ORIG_IMG / dst).write_bytes(z.read(src))


def build() -> Path:
    extract_original_images()
    d = Doc(ORIG / "D01_Arquitectura_de_la_Solucion.docx")
    d.capture_templates("1. Propósito y alcance", "1.1 Qué problema resuelve", "Este documento describe", "Telefonía. No hay", "Figura 1.", "1. La persona elige")
    # --- portada
    d.set_par(d.par("Arquitectura de la solución"), "Informe académico consolidado")
    d.set_par(d.par("Componentes, flujo de datos"), "Fase 3: problema, solución y arquitectura, diseño, pruebas y demostración funcional")
    cover(d, "INF", version="1.2", date=DATE_V2)
    for _start, _new in COVER_NAMES.items():
        d.set_par(d.par(_start), _new)
    # --- control: la fila 1.0 del D01 se reemplaza por la primera versión del informe
    t = d.table("Versión")
    row = t.rows[1]
    for cell, v in zip(row.cells, ["1.0 (borrador)", CUT, AUTHOR,
                                   "Primera versión completa del informe académico consolidado de Fase 3, elaborada a partir de D01 a D06 v1.1, la matriz de trazabilidad, el registro de evidencias y el estado de origin/main (77ff85c). Reemplaza como referencia de trabajo al borrador v0.9 resumido de la recuperación documental, que se conserva sin cambios."]):
        d._set_cell(cell, v)
    control_row(d, version="1.1", date=DATE_DS, change="Versión 1.1: incorpora la sesión E2E del 17-nov con DeepSeek (resultados, capturas de la conversación, caso TC-23 y evidencias E06 a E09). Se mantienen sin cambios: latencia objetivo no cumplida, agendamiento simulado y Asterisk, persistencia empresarial y worker persistente pendientes. La v1.0 se conserva sin cambios.")
    control_row(d, version="1.2", date=DATE_V2, change=(
        "Versión 1.2 (saneamiento tras la auditoría del 19-nov, AUD-03 a AUD-11): alcance original frente al MVP implementado, funcionalidades pendientes (Asterisk, guion, persistencia, reservas simuladas), "
        "la demostración dental como validación del pipeline y no del proceso de cobranza, latencia real (3 fuentes), reclasificación de la reunión del 2-sep y de las decisiones atribuidas al cliente, "
        "Scrum como adaptación parcial, EV-20 y EV-21 con las limitaciones de CoreStream, guías oficiales 3.1 y 3.3 y estados de pruebas según D05 v1.3. La v1.0 y la v1.1 se conservan en Fase 3/Entregables/_historico."))
    # --- cuerpo: se elimina el contenido de D01 desde la sección 1
    start = d.par("1. Propósito y alcance")._p
    el = start
    while el is not None and el.tag != qn("w:sectPr"):
        nxt = el.getnext()
        d.body.remove(el)
        el = nxt
    # pie de página
    for sec in d.doc.sections:
        for p in sec.footer.paragraphs:
            for r in p.runs:
                if "Arquitectura de la soluci" in r.text:
                    r.text = r.text.replace("Arquitectura de la solución", "Informe académico consolidado Fase 3")
    d.at_end()

    d.h1("1. Resumen ejecutivo")
    d.para("Alloxentric Real Time Agent es un prototipo de agente de voz en tiempo real, construido para explorar una alternativa a la plataforma de bots de voz de Alloxentric con mayor elasticidad de costos. Al 17-nov-2026 el equipo dispone de un MVP integrado en main (commit 77ff85c) que sostiene conversaciones de voz completas desde el navegador (voz → STT → LLM → TTS → voz) con proveedores intercambiables, siete escenarios de práctica ficticios, transcripción en vivo, historial local, controles de acceso, métricas de latencia e integración continua. [CONFIRMADO]")
    d.para("Las pruebas automáticas verificadas el 17-nov son 214 de Python y 91 de la web, y la CI sobre main concluyó en verde. Tres fuentes de medición (E01 del 30-oct, E2E del 31-oct con Gemini y E2E del 17-nov con DeepSeek, aprobada con observaciones) muestran una latencia de voz a voz con mediana de ≈2,6 a 3,3 s, que no cumple el requisito de 1 s (en la sesión del 17-nov solo 2 de 8 turnos medidos lo alcanzan). El agendamiento de la demostración es una simulación conversacional, sin reservas reales. No existen aún telefonía con Asterisk, guion oficial de cobranza, comparación de costo y efectividad, persistencia de negocio ni un hosting persistente del worker. [CONFIRMADO]")
    d.para("Frente al objetivo original de Fase 1 (un bot de cobranza por voz con LiveKit, Speechmatics, ElevenLabs y la telefonía Asterisk, que compare costo y efectividad con la solución actual con una respuesta de no más de 1 s), el MVP implementado es un agente conversacional sobre LiveKit con Google Chirp 3, un LLM (Gemini o DeepSeek) y ElevenLabs, sin telefonía, sin guion oficial de cobranza y sin comparación de costos. "
           "La demostración con la clínica dental valida el pipeline conversacional con una persona ficticia, no el proceso de cobranza. [CONFIRMADO]")
    d.h1("2. Problema y contexto")
    d.para("[REPORTADO POR EL EQUIPO] Según el informe de definición de Fase 1, en la reunión inicial del 2-sep-2026 Max Kreimerman (dueño de Alloxentric) explicó que su infraestructura de bots de voz, optimizada para gran escala, tiene poca elasticidad de costos cuando baja el volumen de llamadas, y solicitó un prototipo de bot de cobranza por voz con LiveKit, un servicio de transcripción, ElevenLabs y la telefonía Asterisk, para comparar costo y efectividad por llamada con la solución actual, con una respuesta de no más de 1 s (sobre 3 s la persona puede cortar).")
    d.para(REUNION_NOTE)
    d.para(CONTRADICCION_LLM)
    d.table_new(["", "Situación actual (AS-IS)", "Alternativa a evaluar (TO-BE)"], [
        ["Plataforma", "Bots de voz y texto con modelos propios, optimizada para gran escala", "Prototipo con LiveKit, STT, ElevenLabs y Asterisk"],
        ["Costos", "Poca elasticidad con bajo volumen", "Costo por llamada medible y comparable [PENDIENTE: conceptos y tarifas]"],
        ["Interacción", "Guion de agente existente", "Guion de cobranza con reconocimiento de intenciones [PENDIENTE: guion oficial]"],
        ["Latencia", "Referencia del cliente: ≤ 1 s", "Medición actual: medianas ≈2,6 a 3,3 s (E01, E2E 31-oct y 17-nov)"],
    ], [3.0, 6.4, 7.2])
    d.h1("3. Objetivos")
    d.para("Objetivo general heredado de Fase 1: desarrollar y evaluar un prototipo de bot de cobranza por voz basado en LiveKit. No existe un ajuste académico aprobado que lo reemplace; el nombre del proyecto se mantiene. [CONFIRMADO]")
    d.table_new(["Objetivo específico", "Estado al 19-nov", "Justificación"], [
        ["1. Analizar y documentar guion, intenciones, requerimientos y protocolo comparativo", "Parcial", "Requerimientos en D03; faltan guion oficial, intenciones y protocolo"],
        ["2. Diseñar la integración de LiveKit, STT, ElevenLabs y Asterisk y el flujo conversacional", "Parcial", "D01 con arquitectura, casos de uso y actividad; falta Asterisk"],
        ["3. Implementar un prototipo con voz adecuada al contexto chileno", "Parcial", "MVP con 7 escenarios ficticios; sin guion oficial ni validación auditiva"],
        ["4. Planificar y gestionar con Scrum y trazabilidad por integrante", "Parcial", "Adaptación parcial de Scrum: ramas por ticket, PR y CI; faltan backlog, sprints, retrospectivas y actas"],
        ["5. Pruebas funcionales, de integración y de voz, incluida la latencia", "Parcial", "214 + 91 pruebas, CI y E2E; latencia sin cumplir 1 s; TC-03, TC-04 y TC-17 parciales o no verificables (D05 v1.3)"],
        ["6. Comparar costo y efectividad con la solución actual", "No iniciado", "Sin protocolo, tarifas ni datos de referencia"],
    ], [7.0, 2.4, 7.2])
    d.h1("4. Alcance")
    d.para("Matriz del alcance. Demostrada: con evidencia archivada (logs con SHA-256, capturas o pruebas); Simulación: comportamiento conversacional sin sistema real detrás; Pendiente: sin implementación verificable.")
    d.table_new(["Funcionalidad", "Objetivo original (Fase 1)", "Estado al 19-nov", "Evidencia y limitación"], [
        ["Conversación de voz en tiempo real desde el navegador", "Sí (LiveKit)", "Demostrada", "E01, E2E del 31-oct y del 17-nov (una sola persona), 214 + 91 pruebas y CI"],
        ["STT", "Speechmatics", "Demostrada con Google Chirp 3; exactitud no medida", "Logs de STT; TC-03 parcial. Speechmatics solo existe en el PR #18, no integrado. Cambio sin acta"],
        ["LLM", "Evitar un LLM al inicio (según Fase 1)", "Demostrada con Gemini (31-oct) y DeepSeek (17-nov); desviación del plan", "Sin aprobación formal; TC-04 parcial; contradicción con la especificación v0.1 sin resolver"],
        ["TTS ElevenLabs", "Sí", "Demostrada en lo técnico; calidad de la voz chilena no validada", "Primer audio en logs; TC-05 pendiente"],
        ["Latencia ≤ 1 s", "Sí", "Instrumentada; objetivo NO cumplido", "Medianas 2,59 s (n=13), 2,74 s (n=5) y 3,26 s (n=8)"],
        ["Web Demo: acceso por código, transcripción, micrófono e historial", "No (aporte del equipo)", "Demostrada", "Capturas EV-17 y EV-21; 91 pruebas web"],
        ["Siete escenarios (personas)", "No", "Parcial: solo la clínica dental tiene E2E", "Las dos personas de cobranza son ficticias y no tienen E2E"],
        ["Agendamiento de la clínica dental", "No", "Simulación conversacional", "Sin reservas, agenda, CRM ni base de datos"],
        ["Guion oficial de cobranza e intenciones", "Sí", "Pendiente", "Los escenarios ficticios no equivalen al guion oficial"],
        ["Telefonía Asterisk", "Sí", "Pendiente (no iniciada)", "Sin código ni pruebas; depende de accesos del cliente"],
        ["Comparación de costo y efectividad", "Sí (núcleo del objetivo)", "Pendiente", "Solo contadores de uso; sin protocolo ni tarifas"],
        ["Persistencia de negocio, CRM y worker persistente", "No definido", "Pendiente", "Solo localStorage y logs; el worker corre en un equipo del grupo"],
        ["STT seleccionable, Anthropic y LiveKit Inference (PR #18)", "No", "No integrada", "PR abierto sin revisión; no forma parte de la solución"],
        ["Evolución de cobranza para pymes («DART»)", "No", "Propuesta sin autorización académica", "No cambia el nombre ni el alcance del proyecto"],
    ], [4.4, 3.0, 4.0, 5.2])
    d.para("La demostración de la clínica dental es una demostración técnica transversal: valida que el pipeline voz → STT → LLM → TTS → voz funciona con una persona ficticia y cuánto tarda. No valida el proceso de cobranza (guion oficial, reconocimiento de intenciones, conducta ante deudores, resultados de gestión), que sigue pendiente. [CONFIRMADO]")
    d.h1("5. Metodología y gestión")
    d.para("El equipo declaró Scrum como marco de trabajo en Fase 1 y lo aplicó de forma parcial: un flujo Git liviano con una rama por ticket (DART-14-x), Pull Request hacia main y revisión de otro integrante, y CI desde el PR #19. Se fusionaron 19 PR (#1 a #17, #19 y #20) y el PR #18 permanece abierto. Las ceremonias, el backlog, los sprints, las retrospectivas y las actas no están archivados, por lo que Scrum se presenta como una adaptación parcial y no como una aplicación completa. [CONFIRMADO / PENDIENTE]")
    d.table_new(["Fecha", "Hito", "PR / evidencia"], [
        ["2-sep", "Reunión inicial con Max Kreimerman (reportada; evidencia indirecta)", "Informe de Fase 1 (cita una transcripción no archivada); ACTA-01, reconstrucción"],
        ["3 a 8-oct", "Flujo Git, entorno LiveKit, DeepSeek y ElevenLabs", "PR #1 a #4"],
        ["16 a 17-oct", "Gemini, Chirp 3 y pipeline de voz integrado", "PR #5 a #7"],
        ["18 a 22-oct", "Métricas, ADC y Web Demo con acceso seguro", "PR #8 a #12"],
        ["23 a 27-oct", "Correcciones de Netlify y validación E2E (borrador)", "PR #13 a #15"],
        ["30 y 31-oct", "Personas, voces, rediseño, Vercel y nombre configurable; E2E de la clínica dental", "PR #16 y #17; logs con SHA-256"],
        ["7-nov", "Integración continua", "PR #19 y #20; runs de GitHub Actions"],
        ["17-nov", "Recuperación documental, certificación y D01 a D06 v1.1", "Rama docs/fase3-recuperacion-documental"],
        ["17 y 18-nov", "E2E de la clínica dental con DeepSeek y consolidación de sus evidencias", "Logs sanitizados, capturas y hashes (carpeta E2E-2026-11-17-clinica-dental-deepseek)"],
        ["19-nov", "Reporte de CoreStream, expediente histórico de reuniones, DART-14-2.5 sanitizada y saneamiento de los entregables", "EV-20, EV-21, E10; documentos v1.2 y v1.3"],
    ], [2.4, 9.0, 5.2])
    d.para("Decisiones atribuidas al cliente y estado de su respaldo. Ninguna cuenta con acta, transcripción archivada ni aprobación formal verificable.")
    d.table_new(["Decisión", "Fuente", "Estado"], [
        ["Evitar un LLM al inicio", "Informe de Fase 1 y D03, atribuido a Max", "Contradicho por la especificación v0.1 descrita en DART 14 1.1 (DeepSeek Flash); sin resolver [PENDIENTE DE VALIDACIÓN]"],
        ["Cambiar Speechmatics por Chirp 3", "Mensaje del líder citando a Max", "Sin acta; decisión técnica del equipo con indicación atribuida al cliente [PENDIENTE DE VALIDACIÓN]"],
        ["Usar Gemini y DeepSeek como LLM", "Equipo", "Sin aprobación formal del cliente [PENDIENTE DE VALIDACIÓN]"],
        ["Usar DeepSeek en la demostración del 17-nov", "Equipo", "[PROPUESTA] del equipo, tras fallar Gemini por API_KEY_INVALID"],
        ["Hitos: MVP con base de datos (28-sep a 3-oct), proyecto en Docker (26 a 31-oct), entrega documentada (16 a 28-nov)", "REG-04, reconstrucción histórica", "Planificación; cumplimiento no acreditado: no hay base de datos de negocio ni Dockerfile en main [REPORTADO POR EL EQUIPO]"],
    ], [5.2, 4.6, 6.8])
    d.para("[CONFIRMADO] " + CORESTREAM_NOTE)
    d.h1("6. Solución y arquitectura")
    d.para("La solución tiene tres bloques: la web (lo que ve la persona), LiveKit Cloud (transporte de audio en tiempo real y despacho del agente) y el worker Python, que orquesta la cadena de voz con Google Chirp 3 (STT), Gemini o DeepSeek (LLM) y ElevenLabs (TTS). Las funciones serverless de la web validan el acceso y emiten el token; no alojan al worker. El detalle se encuentra en D01.")
    d.figure(ORIG_IMG / "D01_fig1_componentes.png", "Figura 1. Diagrama de componentes (figura original de D01, vigente en main 77ff85c). Fuente: elaboración propia a partir del repositorio técnico.", 16.2)
    d.figure(ORIG_IMG / "D01_fig2_secuencia.png", "Figura 2. Secuencia de una llamada (figura original de D01). La latencia citada corresponde a E01 (30-oct, n=13). Fuente: elaboración propia.", 16.2)
    d.table_new(["Capa", "Tecnología", "Responsabilidad"], [
        ["Web Demo", "Next.js 15.5, React 19, livekit-client", "Acceso, selección de agente, llamada, transcripción e historial local"],
        ["Funciones", "Netlify Functions y Vercel Functions; jose; livekit-server-sdk", "Sesión firmada, origen, token con despacho fijado por el servidor"],
        ["Transporte", "LiveKit Cloud (WebRTC)", "Sala, audio, despacho del agente, turnos e interrupciones"],
        ["Worker", "Python 3.12, livekit-agents 1.8.4, uv", "Sesión de voz, persona, métricas"],
        ["STT / LLM / TTS", "Google Chirp 3; Gemini 3.1 flash-lite o DeepSeek; ElevenLabs eleven_v4_turbo", "Transcripción, respuesta y síntesis en streaming"],
        ["Calidad", "pytest, Vitest, ESLint, TypeScript, GitHub Actions", "Pruebas y controles automáticos"],
    ], [2.8, 6.4, 7.4])
    d.h1("7. Diseño verificable")
    d.para("Los diagramas siguientes se derivaron del código y las pruebas de main (77ff85c). No se añadieron entidades, tablas ni endpoints inexistentes. El código es mayormente funcional y no tiene base de datos; lo pendiente se muestra explícitamente como tal. Los detalles están en D01 §10 y D03 §11.")
    landscape_group(d, [
        (FIG / "fig_casos_uso.png", "Figura 3. Casos de uso implementados (UC-01 a UC-11) y pendientes (UP-1 a UP-4)."),
        (FIG / "fig_actividad_agente.png", "Figura 4. Diagrama de actividad del worker del agente."),
        (FIG / "fig_clases_python.png", "Figura 5. Módulos y clases reales del paquete alloxentric_real_time_agent."),
        (FIG / "fig_almacenamiento.png", "Figura 6. Modelo del almacenamiento actual: localStorage, cookie de sesión y logs; sin base de datos."),
    ])
    d.h1("8. Implementación")
    d.table_new(["Componente", "Detalle verificable", "Integración"], [
        ["Pipeline de voz", "AgentSession con STT, LLM y TTS; endpointing dinámico 0,3 a 1,5 s; generación preventiva; saludo por TTS directo", "main (PR #7, #16)"],
        ["Siete personas", "Guion, saludo y voz por persona; el prompt vive en el worker y el navegador solo envía el id", "main (PR #16)"],
        ["Seguridad", "Código de acceso con hash, cookie firmada HttpOnly/Secure/SameSite=Strict, origen exacto, CSP con hashes, record=False", "main (PR #11 a #16)"],
        ["Métricas", "e2e_latency_s y etapas por turno, uso por sesión; sin contenido de conversación", "main (PR #9)"],
        ["Aislamiento de workers", "Nombre del agente configurable (LIVEKIT_AGENT_NAME)", "main (PR #17)"],
        ["CI", "Jobs python-tests y web-quality sin secretos ni despliegue", "main (PR #19, #20)"],
    ], [3.4, 9.6, 3.6])
    d.h1("9. Pruebas y resultados")
    d.para("[CONFIRMADO] Certificación del 17-nov-2026 sobre una copia limpia de origin/main (77ff85c), sin proveedores reales. Los resultados históricos del 30-oct (200 y 91) y los del PR #18 (281 y 103, rama no integrada) no se combinan con esta ejecución.")
    d.table_new(["Verificación", "Resultado", "Entorno / fuente"], CERT_TABLE, [4.6, 8.4, 3.8])
    d.para("Mediciones de latencia de voz a voz (e2e_latency_s). Son muestras pequeñas y no se combinan; ninguna mediana cumple el requisito de 1 s.")
    d.table_new(["Fuente", "Fecha", "n", "Mediana", "Rango", "Observación"], [
        ["E01 (5 sesiones, 22 turnos)", "30-oct", "13", "2,5941 s", "0,4775 a 4,0839 s", "Mezcla voz humana y sintética; 3 turnos sobre 3 s"],
        ["E2E clínica dental", "31-oct", "5", "2,7411 s", "1,1912 a 3,3519 s", "Una sesión; sin reloj externo"],
        ["E2E clínica dental (DeepSeek)", "17-nov", "8", "3,2640 s", "0,5570 a 5,4985 s", "Una sesión; 2 de 8 turnos ≤ 1 s"],
    ], [3.8, 1.6, 0.9, 2.0, 3.2, 5.1])
    d.figure(FIG / "fig_latencia_actualizada.png", "Figura 7. Latencia de voz a voz medida frente al requisito de 1 s (E01 y E2E del 31-oct; no incluye la sesión del 17-nov, cuyos valores están en la tabla anterior). Fuente: E01 y log del worker del 31-oct.", 16.2)
    d.para("Método: medianas y medias son las habituales; el P90 de E01 usa rango más cercano y los P95 de las sesiones E2E usan interpolación lineal (D05 §4.4). Las comparativas de modelos de Gemini, ElevenLabs y Chirp (D05 §4.1 a §4.3) son reportadas y no reproducibles.")
    d.para("Casos de prueba: D05 v1.3 documenta 24 casos (TC-01 a TC-24). Tras la auditoría, TC-03 (exactitud del STT), TC-04 (coherencia del LLM) y TC-17 (conducta de cobranza) figuran como parcial o no verificable, y TC-02 y TC-07 a TC-10 también se rebajaron, porque los logs no registran texto de conversación y no hay frases de referencia ni transcripciones archivadas. "
           "Los controles de acceso, historial y personas están cubiertos por pruebas automáticas; no cumple el caso de latencia (TC-14); siguen pendientes la validación auditiva de la voz, eco y ruido, y la telefonía con Asterisk. Los defectos y hallazgos están en D05 §7. La prueba de una frase del 19-oct (DART-14-2.5, E10) se incorpora como evidencia adicional con sus limitaciones.")
    d.h1("10. Demostración funcional")
    d.para("[PROPUESTA] Guion de la demostración (≈5 a 7 minutos) sobre el estado integrado de main. Debe ajustarse a los 20 minutos máximos de la guía 3.3 (incluidas las preguntas) y ensayarse antes de la entrega; el procedimiento y la lista de verificación están en D06 §12 y §13. La demostración muestra el pipeline conversacional con una persona ficticia, no el proceso de cobranza.")
    for i, x in enumerate([
        "Presentar la pantalla de acceso e ingresar el código temporal (mostrar también el rechazo con un código incorrecto).",
        "Elegir la persona clínica dental (única con E2E archivado, en dos sesiones) y comenzar la conversación; el agente saluda con su voz.",
        "Conversar al menos cuatro turnos, incluyendo una interrupción, mostrando la transcripción en vivo.",
        "Mostrar el selector de micrófono y el silencio; finalizar la llamada.",
        "Abrir el historial local, descargar una conversación y mostrar que se guarda solo en el navegador.",
        "Mostrar las métricas del worker (solo números) y explicar honestamente la brecha de latencia.",
    ], start=1):
        d.step(f"{i}.", x)
    d.figure(SHOT / "01_acceso.png", "Figura 8. Pantalla de acceso (captura del producto, 17-nov-2026; no es un mockup previo).", 13.5)
    d.figure(SHOT / "03_seleccion_agente.png", "Figura 9. Selección de agente entre las 7 personas (captura del 17-nov-2026; nombre del deudor ficticio de una tarjeta omitido).", 11.5)
    d.figure(SHOT / "04_historial.png", "Figura 10. Historial local con dos conversaciones sintéticas de captura (17-nov-2026).", 11.5)
    d.h2("10.1 Resultado del ensayo E2E del 17 de noviembre (DeepSeek)")
    d.para("[CONFIRMADO] Sesión AJ_zm9g5TDNqgG5 con la persona clínica dental desde la Web Demo local y un worker local de desarrollo. Dictamen: APROBADO CON OBSERVACIONES. Dos intentos previos del mismo día con Gemini fallaron por API_KEY_INVALID; el cambio de proveedor a DeepSeek es una decisión PROPUESTA del equipo, sin acta de aprobación del cliente.")
    d.table_new(["Indicador", "Resultado"], E2E_DS_TABLE, [5.2, 11.4])
    d.figure(SHOT_DS / "captura-03-respuestas-generadas-t060s.png", "Figura 11. Transcripción en vivo con respuestas generadas (video de la sesión del 17-nov, 1:00; recorte al área de la aplicación).", 11.5)
    d.figure(SHOT_DS / "captura-05-continuidad-turnos-15-mensajes-t140s.png", "Figura 12. Continuidad de la conversación con quince mensajes (video, 2:20). El agendamiento es simulado: «queda reservada» es texto conversacional, no una reserva real.", 11.5)
    d.para("[PENDIENTE] No hay capturas del cierre de la llamada ni del historial de esta sesión. Las tres capturas restantes de la conversación están en la carpeta de evidencias; el video original queda fuera de Git porque expone datos del equipo. Plan B para la presentación: video del ensayo.")
    d.h1("11. Riesgos")
    d.table_new(["Riesgo", "Nivel / estado", "Respuesta"], [
        ["Latencia de voz a voz > 1 s (R-01)", "Crítico; materializado", "Declarar la brecha; ampliar la muestra con un protocolo acordado; evaluar alternativas de STT (PR #18, no integrado)"],
        ["Worker y proveedores no disponibles durante la demo (R-10, R-12)", "Alto; activo", "Ensayo previo, video de respaldo y verificación de credenciales y saldos"],
        ["Falta de guion oficial y accesos de Alloxentric (R-04), Asterisk (R-05)", "Crítico; activo", "Presentar como pendientes dependientes del cliente; solicitar fechas por escrito"],
        ["Documentación obligatoria de Fase 3 sin confirmar (R-21)", "Crítico; activo [PROPUESTA]", "Guías 3.1 y 3.3 obtenidas; faltan las planillas de evaluación; la tabla de la sección 13 no equivale a cobertura de evaluación"],
        ["Presentar lo no integrado como implementado (R-22)", "Alto; activo [PROPUESTA]", "Revisión cruzada contra la matriz de trazabilidad; rótulos explícitos"],
        ["Evidencias y registros Scrum insuficientes (R-17)", "Alto; parcialmente mitigado", "Adjuntar backlog, actas y registros disponibles; presentar Scrum como adaptación parcial"],
        ["Presentar como aprobadas decisiones solo atribuidas al cliente", "Alto; activo [PROPUESTA]", "Usar «reportado por el equipo»; localizar la transcripción del 2-sep y la especificación atribuida a Max"],
    ], [6.2, 3.4, 7.0])
    d.h1("12. Contribuciones individuales")
    d.para("La autoría se basa en commits y PR verificables; los merges no se cuentan como autoría. Las decisiones tomadas en reuniones externas requieren actas. El reporte agregado de CoreStream (EV-20) no permite atribuir actividades ni medir contribuciones individuales (ver sección 5); Javier Cerna figura en ese reporte de la herramienta del cliente, pero no forma parte del equipo Capstone. [PENDIENTE DE VALIDACIÓN]")
    d.table_new(["Integrante", "Rol", "Contribución verificable", "Evidencia"], [
        ["Fernando Olguea", "Líder de proyecto y desarrollador", "Entorno inicial, LiveKit, DeepSeek, Gemini, pipeline, métricas, ADC, Web Demo inicial, seguridad, incidentes, nombre configurable y CI", "PR #1 a #3, #5, #7, #9 a #15, #17, #19, #20"],
        ["David Sepúlveda", "Scrum Master y desarrollador", "TTS ElevenLabs, pruebas y script de verificación real; diario individual", "PR #4 y archivos de TTS"],
        ["Juan Díaz", "Product Owner y desarrollador", "STT Chirp 3, personas y voces, optimizaciones, rediseño web, historial, Vercel, PR #18, D01 a D06 y E01", "PR #6, #16, #18; commit 31f096e de la rama documental"],
    ], [2.8, 3.2, 7.0, 3.6])
    d.h1("13. Documentación de Fase 3")
    d.para(GUIA_33 + " " + PAUTAS_PENDIENTES)
    d.table_new(["Elemento", "Clasificación", "Dónde se cubre", "Estado al 19-nov"], DOC_TABLE_V12, [4.6, 3.2, 4.4, 4.6])
    d.h1("14. Limitaciones")
    for x in ["Las muestras de latencia son pequeñas (13, 5 y 8 turnos) y de una sola red; no hay protocolo acordado con el cliente.",
              "Solo la persona clínica dental tiene E2E archivado; las otras seis no se validaron con logs.",
              "No hay telefonía, guion oficial, comparación de costos, persistencia de negocio ni hosting persistente del worker.",
              "La certificación del 17-nov se hizo en un solo equipo y sin proveedores reales; falta ejecución independiente.",
              "La sesión del 17-nov es una sola, con voz humana no controlada, un proveedor de LLM y un worker local; el agendamiento es simulado (sin reservas reales). Faltan capturas del cierre y del historial de esa sesión.",
              "CoreStream solo aporta un reporte agregado (EV-20) sin tickets; el backlog, los sprints, las retrospectivas y las actas no están adjuntos y Scrum es una adaptación parcial.",
              "La reunión del 2-sep y lo atribuido a Max son evidencia indirecta (transcripción y especificación v0.1 sin localizar); el cambio de STT y el uso de LLM no tienen aprobación formal verificable.",
              "Las comparativas de Gemini, ElevenLabs y Chirp son reportadas y no reproducibles; la exactitud del STT, la coherencia del LLM y la conducta de cobranza no están verificadas (TC-03, TC-04, TC-17).",
              "No están disponibles las planillas de evaluación de Fase 3; la cobertura de evaluación no se declara completa."]:
        d.bullet(x)
    d.h1("15. Conclusiones")
    d.para("El equipo dispone de un MVP técnicamente funcional y demostrable, con pruebas automáticas en verde, CI y evidencia E2E (la última, del 17-nov con DeepSeek, aprobada con observaciones). Su principal brecha respecto del objetivo es la latencia (objetivo de 1 s no cumplido), junto con los componentes que dependen del cliente (guion, telefonía, costos). Para la entrega y la presentación, la prioridad es ensayar y registrar la demostración completa y presentar con precisión qué está integrado, qué se midió y qué sigue pendiente, manteniendo el nombre y el alcance del proyecto. Siguen pendientes Asterisk, la persistencia empresarial, el worker persistente y la integración del PR técnico #18; el agendamiento es simulado. La demostración valida el pipeline conversacional con una persona ficticia, no el proceso de cobranza, y la reunión inicial y las decisiones atribuidas a Max constan como evidencia indirecta. [CONFIRMADO]")
    d.h1("16. Trabajo futuro y próximos pasos")
    for x in ["Obtener las planillas de evaluación de Fase 3 (las guías 3.1 y 3.3 ya están disponibles), incorporar la retroalimentación del informe final de Fase 2 y confirmar los documentos obligatorios.",
              "Localizar la transcripción del 2-sep y la especificación atribuida a Max, y reclasificar lo que respalden.",
              "Exportar los tickets de CoreStream (DART_14), si la herramienta lo permite, para sustentar backlog y hitos.",
              "Ensayar la demostración sobre main, grabar un video de respaldo y ampliar la muestra de latencia con más sesiones.",
              "Revisar y decidir el PR #18; si se integra, repetir pruebas y mediciones.",
              "Acordar con Alloxentric el protocolo de latencia, el guion oficial, el entorno de Asterisk y los conceptos de costo.",
              "Mover el worker a un servicio persistente con cuenta de servicio de Google y límites de gasto.",
              "Registrar Scrum (backlog, sprints, retrospectivas) y las actas en CoreStream."]:
        d.bullet(x)
    d.h1("17. Referencias")
    for x in ["D01 v1.2, D02 v1.2, D03 v1.2, D04 v1.2, D05 v1.3 y D06 v1.2 (Fase 3/Entregables); versiones anteriores en Fase 3/Entregables/_historico y v1.0 en Fase 2/Evidencias Proyecto.",
              "Repositorio técnico fernandoknvz/alloxentric-real-time-agent, corte 77ff85c (PR #1 a #17, #19 y #20; PR #18 abierto).",
              "Registro consolidado de evidencias y matriz de trazabilidad (Fase 3/07_Evidencias y Fase 3/MATRIZ_TRAZABILIDAD_PRELIMINAR.md).",
              "Logs E2E del 31-oct, capturas y certificación del 17-nov, y evidencias E2E DeepSeek del 17-nov (Fase 3/07_Evidencias).",
              "Informe de definición del proyecto APT (Fase 1) y guía 2.4 de avance (Fase 2); guías oficiales 3.1 (diario de reflexión) y 3.3 (presentación) de Fase 3 (Fase 3/Pautas_Oficiales/).",
              "Reporte de CoreStream (EV-20), capturas de la demostración (EV-21), expediente histórico de reuniones y DART-14-2.5 sanitizada (Fase 3/07_Evidencias).",
              "Documentación oficial de LiveKit Agents, Google Cloud Speech-to-Text, ElevenLabs y Gemini."]:
        d.bullet(x)
    d.h1("Anexo A. Evidencias verificables")
    d.table_new(["ID", "Evidencia", "Referencia", "Limitación"], [
        ["E01", "Métricas de latencia del 30-oct", "SHA-256 69AF78CA...4A71C7A", "Mezcla voz humana y sintética"],
        ["E02", "Log del worker E2E del 31-oct", "SHA-256 844E3492...97B41", "Una sesión; cinco E2E"],
        ["E03", "Log de Netlify CLI del 31-oct", "SHA-256 A5FE4E40...FD6C3", "No demuestra audio ni calidad"],
        ["E04", "Capturas de la Web Demo (17-nov)", "Fase 3/07_Evidencias/capturas-web-demo-2026-11-17/", "Sin conversación en vivo (ver E08)"],
        ["E05", "Certificación de pruebas (17-nov)", "Fase 3/07_Evidencias/CERTIFICACION_PRUEBAS_2026-11-17.md", "Un solo equipo; sin proveedores"],
        ["E06", "Registro E2E DeepSeek (17-nov)", EV_DS + "README.md (hashes en SHA256SUMS.txt)", "Una sesión; n=8 turnos con E2E"],
        ["E07", "Logs sanitizados del 17-nov", "SHA-256 D7525A21...016649 (worker) y 00DDF21D...175BCA6C (Netlify)", "No contienen texto de la conversación"],
        ["E08", "Capturas de la conversación (17-nov)", EV_DS + "capturas/", "Pantalla del cliente; no prueban audio ni latencia"],
        ["E09", "Video original del 17-nov (fuera de Git)", "SHA-256 D6FE9270...5CABFA", "Expone datos del equipo; no se incorpora"],
        ["E10", "Informe DART-14-2.5 sanitizado (19-oct; EV-22 del registro)", EV_D25, "Una frase; sin latencia; audio solo por testimonio; cierre con errores"],
        ["EV-20", "Reporte agregado de CoreStream (19-nov)", "Fase 3/07_Evidencias/CoreStream/ (SHA-256 CBDADA1B...EE869)", "Sin tickets; no acredita avance, hitos ni rendimiento individual; Javier Cerna no pertenece al equipo Capstone"],
        ["EV-21", "Capturas derivadas de la demo de clínica dental (17-nov)", "Fase 3/07_Evidencias/Demo_E2E_2026-11-17/", "No prueban audio, latencia, telefonía ni reservas reales"],
        ["CI", "GitHub Actions sobre main", "Run 42435613596 (success) en 77ff85c", "PR #19 fusionado sin aprobación independiente"],
    ], [1.2, 5.0, 6.4, 4.0])
    out = OUT / "Informe_Academico_Consolidado_v1.2_Fase3.docx"
    d.doc.core_properties.title = "Informe académico consolidado — Alloxentric Real Time Agent"
    d.save(out)
    return out


if __name__ == "__main__":
    print(build())
