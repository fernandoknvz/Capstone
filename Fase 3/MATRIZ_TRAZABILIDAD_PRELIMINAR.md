# Matriz de trazabilidad preliminar

Estados: **MAIN** integrado en `origin/main`; **PR ABIERTO** solo PR #18; **PENDIENTE** sin implementación verificable.

| Funcionalidad | Requerimiento / fuente | Implementación | Prueba | Resultado verificable | Evidencia | Responsable verificable | Estado |
|---|---|---|---|---|---|---|---|
| Entorno LiveKit | MVP voz-a-voz, Fase 1 | `agent.py`, `config.py` | `test_project_bootstrap.py`, `test_config.py` | Composición y configuración cubiertas sin red | PR #2 | Fernando | MAIN |
| LLM DeepSeek | Decisión técnica posterior; aprobación cliente pendiente | `llm.py`, `config.py` | `test_llm.py`, script manual | Unitarias históricas aprobadas; prueba real reportada | PR #3 | Fernando | MAIN |
| TTS ElevenLabs | Objetivo Fase 1 | `tts.py`, `config.py` | `test_tts.py`, `check_elevenlabs_tts.py` | Unitarias históricas; TTS operativo en E2E | PR #4, E01, E2E 31-oct | David; ajustes posteriores Juan | MAIN |
| LLM Gemini | Alternativa temporal reportada | `llm_gemini.py`, `config.py` | `test_llm_gemini.py` | Operativo en E01 y E2E 31-oct | PR #5 | Fernando; optimizaciones Juan | MAIN |
| STT Chirp 3 | Reemplazo de Speechmatics reportado por cliente | `stt.py`, `config.py` | `test_stt.py`, `check_google_stt.py` | Operativo; espera final STT visible en métricas | PR #6, E01, E2E 31-oct | Juan | MAIN |
| Pipeline voz-a-voz | MVP confirmado | `pipeline.py`, `agent.py` | `test_pipeline.py`, E2E | Conversación real completada | PR #7, E2E 31-oct | Fernando | MAIN |
| Métricas | Verificar latencia ≤1 s | `metrics.py` | `test_metrics.py` | E01: 13 E2E medibles; no cumple 1 s | PR #9, E01 | Fernando | MAIN |
| ADC en arranque | Evitar bloqueo del worker | `agent.py`, `pipeline.py`, `stt.py` | pruebas de pipeline/STT | Corrección integrada | PR #10 | Fernando | MAIN |
| Web Demo y token | Demostración controlada | `web-demo/app`, `components`, `lib/server`, funciones Netlify | tests web de sesión/token/config | Flujo web probado; incidentes corregidos | PR #11-#14 | Fernando | MAIN |
| Seguridad web | Proteger secretos, origen y sesión | `session.ts`, `http.ts`, CSP | tests login/session/origin/CSP | 401/403 y CSP verificados históricamente | PR #11-#16 | Fernando/Juan | MAIN |
| Personas y UI | Escenarios de práctica del equipo | `personas.py`, frontend personas/historial | tests personas, historial y conversación | 7 personas integradas; solo clínica con log E2E recuperado | PR #16 | Juan | MAIN |
| Despliegue Vercel | Ruta alternativa propuesta | `vercel.json`, scripts y funciones Vercel | tests postbuild/origin | Código integrado; despliegue histórico reportado | PR #16 | Juan | MAIN |
| Nombre aislado de worker | Evitar despachos cruzados en desarrollo | `agent.py`, `config.py` | `test_agent_name.py` | 214 pruebas Python declaradas en PR | PR #17 | Fernando | MAIN |
| CI | Automatizar control de calidad | `.github/workflows/ci.yml` | GitHub Actions | Ejecuciones documentadas; sin aprobación independiente del PR #19 | PR #19/#20 | Fernando | MAIN |
| LLM Anthropic/Inference | Propuesta DART-14-5.2 | `llm_anthropic.py`, `llm_inference.py` | tests específicos | 281 Python/103 web declaradas en rama | PR #18 | Juan | PR ABIERTO |
| STT seleccionable | Propuesta DART-14-5.2 | `stt_choice.py`, selector web | tests STT/selector | Medición sintética; sin voz real | PR #18 | Juan | PR ABIERTO |
| Telefonía Asterisk | Objetivo Fase 1 | No encontrada | No existe | Sin llamada telefónica | D01-D06 | Dependencia cliente/equipo | PENDIENTE |
| Persistencia de negocio | Rúbrica/evolución de producto | No encontrada | No existe | Solo `localStorage` y logs | Código | PENDIENTE |
| Costo y efectividad | Objetivo Fase 1 | Contadores de uso, sin protocolo | No existe comparación | Sin conclusión | D03/D05 | Equipo/cliente | PENDIENTE |
| Cobranza para pymes/DART | Propuesta Fase 3 | No hay implementación específica identificada | No existe | No medido | Ninguna | PENDIENTE | PENDIENTE |
