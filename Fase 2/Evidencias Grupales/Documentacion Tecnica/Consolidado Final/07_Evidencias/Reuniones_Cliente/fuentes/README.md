# Catálogo de fuentes y evidencias multimedia pendientes

Este directorio está reservado para fuentes sanitizadas y autorizadas. Actualmente no contiene archivos probatorios. No se deben copiar videos grandes ni materiales con secretos o datos personales; para esos casos se registrará ubicación controlada, hash y condiciones de acceso.

| ID | Descripción | Fecha | Ubicación o URL | Acceso | Relación | Sanitización |
|---|---|---|---|---|---|---|
| FUE-01 | Invitación, notas o minuta de reunión inicial | 02-09-2026 | Pendiente | No disponible | ACTA-01; levantamiento inicial | Pendiente |
| FUE-02 | Documento de priorización/preguntas del MVP | 09-09-2026 | Pendiente | No disponible | REG-02; requisitos | Pendiente |
| FUE-03 | Especificación atribuida a Max Kreimerman | 16-09-2026 | Pendiente | No disponible | REG-03; arquitectura | Pendiente |
| FUE-04 | `BOT_HITES.zip` y `discador (1).py` | 16-09-2026 | Pendiente; no incorporar sin revisión | No disponible | REG-03; dependencias/seguridad | Revisión de secretos obligatoria |
| FUE-05 | Reporte agregado CoreStream | 19-11-2026 | `../../CoreStream/corestream-reporte-year-2026-11-19.pdf` | Disponible | Contexto de gestión posterior a REG-04 | Original incorporado; no contiene tickets ni `DART_14` |
| FUE-05A | Exportación detallada CoreStream de `DART_14` | 21-09-2026 | Pendiente | No disponible | REG-04; hitos | Pendiente |
| FUE-06 | Ticket/correos/logs del 403 de Gemini | 15–16-10-2026 | Pendiente | No disponible | REG-05; incidente | Redactar IP, claves y datos personales |
| FUE-07 | Registro Fireflies del 28-oct | 28-10-2026 | <https://app.fireflies.ai/view/Alloxentric-Real-Time-Agent-Duoc::01M5W6P4A3G4E7X6NQAVJAJWN8> | No verificado | REG-06 | Revisar permisos y datos personales |
| FUE-08 | Notificación de correo Fireflies | 28-10-2026 | Pendiente | Reportada, no incorporada | REG-06 | Sanitización pendiente |
| FUE-09 | Registro Fireflies del 4-nov | 04-11-2026 | <https://app.fireflies.ai/view/Alloxentric-Real-Time-Agent-Duoc::01M6E7F6HDH89CXAP38YNJE736> | No verificado | REG-07 | Revisar permisos y datos personales |
| FUE-10 | Notificación de correo Fireflies | 04-11-2026 | Pendiente | Reportada, no incorporada | REG-07 | Sanitización pendiente |
| FUE-11 | Capturas de reuniones/coordinaciones | Varias | Pendiente | No disponible | Registros aplicables | Redactar participantes y secretos |
| FUE-12 | Videos o grabaciones de demostración/reunión | Varias | Almacenamiento externo pendiente; no Git | No disponible | Requisitos y pruebas aplicables | Consentimiento, recorte y hash pendientes |
| FUE-13 | Logs y resultados de latencia adicionales | Varias | Pendiente; conservar logs grandes fuera de Git | No disponible | RNF de latencia | Sanitización y metodología pendientes |
| FUE-14 | Cuatro capturas derivadas de demo clínica dental | 17-11-2026 | `../../Demo_E2E_2026-11-17/` | Disponible | Evidencia funcional E2E, no de reunión | Recorte determinístico documentado; originales en ZIP externo |

## Protocolo de incorporación

1. Confirmar autorización, procedencia, fecha y propietario.
2. Trabajar sobre una copia; conservar el original fuera de Git cuando contenga datos sensibles.
3. Redactar secretos, IP, correos, nombres no necesarios y rutas personales.
4. Registrar SHA-256 del original y de la versión sanitizada cuando corresponda.
5. Documentar toda transformación y limitación.
6. Actualizar el índice maestro y la matriz sin convertir automáticamente la fuente en aprobación del cliente.
