# Anexo — Evolución del proyecto: de Alloxentric Real Time Agent a la demostración VOXENTRA

**Estado:** BORRADOR para revisión del equipo. **No está aprobado por el docente ni por el cliente.** Corte: 20-nov-2026. No sustituye ni modifica los entregables vigentes ni las evidencias históricas; los complementa.

Clasificación: **[CONFIRMADO]** verificado en archivos o ejecución propia; **[REPORTADO POR EL EQUIPO]** informado sin respaldo archivado; **[INFERENCIA]** deducido; **[PENDIENTE]** falta información.

> **Aviso.** VOXENTRA es un **nombre provisional** de una demostración académica. **No es una empresa constituida**, ni un producto comercial aprobado, ni una marca verificada. El nombre oficial del proyecto en los entregables sigue siendo **Alloxentric Real Time Agent**.

## 1. Problema original

[REPORTADO POR EL EQUIPO] Según el informe de definición de Fase 1, en la reunión inicial del 2-sep-2026 el representante de Alloxentric explicó que su infraestructura de bots de voz, pensada para gran escala, tiene poca elasticidad de costos cuando baja el volumen de llamadas, y solicitó un prototipo de bot de cobranza por voz para explorar una alternativa.

La transcripción de esa reunión y la especificación técnica atribuida al cliente (v0.1, 02-09-2026) **no están archivadas** en el expediente [PENDIENTE]. El registro histórico ACTA-01 es una reconstrucción sin convocatoria ni lista de asistentes.

## 2. Objetivos del proyecto

[CONFIRMADO] Objetivo general heredado de Fase 1 (Informe v1.2, §3): desarrollar y evaluar un prototipo de bot de cobranza por voz basado en LiveKit. **No existe un ajuste académico aprobado que lo reemplace.**

Elementos del objetivo original, según el Informe: LiveKit, un servicio de transcripción, ElevenLabs, telefonía Asterisk, comparación de costo y efectividad con la solución actual y una respuesta de no más de 1 segundo. [CONFIRMADO como contenido del Informe]

## 3. Trabajo realizado para Alloxentric

[CONFIRMADO] en el repositorio técnico y en los entregables:

- Pipeline voz → STT → LLM → TTS → voz sobre LiveKit Agents, con proveedores intercambiables (Google Chirp 3; Gemini o DeepSeek; ElevenLabs).
- Demo web con acceso por código, token de LiveKit emitido por el servidor y siete escenarios conversacionales.
- Pruebas automatizadas, integración continua, instrumentación de métricas y registro de incidentes.
- Entregables D01 a D06, Informe consolidado, matriz de trazabilidad y expediente de evidencias.
- Sesiones E2E de la clínica dental: 19-oct (una frase), 31-oct (Gemini) y 17-nov (DeepSeek).

**Lo que no se implementó** respecto del objetivo original [CONFIRMADO en el Informe §14]: telefonía Asterisk, guion oficial de cobranza, comparación de costos, persistencia de negocio y protocolo de medición acordado con el cliente.

## 4. Dificultades de coordinación documentadas

Esta sección se limita a lo que el expediente permite sostener. **No se afirman reuniones incumplidas ni conductas del cliente.**

| Hecho | Fuente | Estado |
|---|---|---|
| La transcripción del 2-sep y la especificación v0.1 no están archivadas | Informe §2 y §14 | [CONFIRMADO] que no están en el expediente |
| Ninguna decisión atribuida al cliente cuenta con acta, transcripción archivada o aprobación formal verificable | Informe, decisiones atribuidas | [CONFIRMADO] |
| Contradicción entre fuentes sobre usar o no un LLM al inicio y sobre el proveedor de STT; no resuelta | Informe §2 | [CONFIRMADO] como contradicción |
| REG-02 (9-sep): «no se acredita reunión»; REG-04 (21-sep): «cumplimiento no acreditado»; REG-06 y REG-07 (28-oct y 4-nov): existencia en Fireflies sin contenido recuperado | `Reuniones_Cliente/INDICE_MAESTRO.md` | [CONFIRMADO] como estado de la evidencia; no prueba incumplimiento de nadie |
| No hay protocolo de medición de latencia ni guion oficial de cobranza acordados con el cliente | Informe §14 | [CONFIRMADO] |
| CoreStream (herramienta de gestión del cliente): el equipo informa deficiencias; el reporte agregado del 19-nov no contiene tickets | Informe §5 | [REPORTADO POR EL EQUIPO] |
| Bloqueo HTTP 403 de Gemini y coordinación de red (15–16 oct) | REG-05 | Antecedente retrospectivo sin ticket ni correos [PENDIENTE] |

**Lo que el expediente no documenta:** cuántas reuniones se convocaron, cuáles no se realizaron o por qué, ni si hubo una negativa o falta de respuesta del cliente. Si el equipo quiere sostener una dificultad de coordinación como causa de la decisión del §5, necesita aportar correos, convocatorias, tickets o exportaciones; mientras tanto debe presentarla como **«según el equipo»** y sin generalizar.

## 5. Decisión del equipo de continuar el MVP

[REPORTADO POR EL EQUIPO] El equipo propone continuar el desarrollo de manera autónoma y presentar el MVP como una demostración de agentes conversacionales para pequeñas y medianas empresas.

| Dato | Estado |
|---|---|
| Fecha de la decisión, participantes y motivación detallada | [PENDIENTE]; no hay acta |
| Aprobación del docente guía | [PENDIENTE]; no hay evidencia |
| Conocimiento o conformidad del cliente original | [PENDIENTE]; no hay evidencia; **no se afirma que el cliente aprobó la reorientación** |
| Permiso para reutilizar código e identidad visual de Alloxentric | [PENDIENTE] |

## 6. Reorientación demostrativa hacia VOXENTRA

[CONFIRMADO] en el repositorio técnico (PR #21 fusionado el 20-nov):

- Nombre visible provisional VOXENTRA y eslogan «Agentes de voz inteligentes para tu negocio».
- Identidad VOXENTRA Red Edition: fondo oscuro, tarjetas grafito y acentos rojos; verde reservado para estados funcionales de éxito; tipografía existente.
- Aviso permanente: «Demostración con datos ficticios. No realiza operaciones reales ni está integrada con sistemas empresariales».
- Indicadores de alcance en cada agente.
- **Sin cambios** en proveedores, pipeline, nombre interno del worker, paquete Python, cookies ni claves de historial.

El alcance **no** es una plataforma SaaS: es una demostración académica sobre el MVP existente. Las referencias a Alloxentric se mantienen en el expediente histórico y en los nombres técnicos del código.

## 7. Arquitectura conservada

[CONFIRMADO] en el código:

| Capa | Componente |
|---|---|
| Voz en tiempo real | LiveKit Agents (worker en Python) |
| STT | Google Chirp 3 (`chirp_3`, `es-US`) |
| LLM | Gemini (por defecto) o DeepSeek (`deepseek-flash`), según la variable `LLM_PROVIDER` |
| TTS | ElevenLabs (`eleven_v4_turbo`), una voz por agente |
| Turnos | Detección de fin de turno dinámica y generación anticipada |
| Frontend | Next.js estático; acceso por código; sesión por cookie; token de LiveKit con despacho forzado desde el servidor y solo el identificador del agente en el cliente |
| Seguridad | CSP sin `unsafe-inline` ni `unsafe-eval`; sin grabación de audio |
| Calidad | Pruebas automatizadas y CI en GitHub Actions |

Los proveedores y modelos efectivamente usados en la sesión del 20-nov son [REPORTADO POR EL EQUIPO]; el registro del worker no está archivado.

## 8. Nuevos escenarios ficticios

[CONFIRMADO] (PR #21 y PR #22). Siete agentes con empresas y personas ficticias, sin marcas comerciales reales y sin nombres de integrantes:

| Agente (visible) | Empresa ficticia | Estado de prueba real |
|---|---|---|
| Clínica dental | Clínica Dental Sonrisa Norte | **Una sesión E2E documentada** (20-nov); también 19-oct, 31-oct y 17-nov |
| Ventas de telefonía | MóvilAndes | Una conversación el 20-nov: **evidencia parcial favorable**; no aprobado integralmente; sin métricas |
| Cobranza retail | Casa Aurora | Una conversación de 33 s (solo la ruta del tercero): **evidencia parcial favorable**; no aprobado integralmente; sin métricas |
| Cobranza financiera | Financiera Costanera | Una conversación: **evidencia parcial favorable**; no aprobado integralmente; métricas parciales |
| Soporte de internet | FibraSur | Una conversación: **evidencia favorable con observaciones**; no aprobado integralmente; métricas parciales |
| Entrevista laboral | Talento Cordillera | Una conversación: **evidencia favorable con observaciones** (interrupción del agente y latencia de 8,9 s); no aprobado integralmente; métricas parciales |
| Atención postventa | Tienda Brújula | Una conversación: **evidencia favorable con observaciones**; no aprobado integralmente; métricas parciales |

Las seis conversaciones del 20-nov (evidencia **preliminar**, paquete del equipo y video) mostraron saludos con el texto configurado, respuestas coherentes con el guion y aclaración de que las operaciones eran simuladas. Ninguna se declara aprobada integralmente: cada sesión cubre solo parte de los criterios de la matriz de la Etapa 10B y falta el log del worker, la escucha de las voces y la acreditación de la versión desplegada. La insignia de la interfaz todavía dice «sin prueba real documentada».

Todas las operaciones (agendamiento, mensajería, pagos, folios, visitas técnicas) son **simuladas**. Los identificadores técnicos heredados con marcas históricas siguen en el código porque son la clave de despacho; no se muestran al usuario.

## 9. Resultados verificables

| Resultado | Valor | Estado |
|---|---|---|
| Pruebas automatizadas de Python | 231 aprobadas | [CONFIRMADO] (ejecución del 20-nov) |
| Pruebas del frontend | 94 aprobadas | [CONFIRMADO] |
| Agentes configurados | 7 | [CONFIRMADO] |
| Conversaciones E2E con VOXENTRA el 20-nov | 7: 1 dental documentada (2 min 15 s, 8 turnos) y 6 con evidencia preliminar (una por agente) | [CONFIRMADO] en capturas y video; turnos y proveedores [REPORTADO] |
| Latencia E2E dental, mediana (n = 8) | 2,850 s | [REPORTADO POR EL EQUIPO] |
| Latencia E2E dental, promedio (n = 8) | 2,989 s | [REPORTADO POR EL EQUIPO] |
| Latencia E2E de cuatro de los seis agentes | Medianas de 3,1135 s a 3,9832 s; E2E entre 0,6608 s (turno interrumpido, no válido) y 8,9018 s; sin promedio combinado; ventas y cobranza retail sin métricas | [REPORTADO] (extracto parcial del log) |
| Rango de latencia E2E | 2,6067 s a 4,1406 s | [REPORTADO] |
| Objetivo de 1 s | **No cumplido ni demostrado** en ninguna sesión | [REPORTADO] |
| Incidencias del worker | Bloqueo del bucle de eventos (136 ms); error de decodificación de audio; la conversación continuó; `errors {}` en el resumen | [REPORTADO]; sin causa determinada |
| Operaciones empresariales | Simuladas | [CONFIRMADO] |

**Las métricas del worker fueron transcritas por el usuario; no hay archivo original archivado ni hash.** La sesión (09:13–09:15) ocurrió antes de que se fusionara el PR #22 (09:41), que modificó los prompts; la evidencia no demuestra el comportamiento con esos prompts.

Hallazgos funcionales de la sesión: I-01 (dirección y teléfono no definidos en el prompt), I-02 (saludo distinto del configurado), I-03 (reserva y mensajería afirmadas antes de aclarar la simulación) e I-05 (mensaje inicial incompleto en las capturas; no se reconstruyó).

## 10. Limitaciones y trabajo futuro

**Limitaciones**

- De los seis agentes restantes hay **evidencia preliminar** (una conversación por agente), pero **ninguno está aprobado integralmente**: faltan criterios de la matriz de la Etapa 10B, el log del worker y la escucha de las voces. **No se afirma que los siete aprobaron.**
- Una sola sesión por agente, con un solo probador. La aplicación no graba audio; existe un video de pantalla de las seis sesiones, que contiene audio pero también el escritorio completo y no es publicable.
- No se cumplió el objetivo de latencia de 1 s.
- Métricas del 20-nov sin registro archivado; versión exacta del frontend y del worker no acreditada.
- Voces sin validación de oído.
- Sin telefonía, guion oficial de cobranza, comparación de costos ni integración con sistemas empresariales.
- Reorientación sin aprobación académica ni del cliente; marca VOXENTRA sin verificar.
- Rúbrica de Fase 3 y retroalimentación del informe final pendientes.

**Trabajo futuro (propuesta, sin compromiso)**

1. Archivar el registro del 20-nov, sanitizado y con hash.
2. Completar la validación de cada agente con las rutas no cubiertas de la matriz de la Etapa 10B (objeción y cobertura, titular en cobranza retail, datos bancarios, cupo y datos sensibles) antes de cambiar su estado visible.
3. Probar los prompts actuales frente a I-01 e I-03.
4. Medir latencia con un protocolo definido y evaluar palancas ya propuestas (sin medir).
5. Validar las voces de oído.
6. Resolver la aprobación académica y el uso del nombre y del código.
7. Si hubiera interés comercial, abordar integraciones reales (calendario, mensajería) como proyecto distinto.

## Aprobaciones pendientes (resumen)

Docente guía: reorientación y alcance de la presentación. Cliente: conocimiento o conformidad, si el equipo decide solicitarlo. Equipo: nombre VOXENTRA, publicación de diarios y guías, revisión cruzada de este anexo.

## Referencias de evidencia (repositorio técnico, sin seguimiento a la fecha)

- Sesión dental del 20-nov: `docs/validation/E2E-2026-11-20-voxentra-clinica-dental/` (README, matriz, métricas, incidencias, recomendaciones, capturas y hashes).
- Seis agentes restantes: `docs/validation/E2E-2026-11-20-voxentra-siete-agentes/` (informe consolidado, matriz de siete agentes, métricas consolidadas, incidencias, inventario de capturas, capturas derivadas y hashes).
- Paquete original `VOXENTRA_evidencias_E2E_20nov.zip` y video de la sesión: fuera de Git; solo se registran sus hashes. El video no es publicable.
- Matriz de validación de la Etapa 10B: `docs/validation/ETAPA-10B-siete-agentes-2026-11-20.md`.
