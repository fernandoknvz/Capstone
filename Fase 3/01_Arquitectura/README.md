# Arquitectura - versión de trabajo

Fuente principal: D01 histórico, contrastado con `origin/main` del repositorio técnico.

## Estado integrado

`Navegador → LiveKit Cloud → worker Python → Chirp 3 → Gemini/DeepSeek → ElevenLabs → LiveKit → navegador`.

La Web Demo y sus funciones serverless no alojan al worker. El worker persistente, Asterisk y la persistencia de negocio permanecen pendientes.

## Actualizaciones pendientes

- Incorporar PR #17 y CI de PR #19/#20.
- Cambiar PR #16 de “en revisión” a “integrado”.
- Incorporar E2E 31-oct como evidencia recuperada.
- Mantener Anthropic, LiveKit Inference y STT seleccionable fuera del diagrama de `main`.
