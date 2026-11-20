# Consolidación de la Fase 3 (corte: 20-nov-2026, actualizada con la evidencia de los siete agentes)

**Estado:** borrador de trabajo para revisión del equipo (Fernando, David y Juan). No es un entregable oficial ni sustituye a los entregables vigentes. Presentación: 21-nov-2026.

Clasificación usada: **[CONFIRMADO]** verificado en archivos o ejecución propia; **[REPORTADO POR EL EQUIPO]** informado por el equipo sin respaldo archivado; **[INFERENCIA]** deducido; **[PENDIENTE]** falta información.

## 1. Requisitos de la presentación (guía oficial 3.3) [CONFIRMADO]

| Requisito | Fuente | Cómo se atiende |
|---|---|---|
| Describir los aspectos más relevantes del proyecto y **fundamentar las decisiones** tomadas | Guía 3.3 | `ESTRUCTURA_PRESENTACION.md`, diapositivas 2 a 12 |
| Máximo **20 minutos, incluidas las preguntas** de la comisión | Guía 3.3 | 14:30 de exposición y 5:30 reservados para preguntas (`GUION_DEFENSA.md`) |
| Apoyo audiovisual si el proyecto lo requiere | Guía 3.3 | Diapositivas más demostración en vivo |
| Usar como orientación los campos de la guía del **Informe Final** | Guía 3.3 | **[PENDIENTE]**: esa guía no está en el expediente; se usó la estructura del Informe v1.2 como aproximación [INFERENCIA] |
| Presentar los resultados del proyecto e **incorporar ajustes de la última retroalimentación del docente** sobre el informe final | Guía 3.3 | **[PENDIENTE]**: la retroalimentación no consta en el expediente (ver §6) |
| Evidencias necesarias que el proyecto haya definido | Guía 3.3 | Anexo A del Informe, evidencias E2E, `CHECKLIST_PRESENTACION.md` |
| Comisión: docente(s) de la asignatura y Dirección de Carrera | Guía 3.3 | Preparar respuestas para perfil académico y de carrera |
| **Nota individual** por integrante; pondera **30 %** de la nota final | Guía 3.3 | Cada integrante debe dominar todo el contenido y poder responder cualquier pregunta |
| Rúbrica o planilla de evaluación de Fase 3 | — | **[PENDIENTE]**: no está en el expediente; no se infiere desde Fase 1 o 2 |

## 2. Estado de los documentos

| Documento | Versión vigente | Estado | Observación |
|---|---|---|---|
| D01 Arquitectura | v1.2 | En `main` (PR #8) | Cita 214 + 91 pruebas y escenarios con marcas anteriores |
| D02 Riesgos | v1.2 | En `main` | No incluye el riesgo de reorientación ni de marca |
| D03 Requerimientos | v1.2 | En `main` | Describe los escenarios anteriores |
| D04 Estado de avance | v1.2 | En `main` | No incluye VOXENTRA ni la sesión del 20-nov |
| D05 Pruebas y resultados | v1.3 | En `main` | Cifras previas (214 + 91); sin la sesión del 20-nov |
| D06 Despliegue y operación | v1.2 | En `main` | Sin cambios de VOXENTRA |
| Informe académico consolidado | v1.2 | En `main` | Objetivo general sigue siendo el bot de cobranza; no menciona VOXENTRA |
| Diarios individuales 3.1 | Borradores | **Solo copia local**, no publicados | Cada integrante debe validar y reescribir el suyo; falta autorización para publicarlos |
| Guías 3.1 y 3.3 | Copias | Solo copia local | Falta confirmar si se pueden redistribuir |
| Evidencia E2E del 20-nov | Borrador | **Solo en el repositorio técnico, sin seguimiento** (carpeta `docs/validation/E2E-2026-11-20-voxentra-clinica-dental/`) | No está en este repositorio ni en una rama integrada |
| Evidencia E2E de los seis agentes restantes (20-nov) | Borrador preliminar | **Solo en el repositorio técnico, sin seguimiento** (`docs/validation/E2E-2026-11-20-voxentra-siete-agentes/`); el paquete original y el video quedan fuera de Git | Falta el log del worker; el video no es publicable (muestra el escritorio) |
| Anexo de evolución VOXENTRA | Borrador actualizado | Nuevo (esta carpeta) | Requiere revisión del equipo y aprobación académica |
| Propuesta de actualización de entregables | Propuesta | Nuevo (`PROPUESTA_ACTUALIZACION_ENTREGABLES.md`) | Inventario de cambios por DOCX; no se modificó ningún DOCX |

Los entregables v1.2 y v1.3 **no están actualizados** con los resultados posteriores al 19-nov (231 + 94 pruebas, sesión del 20-nov, VOXENTRA). El anexo de evolución cubre esa brecha sin sobrescribirlos. Las versiones anteriores siguen en `Fase 3/Entregables/_historico/`.

## 3. Estado técnico (repositorio `alloxentric-real-time-agent`)

Revisado el 20-nov-2026. `main` en `b955e41` (merge del PR #22).

| Elemento | Hallazgo | Estado |
|---|---|---|
| Pruebas Python | **231 aprobadas**, 1 advertencia del SDK (ejecución propia del 20-nov sobre el árbol equivalente a `main`) | [CONFIRMADO] |
| Pruebas del frontend | **94 aprobadas** en 14 archivos; `tsc` sin errores | [CONFIRMADO] |
| ESLint, build y CSP del PR #22 | Informados en la descripción del PR; no se repitieron aquí | [REPORTADO] |
| Agentes configurados | **Siete**, con empresa ficticia, guion, saludo y voz; identificadores en el mismo orden en Python y TypeScript | [CONFIRMADO] |
| Arquitectura | LiveKit Agents; STT Google Chirp 3; LLM Gemini (por defecto) o DeepSeek, según `LLM_PROVIDER`; TTS ElevenLabs; frontend Next.js estático con funciones en Netlify | [CONFIRMADO] en código |
| PR #21 (rebranding VOXENTRA) y PR #22 (siete agentes) | Fusionados el 20-nov (08:46 y 09:41, hora de Chile) | [CONFIRMADO] |
| PR #18 (LLM por Inference/Anthropic y STT elegible) | **Abierto**; no integrado | [CONFIRMADO] |
| Matriz de validación E2E de los otros seis agentes | Preparación en `ETAPA-10B-...md`. **Desde el 20-nov hay evidencia preliminar** (video y capturas) de una conversación por agente; **ninguno está aprobado integralmente** (ver §4.1) | [CONFIRMADO] |
| Voces | No validadas de oído para ninguno de los siete | [PENDIENTE] |
| Estado visible en la interfaz | Clínica dental: «Prueba conversacional real documentada»; otros seis: «Guion configurado, sin prueba real documentada». **La insignia no refleja aún la evidencia preliminar**; cambiarla exige código y una decisión del equipo | [CONFIRMADO] |

## 4. Resultados verificables

| Resultado | Valor | Estado |
|---|---|---|
| Pruebas Python | 231 aprobadas | [CONFIRMADO] |
| Pruebas del frontend | 94 aprobadas | [CONFIRMADO] |
| Agentes configurados | 7 | [CONFIRMADO] |
| Sesiones E2E con VOXENTRA el 20-nov | **7 conversaciones**: 1 dental **documentada** (2 min 15 s, 8 turnos) y 6 con **evidencia preliminar** (una por agente, de 33 s a 3 min 14 s) | [CONFIRMADO] en capturas y video; métricas y proveedores [REPORTADO] |
| Latencia E2E dental (n = 8, antes del PR #22) | Mediana **2,850 s**; promedio **2,989 s**; mínimo 2,6067 s; máximo 4,1406 s | [REPORTADO POR EL EQUIPO] |
| Latencia E2E de cuatro de los seis agentes | Medianas de 3,1135 s a 3,9832 s; mínimos y máximos entre 0,6608 s (turno interrumpido) y 8,9018 s; **sin promedio combinado**; ventas y cobranza retail sin métricas | [REPORTADO] (extracto parcial del log) |
| Objetivo de latencia de 1 s | **No cumplido ni demostrado**: 0 de 8 turnos en la sesión dental y ningún turno válido en las otras cuatro | [REPORTADO] |
| Incidencias del worker | Bloqueo del bucle de eventos de 136 ms; un error de decodificación de audio (la conversación continuó); `errors {}` en el resumen | [REPORTADO] |
| Operaciones empresariales | **Simuladas** (agenda, mensajería, pagos, folios, visitas) | [CONFIRMADO] |

**Las métricas del worker fueron transcritas por el usuario; no hay archivo original archivado ni hash.** Ningún documento debe presentarlas como verificadas contra el registro.

### 4.1 Los seis agentes restantes (evidencia preliminar del 20-nov)

Fuente: paquete `VOXENTRA_evidencias_E2E_20nov.zip` (hashes 8 de 8 verificados), video original (773,2 s; no publicable) y CSV parcial. Detalle en `docs/validation/E2E-2026-11-20-voxentra-siete-agentes/` del repositorio técnico. **El log del worker que cita el paquete no fue recibido.**

| Agente | Mensajes | Duración | E2E mediana (n) | Dictamen |
|---|---|---|---|---|
| MóvilAndes — Ventas | 11 | 1:37 | sin métricas | Evidencia parcial favorable; no aprobado integralmente |
| Casa Aurora — Cobranza retail | 5 | 0:33 | sin métricas | Evidencia parcial favorable (solo la ruta del tercero); no aprobado integralmente |
| Financiera Costanera — Cobranza financiera | 14 | 1:54 | 3,3598 s (5) | Evidencia parcial favorable; no aprobado integralmente |
| FibraSur — Soporte | 16 | 1:55 | 3,4567 s (6) | Evidencia favorable con observaciones; no aprobado integralmente |
| Talento Cordillera — Reclutamiento | 23 | 3:14 | 3,1135 s (8, con un turno interrumpido) | Evidencia favorable con observaciones; no aprobado integralmente |
| Tienda Brújula — Postventa | 13 | 2:03 | 3,9832 s (6) | Evidencia favorable con observaciones; no aprobado integralmente |

Duración: la que muestra el historial local de la interfaz (retail, financiera, soporte y reclutamiento) o el cronómetro de la llamada (ventas y postventa).

- **Lo observado [CONFIRMADO]:** en las seis conversaciones el agente saludó con el texto configurado, respondió coherentemente con su guion, **aclaró que las operaciones eran simuladas** y no se observaron datos inventados ni datos reales solicitados. En cobranza retail no reveló la deuda a un tercero.
- **Incidencias:** una interrupción del agente al usuario en reclutamiento (confirmada en video), un E2E de 8,9018 s, y avisos de bloqueo del bucle de eventos, transcripciones tardías, tiempo de espera del detector de fin de turno y errores de tareas pendientes [REPORTADO; sin log].
- **No evaluable:** calidad de las voces (no escuchadas), rutas no cubiertas de la matriz de la Etapa 10B (objeción y cobertura, titular de cobranza retail, datos bancarios, cupo, datos sensibles), versión desplegada y log completo.
- **Sobre el PR #22:** las seis sesiones ocurrieron **después** del PR #22 y su comportamiento es **consistente** con esos prompts (números ficticios configurados, folio ficticio, cierres que aclaran la simulación) [INFERENCIA]. **No valida** la corrección de los incidentes dentales I-01 e I-03: la clínica no se repitió tras el PR #22.

### Hallazgos de la sesión del 20-nov (conservados)

- **I-01:** el agente dijo una dirección y un teléfono que no estaban en su configuración.
- **I-02:** el saludo observado difiere del configurado.
- **I-03:** afirmó una reserva y ofreció mensajería antes de aclarar que era simulado.
- **I-05:** falta el contenido del mensaje inicial del usuario en las capturas.

**Orden de los hechos [CONFIRMADO por marcas de tiempo]:** la sesión (09:13–09:15) ocurrió **antes** de que se fusionara el PR #22 (09:41), que endureció los prompts (no inventar datos, aclarar lo simulado, no afirmar operaciones realizadas). Por tanto la evidencia del 20-nov **describe el comportamiento previo a esos cambios**; el efecto de los prompts actuales sobre I-01 e I-03 **no está probado** [INFERENCIA].

## 5. Contradicciones y desajustes detectados

| # | Contradicción | Documentos | Tratamiento sugerido |
|---|---|---|---|
| C-1 | El documento de la Etapa 10B marca como CONFIRMADO que Chirp 3, DeepSeek Flash y ElevenLabs estaban «operativos» el 20-nov; el registro de evidencia del 20-nov los clasifica como REPORTADO por falta del registro del worker | `ETAPA-10B-siete-agentes-...md` (repo técnico) frente a `E2E-2026-11-20-.../README.md` | Corregir la 10B en una revisión posterior; no se modificó |
| C-2 | Entregables v1.2/v1.3 citan 214 + 91 pruebas; hoy son 231 + 94 | D01 a D06, Informe | Actualizar mediante el anexo o versión posterior |
| C-3 | Los entregables describen escenarios con marcas y nombres anteriores; hoy son empresas ficticias | D01 a D04 | Declarar el cambio en el anexo; mantener la referencia histórica |
| C-4 | `GUION_PRELIMINAR.md` ordena usar Alloxentric como nombre oficial y tratar la cobranza para pymes como propuesta no aprobada; la reorientación a VOXENTRA lo contradice | `09_Presentacion/GUION_PRELIMINAR.md` | `GUION_DEFENSA.md` lo reemplaza como borrador; el preliminar no se sobrescribió |
| C-5 | El Informe indica que **no existe ajuste académico aprobado** que reemplace el objetivo (bot de cobranza); la presentación mostraría una demostración orientada a pymes | Informe §3 | Presentarlo como evolución del equipo con aprobación académica **pendiente** |
| C-6 | El PR #8 se fusionó el 20-nov a las 11:49 UTC **sin revisiones registradas**, aunque su descripción pedía la revisión de los tres integrantes y el flujo de trabajo del proyecto exige revisión por otro integrante | PR #8; `docs/GIT_WORKFLOW.md` del repo técnico | Reconocerlo y pedir revisión posterior; no ocultarlo si preguntan |
| C-7 | El Informe describe la sesión del 17-nov con un worker y una web locales; la del 20-nov se informa sobre la versión publicada | Informe §10.1; E2E 20-nov | No comparar latencias como si fueran las mismas condiciones |
| C-8 | `07_Evidencias/README.md` aún lista como faltante la «pauta oficial Fase 3»; ya constan las guías 3.1 y 3.3 (siguen sin rúbrica) | `07_Evidencias/README.md` | Aclarar en una actualización futura |
| C-10 | El informe preliminar del paquete cita un extracto de log (`Texto pegado(10).txt`) que **no está en el paquete ni se encontró en el equipo**; sus métricas y advertencias no se pudieron contrastar | `INFORME_PRELIMINAR.md` del paquete | Pedir el archivo; hasta entonces todo es REPORTADO |
| C-11 | La Etapa 10B dejó los seis agentes «PENDIENTES de validación»; ahora hay evidencia preliminar, pero la interfaz sigue diciendo «sin prueba real documentada» | 10B; interfaz | Decidir el criterio y el momento del cambio; no se modificó código |
| C-12 | En reclutamiento el CSV tiene 10 turnos y la interfaz registró 23 mensajes: no cuadran sin el log | CSV; video | Reconciliar con el log completo |
| C-13 | El informe preliminar incluye el turno interrumpido de reclutamiento (E2E 0,6608 s) en sus estadísticas | `INFORME_PRELIMINAR.md` | `METRICAS_CONSOLIDADAS.md` muestra las cifras con y sin ese turno |
| C-14 | **Resuelta (Etapa 10E).** El encargo de la Etapa 10D nombraba a un integrante «Fernando D.»; las portadas respaldan Fernando Patricio Olguea González, David Sepúlveda y Juan Díaz (Juan es quien se apellida Díaz) | Instrucciones; portadas de los entregables | Se usan los nombres de las portadas; ver `CIERRE_FASE3_VERIFICACION.md` §1 |
| C-9 | El Informe sostiene «medianas de ≈ 2,6 a 3,3 s»; la sesión del 20-nov reporta 2,85 s: coherente, pero n = 8 y condiciones distintas | Informe §1 | Sin contradicción de fondo; citar con n y fecha |

## 6. Evidencia faltante

| Falta | Impacto |
|---|---|
| Rúbrica o planilla de evaluación de Fase 3 | No se puede verificar cobertura de evaluación |
| **Retroalimentación del docente sobre el informe final** (Fase 2) | La guía 3.3 exige incorporarla; sin ella el requisito queda sin cumplir ni verificar |
| Guía del Informe Final | La estructura de la presentación es una aproximación |
| Log completo y escucha de las sesiones de los seis agentes; rutas no cubiertas de la matriz 10B | Hay evidencia preliminar, pero **no aprobación integral**; no presentarlos como aprobados |
| Registro del worker del 20-nov (dental y seis agentes), sanitizado y con hash; el extracto que cita el paquete no se recibió | Métricas y advertencias siguen como REPORTADO |
| Prueba de la versión desplegada (commit del frontend y del worker) | No acreditada |
| Aprobación del docente a la reorientación; consentimiento o conocimiento del cliente | Ver §7 |
| Transcripción del 2-sep, especificación v0.1, actas, tickets de CoreStream | Antecedentes con el cliente siguen indirectos |
| Voces validadas de oído (el video tiene audio y puede escucharse) | Calidad de voz no verificada |
| Copia de la evidencia E2E del 20-nov en este repositorio (hoy solo en el técnico, sin seguimiento) | Riesgo de que no quede archivada |
| Presentación (diapositivas) y ensayo cronometrado | No existen todavía |
| Diarios individuales validados y autorización para publicarlos | Siguen como borradores locales |
| Contribuciones de David en Fase 3 | No hay actividad suya atribuida en la documentación |

## 7. Aprobaciones pendientes (no inferidas)

| Aprobación | Estado | Quién debe darla |
|---|---|---|
| Reorientación del proyecto hacia una demostración para pymes bajo el nombre VOXENTRA | **PENDIENTE**: no hay evidencia | Docente guía de la asignatura |
| Conocimiento o conformidad del cliente original (Alloxentric) sobre la reorientación y el reuso de código e identidad | **PENDIENTE**: no hay evidencia de que se haya informado | El equipo debe aclararlo |
| Uso del nombre VOXENTRA (disponibilidad de marca y dominio) | **PENDIENTE**: no verificado | El equipo |
| Cambio de STT y uso de LLM | Sin aprobación formal verificable (ya registrado en el Informe) | — |
| Publicación de diarios y guías oficiales | **PENDIENTE** | Cada integrante; la institución |

VOXENTRA **no es una empresa constituida** ni un producto comercial aprobado: es un nombre provisional de una demostración académica.

## 8. Riesgos académicos

| Riesgo | Probabilidad (juicio) | Mitigación |
|---|---|---|
| Presentar como proyecto vigente algo cuya reorientación no tiene aprobación | Media | Decirlo expresamente y consultar al docente antes del 21-nov |
| Que la comisión elija un agente cuyo guion se probó solo en una sesión y falle o interrumpa | Media a alta | Protocolo de demostración, ensayo previo con los siete agentes, plan de contingencia con capturas reales |
| Latencia de 2,5 a 5 s (y un valor de 8,9 s) percibida como falla frente a la meta de 1 s | Alta | Declarar que el objetivo no se cumplió y mostrar los datos |
| Interrupción del agente al usuario (observada en reclutamiento) o respuestas tardías durante la demo | Media | Avisar al público; no insistir; pasar a capturas |
| Afirmar como verificado lo que solo es REPORTADO | Media | Citar siempre la clasificación; no decir «verificado» para métricas del worker |
| Desconocimiento de integrantes sobre partes que no presentaron | Media | Cada uno estudia todas las secciones; ronda de preguntas cruzadas |
| Datos inventados por el LLM (I-01) en vivo | Media | Preparar la explicación; los prompts nuevos no están probados |
| Fallo de red, cuota o clave de proveedores | Media | Checklist y respaldo |
| Contribuciones de David sin documentar | Media | Que David las documente antes de la defensa, con respaldo |
| PR #8 fusionado sin revisión | Baja a media | Reconocerlo; solicitar revisión de los otros dos integrantes |
| Referencias cruzadas a archivos que no están en el repositorio público | Baja | Informar que las guías y diarios están fuera por privacidad |

## 9. Próximos pasos propuestos

1. Consultar al docente guía sobre la reorientación y la selección libre de agentes (antes de la presentación).
2. Archivar el registro del worker del 20-nov, sanitizado y con hash.
3. Conseguir la retroalimentación del informe final y revisar qué ajustes exige la guía 3.3.
4. Ensayo cronometrado del equipo y prueba previa de la demostración (requiere autorización para llamadas con proveedores).
5. Decidir qué hacer con I-01 e I-03 (probar los prompts actuales o declararlos como limitación).
6. Revisión cruzada de los diarios y del anexo por Fernando, David y Juan.
