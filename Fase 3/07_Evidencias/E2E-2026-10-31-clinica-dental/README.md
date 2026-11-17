# Evidencia E2E - Clínica dental - 31 de octubre de 2026

Estado: evidencia recuperada, pendiente de revisión humana.

## Entorno

- Rama/commit probado: `main` / `d80c419` (PR #16 y #17).
- Worker de desarrollo aislado por nombre.
- LiveKit Agents 1.8.4, Python 3.12.6.
- STT Chirp 3, LLM Gemini `gemini-3.1-flash-lite`, TTS ElevenLabs `eleven_v4_turbo`.
- Web Demo local servida mediante Netlify CLI.
- Conversación con voz humana; `record=False`.

## Resultados

| Métrica | Resultado |
|---|---:|
| Duración aproximada de sesión | 87,2 s |
| Turnos del agente | 7 |
| Turnos con E2E | 5 |
| Media E2E | 2,330 s |
| Mediana E2E | 2,741 s |
| Mínimo E2E | 1,191 s |
| Máximo E2E | 3,352 s |
| P95 estimado | 3,237 s |
| Errores de sesión | 0 |

Uso registrado: Gemini 2.493 tokens de entrada y 139 de salida; ElevenLabs 640 caracteres y 42,8 s de audio; Chirp 3 72,0 s de audio.

## Limitaciones

- Una sesión, un hablante y frases no controladas.
- Cinco muestras E2E; el P95 no es robusto.
- Sin grabación ni verificación externa con reloj independiente.
- Dos turnos sin E2E disponible.
- Solo se validó la persona clínica dental.
- No incluye Asterisk.
- No cumple el objetivo declarado de un segundo.

## Integridad y privacidad

| Archivo | SHA-256 |
|---|---|
| `worker-AJ_vzjEF7rJwWqB.sanitizado.log` | `844E3492283B2EB9F40F5D97ACCFAE7B28694B64880726588D3B58A49B797B41` |
| `netlify-cli.sanitizado.log` | `A5FE4E40B3553D3B664AE153CAF8B8930C3B38DBFA511675E7B6FCCF754FD6C3` |

Se buscaron credenciales, JWT, secretos, códigos de acceso, correos, rutas locales y URL privadas. No se detectaron valores sensibles en los logs. Los identificadores técnicos de job/worker se conservan por trazabilidad y no son credenciales.

El informe fuente no se copió literalmente porque contenía una ruta personal absoluta al respaldo original; esta ficha conserva los resultados y limitaciones sin esa ruta.
