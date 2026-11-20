# Matriz de trazabilidad Fase 3

Fecha de corte: 17 de noviembre de 2026. Repositorio técnico `main`: `77ff85c3ad252b52df429380ea916cf84c1725a4`.

Atención a la numeración: el **RF-04 de esta matriz** (generación de respuesta del LLM) equivale al **RF-03 de D03**; el **RF-04 de D03** (voz de contexto chileno, TTS) equivale al **RF-05 de esta matriz**. Ver la tabla de equivalencias al final.

Actualización del 18-nov-2026: se incorpora la evidencia E2E con DeepSeek (`Fase 3/07_Evidencias/E2E-2026-11-17-clinica-dental-deepseek/`). El agendamiento de esa sesión es una simulación conversacional: no hay reservas reales, Asterisk ni persistencia empresarial.

Actualización del 19-nov-2026: se incorporan EV-20 (reporte agregado CoreStream) y EV-21 (cuatro capturas derivadas por recorte determinístico de la demostración del 17-nov). EV-20 es evidencia de gestión y EV-21 es evidencia funcional visual; ninguna modifica por sí sola el estado de cumplimiento de requisitos o hitos.

Actualización del 19-nov-2026 (Etapa 2): D01 v1.2, D02 v1.2, D03 v1.2, D04 v1.2, D05 v1.3, D06 v1.2 e Informe v1.2 son los entregables vigentes (versiones anteriores en `Fase 3/Entregables/_historico/`). D05 v1.3 rebajó TC-02, TC-03, TC-04, TC-07 a TC-10 y TC-17 al respaldo archivado; se incorpora EV-22 (DART-14-2.5, sanitizada). Las filas RF-03 y RF-04 conservan su estado de integración, pero indican lo no verificado.

Estados usados:

- **MAIN PROBADO:** integrado en `main` y con prueba o evidencia verificable.
- **MAIN PARCIAL:** integrado, pero la validación real es limitada o indirecta.
- **RAMA PROBADA:** existe y tiene pruebas en una rama o PR abierto; no está integrado.
- **NO PROBADO:** implementado sin prueba verificable del comportamiento indicado.
- **PENDIENTE:** no existe implementación verificable.
- **PROPUESTO:** evolución no aprobada.

| ID | Requerimiento | Implementación | Integración | Prueba | Resultado | Evidencia verificable | Responsable | Estado |
|---|---|---|---|---|---|---|---|---|
| RF-01 | Conversación de voz en tiempo real | `agent.py`, `pipeline.py` | `main`, PR #2/#7 | Unitarias y E2E web | Conversación completada | PR #7; logs E2E 31-oct; E2E 17-nov (EV-14 a EV-17); continuidad textual visible en EV-21 | Fernando | MAIN PROBADO |
| RF-02 | Transporte de audio LiveKit | Worker y sala LiveKit | `main` | E2E web | Audio de entrada y salida operativo | Log worker 31-oct | Fernando | MAIN PROBADO |
| RF-03 | Transcripción streaming | `stt.py`, Chirp 3 | `main`, PR #6 | `test_stt.py`, E01 y E2E | Operativo; espera final visible; exactitud no medida (TC-03 parcial en D05 v1.3) | PR #6; E01; log 31-oct; EV-22 | Juan | MAIN PROBADO — funcional; exactitud no medida |
| RF-04 | Generación de respuesta | `llm.py`, `llm_gemini.py` | `main`, PR #3/#5 | Unitarias y E2E Gemini | Gemini operativo (31-oct); DeepSeek verificado en log: 9 respuestas, `errors: {}` (17-nov). Observaciones: una sola sesión por proveedor; calidad semántica no evaluada formalmente; el uso de LLM sigue pendiente de validación con el cliente (D03 RF-03) | PR #3/#5; log 31-oct; EV-14/EV-15 | Fernando; optimización Juan | MAIN PROBADO — con observaciones; coherencia y conducta no verificadas (TC-04 parcial) |
| RF-05 | Síntesis de voz | `tts.py` | `main`, PR #4 | `test_tts.py`, script y E2E | Audio ElevenLabs operativo | PR #4; E01; log 31-oct | David; ajustes Juan | MAIN PROBADO |
| RF-06 | Web Demo controlada | `web-demo/app`, componentes y funciones | `main`, PR #11-#16 | Tests web y E2E | Acceso, llamada y transcripción funcionales | PR #11-#16; log Netlify 31-oct | Fernando/Juan | MAIN PROBADO |
| RF-07 | Personas de demostración | `personas.py`, selector e historial | `main`, PR #16 | Tests personas/historial | Siete personas; solo la clínica dental tiene E2E real (31-oct y 17-nov) | PR #16; E2E clínica dental; EV-21 | Juan | MAIN PARCIAL |
| RF-08 | Nombre aislado del worker | `resolve_agent_name`, configuración | `main`, PR #17 | `test_agent_name.py` | Worker dev aislado por nombre | PR #17; log 31-oct | Fernando | MAIN PROBADO |
| RF-09 | Telefonía Asterisk | No encontrada | No integrado | Sin prueba | Sin llamada telefónica | D01-D06 | Equipo/cliente | PENDIENTE |
| RF-10 | Guion oficial de cobranza | Personas ficticias no equivalentes | No integrado | Sin prueba oficial | No validado con cliente | D01/D03 | Equipo/cliente | PENDIENTE |
| RF-11 | Comparar costo y efectividad | Contadores de uso únicamente | No integrado | Sin protocolo | Sin conclusión económica | D03/D05 | Equipo/cliente | PENDIENTE |
| RF-12 | STT seleccionable y LLM adicionales | `stt_choice.py`, Anthropic e Inference | PR #18 abierto | 281 Python/103 web declaradas; audio sintético | No probado con voz real | PR #18 | Juan | RAMA PROBADA |
| RNF-01 | Latencia no mayor a un segundo | `metrics.py` | `main`, PR #9 | E01 y E2E | No cumple: medianas 2,5941 s y 2,7411 s; 17-nov: media 2,96 s, mediana 3,26 s, 2 de 8 turnos ≤ 1 s | E01; log worker 31-oct; EV-14/EV-15 | Fernando | MAIN PROBADO NO CUMPLE |
| RNF-02 | Secretos fuera de Git | `.gitignore`, configuración, sanitización | `main` | Tests y escaneo documental | Logs recuperados sin secretos detectados | PR #10-#16; hashes E2E | Fernando/Juan | MAIN PROBADO |
| RNF-03 | Seguridad de sesión | Cookie firmada, origen, CSP, despacho fijo | `main` | Tests login/session/origin/CSP | 401/403 y controles históricos | PR #11-#16 | Fernando/Juan | MAIN PROBADO |
| RNF-04 | Observabilidad privada | `metrics.py`, `record=False` | `main` | `test_metrics.py`, logs | Métricas numéricas sin conversación | PR #9; E01; E2E | Fernando | MAIN PROBADO |
| RNF-05 | Integración continua | `.github/workflows/ci.yml` | `main`, PR #19/#20 | GitHub Actions | Ejecuciones documentadas | PR #19/#20 | Fernando | MAIN PROBADO |
| RNF-06 | Persistencia de negocio | No encontrada | No integrado | Sin prueba | Solo `localStorage` e logs | Código de `main` | Equipo | PENDIENTE |
| RNF-07 | Worker persistente | Ejecución local | No integrado | Sin prueba persistente | Disponibilidad depende de un equipo | D06 | Equipo | PENDIENTE |
| AC-01 | Evidencias académicas consolidadas | D01-D06, E01, matriz y registro | `main` (PR #5, merge 260526e); evidencias E2E del 17-nov en el PR #6 | Revisión estructural y hashes | Recuperadas; revisión humana pendiente | Commit `7369bbc`, PR #5 y PR #6 | Equipo | MAIN PARCIAL |
| EV-01 | DART y cobranza para pymes | No hay implementación específica identificada | No integrado | Sin prueba | Sin autorización académica | Informe Fase 3 | Pendiente | PROPUESTO |

## Requisitos académicos pendientes

- La pauta oficial de Fase 3 no está disponible.
- No existe autorización académica para cambiar el nombre o el alcance a DART.
- Las decisiones de cliente sobre STT, LLM, guion y Asterisk requieren acta o fuente adjunta.

## Equivalencia de identificadores con D03 v1.1

Esta matriz usa identificadores propios de la recuperación documental. Los documentos D01 a D06 v1.1 conservan los identificadores de D03 (RF-01 a RF-12, RNF-01 a RNF-11, HU-01 a HU-08, TC-01 a TC-22). Para citar la matriz en la presentación, use esta equivalencia:

| Matriz | D03 v1.1 |
|---|---|
| RF-01 Conversación de voz | RF-01 |
| RF-02 Transporte LiveKit | RF-01 (pipeline) |
| RF-03 Transcripción | RF-02 |
| RF-04 Generación de respuesta del LLM | RF-03 (D03: generar la respuesta a partir del texto y del historial) |
| RF-05 Síntesis de voz | RF-04 (D03: voz de contexto chileno, TTS; «Parcial: voz sin validar») |
| RF-06 Web Demo | RF-09 |
| RF-07 Personas | RF-10 |
| RF-08 Nombre aislado del worker | RNF-09 (PR #17) |
| RF-09 Telefonía Asterisk | RF-07 |
| RF-10 Guion oficial de cobranza | RF-05 |
| RF-11 Comparar costo y efectividad | RF-12 |
| RF-12 STT seleccionable (PR #18) | Sin requisito; propuesta no integrada |
| RNF-01 a RNF-05 | RNF-01, RNF-04, RNF-05, RNF-08 y RNF-11 (ver D03 §10) |
| RNF-06 Persistencia de negocio | Sin requisito en D03 (D01 §10.5) |
| RNF-07 Worker persistente | RNF-09 |
