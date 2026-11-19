# Capturas de demostración E2E - clínica dental - 17 de noviembre de 2026

## Procedencia

Cuatro capturas derivadas de manera determinística del archivo fuente `evidencias_alloxentric_2026-11-17.zip`, SHA-256 `795F769DFD57F0FA8CC0AFC61B6BC054081530F803486235A05017B54993680D`. El ZIP original se conserva fuera del repositorio y no se incorpora. No se incorporó video.

Las imágenes muestran una demostración local del agente conversacional de clínica dental. La propia interfaz la rotula como **“SIMULACIÓN · DATOS FICTICIOS”** y **“LLAMADA DE PRÁCTICA”**.

## Catálogo

| Archivo | Dimensiones | Qué demuestra visualmente | Limitación específica |
|---|---:|---|---|
| [captura_35s_recortada.png](captura_35s_recortada.png) | 1160×913 | Interfaz de clínica dental activa, controles de micrófono y primer mensaje del agente | El nombre del archivo no acredita una medición exacta de 35 segundos |
| [captura_70s_recortada.png](captura_70s_recortada.png) | 1160×913 | Conversación visible con siete mensajes y continuidad entre usuario y agente | El contenido es una simulación; no acredita disponibilidad real de agenda |
| [captura_110s_recortada.png](captura_110s_recortada.png) | 1160×913 | Conversación visible con once mensajes y negociación de horario | No demuestra que una hora se haya persistido en un sistema externo |
| [captura_150s_recortada.png](captura_150s_recortada.png) | 1160×913 | Conversación visible con dieciséis mensajes y solicitud de nombre dentro del guion ficticio | El texto “reservada” es conversacional; no prueba una reserva real; el fotograma fuente ya presenta artefactos visuales en la columna izquierda |

## Relación con evidencia E2E existente

Las capturas son coherentes con `../E2E-2026-11-17-clinica-dental-deepseek/`, que contiene registro, logs sanitizados, métricas y capturas recortadas de la misma fecha. Los archivos aquí incorporados tienen dimensiones y hashes distintos: son evidencia complementaria, no duplicados exactos.

## Límites probatorios

Estas imágenes acreditan estados visibles de la interfaz y continuidad textual. No prueban por sí mismas:

- tiempos de respuesta o latencia;
- audio de entrada o salida;
- llamadas telefónicas reales o integración Asterisk;
- reservas persistidas;
- integración con una agenda, CRM o base de datos;
- identidad del proveedor LLM, STT o TTS no visible en pantalla.

## Privacidad y seguridad

No se observaron claves, tokens, correos, direcciones IP ni URL con credenciales. La conversación y sus nombres están rotulados como datos ficticios.

Como el repositorio académico es público, las copias completas no se incorporan: mostraban pestañas, marcadores, dirección local, avatar y barra de tareas. Se generaron derivados determinísticos con Pillow usando el mismo rectángulo sobre cada original: esquina superior izquierda `(380, 115)`, esquina inferior derecha `(1540, 1028)`, resultado `1160×913`. No se escaló, retocó, regeneró ni alteró el contenido de la conversación. Los originales permanecen únicamente dentro del ZIP fuente externo.

| Original dentro del ZIP | SHA-256 original | Derivado publicable |
|---|---|---|
| `captura_35s.png` | `BF898B6AE55769075347A0E1D35B06FD73A9283EB93402F11C044A6694BA239F` | `captura_35s_recortada.png` |
| `captura_70s.png` | `E7D2693208372D4627383D6EB3BC0CB67D6BBEFC1CB19DAA2A45D7821E3B6173` | `captura_70s_recortada.png` |
| `captura_110s.png` | `0FE5155AE64A51A79834B1C13CE29EC4E26C6708E4CBE8FB0A721FD6225E6EF7` | `captura_110s_recortada.png` |
| `captura_150s.png` | `75C62E0807A5AD693607E44BD5338C8DDA2E76415B351E0E10EE65680EC03167` | `captura_150s_recortada.png` |

## Integridad

Los SHA-256 publicables se registran en [SHA256SUMS.txt](SHA256SUMS.txt). Las cuatro imágenes derivadas son PNG RGB válidos de 1160×913.
