# Matriz de trazabilidad inicial

Esta matriz no sustituye la matriz transversal de Fase 3. Vincula antecedentes históricos solo cuando existe apoyo interno suficiente y separa explícitamente la actividad reconstruida de la evidencia técnica posterior.

| Necesidad o requisito | Actividad histórica | Decisión o implementación verificable | Archivo, commit o PR referido internamente | Prueba / resultado | Documento académico | Estado y cautela |
|---|---|---|---|---|---|---|
| Conversación de voz en tiempo real | ACTA-01: discusión inicial reconstruida | Pipeline de voz y transporte LiveKit descritos como integrados | PR #2/#7, según `Fase 2/Evidencias Grupales/Documentacion Tecnica/Consolidado Final/MATRIZ_TRAZABILIDAD_PRELIMINAR.md` | E2E 31-oct y 17-nov; conversación completada | D01, D03, D05 | Implementado/probado; no demuestra aprobación en ACTA-01 |
| STT y TTS | ACTA-01 y REG-03: Speechmatics y ElevenLabs como antecedentes | STT Chirp 3 y TTS ElevenLabs descritos en `main` | PR #6 (STT) y PR #4 (TTS), según matriz existente | Pruebas unitarias y E2E referidas; ElevenLabs operativo | D01, D03, D05 | Parcial respecto del antecedente: Speechmatics no queda acreditado como implementación vigente |
| Generación de respuesta | REG-03 y REG-05: proveedores LLM y acceso Gemini | Gemini y DeepSeek descritos como operativos en cortes posteriores | PR #3/#5 y EV-14/EV-15, según matriz/registro existentes | Gemini E2E 31-oct; DeepSeek 9 respuestas el 17-nov | D03, D05 | Implementado con observaciones; esas pruebas no prueban el incidente del 15–16 oct |
| Latencia p95 inferior a 1 s | ACTA-01/REG-03: objetivo retrospectivo | Instrumentación de métricas integrada | PR #9 y E01/EV-14/EV-15, según fuentes internas | No cumple: métricas publicadas superan 1 s en la mayoría de turnos | D01, D03, D05, D06 | Implementación parcial; p95 específico no acreditado en este expediente |
| Telefonía Asterisk | ACTA-01/REG-03: integración posible | No se encontró integración acreditada | Sin archivo/commit verificable en la matriz vigente | Sin prueba de llamada telefónica | D01, D03, D05 | Pendiente |
| Multitenancy / administración SaaS | REG-02/REG-03: posibilidad no confirmada | No se identificó persistencia empresarial ni implementación multitenant verificable | Sin correspondencia segura | Sin prueba | D01, D03 | Pendiente/propuesto; no aprobado |
| Seguridad de secretos | REG-03: hallazgo histórico de credenciales embebidas | Configuración y sanitización descritas en el estado actual | PR #10–#16, según matriz vigente | Escaneo documental reportado sin secretos detectados | D02, D06 | El control actual no constituye auditoría del archivo histórico mencionado |
| Planificación por hitos | REG-04: tres ventanas comunicadas | Entregables y evidencias posteriores existen; EV-20 aporta un reporte agregado de CoreStream | Commits académicos `7369bbc`, `260526e`, `27703cd`; `CoreStream/corestream-reporte-year-2026-11-19.pdf` | El reporte registra 16 tareas completadas, pero no incluye tickets ni permite evaluar cada hito | D04 | Evidencia de gestión separada; REG-04 conserva E2/P y el cumplimiento no está acreditado |
| Continuidad visual de la demo de clínica dental | No corresponde a una reunión histórica | Interfaz de demostración y conversación visible | `Demo_E2E_2026-11-17/` (EV-21) y expediente E2E del 17-nov | Capturas muestran entre 1 y 16 mensajes; logs existentes aportan métricas por separado | D05 | Evidencia funcional complementaria; no acredita latencia, telefonía o persistencia |

## Vacíos de trazabilidad

- No hay fuente accesible que vincule formalmente las prioridades MoSCoW, los roles propuestos o DART_14 con una aprobación del cliente.
- Existe un reporte agregado de CoreStream, pero no una exportación detallada de tickets ni trazabilidad verificable de `DART_14`; tampoco hay acta firmada ni transcripción de Fireflies.
- `BOT_HITES.zip` y `discador (1).py` no están incorporados; no se realizó auditoría actual de su contenido.
- Las métricas técnicas existentes se conservan con sus propias limitaciones y no deben atribuirse retrospectivamente a una reunión.
