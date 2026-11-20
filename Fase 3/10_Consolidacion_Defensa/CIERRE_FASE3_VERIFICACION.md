# Cierre documental de la Fase 3 — verificación y dictamen de preparación (20-nov-2026)

**Estado:** BORRADOR para revisión del equipo. Resume la verificación de identidad, el estado del extracto del worker, el estado de los entregables, la consistencia entre documentos, los requisitos de la guía sin evidencia, las contradicciones pendientes, los riesgos críticos y el dictamen de preparación.

## 1. Identidad académica

Verificada en las portadas oficiales de los siete entregables vigentes (D01 v1.2 a D06 v1.2 e Informe v1.2):

| Integrante | Rol en la portada |
|---|---|
| **Fernando Patricio Olguea González** | Líder de proyecto y desarrollador |
| **David Sepúlveda** | Scrum Master y desarrollador |
| **Juan Díaz** | Product Owner y desarrollador |

Docente guía: **Luis Bravo Yáñez**. Asignatura: Capstone (PTY4614 / 001V), Duoc UC, sede Plaza Oeste.

**Corrección aplicada:** el encargo de la Etapa 10D llamaba «Fernando Díaz» a uno de los integrantes. El nombre respaldado es **Fernando Olguea (Fernando Patricio Olguea González)**; **Juan** es quien se apellida Díaz. Revisé todos los documentos de las etapas 10C y 10D de ambos repositorios: la única mención del nombre equivocado estaba en el registro de contradicciones de `CONSOLIDACION_FASE3.md` (C-14) y ya figura como resuelta. No se alteró ningún documento histórico. En el cuerpo de los documentos se usan los nombres de pila; los nombres completos de la portada se usan en encabezados.

## 2. Extracto original del worker (`Texto pegado(10).txt`)

**Estado: NO RECIBIDO.** Busqué el archivo en Descargas, Escritorio, Documentos, Videos, Imágenes y los repositorios; no existe en el equipo ni está dentro del paquete `VOXENTRA_evidencias_E2E_20nov.zip`. **Se solicita al usuario su ubicación exacta.**

Consecuencia: las métricas del worker y las advertencias siguen como **[REPORTADO POR EL EQUIPO]**. No se reclasificó ningún dato.

### Procedimiento al recibirlo (preparado, no ejecutado)

1. **Conservar una copia original** sin modificar en una carpeta de evidencias fuera de Git y calcular su SHA-256.
2. Identificar las **sesiones por persona y hora** (campos `persona=…` y marcas de tiempo del extracto) y compararlas con las ventanas del video: ventas ≈ 09:58:32, cobranza retail ≈ 10:00:15, financiera ≈ 10:01:08, soporte ≈ 10:03:18, reclutamiento ≈ 10:05:33, postventa ≈ 10:09:07 (horas locales).
3. **Contrastar** las líneas de métricas por turno con `metricas_parciales.csv`: turnos registrados, E2E, EOT, TTFT del LLM y TTFB del TTS; anotar diferencias.
4. **Recalcular** promedios, medianas, mínimos y máximos desde el extracto.
5. **Documentar** advertencias y errores con su hora y su sesión (bloqueo del bucle de eventos, transcripciones tardías, `eot prediction timed out`, `Task was destroyed but it is pending!`, `InvalidDataError`, `skipping user input`), sin atribuir causa.
6. **Sanitizar** las copias publicables: identificadores de sala, de participante y de trabajo, direcciones IP, URL personales, nombres de máquina y cualquier secreto.
7. **Reclasificar de [REPORTADO] a [CONFIRMADO] solo lo verificable directamente en el extracto.** El extracto **no se presenta como el log completo del worker** (comienza a mitad de una traza). No se infieren versiones desplegadas a partir de los nombres de las personas ni de su comportamiento.

Nota de método: en la Etapa 10D se observó que los datos de contacto citados por los agentes coinciden con los prompts del PR #22. Eso es solo una [INFERENCIA] sobre el comportamiento y **no acredita la versión desplegada**; en estos documentos no se usa como prueba.

## 3. Estado de los entregables

| Documento | Versión vigente | Estado | Qué falta |
|---|---|---|---|
| D01 Arquitectura | v1.2 | En `main`; sin modificar | Cifras previas (214 + 91) y nombres de escenarios anteriores; el anexo las complementa |
| D02 Riesgos | v1.2 | En `main`; sin modificar | No incluye los riesgos de la reorientación |
| D03 Requerimientos | v1.2 | En `main`; sin modificar | RF-10 con escenarios anteriores |
| D04 Estado de avance | v1.2 | En `main`; sin modificar | Sin VOXENTRA ni sesiones del 20-nov |
| D05 Pruebas | v1.3 | En `main`; sin modificar | Sin la certificación del 20-nov (231 + 94) ni las sesiones E2E del 20-nov |
| D06 Despliegue | v1.2 | En `main`; sin modificar | Cifras previas |
| Informe consolidado | v1.2 | En `main`; sin modificar | Resumen y alcance anteriores a la reorientación |
| **Anexo académico final** | Nuevo | `ANEXO_ACADEMICO_FINAL_FASE3.md` (borrador) | Revisión de los tres integrantes y aprobación académica |
| Anexo de evolución | Nuevo | `ANEXO_EVOLUCION_VOXENTRA.md` (borrador) | Ídem |
| Propuesta de actualización | Nuevo | `PROPUESTA_ACTUALIZACION_ENTREGABLES.md` | Decidir la opción A, B o C |
| Diarios individuales (3.1) | Borradores | **Solo copia local**; no modificados | Validación y autorización de cada integrante |
| Evidencia E2E del 20-nov | Borrador | Repositorio técnico, **sin seguimiento** | Copia segura; log del worker |

**No se modificó ninguno de los siete DOCX**, ni las versiones de `Entregables/_historico/`.

## 4. Verificación de consistencia

Revisión mecánica de los documentos de `10_Consolidacion_Defensa/` (script de lectura, sin modificar nada):

| Comprobación | Resultado |
|---|---|
| Nombres de integrantes | Sin «Fernando Díaz» como dato (solo en el registro de la corrección) |
| Cifras de pruebas | **231 y 94** en el anexo final, la presentación, el guion y las preguntas. Las menciones de **214 y 91** aparecen únicamente como cifras históricas o como cifras desactualizadas de los entregables |
| Métricas dental | **2,850 s** (mediana) y **2,989 s** (promedio) coinciden en anexo, presentación, guion y preguntas |
| Afirmaciones prohibidas (siete aprobados, 1 s cumplido, aprobación del cliente, audio grabado) | Aparecen solo como **prohibiciones** o negaciones |
| Tiempos por diapositiva | La presentación y la estructura **coinciden en las 12 diapositivas** (responsable y tiempo) |
| Suma de tiempos | Fernando **5:30**, Juan **4:50**, David **4:10**: **14:30** más **5:30** de preguntas = **20:00** |
| Encabezados del guion | 5:30, 4:50 y 4:10, iguales a la presentación |
| Dictámenes | Dental «aprobado con observaciones»; los otros seis «evidencia parcial favorable» o «favorable con observaciones», **sin aprobación integral**, en el anexo, la consolidación y la presentación |

Consistencia con las fuentes técnicas (`MATRIZ_SIETE_AGENTES.md`, `METRICAS_CONSOLIDADAS.md`): las cifras de las secciones 6 y 7 del anexo final provienen de ellas y de la ejecución propia de pruebas.

## 5. Requisitos de la guía 3.3 sin evidencia

| Requisito | Estado |
|---|---|
| Ajustes de la **última retroalimentación del informe final** | **Sin evidencia** |
| Guía del **Informe Final** como estructura | **Sin evidencia** (se usó el Informe v1.2 como aproximación) |
| Rúbrica de Fase 3 | **Sin evidencia** |
| Diapositivas | **No existen** todavía |
| Ensayo cronometrado de 20 minutos | **No realizado** |
| Aprobación académica de la reorientación | **Sin evidencia** |

## 6. Contradicciones pendientes

| # | Contradicción | Estado |
|---|---|---|
| C-1 | La 10B marca como CONFIRMADO que los proveedores estaban operativos; los registros del 20-nov los clasifican REPORTADO | Pendiente; no se modificó la 10B |
| C-2 y C-3 | Los DOCX vigentes citan 214 + 91 y nombres de escenarios anteriores | Complementado por el anexo; los DOCX no se tocaron |
| C-4 | `GUION_PRELIMINAR.md` manda usar solo el nombre Alloxentric | Reemplazado como borrador por `GUION_DEFENSA.md` |
| C-5 | El Informe dice que no hay ajuste académico aprobado; la defensa muestra una demostración para pymes | Pendiente de aprobación académica |
| C-6 | PR #8 fusionado sin revisiones | Pendiente; reconocerlo si preguntan |
| C-7 | Sesiones del 17-nov (locales) y del 20-nov (versión publicada): condiciones distintas | Documentado; no comparar como mejora |
| C-10 | El informe preliminar cita un log que no se recibió | **Abierta** (ver §2) |
| C-11 | La insignia dice «sin prueba real documentada» pese a la evidencia preliminar | Pendiente de decisión del equipo |
| C-12 | CSV (10 turnos) y la interfaz (23 mensajes) no cuadran en reclutamiento | Pendiente del log |
| C-13 | El informe preliminar incluye el turno interrumpido en sus estadísticas | Documentado con y sin ese turno |
| C-14 | Nombre «Fernando Díaz» en el encargo de la 10D | **Resuelta** (§1) |

## 7. Riesgos críticos restantes

| # | Riesgo | Gravedad | Mitigación |
|---|---|---|---|
| 1 | Reorientación sin aprobación del docente | Alta | Consultar hoy; decirlo en la defensa |
| 2 | Retroalimentación del informe final y rúbrica ausentes | Alta | Obtenerlas; sin ellas no se puede verificar el cumplimiento de la guía |
| 3 | Demostración de selección libre con agentes de una sola sesión previa; interrupciones y latencia de 2,5 a 8,9 s | Alta | Ensayo con los siete agentes, plan de capturas, protocolo |
| 4 | Extracto del worker no incorporado: las métricas siguen REPORTADAS | Media | Entregar el archivo; ejecutar el procedimiento de §2 |
| 5 | Diapositivas y ensayo cronometrado inexistentes | Alta | Construir con `PRESENTACION_FINAL_12_DIAPOSITIVAS.md` y ensayar dos veces |
| 6 | La evidencia E2E del 20-nov solo está sin seguimiento en el repositorio técnico y el video fuera de Git | Media | Copia segura (sin el video en espacios públicos) |
| 7 | Defensa individual: David sin actividades de Fase 3 documentadas; todos deben dominar todo | Media | David documenta con respaldo; ronda de preguntas cruzadas |
| 8 | I-01 e I-03 (dental) sin repetir tras el PR #22 | Media | Prueba breve autorizada o declararlo como limitación |
| 9 | PR #8 fusionado sin revisión cruzada | Baja a media | Reconocerlo; pedir revisión posterior |
| 10 | Calidad de voz sin validar | Media | Que una persona escuche el video |

## 8. Dictamen de preparación

| Ámbito | Dictamen |
|---|---|
| **Documentación de cierre** (anexo final, matriz, métricas, guion, 12 diapositivas, demostración, checklist) | **LISTA CON OBSERVACIONES** para construir las diapositivas |
| **Defensa del 21-nov** | **CONDICIONADA**: no se considera lista hasta cerrar al menos los riesgos 1, 2 y 5 de la tabla anterior |

Condiciones mínimas antes de defender:
1. Consulta al docente guía sobre la reorientación y la demostración libre.
2. Retroalimentación del informe final obtenida y revisada.
3. Diapositivas construidas con el contenido de este expediente, y dos ensayos cronometrados.
4. Una prueba corta con voz de los siete agentes (con autorización) o la decisión explícita de depender de las capturas de respaldo.
5. Cada integrante domina todo el contenido; David documenta sus aportes de Fase 3.

El extracto del worker (§2) mejora la solidez de las métricas, pero **no es condición mínima** para defender, siempre que las métricas se sigan presentando como reportadas.

**No se realizó ninguna publicación.** El siguiente paso previsto es construir las diapositivas con el contenido de `PRESENTACION_FINAL_12_DIAPOSITIVAS.md`.
