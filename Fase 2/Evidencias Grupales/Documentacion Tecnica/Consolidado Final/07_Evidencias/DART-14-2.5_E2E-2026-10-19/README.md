# Evidencia DART-14-2.5 — Validación E2E del 19 de octubre de 2026 (versión sanitizada)

Estado: evidencia recuperada, pendiente de revisión humana. Elaborada el 19-nov-2026.

## Procedencia

| Elemento | Valor |
|---|---|
| Documento original | `DART-14-2.5_Informe_Validacion_E2E_Alloxentric.docx` (informe del ticket DART-14-2.5, CoreStream, 19-oct-2026) |
| Ubicación del original | Fuera de Git (carpeta de descargas del responsable de la prueba); no se modifica |
| SHA-256 del original | `FB5A857F5BBEB5B8B8EC61BDC788EEBE6E39851A465EFA77FD79E0E7C89E7AC3` |
| Responsable declarado | Fernando Olguea González (operación del cliente y evidencia), según el propio informe |
| Generado con | `tools/archive_dart25.py` (reproducible a partir del original) |

## Transformaciones aplicadas

1. **Texto:** se extrajo el contenido del DOCX a Markdown (`DART-14-2.5_informe_sanitizado.md`) sin cambiar palabras ni cifras; solo cambia el formato (tablas y párrafos). Se agregó un encabezado que remite a este README. No se redactó ningún dato porque el texto no contiene credenciales, rutas locales, correos ni direcciones IP.
2. **Captura (Figura 1 del original):** se recortó el área de la consola (`captura_agent_console_recortada.png`, 1035×420 px) desde la captura original de 1361×710 px, con el rectángulo (310, 125)–(1345, 545). El recorte excluye la barra de pestañas y de direcciones (con identificadores del proyecto de LiveKit), los marcadores personales, el avatar del perfil y el panel lateral con el nombre de la cuenta. No se escaló ni se retocó el interior.
3. Los nombres de participantes que figuran en el texto original se conservan.

## Qué demuestra (y qué no)

Según el propio informe: un job recibido por el worker local, una pregunta de prueba transcrita y visible en Agent Console, una respuesta textual coherente, desconexión del cliente y grabación desactivada. La conclusión del informe es «VALIDACIÓN FUNCIONAL E2E EXITOSA, con observaciones de cierre y rendimiento».

- **STT (Chirp 3):** confirmado funcionalmente por la pregunta visible; no hay métrica de precisión ni texto de referencia comparable.
- **LLM (Gemini):** inferencia fuerte; el log no contiene la salida del modelo.
- **TTS (ElevenLabs):** audio confirmado solo por testimonio del operador; no hay métrica instrumental.
- **Latencia:** no se midió (OBS-04); no acredita el requisito de 1 s ni su incumplimiento.
- **Cierre:** el informe registra errores de liberación de recursos al apagar el worker (OBS-03) y marca ese criterio como no cumplido.
- **Pruebas automáticas:** el informe cita 86 pruebas de pytest aprobadas en ejecución local previa; es un dato reportado sin archivo y no reemplaza la certificación del 17-nov (214 Python y 91 web).
- Una sola sesión y una sola frase; no valida concurrencia, calidad conversacional, telefonía ni cobranza.

## Archivos

| Archivo | Descripción | SHA-256 |
|---|---|---|
| `DART-14-2.5_informe_sanitizado.md` | Transcripción textual del informe | ver `SHA256SUMS.txt` |
| `captura_agent_console_recortada.png` | Captura recortada de Agent Console | ver `SHA256SUMS.txt` |
| `SHA256SUMS.txt` | Manifiesto de los dos archivos anteriores | — |

Verificación: `sha256sum -c SHA256SUMS.txt` dentro de esta carpeta.

## Relación con otros documentos

D05 v1.3 lo incorpora como evidencia E10 y como respaldo parcial de TC-01 y TC-03. No sustituye las sesiones E2E del 31-oct y del 17-nov.
