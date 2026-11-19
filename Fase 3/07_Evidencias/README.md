# Evidencias

Cada evidencia debe conservar procedencia, fecha, commit o rama, estado de integración, hash cuando corresponda y limitaciones.

## Recuperadas

- D01-D06 y E01 en la ubicación histórica de Fase 2.
- Logs sanitizados E2E del 31-oct en `E2E-2026-10-31-clinica-dental/` (SHA-256 verificados el 17-nov).
- Certificación de pruebas sobre `main` del 17-nov: `CERTIFICACION_PRUEBAS_2026-11-17.md`.
- Capturas de la Web Demo (acceso, acceso rechazado, selección de agente, historial) en `capturas-web-demo-2026-11-17/`. En las capturas 03 y 04 se tapó con un recuadro rotulado «omitido» el nombre de una persona que el producto muestra como deudor ficticio en la tarjeta «Cobranza Falabella»; el resto de la imagen no se modificó.
- E2E del 17-nov con DeepSeek en `E2E-2026-11-17-clinica-dental-deepseek/`: registro, logs sanitizados, cinco capturas recortadas de la conversación y manifiesto SHA-256 (APROBADO CON OBSERVACIONES: latencia objetivo no cumplida, agendamiento simulado). El video original y los logs originales no se incorporan a Git; su hash consta en el registro.
- Reporte agregado de rendimiento de CoreStream del 19-nov en `CoreStream/`: PDF original, ficha de alcance y manifiesto SHA-256. Es evidencia de gestión agregada; no contiene tickets ni acredita avance real o cumplimiento de hitos.
- Cuatro capturas derivadas por recorte determinístico de la demostración de clínica dental del 17-nov en `Demo_E2E_2026-11-17/`: estados visibles de la conversación a 35, 70, 110 y 150 segundos según los nombres de origen, con manifiesto SHA-256. Los originales se conservan en el ZIP fuente fuera del repositorio público. Complementan el expediente E2E existente, sin probar latencia, telefonía ni reservas reales.

## Faltantes

- Pauta oficial Fase 3.
- Exportación detallada de tickets de CoreStream y trazabilidad de `DART_14`; el reporte agregado recuperado no incluye ese detalle.
- Actas de reuniones y decisiones del cliente.
- Aprobación del cambio de STT y uso de LLM.
- Prueba Asterisk.
- Capturas del cierre de la llamada y del historial de la sesión del 17-nov (el tramo final del video muestra un nombre completo pronunciado durante la demostración y requeriría enmascararlo).
- Más sesiones E2E (una sola sesión DeepSeek; las otras seis personas sin E2E real).
- Validación de seis personas restantes.
- Protocolo y resultados de costo/efectividad.
