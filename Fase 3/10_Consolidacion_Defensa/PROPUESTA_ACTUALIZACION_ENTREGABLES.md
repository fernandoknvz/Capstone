# Propuesta de actualización de los entregables académicos

**Estado:** PROPUESTA. **No se modificó ningún DOCX.** Este inventario identifica, por documento y sección, qué quedó desactualizado tras el 19-nov y qué cambio se necesitaría. Las versiones vigentes (D01 v1.2, D02 v1.2, D03 v1.2, D04 v1.2, D05 v1.3, D06 v1.2 e Informe v1.2) y sus antecesoras en `Entregables/_historico/` **no se sobrescriben**: cualquier cambio se haría en una versión nueva (por ejemplo v1.3 o v1.4, según el documento), con control de versiones y revisión de los tres integrantes.

Corte: 20-nov-2026. Cifras actuales [CONFIRMADO]: 231 pruebas de Python y 94 del frontend. Evidencia nueva: sesión dental del 20-nov (carpeta `docs/validation/E2E-2026-11-20-voxentra-clinica-dental/`) y evidencia preliminar de los seis agentes (`docs/validation/E2E-2026-11-20-voxentra-siete-agentes/`), ambas en el repositorio técnico, sin seguimiento.

## 1. Opciones de actualización

| Opción | Descripción | Ventajas | Riesgos |
|---|---|---|---|
| **A. Anexo único** (recomendada para el 21-nov) | Entregar `ANEXO_EVOLUCION_VOXENTRA.md` (convertido a DOCX o PDF) junto a los entregables v1.2/v1.3, con una nota de portada que explique que las cifras posteriores al 19-nov están en el anexo | Rápida; no toca los documentos revisados; trazabilidad clara | La comisión verá cifras distintas entre anexo y entregables si no se advierte |
| **B. Versiones nuevas mínimas** | Nueva versión de D05, Informe y D04 con las cifras y la evidencia del 20-nov; el resto queda igual con la advertencia del anexo | Entregables coherentes en lo que más importa | Regenerar DOCX con los scripts toma tiempo y exige revisión visual; ya hay un PR fusionado sin revisión cruzada |
| **C. Actualización completa D01 a D06 e Informe** | Todas las versiones nuevas | Máxima coherencia | Poco realista hasta el 21-nov; alto riesgo de errores |

Recomendación: **A para la defensa**, y **B** solo si el docente lo pide o si sobra tiempo tras confirmar la reorientación.

## 2. Inventario de cambios necesarios por documento

Prioridad: **P1** corrige una cifra o afirmación ahora inexacta; **P2** actualiza evidencia; **P3** mejora de coherencia.

### D01 Arquitectura de la Solución (v1.2)

| Sección | Texto actual (resumen) | Cambio necesario | Prioridad |
|---|---|---|---|
| 1.2 Alcance, tabla de escenarios | «7 personas, una con E2E archivado (clínica dental)» | Indicar que las seis restantes tienen evidencia preliminar del 20-nov, sin aprobación integral | P2 |
| 8. Atributos de calidad (Mantenibilidad) | «214 de Python y 91 de la web, ejecutadas el 17-nov» | Actualizar a 231 y 94 (20-nov), citando el corte | P1 |
| 9. Limitaciones | «Escenarios de cobranza actuales (Falabella, Ripley)» | Reemplazar por los nombres ficticios actuales (Casa Aurora, Financiera Costanera) y mantener la nota histórica | P1 |
| 6. Presupuesto de latencia | Cifras del 31-oct | Agregar la sesión del 20-nov (mediana 2,850 s, objetivo no cumplido) y las medianas parciales de las cuatro sesiones adicionales | P2 |
| Control del documento | Última versión 1.1/1.2 | Registrar la nueva versión | P3 |

### D02 Plan de Respuesta a Riesgos (v1.2)

| Sección | Cambio necesario | Prioridad |
|---|---|---|
| 3. Registro de riesgos y 9. Actualización | Agregar riesgos nuevos: reorientación sin aprobación académica; marca VOXENTRA sin verificar; datos inventados por el LLM (I-01); interrupciones del agente (reclutamiento); demostración de selección libre; dependencia de proveedores en vivo | P2 |
| R-04 (falta de guion oficial y flujo de Hites) | Mantener; el nombre «Hites» es histórico y legítimo; aclarar que el escenario demostrativo se llama ahora «Tienda Brújula» | P3 |
| 9.2 Lecciones | Actualizar los cortes de cifras de pruebas (231 y 94) | P1 |

### D03 Levantamiento de Requerimientos (v1.2)

| Sección | Cambio necesario | Prioridad |
|---|---|---|
| 4 (RF-10) y 10 (trazabilidad RF-10) | RF-10 («7 agentes ... ventas, cobranza, salud...»): actualizar nombres demostrativos y estado: «una sesión documentada y seis con evidencia preliminar» | P1 |
| 5 (RNF-01, RNF-02) y 10 (RNF-01) | Agregar las sesiones del 20-nov (RNF-02: turnos sobre 3 s) | P2 |
| 5 (RNF-08) y 10 | 214 + 91 → 231 + 94 | P1 |
| 8. Gestión de cambios | Agregar el cambio de alcance de la reorientación VOXENTRA (aprobación académica pendiente) y la fila EV-01 | P1 |
| 7.2 Fuera de alcance | Mantener; agregar que no hay integración empresarial real | P3 |

### D04 Estado de Avance del Proyecto (v1.2)

| Sección | Cambio necesario | Prioridad |
|---|---|---|
| 9.1 Indicadores | Pruebas: 231 + 94 (20-nov); agregar evidencia E2E del 20-nov; escenarios con nombres actuales | P1 |
| 9.3 Estado por componente | «E2E solo con la persona clínica dental»: indicar la evidencia preliminar de los seis agentes | P1 |
| 9.4 Avance por objetivo específico y 9.5 Plan | Actualizar el estado del objetivo 5 y la fila «Capturar la conversación» | P2 |
| 9.2 Línea de tiempo | Agregar los hitos del 19 y 20-nov (PR #21 y #22; sesiones E2E; PR #8) | P2 |
| 6. Cambios respecto del plan | Agregar la reorientación como cambio con aprobación pendiente | P1 |

### D05 Plan de Pruebas y Resultados (v1.3) — el más afectado

| Sección | Cambio necesario | Prioridad |
|---|---|---|
| 2.1 a 2.4, tablas de certificación | Agregar certificación del 20-nov: 231 Python y 94 web (el PR #21 y #22 modificaron las suites); mantener la del 17-nov | P1 |
| 2.2 y 2.3 (inventarios) | Actualizar los conteos por archivo | P1 |
| 4.4 Latencia en sesiones reales | Agregar las cinco sesiones del 20-nov: dental (n = 8) y cuatro parciales; sin promedio combinado | P2 |
| Nueva sección 4.8 | Resultado de la sesión dental del 20-nov y de los seis agentes (resumen de `README.md` y `METRICAS_CONSOLIDADAS.md`) | P2 |
| 5. Catálogo de casos de prueba: TC-01, TC-02, TC-06, TC-14, TC-23 | Agregar TC nuevos por agente o ampliar TC-06 (escenarios); TC-02 (saludo): los seis saludos estáticos observados | P2 |
| 7. Defectos y hallazgos | Agregar I-01, I-02, I-03 e I-05 (dental) y S-03 a S-08 (seis agentes) | P1 |
| 8. Limitaciones | Agregar: log no archivado; voces sin validar; versión desplegada no acreditada | P1 |
| 9. Evidencia archivada | Agregar E10 en adelante: capturas derivadas, CSV parcial, hashes; el video queda fuera de Git | P2 |
| 10. Evidencias visuales | Agregar figuras de las sesiones del 20-nov (derivadas y sanitizadas) | P3 |

### D06 Guía de Despliegue y Operación (v1.2)

| Sección | Cambio necesario | Prioridad |
|---|---|---|
| 1. Qué corre dónde | Indicar que las sesiones del 20-nov se hicieron sobre la versión publicada (sitio de Netlify); la versión exacta no está acreditada | P1 |
| 4.3 Pruebas | 214 → 231; 91 → 94 | P1 |
| 12. Ensayo y ejecución | «Solo la clínica dental tiene E2E archivado»: actualizar; agregar el protocolo de selección libre | P2 |
| 13. Verificación previa | Certificación local: 231 + 94 | P1 |
| 14. Qué no declarar | Mantener; agregar «los siete agentes aprobados» | P2 |

### Informe Académico Consolidado (v1.2)

| Sección | Cambio necesario | Prioridad |
|---|---|---|
| 1. Resumen ejecutivo | 214 + 91 → 231 + 94; incluir la sesión del 20-nov y la reorientación (no aprobada) | P1 |
| 3. Objetivos | Mantener «sin ajuste académico aprobado»; referenciar el anexo | P1 |
| 4. Alcance | Fila «Siete escenarios»: actualizar el estado; las dos personas de cobranza ya no usan marcas | P1 |
| 9. Pruebas y resultados | Certificación del 20-nov; tabla de latencia con las cinco sesiones del 20-nov | P1 |
| 10.1 | Agregar subsección «Sesión del 20-nov y seis agentes» | P2 |
| 14. Limitaciones | Actualizar «solo la clínica dental tiene E2E archivado» | P1 |
| 15. Conclusiones y 16. Próximos pasos | Ajustar | P2 |
| Anexo A | Agregar las evidencias del 20-nov (derivadas, hashes) | P2 |
| Portada y control | Nueva versión | P3 |

## 3. Elementos que no se tocan

- Registros de reuniones, actas, evidencias históricas del cliente y referencias legítimas a Alloxentric.
- Versiones en `_historico/`.
- Diarios individuales.

## 4. Restricciones de integridad para cualquier actualización

1. Mantener las etiquetas [CONFIRMADO], [REPORTADO POR EL EQUIPO], [INFERENCIA] y [PENDIENTE].
2. No sumar ni promediar las sesiones del 20-nov sin una metodología justificada.
3. No presentar los seis agentes como aprobados.
4. No afirmar que el PR #22 corrigió I-01 ni I-03.
5. Conservar las referencias al cliente original y declarar la reorientación como decisión del equipo con aprobación pendiente.
6. Revisión cruzada de los tres integrantes antes de fusionar (el PR #8 se fusionó sin ella).

## 5. Esfuerzo estimado (juicio, no medido)

| Opción | Esfuerzo | Riesgo |
|---|---|---|
| A (anexo) | 1 a 2 horas de formato y revisión | Bajo |
| B (D05, Informe y D04) | 1 jornada con revisión visual | Medio |
| C (todo) | 2 jornadas | Alto antes del 21-nov |
