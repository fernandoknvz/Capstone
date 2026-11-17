# Inventario de recuperación documental

## Artefactos históricos recuperados sin edición

Origen: rama `origin/docs/fase2-juan-documentacion-y-diario`, commit `31f096e46ca6c7f1557a2329be60380e3d2bd356`.

| ID | Artefacto | Fecha interna | Autoría verificable | Estado interno | Estado de recuperación |
|---|---|---|---|---|---|
| D01 | Arquitectura de la solución | 30-oct-2026 | Juan Díaz | v1.0, borrador | Recuperado en Fase 2, sin edición |
| D02 | Plan de gestión y respuesta a riesgos | 30-oct-2026 | Juan Díaz | v1.0, borrador | Recuperado en Fase 2, sin edición |
| D03 | Levantamiento de requerimientos | 30-oct-2026 | Juan Díaz | v1.0, borrador | Recuperado en Fase 2, sin edición |
| D04 | Estado de avance del proyecto | 30-oct-2026 | Juan Díaz | v1.0, borrador | Recuperado en Fase 2, sin edición |
| D05 | Plan de pruebas y resultados | 30-oct-2026 | Juan Díaz | v1.0, borrador | Recuperado en Fase 2, sin edición |
| D06 | Guía de despliegue y operación | 30-oct-2026 | Juan Díaz | v1.0, borrador | Recuperado en Fase 2, sin edición |
| E01 | Extracto de métricas de latencia | 30-oct-2026 | Juan Díaz, por commit | Evidencia numérica | Recuperado; SHA-256 `69AF78CA176BDFB944D95D3A02B61F63EEC8280DED2362644BA525FED4A71C7A` |

## Evidencia E2E recuperable del repositorio técnico

| Artefacto | Estado | Observación |
|---|---|---|
| Informe E2E Clínica dental, 31-oct | Local, no versionado en el repositorio técnico | No se copia literalmente porque contiene una ruta personal absoluta; se preparó una ficha académica sanitizada. |
| Log sanitizado del worker | Local, no versionado | Apto para recuperación; sin credenciales ni transcripciones detectadas. |
| Log sanitizado de Netlify CLI | Local, no versionado | Apto para recuperación; sin credenciales ni códigos de acceso detectados. |

## Controles aplicados

- Inspección de contenido completo de D01-D06 y E01.
- Comparación con `origin/main` del repositorio técnico, cuyo corte es el merge del PR #20.
- Revisión específica de PR #16, #17, #18, #19 y #20.
- Búsqueda de claves, JWT, encabezados `Authorization`, secretos, correos, rutas personales y URL privadas en la evidencia E2E.
- Cálculo de SHA-256 de los logs recuperados.

## Exclusiones

- No se fusionó la rama de Juan.
- No se recuperó el diario individual de Juan en esta actividad porque el alcance solicitado fue D01-D06 y E01.
- No se importaron respaldos originales no sanitizados.
- No se incorporaron capturas de CoreStream, actas ni materiales del cliente porque no estaban disponibles.
