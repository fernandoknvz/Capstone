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
| `09_Presentacion` | Guion preliminar y material sujeto a revisión. |

La matriz transversal se encuentra en `MATRIZ_TRAZABILIDAD_PRELIMINAR.md`.

## Entregables de trabajo

La carpeta `Entregables` contiene las versiones completas y actualizadas de Fase 3. Cada una parte de una copia íntegra del documento original (los originales de `Fase 2/Evidencias Proyecto/Evidencias Documentacion/` no se modificaron) y agrega las actualizaciones verificadas contra `origin/main` (`77ff85c`):

| Entregable | Base | Qué se actualizó |
|---|---|---|
| `D01_Arquitectura_de_la_Solucion_v1.1_Fase3.docx` | D01 v1.0 | Estados de decisiones, CI, E2E 31-oct, vista de diseño (casos de uso, actividad, módulos y clases, almacenamiento), PR #18 como no integrado |
| `D02_Plan_de_Respuesta_a_Riesgos_v1.1_Fase3.docx` | D02 v1.0 | Revaloración al 17-nov y riesgos R-21 y R-22 (propuestos) |
| `D03_Levantamiento_de_Requerimientos_v1.1_Fase3.docx` | D03 v1.0 | Estados al 17-nov, fuentes, RNF-11, trazabilidad ampliada, casos de uso, documentación obligatoria vs de referencia |
| `D04_Estado_de_Avance_del_Proyecto_v1.1_Fase3.docx` | D04 v1.0 | Sección 9: estado al 17-nov |
| `D05_Plan_de_Pruebas_y_Resultados_v1.1_Fase3.docx` | D05 v1.0 | Certificación del 17-nov, E2E 31-oct, TC-19 a TC-22, evidencias y capturas |
| `D06_Guia_de_Despliegue_y_Operacion_v1.1_Fase3.docx` | D06 v1.0 | CI, nombre del agente, ensayo de la demo del 19-nov |
| `Informe_Academico_Consolidado_v1.0_Fase3.docx` | Estilo de D01 | Informe completo de Fase 3 con diagramas, resultados y demostración |

`Entregables/_Referencia_resumenes_Codex/` conserva, sin cambios, los siete resúmenes generados por Codex; son solo referencia y no deben usarse como entregables.

Todos son borradores para revisión humana y no están aprobados para publicación. Los diagramas fuente están en `03_Diseno/diagramas/` y las capturas de la Web Demo en `07_Evidencias/capturas-web-demo-2026-11-17/`. La certificación de pruebas del 17-nov está en `07_Evidencias/CERTIFICACION_PRUEBAS_2026-11-17.md`. Los scripts que generan y verifican los documentos están en `tools/` (ver `tools/README.md`).
