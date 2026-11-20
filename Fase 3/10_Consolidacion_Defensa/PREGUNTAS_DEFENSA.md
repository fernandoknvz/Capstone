# Preguntas probables de la comisión y respuestas fundamentadas

**Estado:** PROPUESTA para ensayo del equipo. Las respuestas solo usan lo documentado y marcan su certeza. Si la comisión pregunta algo no cubierto, usar: «No tenemos ese dato documentado; lo que sí está documentado es…». Cualquier integrante puede responder cualquier pregunta; la columna «Sugerido» indica quién debería tomar la primera respuesta.

Certeza: **[C]** confirmado en archivos o ejecución propia; **[R]** reportado por el equipo, sin respaldo archivado; **[P]** pendiente; **[I]** inferencia.

## A. Alcance, decisiones y cliente

| N.º | Pregunta | Respuesta propuesta | Evidencia | Sugerido |
|---|---|---|---|---|
| 1 | ¿Cumplieron el objetivo original del proyecto? | Parcialmente. [C] Se construyó un pipeline de voz con LiveKit, STT, LLM y TTS, con pruebas y CI. [C] No se logró la telefonía Asterisk, el guion oficial de cobranza, la comparación de costos ni la respuesta de 1 s. | Informe §3, §14; D05 | Fernando |
| 2 | ¿Por qué cambiaron a VOXENTRA? ¿Lo aprobó el cliente? | [R] El equipo decidió continuar el MVP de forma autónoma y presentarlo como demostración para pymes. **No tenemos aprobación del cliente ni del docente documentada [P].** VOXENTRA es un nombre provisional, no una empresa. | Anexo §5–§6 | Fernando |
| 3 | ¿Hubo problemas de coordinación con el cliente? ¿Cuáles? | Lo documentado es limitado: [C] no están archivadas la transcripción del 2-sep ni las actas; [C] las decisiones atribuidas al cliente no tienen aprobación formal verificable; [C] no hay protocolo de latencia ni guion oficial acordados; [R] el equipo informa deficiencias de CoreStream. **No podemos afirmar reuniones incumplidas con evidencia.** | Anexo §4; `INDICE_MAESTRO.md` | Fernando |
| 4 | ¿Puede el equipo reutilizar el código y la identidad de Alloxentric? | Es una pregunta abierta: [P] no hay un permiso escrito en el expediente; por eso lo declaramos como pendiente y mantenemos las referencias históricas. | Anexo §5 | Fernando |
| 5 | ¿Quién tomó la decisión de cambiar de STT y de usar DeepSeek? | [C] El expediente no tiene aprobación formal verificable; el cambio de STT y de LLM es una decisión del equipo con motivos técnicos reportados (por ejemplo, fallas de API con Gemini el 17-nov). | Informe §14; D05 | Fernando |
| 6 | ¿VOXENTRA existe como empresa o producto? | No. [C] Es un nombre provisional de una demostración académica; no está verificada su disponibilidad como marca. | Anexo | Cualquiera |
| 7 | ¿Se incorporaron los ajustes de la retroalimentación del informe final? | [P] La retroalimentación no consta en nuestro expediente; debemos aclarar qué ajustes corresponden. (Resolver antes de la defensa.) | Guía 3.3 | Fernando |

## B. Arquitectura y técnica

| N.º | Pregunta | Respuesta propuesta | Evidencia | Sugerido |
|---|---|---|---|---|
| 8 | ¿Cómo funciona la arquitectura? | [C] El navegador entra a una sala de LiveKit con un token del servidor; un worker en Python transcribe con Chirp 3, genera la respuesta con un LLM y sintetiza con ElevenLabs. El cliente solo envía el id del agente. | Código; D01 | Fernando |
| 9 | ¿Por qué esos proveedores? | [C] El proyecto parte con ElevenLabs y un servicio de transcripción por pedido original; Chirp 3 reemplazó a Speechmatics y el LLM es intercambiable (Gemini o DeepSeek). [R] Las comparativas entre proveedores son reportadas y no reproducibles; **no hay una evaluación archivada que justifique la elección**, y no hay que atribuir motivos que no consten. | D01, D05 | Juan / David |
| 10 | ¿Cuántos agentes hay y están todos probados? | [C] Siete agentes configurados. **La clínica dental tiene una sesión documentada** (con métricas reportadas). **De los otros seis hay evidencia preliminar de una conversación por agente (20-nov), pero ninguno está aprobado integralmente**: cada sesión cubre solo parte de los criterios y falta el log del worker. | Código; `MATRIZ_SIETE_AGENTES.md` | Juan |
| 11 | ¿Cómo evitan que el LLM invente datos? | [C] Los prompts incluyen la regla de no inventar disponibilidad, saldos ni condiciones y de aclarar lo simulado (PR #22). **Pero en la sesión del 20-nov el agente inventó dirección y teléfono, y esa sesión fue anterior a esa regla; el efecto de la regla no está probado.** | I-01, I-03; PR #22 | David |
| 12 | ¿Hay seguridad y privacidad? | [C] Acceso por código; sesión por cookie; token del servidor con despacho forzado; CSP sin permisos amplios; sin grabación de audio; datos ficticios. | README del frontend | Fernando |
| 13 | ¿Qué pasa con las llamadas telefónicas reales? | [C] No hay telefonía; era parte del objetivo original y no se implementó. | Informe §14 | Fernando |

## C. Resultados y métricas

| N.º | Pregunta | Respuesta propuesta | Evidencia | Sugerido |
|---|---|---|---|---|
| 14 | ¿Qué latencia tiene el sistema? | [R] Dental (20-nov, n = 8): mediana 2,850 s, promedio 2,989 s, rango 2,61 a 4,14 s. En otros cuatro agentes, con datos parciales: medianas de 3,11 a 3,98 s y un valor máximo de 8,90 s (reclutamiento). **El objetivo de 1 s no se cumplió ni se demostró en ninguna sesión.** | `METRICAS.md`; `METRICAS_CONSOLIDADAS.md` | David |
| 15 | ¿Son confiables esas métricas? | Son medidas por el worker y transcritas por el equipo; **el registro original no está archivado**, por eso las clasificamos como reportadas. Una sola sesión no es una validación estadística. | `METRICAS.md` | David |
| 16 | ¿Qué componente causa la latencia? | [R] El fin de turno (≈ 1,3 s en promedio) y la primera respuesta del LLM (≈ 1,2 s en promedio, con un valor de 2,56 s en el turno más lento) son los mayores componentes informados. [I] El razonamiento del modelo (62 % de los tokens de salida) podría contribuir; no se aisló. | `METRICAS.md` | David |
| 17 | ¿Mejoró la latencia respecto de la sesión del 17-nov? | No podemos afirmarlo: la mediana fue 3,26 s el 17-nov y 2,85 s el 20-nov en la sesión dental, pero son sesiones únicas con condiciones distintas; y las medianas de otros cuatro agentes del 20-nov (3,11 a 3,98 s) son más altas. No concluimos tendencia ni causa. | `METRICAS_CONSOLIDADAS.md` §5 | David |
| 18 | ¿Qué errores hubo? | [R] Una advertencia de bloqueo del bucle de eventos (136 ms) y un error de decodificación de audio; la conversación continuó y el resumen reporta `errors {}`. No determinamos la causa. | `INCIDENCIAS.md` | David |
| 19 | ¿Cuántas pruebas automáticas hay? | [C] 231 de Python y 94 del frontend, todas aprobadas el 20-nov. Prueban estructura y compatibilidad, no la calidad de la conversación. | pytest y vitest | David |
| 20 | ¿Se grabó el audio de la prueba? | No. [C] La aplicación no graba audio; no tenemos grabación de la sesión. Hay capturas de la transcripción. | Inventario de capturas | Juan |
| 21 | ¿Cuánto cuesta operar el sistema? | [P] No hay comparación de costos; el uso informado en la sesión (118 s de audio de entrada, 927 caracteres de TTS y 5 243 tokens de entrada y 780 de salida del LLM) permitiría estimarlo, pero no se hizo. | `METRICAS.md` §6 | Fernando |

## D. Demostración, marca y proceso

| N.º | Pregunta | Respuesta propuesta | Evidencia | Sugerido |
|---|---|---|---|---|
| 22 | ¿Por qué el agente dental dio una dirección y un teléfono? | [C] No estaban en su configuración; el modelo los generó (I-01). La sesión fue **anterior** al PR #22, que reforzó los prompts; en las otras seis sesiones los datos de contacto citados sí coincidían con los configurados. **No repetimos la prueba dental**, así que no podemos afirmar que I-01 esté corregido. | Captura 04 dental; `INCIDENCIAS.md` | David |
| 23 | ¿Las reservas y los mensajes son reales? | No. [C] Todo es simulado: no hay calendario ni mensajería; el agente lo aclara, aunque en la sesión lo hizo después de afirmar la reserva (I-03). | Capturas 03 a 05 | Juan |
| 24 | ¿Funcionan los otros seis agentes? | En una conversación cada uno respondieron de forma coherente con su guion y aclararon que las operaciones eran simuladas [C, en video y capturas]. **No los presentamos como aprobados**: faltan rutas de prueba, el log y la escucha de las voces. Si quieren probar uno, la demo lo permite con ese aviso. | Anexo §8; `MATRIZ_SIETE_AGENTES.md` | Juan |
| 25 | ¿Quién hizo qué en el equipo? | [C] Según commits y PR: Fernando, la integración del pipeline, métricas, seguridad y CI; David, ElevenLabs y sus pruebas; Juan, Chirp 3, personas y voces, rediseño de la interfaz y el historial. Los merges no cuentan como autoría. [P] Las actividades de Fase 3 de David no están atribuidas en los documentos. | `MATRIZ_CONTRIBUCIONES.md` | Cada uno |
| 26 | ¿Usaron Scrum? ¿Hay evidencia? | [R] Una adaptación parcial; CoreStream solo entrega un reporte agregado sin tickets, y backlog, sprints y retrospectivas no están adjuntos. | Informe §5 | David |
| 27 | ¿Usaron inteligencia artificial para desarrollar? | [C] Sí: el repositorio técnico incluye un `CLAUDE.md` y los controles de versión de los entregables registran «consolidación asistida con Claude Code». Los diarios individuales también son borradores asistidos. Cada integrante debe responder por su propia parte y por cómo verificó lo que produjo la herramienta. | Control de versiones; diarios | Cada uno |
| 28 | ¿Por qué se fusionó el PR documental sin revisión? | [C] Se fusionó el 20-nov sin revisiones registradas, aunque pedía la revisión de los tres; lo reconocemos y solicitamos revisión posterior. | PR #8 | Fernando |
| 29 | ¿Qué cambiarían si empezaran de nuevo? | [P] Es una respuesta personal: cada integrante la formula desde su propio diario y experiencia. Puntos que la documentación respalda como brechas: archivar registros desde el inicio, protocolo de latencia acordado, guion oficial, validación de voces y revisión de los PR por pares. | Diarios (borradores); Informe §14 | Cada uno |
| 30 | ¿Qué sigue? | Archivar el registro del 20-nov, probar uno a uno los otros seis agentes, validar las voces, resolver la aprobación de la reorientación y evaluar palancas de latencia (sin medir). | Anexo §10 | Fernando |

## Preguntas de la Dirección de Carrera (perfil de empleabilidad)

| Pregunta | Respuesta propuesta |
|---|---|
| ¿Qué competencias desarrollaron? | Cada integrante responde desde su diario de reflexión y su evidencia documentada; no atribuir competencias no respaldadas. |
| ¿Cómo aplican esto en un contexto laboral? | Responder con lo aprendido sobre latencia, pruebas automatizadas, trazabilidad de evidencia y gestión de alcance, citando los límites del proyecto. |
| ¿Qué riesgo ético vieron? | Datos inventados por el modelo, suplantación de marcas (se reemplazaron por empresas ficticias), privacidad (sin grabación) y no presentar simulaciones como operaciones reales. |

## Preguntas trampa y respuesta

- «Entonces, ¿el proyecto cumplió?»: cumplió en lo técnico demostrable y declaramos lo que no cumplió (1 s, telefonía, costos, guion oficial).
- «¿Se puede usar hoy en una pyme?»: no; es una demostración con operaciones simuladas y sin integraciones.
- «Díganme que los siete agentes funcionan»: solo uno tiene prueba real documentada; los otros no se han probado de punta a punta.
- «¿El cliente está de acuerdo?»: no tenemos evidencia de aprobación del cliente.

## Preguntas nuevas tras la evidencia de los seis agentes (20-nov)

| N.º | Pregunta | Respuesta propuesta | Evidencia | Sugerido |
|---|---|---|---|---|
| 31 | ¿Qué tienen de evidencia los otros seis agentes? | Una conversación por agente el 20-nov: capturas, un video de pantalla (no publicable) y un CSV parcial de métricas para cuatro de ellos. [C] Hashes del paquete verificados. [R] Las métricas provienen de un extracto de log que no recibimos. | `INVENTARIO_CAPTURAS.md` | Juan |
| 32 | ¿Por qué la pantalla dice «sin prueba real documentada» si hay evidencia? | Porque la evidencia es preliminar y está pendiente de revisión; cambiar la insignia exige modificar código y una decisión del equipo (la Etapa 10B pide no cambiarla sin evidencia aprobada). | Incidencia S-12 | Juan |
| 33 | ¿Hubo errores en las seis sesiones? | [R] Advertencias de bloqueo del bucle de eventos, transcripciones tardías, un tiempo de espera del detector de fin de turno (reclutamiento) y errores de tareas pendientes (postventa). [C] En reclutamiento el agente interrumpió al usuario («Gracias,») y una respuesta tardó 8,9 s. Las conversaciones se completaron. No determinamos las causas. | `INCIDENCIAS.md` S-03 a S-08 | David |
| 34 | ¿Por qué no hay métricas de ventas ni de cobranza retail? | El extracto de log que recibimos no las contiene; las dos sesiones existen en el video, pero sin log no se pueden medir. | `METRICAS_CONSOLIDADAS.md` | David |
| 35 | ¿Por qué no promedian todas las sesiones? | Porque son extractos parciales de sesiones únicas, con distinto número de turnos, un turno interrumpido y un valor atípico; un promedio global daría una precisión que los datos no sostienen. Informamos por agente y el rango. | `METRICAS_CONSOLIDADAS.md` §4 | David |
| 36 | ¿Alguien escuchó las voces? | No hay una valoración auditiva documentada; es una limitación declarada. El video incluye audio y está pendiente de escucha por una persona del equipo. | Incidencia S-13 | Cualquiera |
| 37 | ¿Pueden mostrarnos la prueba de un agente que no sea el dental? | Sí: la demo permite elegirlo, o pueden ver una captura real del 20-nov; no incluimos el video porque muestra el escritorio y datos de terceros. | `ESTRUCTURA_PRESENTACION.md` | Juan |
