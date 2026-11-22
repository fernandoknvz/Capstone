# Fase 3 - recuperación documental controlada

Estado: **BORRADOR DE TRABAJO - NO PUBLICADO**  
Fecha de corte: 17 de noviembre de 2026  
Proyecto oficial: **Alloxentric Real Time Agent**

Esta estructura consolida documentación y evidencia existentes sin reemplazar ni modificar los artefactos históricos de las fases 1 y 2.

## Límites

- La pauta oficial de Fase 3 no está disponible en el repositorio: **PENDIENTE**.
- DART y el caso de cobranza para pymes son una **PROPUESTA no aprobada académicamente**.
- No se incorporan cambios de código funcional.
- No se presentan como integradas las funcionalidades del PR #18.
- Ningún documento de esta carpeta está aprobado para publicación.

## Estructura

| Carpeta | Propósito |
|---|---|
| `00_Control_Recuperacion` | Inventario, evaluación documental y plan de actualización. |
| `01_Arquitectura` | Estado arquitectónico y diagramas vigentes. |
| `02_Requerimientos` | Requerimientos confirmados, propuestos y pendientes. |
| `03_Diseno` | Diseño del flujo conversacional, seguridad y despliegue. |
| `04_Implementacion` | Componentes implementados e integración real en `main`. |
| `05_Pruebas` | Estrategia, casos y estado de ejecución. |
| `06_Metricas` | Resultados medidos y reglas de interpretación. |
| `07_Evidencias` | Evidencias recuperadas, con procedencia e integridad. |
| `08_Contribuciones` | Autoría verificable y participación declarada. |
| `09_Presentacion` | Retirada en 11H: la presentación vigente es `Evidencias Grupales/Presentación Final de proyecto.pptx`. |

**Nota de reubicación (11G/11H):** las carpetas `01_Arquitectura` a `08_Contribuciones`, los entregables vigentes y la matriz transversal `MATRIZ_TRAZABILIDAD_PRELIMINAR.md` se encuentran ahora en `Fase 2/Evidencias Grupales/Documentacion Tecnica/Consolidado Final/`. En las secciones siguientes, las rutas `0X_...` y `Entregables/` (vigentes) se leen relativas a esa carpeta; `Entregables/_historico/` y `Entregables/_Referencia_resumenes_Codex/` permanecen en `Fase 3/Entregables/`.

## Entregables de trabajo

`Entregables/` contiene **solo las versiones vigentes** (actualizadas el 19-nov-2026). Cada una parte de la versión anterior, conservada sin cambios en `Entregables/_historico/`; los originales de Fase 2 (`Fase 2/Evidencias Grupales/Documentacion Tecnica/`) tampoco se modificaron. El contenido técnico se contrastó con `origin/main` del repositorio técnico (`77ff85c`).

| Entregable vigente | Versión | Qué cambió en la versión actual |
|---|---|---|
| `D01_Arquitectura_de_la_Solucion_v1.2_Fase3.docx` | v1.2 (19-nov) | Solo portada, identificación del equipo y referencias cruzadas; sin cambios de contenido técnico |
| `D02_Plan_de_Respuesta_a_Riesgos_v1.2_Fase3.docx` | v1.2 (19-nov) | Solo portada, identificación del equipo y referencias cruzadas; sin cambios de contenido |
| `D03_Levantamiento_de_Requerimientos_v1.2_Fase3.docx` | v1.2 (19-nov) | F-01 como evidencia indirecta y contradicción sobre el LLM; RF-01 a RF-03, RF-10, RNF-01/02 y trazabilidad de pruebas; F-10 alineado con las guías 3.1 y 3.3; fuentes F-11 y F-12 |
| `D04_Estado_de_Avance_del_Proyecto_v1.2_Fase3.docx` | v1.2 (19-nov) | Estado histórico (30-oct) distinguido del final (19-nov); PR #16, E2E del 17-nov, CoreStream, Scrum parcial e hitos |
| `D05_Plan_de_Pruebas_y_Resultados_v1.3_Fase3.docx` | v1.3 (19-nov) | TC-02, TC-03, TC-04, TC-07 a TC-10 y TC-17 rebajados al respaldo archivado; comparativas 4.1 a 4.3 como reportadas; método de percentiles; DART-14-2.5 (E10, TC-24) |
| `D06_Guia_de_Despliegue_y_Operacion_v1.2_Fase3.docx` | v1.2 (19-nov) | Estado real de despliegue (sin producción permanente) y limitaciones de la demostración |
| `Informe_Academico_Consolidado_v1.2_Fase3.docx` | v1.2 (19-nov) | Alcance original frente a MVP, pendientes, demo dental como validación del pipeline, reunión del 2-sep y decisiones del cliente como evidencia indirecta, Scrum parcial, EV-20/EV-21 y guías 3.1/3.3 |

Versiones anteriores (archivadas, no vigentes) en `Entregables/_historico/`: D01 v1.1, D02 v1.1, D03 v1.1, D04 v1.1, D05 v1.1 y v1.2, D06 v1.1, Informe v1.0 y v1.1. `Entregables/_Referencia_resumenes_Codex/` conserva sin cambios los resúmenes generados por Codex; son solo referencia y no deben usarse como entregables.

Todos son borradores para revisión humana y no están aprobados para publicación. Convención de portada: Fernando Patricio Olguea González, David Sepúlveda y Juan Díaz. Las guías oficiales 3.1 y 3.3 se conservan solo en la copia local del responsable (`Pautas_Oficiales/`, no publicadas en este repositorio público hasta confirmar que la institución permite redistribuirlas); los pendientes que debe aportar el usuario están en `00_Control_Recuperacion/DOCUMENTOS_PENDIENTES_USUARIO.md`. Faltan las planillas de evaluación de Fase 3 (individual y grupal): hasta obtenerlas no se declara completa la cobertura de evaluación. La evidencia del ensayo E2E del 17-nov con DeepSeek (aprobado con observaciones: latencia objetivo no cumplida y agendamiento simulado) está en `07_Evidencias/E2E-2026-11-17-clinica-dental-deepseek/`; la del 19-oct (DART-14-2.5, sanitizada) en `07_Evidencias/DART-14-2.5_E2E-2026-10-19/`. Los diagramas fuente están en `03_Diseno/diagramas/` y las capturas de la Web Demo en `07_Evidencias/capturas-web-demo-2026-11-17/`. La certificación de pruebas del 17-nov está en `07_Evidencias/CERTIFICACION_PRUEBAS_2026-11-17.md`. Los scripts que generan y verifican los documentos están en `tools/` (ver `tools/README.md`).

## Diarios de reflexión individual (pauta 3.1)

Los tres diarios de Fase 3 están preparados como **borradores pendientes de validación individual** (cada integrante debe reescribirlos, resolver las marcas `[PENDIENTE DE CONFIRMACIÓN PERSONAL]` y quitar el aviso). Contienen reflexiones personales y **no se publican en este repositorio** mientras no exista autorización explícita y por escrito de cada integrante; permanecen en la copia local (`Evidencias Individuales/`). Mecanismo propuesto para compartirlos: carpeta privada del equipo (acceso solo para los tres integrantes) o envío directo entre ellos; cada persona decide si lo sube a la plataforma de Duoc UC. La trazabilidad interna de sus fuentes tampoco se publica.
