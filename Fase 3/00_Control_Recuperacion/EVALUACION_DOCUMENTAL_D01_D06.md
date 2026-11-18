# Evaluación de calidad documental D01-D06

## Evaluación general

Los seis documentos tienen buena estructura, clasificación explícita de afirmaciones, tablas de control y referencias cruzadas. Son una base sólida para Fase 3, pero no deben publicarse en su estado actual: fueron preparados el 30 de octubre con corte en PR #16 y todos indican “borrador para revisión del equipo”.

Control técnico realizado: los seis paquetes DOCX abren correctamente, no contienen comentarios ni cambios controlados pendientes y su texto, tablas, encabezados y referencias fueron inspeccionados. La rasterización visual página por página quedó **PENDIENTE** porque el entorno de auditoría no dispone del módulo `pdf2image` ni de un renderizador DOCX/PDF; antes de publicar nuevas versiones se debe ejecutar el flujo de renderizado y revisar todas las páginas.

| Documento | Fortalezas | Información desactualizada o contradictoria | Evidencia faltante | Actualización requerida |
|---|---|---|---|---|
| D01 Arquitectura | Componentes, secuencia, seguridad, decisiones y latencia bien separados. | PR #16 figura abierto; controles de persona/origen/Vercel figuran como propuesta; conteos 200/91; no incluye PR #17-#20. | Aprobaciones del cambio de STT/LLM; hosting persistente; Asterisk; guion oficial. | Cambiar estado de PR #16 a integrado; añadir nombre configurable, CI y evidencia E2E 31-oct; mantener PR #18 separado. |
| D02 Riesgos | Registro amplio, valoración y protocolos accionables. | Fechas, estados y riesgo temporal corresponden al 30-oct; CI aparece implícitamente ausente. | Evidencia de rotación de claves, licencias de voces, límites de gasto, actas. | Revalorar riesgos al 17-nov y agregar riesgo académico por Fase 3/DART no aprobado. |
| D03 Requerimientos | Distingue confirmados, propuestos y pendientes; matriz funcional/no funcional. | Estados de escenarios y despliegue dependen de PR #16 abierto; algunas fuentes son declaraciones no adjuntas. | Pauta Fase 3, aceptación del cliente, normativa, Asterisk y protocolo costo/efectividad. | Actualizar estados y agregar columna fuente verificable/fecha de validación. |
| D04 Avance | Buena cronología y reconocimiento de desviaciones. | Indica 15 PR fusionados y PR #16 abierto; no refleja PR #17, #19 y #20; atribuciones pendientes pueden resolverse con commits. | CoreStream, actas, pauta Fase 3, revisión formal de algunos PR. | Actualizar corte y separar avance académico, técnico integrado y trabajo abierto. |
| D05 Pruebas | Distingue unitarias, manuales, E2E y telefonía; declara limitaciones. | Afirma que no existe CI; usa 200 Python/91 web; no incorpora E2E con logs del 31-oct. | Ejecución reproducible actual, Asterisk, muestra suficiente, validación de seis personas. | Incorporar CI de PR #19/#20 y E2E 31-oct; conservar E01 como corte histórico. |
| D06 Despliegue | Procedimiento claro, variables sin valores y diagnóstico de incidentes. | Conteos 200/91; no incorpora evidencia CI; sigue describiendo rutas del corte PR #16. | Hosting persistente del worker, cuenta de servicio productiva, límites de gasto. | Actualizar verificación, CI y advertencias; no añadir PR #18 como disponible. |

## Información que continúa vigente

- Arquitectura navegador → LiveKit Cloud → worker Python → STT → LLM → TTS → LiveKit.
- Google Chirp 3 como STT de `main`.
- Gemini o DeepSeek como LLM de `main`.
- ElevenLabs como TTS.
- Web Demo con funciones de sesión y token.
- Métricas locales estructuradas sin texto de conversación.
- Falta de Asterisk, persistencia de negocio, protocolo de costo/efectividad y worker persistente demostrado.
- Incumplimiento del objetivo de latencia de un segundo.
- Escenarios de cobranza ficticios y no equivalentes a un guion oficial del cliente.

## Referencias a funcionalidades no integradas

- Toda alternativa de STT seleccionable, Anthropic y LiveKit Inference pertenece al PR #18 abierto.
- Las mediciones de PR #18 con audio sintético no representan el estado integrado de `main`.
- DART/cobranza para pymes no constituye requerimiento aprobado ni funcionalidad identificable en `main`.

## Contradicciones internas o con el estado actual

1. D05 declara “no hay integración continua”; desde PR #19 existe workflow y PR #20 documenta ejecuciones.
2. D01, D04 y D06 tratan PR #16 como abierto; fue fusionado el 30-oct.
3. D01/D04 clasifican Vercel, personas y optimizaciones como no integradas; actualmente están en `main`.
4. Los conteos 200/91 corresponden a PR #16; PR #17 declaró 214 pruebas Python. El PR #18 declaró 281/103, pero esos conteos son de una rama no integrada.
5. La evidencia del 26-oct sigue correctamente marcada como reportada y sin logs; no debe sustituirse por la del 31-oct ni mezclarse estadísticamente.
