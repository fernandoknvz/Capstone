# Registro de evidencias — E2E Clínica dental con DeepSeek (2026-11-17)

Estado: borrador para revisión del equipo (v2, 2026-11-18: se agregan §7 capturas y §8 verificación cruzada; v1 conservada en el respaldo externo del equipo, SHA-256 6c795d40134af70836f649a4d5ca17833f3881cab0b2ec30e242962071cac466). Sesión única; no es validación estadística.
Leyenda: [CONFIRMADO] verificable en logs; [REPORTADO] informado por una persona, sin respaldo en logs; [INFERENCIA]; [PENDIENTE].

## 1. Identificación de la sesión
| Elemento | Valor | Estado |
|---|---|---|
| Commit ejecutado | fe88e2687fdfefbe2102c62df3cb6c310afe2a04 (rama docs/DART-14-5.6-ci-documentation; mismo árbol Git que origin/main 77ff85c (ver §8)) | [CONFIRMADO] |
| Worker | alloxentric-real-time-agent-dev, id AW_vAjwQSEeW2dW, región Brazil, registrado 22:38:26 | [CONFIRMADO] |
| Job / Dispatch / Room id | AJ_zm9g5TDNqgG5 / AD_n7HS96fqwCXK / RM_ffMVBTym2BpX (nombre de sala e identidad redactados) | [CONFIRMADO] |
| Persona | clinica-dental | [CONFIRMADO] |
| Solicitud del job | 2026-11-17 22:41:56,995 (UTC-03:00) | [CONFIRMADO] |
| Desconexión del cliente | 22:44:22,944 (CLIENT_INITIATED); cierre de sesión 22:44:25 | [CONFIRMADO] |
| Duración (job → desconexión) | 145,9 s | [CONFIRMADO] |
| LLM | DeepSeek, modelo deepseek-flash (llm_usage: api.deepseek.com) | [CONFIRMADO] |
| STT | Google Chirp 3 (chirp_3) | [CONFIRMADO] |
| TTS | ElevenLabs eleven_v4_turbo | [CONFIRMADO] |
| Grabación del servidor | enable_recording=false, record=False | [CONFIRMADO] |

Esta sesión es distinta de las anteriores del 2026-11-17 (Gemini, API_KEY_INVALID; jobs AJ_85xF2YcY3Thz y AJ_FfgnQQhpXcrz), que no tienen respuestas del LLM.

## 2. Validación técnica
| Componente | Dictamen | Evidencia |
|---|---|---|
| Conexión LiveKit | CONFIRMADO FUNCIONAL | job recibido, RoomIO linked, cierre limpio |
| STT Chirp 3 | CONFIRMADO FUNCIONAL | stt_usage 134,0 s; transcription_delay_s presente en 5 turnos. El texto transcrito no se registra por diseño: lo observado en pantalla es [REPORTADO] y consta en el video |
| Detección de turnos | CONFIRMADO FUNCIONAL | eot_usage (turn-detector-v1); end_of_turn_delay_s en 8 turnos |
| LLM DeepSeek | CONFIRMADO FUNCIONAL | 9 respuestas con llm_node_ttft_s; llm_usage 5 308 tokens de entrada, 1 050 de salida (771 de razonamiento); errors: {} |
| TTS ElevenLabs | CONFIRMADO FUNCIONAL | 10 turnos con tts_node_ttfb_s; 890 caracteres, 66,6 s de audio |
| Reproducción audible | NO VERIFICABLE en logs | playback_latency_s medido en el cliente; la audición consta solo en el video [REPORTADO] |
| Historial en el navegador | NO VERIFICABLE en logs | vive en localStorage; verificar en capturas/video |
| Cierre de sesión | CONFIRMADO | participant_disconnected |
| Errores y excepciones | Ninguno | session_summary errors {}; sin trazas |

Cantidad de turnos del agente: 10 (1 saludo estático + 9 respuestas generadas por el LLM). El saludo no pasa por el LLM (agent.py: session.say).

## 3. Métricas (segundos; fuente: líneas "metrics turn", mediciones del SDK)
| Métrica | n | Media | Mediana | Mín. | Máx. | p95 |
|---|---:|---:|---:|---:|---:|---:|
| E2E (todos los turnos con dato) | 8 | 2,961 | 3,264 | 0,557 | 5,499 | 5,009 |
| E2E sin turno interrumpido | 7 | 3,304 | 3,650 | 0,610 | 5,499 | 5,079 |
| LLM TTFT | 9 | 1,830 | 1,788 | 0,942 | 2,483 | 2,478 |
| TTS TTFB | 10 | 0,293 | 0,293 | 0,280 | 0,303 | 0,301 |
| Espera STT (solo > 0) | 5 | 1,356 | 1,372 | 1,221 | 1,513 | 1,491 |
| Fin de turno | 8 | 1,097 | 1,256 | 0,472 | 1,527 | 1,513 |

E2E por turno: T2 0,557 (interrumpido) · T4 3,650 · T5 0,610 · T6 3,814 · T7 2,581 · T8 5,499 · T9 4,100 · T10 2,879. T1 (saludo) y T3 sin E2E (sin emparejamiento con turno de usuario). T8 tuvo playback_latency_s de 2,134 s; las demás, ≤ 0,08 s.
Las etapas pueden solaparse: no se suman. El p95 con n=8 no es estadísticamente robusto. Startup: startup_s 0,410; el runner tardó 2,92 s en inicializar.

**Comparación con el objetivo de 1 s:** solo 2 de 8 turnos medidos (T2 y T5) tuvieron E2E ≤ 1 s; la mediana (3,26 s) lo triplica. El objetivo de 1 s NO se cumple. Los dos valores bajos coinciden con transcription_delay_s = 0 (transcripción disponible antes del cierre del turno), y no con un LLM más rápido (TTFT 1,15 y 1,62 s). [INFERENCIA]

## 4. Hallazgos / incidencias
- Latencia: el TTFT de DeepSeek (0,94–2,48 s) y la espera de la transcripción final (~1,2–1,5 s) dominan. 771 de 1 050 tokens de salida son de razonamiento (73 %). [INFERENCIA: el razonamiento contribuye al TTFT; no se aisló]
- Aviso del SDK en T2: "transcript arrives after turn has been committed" (sugiere subir min_delay del endpointing).
- Dos POST /api/livekit-token (201) para un único job; causa no investigada (también el 2026-10-31). [PENDIENTE]
- Un 401 en GET /api/demo/session previo al login (204); comportamiento normal sin sesión.
- La interrupción quedó marcada en T2 (interrupted: true).

## 5. Evidencias
| Evidencia | Ubicación | Estado |
|---|---|---|
| Video de pantalla "2026-11-17 22-41-32.mp4" (~2:53, 15 722 688 bytes, guardado 2026-11-17 22:44:26) | Respaldo externo del equipo, carpeta Videos (fuera de Git, sin modificar) | Integridad [CONFIRMADO]: SHA-256 recalculado d6fe9270f86bacab76231fc8ea103dad0b88e8bdc486bbfde3ab7457ed5cabfa, coincide con el informado. Contenido: revisado visualmente por Claude el 2026-11-18 mediante fotogramas (ver §7); el audio no se revisó [REPORTADO]. El video muestra pestañas, marcadores, avatar de perfil y barra de tareas del equipo, y hacia el final un nombre completo pronunciado durante la demostración: NO debe incorporarse a Git ni compartirse sin recorte |
| Log original del worker (fuera de Git) | Respaldo externo del equipo: originales/worker-dev-223820.log | [CONFIRMADO] |
| Log original de Netlify CLI | Respaldo externo del equipo: originales/netlify-223829.log | [CONFIRMADO] |
| Logs sanitizados | worker-AJ_zm9g5TDNqgG5.sanitizado.log; netlify-cli.sanitizado.log | [CONFIRMADO] |
| SHA-256 de originales, sanitizados y documentos | SHA256SUMS.txt (esta carpeta: solo los archivos incorporados a Git). El manifiesto de respaldo externo incluye además los originales y el video, que no están en Git | [CONFIRMADO] |
| Dictamen técnico | APROBADO CON OBSERVACIONES: 10 turnos del agente (1 saludo estático + 9 respuestas de DeepSeek), errors {}; E2E mediana 3,26 s, objetivo de 1 s NO cumplido (2 de 8 turnos) | [CONFIRMADO en logs] |
| Capturas de conversación y transcripción | 5 fotogramas recortados al viewport de la app, en capturas/ (ver §7) | [CONFIRMADO] extraídas del video original y revisadas visualmente; contenido en pantalla [REPORTADO] respecto de la voz |

Sanitización: ANSI eliminado; redactados nombre de sala, identidad del participante, subdominio de LiveKit y rutas locales; pilas de avisos de bloqueo omitidas; el log de Netlify conserva solo carga de funciones y pares solicitud/respuesta. Sin tokens, claves, códigos de acceso, transcripciones ni audio. Permanece la URL pública del gateway de LiveKit.

## 6. Limitaciones
Una sola sesión; n=8 turnos con E2E; voz humana y frases no controladas; el contenido hablado y la audición no son verificables en logs; sin reloj externo; DeepSeek validado solo en esta sesión; el sistema es una simulación de agendamiento sin reservas reales: no existe integración con Asterisk, ni persistencia empresarial, ni reservas reales.

## 7. Capturas extraídas del video (2026-11-18)
Origen: video original «2026-11-17 22-41-32.mp4» (respaldo externo, fuera de Git) (1920×1080, 60 fps, 173,2 s; SHA-256 recalculado el 2026-11-18, idéntico al de §5; el video no se modificó). Método: lectura del fotograma en el instante indicado (OpenCV, entorno aislado) y recorte al viewport de la aplicación (x 350–1570, y 120–1005 px). El recorte excluye pestañas, marcadores, avatar de perfil, barra de tareas, reloj y clima. No se retocó ningún píxel interior. Cada captura fue revisada visualmente: sin credenciales, códigos de acceso, correos ni nombres completos. El reloj de la interfaz (temporizador de llamada) inicia ≈ 25 s después del inicio del video.

| Archivo (carpeta capturas/) | Momento del video | Qué se ve | Funcionalidad que demuestra | Limitaciones | SHA-256 |
|---|---|---|---|---|---|
| captura-01-interfaz-inicial-t000s.png | 0:00 | Pantalla de acceso con campo «Código de acceso» vacío; insignia «Simulación · datos ficticios» | Interfaz inicial y acceso controlado por código | No se ve el ingreso del código ni su validación; la validación consta solo en el log de Netlify (POST login 204) | da8e3de867bf2cb163a3ae3999ba3bf6e9ca0a506d26a4c92e020b29f7e5eb2c |
| captura-02-conversacion-saludo-t030s.png | 0:30 (temporizador 00:05) | Llamada activa con «Clínica dental», estado «HABLANDO», 1 mensaje | Conversación activa; saludo del agente mostrado en la transcripción | Texto del saludo parcial («Clínica Dental»): transcripción en streaming, el saludo completo aparece en la captura 03; el saludo es estático (no pasa por el LLM) | 64a9034a73d0aac4455f3a9018f6b492ffdbf576bb0aeed6cfd84c5ad94c4429 |
| captura-03-respuestas-generadas-t060s.png | 1:00 (00:35) | 5 mensajes; saludo completo, respuesta con horarios; estado «TE ESCUCHA» | Respuestas generadas en contexto (horarios) y transcripción en vivo de ambos interlocutores | El mensaje «Hola, Juan,» está truncado, coherente con el turno 2 interrumpido (interrupted: true) [INFERENCIA: el log no registra texto]; no prueba por sí sola que el LLM fuera DeepSeek (eso consta en el log) | 78f0fbae7674a5d3c0a6b722fe825415e5477f6e285bcc78da98cb4943ded274 |
| captura-04-continuidad-turnos-9-mensajes-t090s.png | 1:30 (01:05) | 9 mensajes: consulta por «doctor Pérez», respuesta que declara no tener su agenda, repetición de horarios | Continuidad multi-turno y respuesta sin inventar datos que el agente no posee | Nombre de un profesional pronunciado durante la demostración (no se verificó su carácter ficticio); sin audio; solo una sesión | 85d3261cfc8d86b8d676dfa710293929be5a6fcd05eb5c8405f337f3fcae85cf |
| captura-05-continuidad-turnos-15-mensajes-t140s.png | 2:20 (01:55) | 15 mensajes: rechazo de las 20:00 (cierre 19:00), oferta de 17:00/18:00, motivo «limpieza», precio de 35.000 pesos | Continuidad de varios turnos, manejo de restricción de horario, agendamiento conversacional simulado | El texto «Anotado…» es conversacional: NO hay reserva real ni persistencia. Mensaje final truncado («¿Me confirma su nombre»). El precio proviene del guion de la persona, no de un sistema de la clínica. El tramo final con nombre completo ficticio se omitió a propósito | 976a81232be3267d7f7eee87f11710fbd65f5f2cf34e4f17e3c0d060c6bce042 |

Fotogramas del video descartados: lista de agentes (≈0:20; muestra un nombre ficticio de deudor, mismo criterio del commit 47d2c53 del repositorio Capstone) y cierre (≈2:50; muestra un nombre completo pronunciado durante la demostración y 19 mensajes). Si se necesita el cierre, hay que enmascarar ese texto con recuadro rotulado «omitido» y declararlo.
Limitaciones comunes: las capturas muestran la pantalla del cliente; no prueban audio ni latencia. Mic. visible: «Microphone Array (Realtek(R) Audio)», nombre genérico de hardware.

## 8. Verificación cruzada (2026-11-18)
| Verificación | Resultado |
|---|---|
| SHA256SUMS.txt v1 vs. archivos (6 de 6 entradas) | Coinciden |
| SHA-256 del video vs. registro | Coincide (d6fe9270…cabfa) |
| Métricas del registro (§3) recalculadas desde el log sanitizado | Coinciden con el registro; diferencia solo de redondeo en p95 de espera STT (1,490 vs 1,491) |
| Turnos con E2E ≤ 1 s | Turnos 2 y 5 (2 de 8): coincide |
| 10 turnos del agente vs. pantalla | 19 mensajes al cierre (02:25) = 10 del agente + 9 de la persona: consistente |
| Duración | Temporizador de la UI 02:25 ≈ 145,9 s job→desconexión del log: consistente |
| Hora | Inicio del video 22:41:32 + ≈25 s ≈ solicitud del job 22:41:56,995: consistente |
| Netlify: 401 previo, login 204, dos POST livekit-token 201 | Coincide con §4 (causa del duplicado sin investigar) |
| Proveedor LLM | llm_usage: deepseek-flash / api.deepseek.com; el log no contiene texto de conversación |
| Código ejecutado: commit fe88e268 frente a origin/main 77ff85c | Commits distintos (fe88e268 es ancestro de 77ff85c, el merge del PR #20) pero **mismo árbol Git** `ed9ad04e68eff160b850308e486cf3c51cf9d060`, verificado el 2026-11-18 en el repositorio técnico: sin diferencias funcionales ni documentales. El log solo registra el hash del commit; no existe evidencia de que el árbol de trabajo local estuviera limpio durante el ensayo |
