# Estructura de la presentación final (21-nov-2026)

**Estado:** PROPUESTA para revisión del equipo. Sustituye como borrador al `09_Presentacion/GUION_PRELIMINAR.md` (que no se sobrescribió y quedó desactualizado: ordena usar solo el nombre Alloxentric).

> **Vigente (Etapa 10E):** el contenido definitivo por diapositiva está en `PRESENTACION_FINAL_12_DIAPOSITIVAS.md` y la demostración en `DEMOSTRACION_SELECCION_LIBRE.md`. Este archivo queda como resumen; los tiempos coinciden.

## Límites oficiales (guía 3.3)

- **Máximo 20 minutos en total, incluidas las preguntas de la comisión.**
- Comisión: docente(s) de la asignatura y Dirección de Carrera. Nota **individual** por integrante (30 % de la nota final).
- Debe fundamentar las decisiones y presentarse acompañada de evidencias; se espera que incorpore ajustes de la última retroalimentación del informe final (**[PENDIENTE]**: no consta en el expediente).

## Presupuesto de tiempo

| Bloque | Tiempo |
|---|---|
| Exposición (11 diapositivas más demostración) | **14:30** |
| Preguntas de la comisión | **5:30** (mínimo reservado) |
| **Total** | **20:00** |

Regla: si la comisión pregunta durante la exposición, esa pregunta cuenta dentro de los 20 minutos. Si la exposición se alarga, se recorta la diapositiva 12 y el apoyo de la 11, nunca el tiempo de preguntas.

## Índice definitivo propuesto

| N.º | Diapositiva | Quién | Tiempo | Acumulado |
|---|---|---|---|---|
| 1 | Portada y equipo | Fernando | 0:20 | 0:20 |
| 2 | Problema y objetivo original | Fernando | 1:00 | 1:20 |
| 3 | Evolución del proyecto y decisión del equipo | Fernando | 1:10 | 2:30 |
| 4 | Arquitectura conservada | Fernando | 1:20 | 3:50 |
| 5 | Frontend VOXENTRA y siete agentes | Juan | 1:20 | 5:10 |
| 6 | Escenarios ficticios y estados de alcance | Juan | 1:00 | 6:10 |
| 7 | **Demostración en vivo** (selección libre) | Juan (con Fernando en apoyo) | 2:30 | 8:40 |
| 8 | Pruebas automatizadas y CI | David | 1:10 | 9:50 |
| 9 | Resultado E2E dental y latencia | David | 1:30 | 11:20 |
| 10 | Limitaciones y riesgos | David | 1:30 | 12:50 |
| 11 | Gestión y contribuciones | Fernando | 0:50 | 13:40 |
| 12 | Conclusiones y trabajo futuro | Fernando | 0:50 | 14:30 |

Distribución: Fernando 5:30; Juan 4:50; David 4:10. [PROPUESTA: el equipo debe acordarla; la asignación sigue las contribuciones documentadas de cada uno.]

## Narrativa por diapositiva, mensaje central y evidencia

| N.º | Mensaje central | Contenido | Evidencia recomendada | Qué no decir |
|---|---|---|---|---|
| 1 | Quiénes somos y qué mostramos | Título «Alloxentric Real Time Agent — demostración VOXENTRA»; integrantes; fecha | — | Que VOXENTRA es una empresa |
| 2 | Había un problema con un cliente real | Plataforma de bots con poca elasticidad de costos; objetivo de Fase 1: prototipo de bot de cobranza por voz con respuesta ≤ 1 s | Informe v1.2 §2–§3 | Atribuir citas o decisiones al cliente como confirmadas (la transcripción no está archivada) |
| 3 | Qué hicimos, qué no, y qué decidimos | Lo implementado para Alloxentric; lo no logrado (telefonía, guion oficial, costos); decisión del equipo de continuar como demostración para pymes; **aprobación académica pendiente** | Anexo de evolución §3–§6 | Que el cliente o el docente aprobaron; que hubo reuniones incumplidas |
| 4 | La arquitectura se mantuvo | LiveKit, Chirp 3, LLM (Gemini o DeepSeek), ElevenLabs; frontend estático; seguridad (CSP, token del servidor, sin grabación) | Diagrama de D01; código | Que el sistema es «para producción» |
| 5 | Una demo coherente para pymes | Marca provisional, navegación existente, aviso de datos ficticios, siete agentes | Capturas de la Etapa 8 | Que existe una plataforma SaaS |
| 6 | Escenarios sin marcas reales y con alcance honesto | Siete empresas ficticias; insignias de alcance; operaciones simuladas; **evidencia preliminar de una conversación por agente el 20-nov**, sin aprobación integral | Tabla del anexo §8; captura del catálogo; una captura derivada por agente | Que los siete agentes fueron aprobados o que la insignia ya refleja la evidencia nueva |
| 7 | Prueba en vivo | Ver «Demostración» más abajo | La propia demo | Prometer latencia de 1 s |
| 8 | La calidad se verifica automáticamente | 231 pruebas Python y 94 del frontend aprobadas; CI; pruebas de compatibilidad de agentes y sin marcas reales | Resultado de pytest y vitest; PR #21 y #22 | Que las pruebas automáticas prueban la calidad de la voz |
| 9 | Resultados reales del 20-nov | **Dental:** 2 min 15 s, 8 turnos, mediana 2,850 s, promedio 2,989 s, rango 2,61–4,14 s (sesión previa al PR #22). **Otros cuatro agentes con métricas parciales:** medianas de 3,11 a 3,98 s, rango hasta 8,90 s, sin promedio combinado; ventas y cobranza retail sin métricas. **Objetivo de 1 s no cumplido ni demostrado**; incidencias de audio y bucle de eventos | Capturas con hash; `METRICAS.md` y `METRICAS_CONSOLIDADAS.md` | «Verificado contra el registro» (el log no está archivado); promediar las sesiones |
| 10 | Lo que falta, dicho primero | Seis agentes con evidencia preliminar pero sin aprobación integral; log del worker no archivado; voces sin escuchar ni validar; interrupción del agente (reclutamiento) y latencia de 8,9 s; sin telefonía ni guion oficial; marca y aprobaciones pendientes; I-01 a I-03 (dental, sin repetir tras el PR #22) | Anexo §10; `INCIDENCIAS.md` de ambas carpetas | Minimizar o esconder el error de audio, la interrupción o la falta de log |
| 11 | Quién hizo qué, con respaldo | Matriz de contribuciones basada en commits y PR; los merges no cuentan como autoría; Scrum parcial | `MATRIZ_CONTRIBUCIONES.md` | Atribuir tareas sin respaldo (en especial las de Fase 3 de David hasta documentarlas) |
| 12 | Qué aprendimos y cómo seguir | Conclusiones; trabajo futuro; cierre y preguntas | Anexo §10 | Compromisos que no pueden cumplirse |

## Demostración de selección libre (diapositiva 7)

**Qué se ofrece:** la comisión elige cualquiera de los siete agentes.

**Protocolo (propuesta):**
1. Mostrar el catálogo; leer el aviso de datos ficticios y señalar la insignia de cada agente.
2. Decir en voz alta: «La clínica dental tiene una sesión documentada con métricas; de los otros seis agentes tenemos evidencia preliminar de una conversación por agente, sin aprobación integral. La insignia de la pantalla todavía dice que no tienen prueba documentada».
3. La comisión elige. Si elige la clínica: usar el flujo conocido (pedir hora, motivo, preferencia horaria, pedir dirección y teléfono). Si elige otro: conversar 60 a 90 segundos con el guion de la matriz de validación (saludo, consulta principal, una pregunta inesperada, un pedido fuera de alcance, cierre).
4. Máximo **2:30** de demostración. Si el agente falla o responde fuera de guion, declararlo y pasar al plan de contingencia.
5. Quien opera la demo no habla de latencia como éxito; si la comisión pregunta, citar la mediana de 2,85 s y el objetivo incumplido.

**Requisitos previos:** acceso con el código temporal, micrófono probado, red estable, claves y cuotas de Google, ElevenLabs, DeepSeek y LiveKit vigentes, sitio de demostración abierto en una pestaña ya autenticada (ver `CHECKLIST_PRESENTACION.md`).

**Riesgos de la selección libre:** cada agente tiene una sola sesión previa y cubre solo parte de los criterios (rutas no probadas: objeción y cobertura en ventas, titular en cobranza retail, datos bancarios, cupo, datos sensibles); posible dato inventado en el agente dental (I-01, sin repetir tras el PR #22); interrupción del agente al usuario (observada en reclutamiento); latencia de 2,5 a 5 s y un valor de 8,9 s. Recomendación: **repetir una prueba corta con voz de los siete agentes antes de la defensa** (requiere autorización explícita) y ajustar lo que se prometa a lo que se vea.

## Plan alternativo con capturas reales (si falla la conexión)

Todas son copias derivadas y sanitizadas, con hash, en `docs/validation/E2E-2026-11-20-voxentra-siete-agentes/` del repositorio técnico (hoy sin seguimiento: **copiarlas a una carpeta local de la defensa**). No incluyen audio.

| Si la comisión elige | Mostrar (captura) | Mostrar (cierre de la sesión, derivado del video) |
|---|---|---|
| Ventas de telefonía | `capturas/01_ventas_movil_andes_derivada.png` | `capturas_video/S1-ventas_cierre_108s.png` |
| Cobranza retail | `capturas/02_cobranza_retail_casa_aurora_derivada.png` | `capturas_video/S2-cobranza-retail_cierre_156s.png` |
| Cobranza financiera | `capturas/03_cobranza_financiera_costanera_derivada.png` | `capturas_video/S3-cobranza-financiera_cierre_291s.png` |
| Soporte de internet | `capturas/04_soporte_fibrasur_derivada.png` | `capturas_video/S4-soporte_cierre_428s.png` |
| Entrevista laboral | `capturas/05_reclutamiento_talento_cordillera_derivada.png` | `capturas_video/S5-reclutamiento_cierre_638s.png` |
| Atención postventa | `capturas/06_postventa_tienda_brujula_derivada.png` | `capturas_video/S6-postventa_cierre_770s.png` |
| Clínica dental | Cinco capturas de `docs/validation/E2E-2026-11-20-voxentra-clinica-dental/capturas/` | — |

Frase de apoyo: «Esta es una sesión real del 20 de noviembre; la captura muestra la transcripción y no prueba el audio ni la latencia. Las operaciones son simuladas». Las capturas muestran la parte derecha cortada: avisar si se pregunta.

El **video original no debe proyectarse ni compartirse**: muestra el escritorio completo, notificaciones de terceros y la URL del sitio.

## Evidencias para llevar (en pantalla o impresas)

- Capturas derivadas de las siete sesiones del 20-nov, con sus hashes, y las tablas de métricas (dental y cuatro agentes con datos parciales; sin promedio combinado).
- Captura del catálogo con las insignias de alcance.
- Resultado de pytest (231) y vitest (94).
- Diagrama de arquitectura (D01).
- `MATRIZ_SIETE_AGENTES.md`: dictamen por agente y criterios no evaluables (la evidencia es preliminar; ninguno aprobado integralmente).
- Anexo de evolución y lista de aprobaciones pendientes.

## Pendientes antes de armar las diapositivas

- Retroalimentación del docente sobre el informe final: definir qué ajustes se incorporan y mostrarlos en la presentación.
- Aprobación del docente sobre la reorientación y sobre el formato de la demo.
- Decidir quién opera el equipo durante la demo y quién conserva el control del reloj.
