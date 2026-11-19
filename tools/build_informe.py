import zipfile
from copy import deepcopy

from docx.oxml.ns import qn

from fase3_common import *  # noqa: F401,F403
from fase3_docx_lib import Doc
from build_d03 import DOC_TABLE

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
    cover(d, "INF", version="1.1", date=DATE_DS)
    # --- control: la fila 1.0 del D01 se reemplaza por la primera versión del informe
    t = d.table("Versión")
    row = t.rows[1]
    for cell, v in zip(row.cells, ["1.0 (borrador)", CUT, AUTHOR,
                                   "Primera versión completa del informe académico consolidado de Fase 3, elaborada a partir de D01 a D06 v1.1, la matriz de trazabilidad, el registro de evidencias y el estado de origin/main (77ff85c). Reemplaza como referencia de trabajo al borrador v0.9 resumido de la recuperación documental, que se conserva sin cambios."]):
        d._set_cell(cell, v)
    control_row(d, version="1.1", date=DATE_DS, change="Versión 1.1: incorpora la sesión E2E del 17-nov con DeepSeek (resultados, capturas de la conversación, caso TC-23 y evidencias E06 a E09). Se mantienen sin cambios: latencia objetivo no cumplida, agendamiento simulado y Asterisk, persistencia empresarial y worker persistente pendientes. La v1.0 se conserva sin cambios.")
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
    d.para("Las pruebas automáticas verificadas el 17-nov son 214 de Python y 91 de la web, y la CI sobre main concluyó en verde. Tres sesiones reales (E01 del 30-oct, E2E del 31-oct con Gemini y E2E del 17-nov con DeepSeek, aprobada con observaciones) muestran una latencia de voz a voz con mediana de ≈2,6 a 3,3 s, que no cumple el requisito de 1 s (en la sesión del 17-nov solo 2 de 8 turnos medidos lo alcanzan). El agendamiento de la demostración es una simulación conversacional, sin reservas reales. No existen aún telefonía con Asterisk, guion oficial de cobranza, comparación de costo y efectividad, persistencia de negocio ni un hosting persistente del worker. [CONFIRMADO]")
    d.h1("2. Problema y contexto")
    d.para("[CONFIRMADO] En la reunión inicial del 2-sep-2026, Max Kreimerman (dueño de Alloxentric) explicó que su infraestructura de bots de voz, optimizada para gran escala, tiene poca elasticidad de costos cuando baja el volumen de llamadas. Solicitó un prototipo de bot de cobranza por voz con LiveKit, un servicio de transcripción, ElevenLabs y la telefonía Asterisk, para comparar costo y efectividad por llamada con la solución actual, con una respuesta de no más de 1 s (sobre 3 s la persona puede cortar).")
    d.table_new(["", "Situación actual (AS-IS)", "Alternativa a evaluar (TO-BE)"], [
        ["Plataforma", "Bots de voz y texto con modelos propios, optimizada para gran escala", "Prototipo con LiveKit, STT, ElevenLabs y Asterisk"],
        ["Costos", "Poca elasticidad con bajo volumen", "Costo por llamada medible y comparable [PENDIENTE: conceptos y tarifas]"],
        ["Interacción", "Guion de agente existente", "Guion de cobranza con reconocimiento de intenciones [PENDIENTE: guion oficial]"],
        ["Latencia", "Referencia del cliente: ≤ 1 s", "Medición actual: mediana ≈2,6 a 2,7 s"],
    ], [3.0, 6.4, 7.2])
    d.h1("3. Objetivos")
    d.para("Objetivo general heredado de Fase 1: desarrollar y evaluar un prototipo de bot de cobranza por voz basado en LiveKit. No existe un ajuste académico aprobado que lo reemplace; el nombre del proyecto se mantiene. [CONFIRMADO]")
    d.table_new(["Objetivo específico", "Estado al 17-nov", "Justificación"], [
        ["1. Analizar y documentar guion, intenciones, requerimientos y protocolo comparativo", "Parcial", "Requerimientos en D03; faltan guion oficial, intenciones y protocolo"],
        ["2. Diseñar la integración de LiveKit, STT, ElevenLabs y Asterisk y el flujo conversacional", "Parcial", "D01 con arquitectura, casos de uso y actividad; falta Asterisk"],
        ["3. Implementar un prototipo con voz adecuada al contexto chileno", "Parcial", "MVP con 7 escenarios ficticios; sin guion oficial ni validación auditiva"],
        ["4. Planificar y gestionar con Scrum y trazabilidad por integrante", "Parcial", "Ramas por ticket, PR y CI; faltan backlog, sprints y actas"],
        ["5. Pruebas funcionales, de integración y de voz, incluida la latencia", "Parcial", "214 + 91 pruebas, CI y E2E; latencia sin cumplir 1 s"],
        ["6. Comparar costo y efectividad con la solución actual", "No iniciado", "Sin protocolo, tarifas ni datos de referencia"],
    ], [7.0, 2.4, 7.2])
    d.h1("4. Alcance")
    d.table_new(["Elemento", "Estado", "Clasificación"], [
        ["Conversación de voz en tiempo real desde el navegador", "Implementada e integrada en main; validada con tres sesiones reales (la última, con DeepSeek, aprobada con observaciones)", "[CONFIRMADO]"],
        ["Web Demo con acceso por código, 7 escenarios, transcripción, micrófono e historial", "Implementada e integrada (PR #11 a #17)", "[CONFIRMADO]"],
        ["Métricas de latencia y uso, seguridad y CI", "Implementadas e integradas (PR #9, #11 a #20)", "[CONFIRMADO]"],
        ["STT seleccionable, Anthropic y LiveKit Inference (PR #18)", "Rama abierta, sin revisión; no integrada", "[PROPUESTA]"],
        ["Telefonía con Asterisk", "No iniciada; depende de accesos del cliente", "[PENDIENTE]"],
        ["Guion oficial de cobranza y reconocimiento de intenciones", "No incorporado; los escenarios son ficticios", "[PENDIENTE]"],
        ["Comparación de costo y efectividad", "Solo contadores de uso; sin protocolo", "[PENDIENTE]"],
        ["Persistencia de negocio y hosting persistente del worker", "No existen", "[PENDIENTE]"],
        ["Evolución de cobranza para pymes («DART»)", "Idea de Fase 3 sin autorización académica; no cambia el nombre ni el alcance", "[PENDIENTE DE VALIDACIÓN]"],
    ], [7.0, 6.2, 3.4])
    d.h1("5. Metodología y gestión")
    d.para("El equipo declaró Scrum como marco de trabajo y aplica un flujo Git liviano: una rama por ticket (DART-14-x), Pull Request hacia main y revisión de otro integrante. Desde el PR #19 existe integración continua. Se fusionaron 19 PR (#1 a #17, #19 y #20) y el PR #18 permanece abierto. Las ceremonias, el backlog y las actas no están en los repositorios y siguen pendientes de adjuntar. [CONFIRMADO / PENDIENTE]")
    d.table_new(["Fecha", "Hito", "PR / evidencia"], [
        ["2-sep", "Reunión inicial con Max Kreimerman", "Informe de Fase 1"],
        ["3 a 8-oct", "Flujo Git, entorno LiveKit, DeepSeek y ElevenLabs", "PR #1 a #4"],
        ["16 a 17-oct", "Gemini, Chirp 3 y pipeline de voz integrado", "PR #5 a #7"],
        ["18 a 22-oct", "Métricas, ADC y Web Demo con acceso seguro", "PR #8 a #12"],
        ["23 a 27-oct", "Correcciones de Netlify y validación E2E (borrador)", "PR #13 a #15"],
        ["30 y 31-oct", "Personas, voces, rediseño, Vercel y nombre configurable; E2E de la clínica dental", "PR #16 y #17; logs con SHA-256"],
        ["7-nov", "Integración continua", "PR #19 y #20; runs de GitHub Actions"],
        ["17-nov", "Recuperación documental, certificación y D01 a D06 v1.1", "Rama docs/fase3-recuperacion-documental"],
        ["17 y 18-nov", "E2E de la clínica dental con DeepSeek y consolidación de sus evidencias", "Logs sanitizados, capturas y hashes (carpeta E2E-2026-11-17-clinica-dental-deepseek)"],
    ], [2.4, 9.0, 5.2])
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
    landscape_figure(d, FIG / "fig_casos_uso.png", "Figura 3. Casos de uso implementados (UC-01 a UC-11) y pendientes (UP-1 a UP-4).")
    landscape_figure(d, FIG / "fig_actividad_agente.png", "Figura 4. Diagrama de actividad del worker del agente.")
    landscape_figure(d, FIG / "fig_clases_python.png", "Figura 5. Módulos y clases reales del paquete alloxentric_real_time_agent.")
    landscape_figure(d, FIG / "fig_almacenamiento.png", "Figura 6. Modelo del almacenamiento actual: localStorage, cookie de sesión y logs; sin base de datos.")
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
    d.para("Casos de prueba: D05 v1.2 documenta 23 casos (TC-01 a TC-23): aprobados o cubiertos por pruebas automáticas la mayoría de los controles de acceso, historial y personas; no cumple el caso de latencia (TC-14); pendientes la validación auditiva de la voz, eco y ruido, y la telefonía con Asterisk. Los defectos y hallazgos están en D05 §7.")
    d.h1("10. Demostración funcional")
    d.para("[PROPUESTA] Guion de la demostración (≈5 a 7 minutos) sobre el estado integrado de main. Debe ensayarse antes del 19-nov; el procedimiento y la lista de verificación están en D06 §12 y §13.")
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
        ["Documentación obligatoria de Fase 3 sin confirmar (R-21)", "Crítico; activo [PROPUESTA]", "Obtener la pauta oficial; usar la tabla de la sección 13 como verificación"],
        ["Presentar lo no integrado como implementado (R-22)", "Alto; activo [PROPUESTA]", "Revisión cruzada contra la matriz de trazabilidad; rótulos explícitos"],
        ["Evidencias y registros Scrum insuficientes (R-17)", "Alto; parcialmente mitigado", "Adjuntar backlog, actas y registros disponibles"],
    ], [6.2, 3.4, 7.0])
    d.h1("12. Contribuciones individuales")
    d.para("La autoría se basa en commits y PR verificables; los merges no se cuentan como autoría. Las decisiones tomadas en reuniones externas requieren actas. Pendiente: contrastar con CoreStream y los acuerdos del equipo. [PENDIENTE DE VALIDACIÓN]")
    d.table_new(["Integrante", "Rol", "Contribución verificable", "Evidencia"], [
        ["Fernando Olguea", "Líder de proyecto y desarrollador", "Entorno inicial, LiveKit, DeepSeek, Gemini, pipeline, métricas, ADC, Web Demo inicial, seguridad, incidentes, nombre configurable y CI", "PR #1 a #3, #5, #7, #9 a #15, #17, #19, #20"],
        ["David Sepúlveda", "Scrum Master y desarrollador", "TTS ElevenLabs, pruebas y script de verificación real; diario individual", "PR #4 y archivos de TTS"],
        ["Juan Díaz", "Product Owner y desarrollador", "STT Chirp 3, personas y voces, optimizaciones, rediseño web, historial, Vercel, PR #18, D01 a D06 y E01", "PR #6, #16, #18; commit 31f096e de la rama documental"],
    ], [2.8, 3.2, 7.0, 3.6])
    d.h1("13. Documentación de Fase 3")
    d.para("Distinción entre lo informado como obligatorio por el equipo y la documentación de referencia, pendiente de validar con la pauta oficial. [REPORTADO POR EL EQUIPO]")
    d.table_new(["Elemento", "Clasificación", "Dónde se cubre", "Estado al 17-nov"], DOC_TABLE, [4.6, 3.2, 4.4, 4.6])
    d.h1("14. Limitaciones")
    for x in ["Las muestras de latencia son pequeñas (13, 5 y 8 turnos) y de una sola red; no hay protocolo acordado con el cliente.",
              "Solo la persona clínica dental tiene E2E archivado; las otras seis no se validaron con logs.",
              "No hay telefonía, guion oficial, comparación de costos, persistencia de negocio ni hosting persistente del worker.",
              "La certificación del 17-nov se hizo en un solo equipo y sin proveedores reales; falta ejecución independiente.",
              "La sesión del 17-nov es una sola, con voz humana no controlada, un proveedor de LLM y un worker local; el agendamiento es simulado (sin reservas reales). Faltan capturas del cierre y del historial de esa sesión.",
              "Backlog, actas y registros de CoreStream no están adjuntos."]:
        d.bullet(x)
    d.h1("15. Conclusiones")
    d.para("El equipo dispone de un MVP técnicamente funcional y demostrable, con pruebas automáticas en verde, CI y evidencia E2E (la última, del 17-nov con DeepSeek, aprobada con observaciones). Su principal brecha respecto del objetivo es la latencia (objetivo de 1 s no cumplido), junto con los componentes que dependen del cliente (guion, telefonía, costos). Para la evaluación del 19-nov, la prioridad es ensayar y registrar la demostración completa y presentar con precisión qué está integrado, qué se midió y qué sigue pendiente, manteniendo el nombre y el alcance del proyecto. Siguen pendientes Asterisk, la persistencia empresarial, el worker persistente y la integración del PR técnico #18; el agendamiento es simulado. [CONFIRMADO]")
    d.h1("16. Trabajo futuro y próximos pasos")
    for x in ["Obtener la pauta oficial de Fase 3 y confirmar los documentos obligatorios.",
              "Ensayar la demostración sobre main, grabar un video de respaldo y ampliar la muestra de latencia con más sesiones.",
              "Revisar y decidir el PR #18; si se integra, repetir pruebas y mediciones.",
              "Acordar con Alloxentric el protocolo de latencia, el guion oficial, el entorno de Asterisk y los conceptos de costo.",
              "Mover el worker a un servicio persistente con cuenta de servicio de Google y límites de gasto.",
              "Registrar Scrum (backlog, sprints, retrospectivas) y las actas en CoreStream."]:
        d.bullet(x)
    d.h1("17. Referencias")
    for x in ["D01 a D06 v1.1 (Fase 3/Entregables) y sus versiones históricas v1.0 (Fase 2/Evidencias Proyecto).",
              "Repositorio técnico fernandoknvz/alloxentric-real-time-agent, corte 77ff85c (PR #1 a #17, #19 y #20; PR #18 abierto).",
              "Registro consolidado de evidencias y matriz de trazabilidad (Fase 3/07_Evidencias y Fase 3/MATRIZ_TRAZABILIDAD_PRELIMINAR.md).",
              "Logs E2E del 31-oct, capturas y certificación del 17-nov, y evidencias E2E DeepSeek del 17-nov (Fase 3/07_Evidencias).",
              "Informe de definición del proyecto APT (Fase 1) y guía 2.4 de avance (Fase 2).",
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
        ["CI", "GitHub Actions sobre main", "Run 42435613596 (success) en 77ff85c", "PR #19 fusionado sin aprobación independiente"],
    ], [1.2, 5.0, 6.4, 4.0])
    out = OUT / "Informe_Academico_Consolidado_v1.1_Fase3.docx"
    d.save(out)
    return out


if __name__ == "__main__":
    print(build())
