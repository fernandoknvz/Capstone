# Informe DART-14-2.5 (transcripción sanitizada)

> Transcripción textual del informe original del 19-oct-2026; ver README.md para procedencia y transformaciones. La Figura 1 se reemplazó por la captura recortada `captura_agent_console_recortada.png`.

ALLOXENTRIC REAL TIME AGENT

Informe de evidencia técnica · DART-14-2.5

Validación end-to-end del pipeline de voz | 19 de octubre de 2026


| Ticket / plataforma | DART-14-2.5 · CoreStream |
| Proyecto académico | Capstone Ingeniería en Informática · Duoc UC · S2 2026 |
| Responsable de la prueba | Fernando Olguea González (operación del cliente y evidencia) |
| Entorno | Worker Python local conectado a LiveKit Cloud; Agent Console como cliente |
| Versión registrada | LiveKit Agents 1.8.4 |
| Base de código | main · e8dc946 (según verificación previa reportada) |
| Dictamen | VALIDACIÓN FUNCIONAL E2E EXITOSA, con observaciones de cierre y rendimiento |

1. Objetivo y alcance

Comprobar, mediante una interacción de voz real y controlada, que el agente recibe audio, obtiene una transcripción, genera una respuesta con el modelo de lenguaje y devuelve una respuesta audible a través de LiveKit. Se realiza una sola intervención del usuario y no se evalúan concurrencia, disponibilidad ni cumplimiento de umbrales de latencia.

2. Escenario ejecutado


| Sala | e2e-alloxentric-test-02 |
| Inicio del worker | 13:10:35 (hora registrada en log) |
| Recepción del job | 13:10:51 |
| Inicio del pipeline | 13:11:04 |
| Pregunta del usuario | «Hola, ¿puedes presentarte en una frase?» |
| Respuesta mostrada | «Hola, soy el asistente de voz de prueba del proyecto Alloxentric Real Time Agent, listo para ayudarte.» |
| Salida del participante | 13:11:31 · CLIENT_INITIATED |
| Cierre de sesión | 13:11:34 · participant_disconnected |
| Apagado del worker | 13:12:29 · shutting down worker |

3. Resultado por componente


| LiveKit / despacho | [CONFIRMADO] Job recibido; sala y participante vinculados; agente registrado. |
| STT · Google Chirp 3 | [CONFIRMADO funcionalmente] La pregunta fue transcrita y mostrada en Agent Console. No hay una métrica aislada de precisión. |
| LLM · Gemini | [INFERENCIA FUERTE] La respuesta coherente es consistente con el pipeline configurado con Gemini; el log no contiene una traza explícita del contenido de salida del LLM. |
| TTS · ElevenLabs | [CONFIRMADO por testimonio del operador] El usuario informó que escuchó la respuesta; el log proporcionado no contiene una métrica de audio generado. |
| Pipeline E2E | [CONFIRMADO] Se observó transcripción, respuesta textual y se reportó audio audible en una misma sesión. |
| Grabación | [CONFIRMADO] El despacho indica enable_recording=false; el panel de sesión muestra grabación desactivada. |

4. Evidencia visual: Agent Console

Figura 1. Captura aportada por el equipo tras la interacción. Se observa la pregunta, la respuesta del agente y la sesión finalizada.

5. Extractos verificables del registro

• 13:10:35 · starting worker · version 1.8.4

• 13:10:51 · received job request · room=e2e-alloxentric-test-02 · enable_recording=false

• 13:11:04 · Pipeline de voz iniciado en la sala

• 13:11:31 · closing agent session · reason=CLIENT_INITIATED

• 13:11:34 · Sesion cerrada: motivo=participant_disconnected

• 13:12:29 · shutting down worker

Fuente: registro de terminal aportado por el equipo (19-10-2026). Se reproducen solo campos relevantes; se excluyen identificadores y rutas locales innecesarios.

6. Hallazgos técnicos y limitaciones


| OBS-01 · Inicialización | [CONFIRMADO] Bloqueo del event loop de 9,574 s durante la obtención de configuración/credenciales de Google Cloud en el inicio del job. No equivale a latencia por turno. |
| OBS-02 · Otros bloqueos | [CONFIRMADO] Advertencias adicionales de 1,574 s, 262 ms, 136 ms y 152 ms. Requieren evaluación si se reproducen. |
| OBS-03 · Finalización | [CONFIRMADO] Tras “shutting down worker” aparecen AssertionError en FfiHandle.__del__ y “Task was destroyed but it is pending!”. No impidieron la respuesta previa. Origen preciso pendiente. |
| OBS-04 · Medición | [PENDIENTE] No existen mediciones confiables de latencia STT, LLM, TTS ni tiempo total por turno. |
| OBS-05 · Alcance | [PENDIENTE] No se ha validado carga, concurrencia, estabilidad prolongada, manejo de fallos ni cumplimiento de SLA. |

7. Criterios de aceptación de esta ejecución


| Despacho a worker local | Cumplido: job recibido y pipeline iniciado. |
| Reconocimiento de frase de prueba | Cumplido: pregunta visible en Agent Console. |
| Generación de respuesta | Cumplido: respuesta visible en Agent Console. |
| Audio de salida | Cumplido según confirmación directa del operador; evidencia instrumental adicional pendiente. |
| Desconexión de usuario | Cumplido: CLIENT_INITIATED y cierre de sesión registrados. |
| Apagado sin errores | No cumplido: errores de liberación de recursos al finalizar. |

8. Conclusión y siguiente acción

La prueba acredita una primera integración funcional end-to-end en ambiente de desarrollo. La interacción fue exitosa, pero el resultado NO acredita todavía rendimiento en tiempo real, robustez ni cierre limpio del worker. Se recomienda adjuntar este informe al ticket DART-14-2.5, registrar las observaciones técnicas y planificar mediciones de latencia y una revisión del ciclo de cierre en actividades posteriores.

Decisión sugerida para CoreStream: completar DART-14-2.5 si su criterio de aceptación es demostrar una conversación E2E funcional. Si exige apagado limpio o métricas de latencia, mantener abierto hasta verificar esos criterios. [PENDIENTE] Contrastar con la definición oficial del ticket.

9. Trazabilidad de evidencias


| E-01 · Captura Agent Console | Demuestra interacción y texto de respuesta. Actividad: prueba E2E. Objetivo: validar integración de servicios de voz. Competencia: integración y pruebas de software. |
| E-02 · Registro de terminal | Demuestra worker, despacho, apertura/cierre y advertencias. Actividad: ejecución y diagnóstico. Competencia: implementación y validación técnica. |
| E-03 · Resultado de pytest | 86 pruebas aprobadas, según ejecución local reportada antes de la prueba real; no reemplaza evidencia E2E. Competencia: aseguramiento de calidad. |
