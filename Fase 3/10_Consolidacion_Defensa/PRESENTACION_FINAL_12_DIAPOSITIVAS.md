# Contenido definitivo de las 12 diapositivas (defensa del 21-nov-2026)

**Estado:** PROPUESTA lista para construir las diapositivas; pendiente de validación del equipo. Este documento es la referencia vigente por diapositiva; `ESTRUCTURA_PRESENTACION.md` queda como resumen y `GUION_DEFENSA.md` contiene el guion hablado.

**Identidad:** Fernando Patricio Olguea González (líder de proyecto y desarrollador), David Sepúlveda (Scrum Master y desarrollador) y Juan Díaz (Product Owner y desarrollador), según las portadas oficiales. Docente guía: Luis Bravo Yáñez. Asignatura: Capstone (PTY4614 / 001V), Duoc UC, sede Plaza Oeste.

## Límites oficiales (guía 3.3)

**20 minutos máximo, incluidas las preguntas.** Plan: exposición **14:30** y **5:30** reservados para preguntas. Nota individual (30 % de la nota final).

| Responsable | Diapositivas | Tiempo |
|---|---|---|
| Fernando | 1, 2, 3, 4, 11, 12 | **5:30** |
| Juan | 5, 6, 7 | **4:50** |
| David | 8, 9, 10 | **4:10** |
| Preguntas | — | **5:30** |
| **Total** | | **20:00** |

Acumulado: 1→0:20 · 2→1:20 · 3→2:30 · 4→3:50 · 5→5:10 · 6→6:10 · 7→8:40 · 8→9:50 · 9→11:20 · 10→12:50 · 11→13:40 · 12→14:30.

## Reglas de diseño para construir las diapositivas

1. **Máximo 5 líneas o 40 palabras visibles por diapositiva** (salvo tablas); el resto va en las notas.
2. Una idea por diapositiva y una evidencia visual por diapositiva.
3. Cada cifra con su etiqueta: **[C]** confirmado, **[R]** reportado por el equipo. Las métricas del worker se rotulan «medidas por el worker, transcritas por el equipo».
4. Paleta VOXENTRA Red Edition: rojo principal `#E53935`, rojo oscuro `#B71C1C`, rojo luminoso `#FF5252`, fondo `#0B1018`, tarjetas `#171E29`, texto principal `#F5F7FA` y texto secundario `#AAB4C3`. Mantener el verde solo para estados funcionales de éxito. Tipografía sans; contraste alto; sin animaciones.
5. **Nunca proyectar el video original.** Usar solo capturas derivadas con hash.
6. Las diapositivas no deben afirmar: aprobación del cliente o del docente, siete agentes aprobados, objetivo de 1 s cumplido, audio grabado ni integraciones empresariales reales.

---

## Diapositiva 1 — Portada y equipo

| Campo | Contenido |
|---|---|
| **Título** | Alloxentric Real Time Agent: de un prototipo para un cliente a una demostración de agentes de voz (VOXENTRA) |
| **Mensaje principal** | Presentamos un MVP de agentes de voz en tiempo real; VOXENTRA es el nombre provisional de la demostración |
| **Texto visible** | Proyecto APT · Capstone (PTY4614 / 001V) · Duoc UC, sede Plaza Oeste · Fernando Patricio Olguea González, David Sepúlveda, Juan Díaz · Docente guía: Luis Bravo Yáñez · 21-nov-2026 · «VOXENTRA: nombre provisional, no es una empresa» |
| **Evidencia o imagen** | Captura del catálogo VOXENTRA: `alloxentric-real-time-agent/docs/validation/ETAPA-8-voxentra-frontend-2026-11-19/03-catalogo-escritorio.png` |
| **Responsable / tiempo** | Fernando · **0:20** |
| **Notas del expositor** | Decir que VOXENTRA no es una empresa constituida. Mantener «Alloxentric Real Time Agent» como nombre oficial del proyecto. No presentar la reorientación como aprobada |

## Diapositiva 2 — Problema y objetivo original

| Campo | Contenido |
|---|---|
| **Título** | El problema y el objetivo de Fase 1 |
| **Mensaje principal** | El proyecto nació de un problema de costos del cliente; el objetivo era un bot de cobranza por voz con respuesta ≤ 1 s |
| **Texto visible** | Problema [R]: plataforma de bots de voz de gran escala con poca elasticidad de costos · Objetivo: prototipo de bot de cobranza por voz (LiveKit, transcripción, ElevenLabs, Asterisk) · Comparar costo y efectividad · Respuesta ≤ 1 s |
| **Evidencia o imagen** | Esquema simple «Problema → Objetivo → Meta de latencia» (a crear); fuente: Informe v1.2, §2 y §3 |
| **Responsable / tiempo** | Fernando · **1:00** |
| **Notas del expositor** | La transcripción de la reunión del 2-sep y la especificación v0.1 **no están archivadas**: decirlo. No atribuir citas ni decisiones al cliente como confirmadas |

## Diapositiva 3 — Evolución del proyecto y decisión del equipo

| Campo | Contenido |
|---|---|
| **Título** | Qué logramos, qué no y qué decidimos |
| **Mensaje principal** | Se logró un MVP de voz; la reorientación a una demostración para pymes es una decisión del equipo, con aprobación pendiente |
| **Texto visible** | Línea de tiempo: sep-2026 objetivo · 10-oct componentes aislados · 17-nov MVP integrado · 20-nov demostración VOXENTRA · No logrado: telefonía, guion oficial, comparación de costos · **Decisión del equipo; aprobación académica y del cliente: pendientes** |
| **Evidencia o imagen** | Línea de tiempo (a crear) con PR #21 y #22 (20-nov); Anexo §3 a §6 |
| **Responsable / tiempo** | Fernando · **1:10** |
| **Notas del expositor** | Decir expresamente: no hay aprobación documentada del cliente ni del docente. No afirmar reuniones incumplidas: el expediente solo muestra falta de actas, transcripción y aprobaciones formales. Ver Anexo §4 |

## Diapositiva 4 — Arquitectura conservada

| Campo | Contenido |
|---|---|
| **Título** | Arquitectura: voz en tiempo real sobre LiveKit |
| **Mensaje principal** | La arquitectura no cambió con VOXENTRA: navegador, token del servidor, LiveKit y un worker en Python |
| **Texto visible** | Navegador (Next.js) → funciones de acceso y token → LiveKit → worker: STT Google Chirp 3 → LLM (Gemini o DeepSeek) → TTS ElevenLabs · El navegador solo envía el id del agente · Sin grabación de audio |
| **Evidencia o imagen** | `Fase 3/03_Diseno/diagramas/originales_fase2/D01_fig1_componentes.png` (muestra Chirp 3, ElevenLabs v4 turbo y la telefonía Asterisk como PENDIENTE) |
| **Responsable / tiempo** | Fernando · **1:20** |
| **Notas del expositor** | Señalar en el diagrama que Asterisk es futuro y no existe. Proveedor de LLM de la sesión dental: DeepSeek (informado). La versión desplegada no está acreditada |

## Diapositiva 5 — Frontend VOXENTRA y siete agentes

| Campo | Contenido |
|---|---|
| **Título** | Una demo coherente para pymes |
| **Mensaje principal** | Cambiamos solo lo visible; la demostración mantiene su navegación y deja claros los límites |
| **Texto visible** | Nombre provisional VOXENTRA · Aviso permanente: «Demostración con datos ficticios. No realiza operaciones reales ni está integrada con sistemas empresariales» · Siete agentes, cada uno con empresa, guion, saludo y voz |
| **Evidencia o imagen** | `…/ETAPA-8-voxentra-frontend-2026-11-19/03-catalogo-escritorio.png` (no usar las capturas 05 y 06, que son simuladas con HTTP) |
| **Responsable / tiempo** | Juan · **1:20** |
| **Notas del expositor** | Los identificadores técnicos internos no se renombraron (son la clave de despacho). No hay panel de latencia en la interfaz. Decir que no existe una plataforma SaaS |

## Diapositiva 6 — Escenarios ficticios y estados de alcance

| Campo | Contenido |
|---|---|
| **Título** | Siete escenarios, todos ficticios |
| **Mensaje principal** | Sin marcas reales; cada agente con un estado de validación honesto |
| **Texto visible** | Tabla: Clínica Sonrisa Norte (dental): **sesión documentada** · MóvilAndes · Casa Aurora · Financiera Costanera · FibraSur · Talento Cordillera · Tienda Brújula: **evidencia preliminar, sin aprobación integral** · Operaciones simuladas |
| **Evidencia o imagen** | Mosaico de las seis capturas derivadas: `…/E2E-2026-11-20-voxentra-siete-agentes/capturas/01…06_*_derivada.png` |
| **Responsable / tiempo** | Juan · **1:00** |
| **Notas del expositor** | La insignia de la interfaz de los seis dice «Guion configurado, sin prueba real documentada»: explicar que la evidencia es preliminar y que cambiarla exige una decisión del equipo. No decir «probados» ni «aprobados» |

## Diapositiva 7 — Demostración en vivo (selección libre)

| Campo | Contenido |
|---|---|
| **Título** | Elijan un agente |
| **Mensaje principal** | La comisión elige; mostramos el sistema funcionando, con sus límites |
| **Texto visible** | «Elija cualquiera de los siete agentes» · Datos ficticios · Respuestas de 2,5 a 5 s |
| **Evidencia o imagen** | La demostración en vivo; respaldo: captura derivada del agente elegido (`DEMOSTRACION_SELECCION_LIBRE.md`) |
| **Responsable / tiempo** | Juan (Fernando en apoyo y reloj) · **2:30 máx.** |
| **Notas del expositor** | Seguir el procedimiento de `DEMOSTRACION_SELECCION_LIBRE.md`. Si falla, pasar a la captura sin extender el tiempo. No hablar de latencia como logro |

## Diapositiva 8 — Pruebas automatizadas y CI

| Campo | Contenido |
|---|---|
| **Título** | Calidad que se verifica automáticamente |
| **Mensaje principal** | Las pruebas automáticas protegen la estructura; no miden la calidad de la voz |
| **Texto visible** | **231** pruebas de Python y **94** del frontend aprobadas [C, 20-nov] · CI en GitHub Actions · Verifican: siete agentes sincronizados, guiones sin marcas reales, aviso de simulación |
| **Evidencia o imagen** | Captura de terminal con `231 passed` y `94 passed` (**por tomar** antes de la defensa) |
| **Responsable / tiempo** | David · **1:10** |
| **Notas del expositor** | Mencionar su aporte documentado: integración de ElevenLabs (PR #4) y sus pruebas. Aclarar que las pruebas no usan proveedores externos |

## Diapositiva 9 — Resultados E2E y latencia

| Campo | Contenido |
|---|---|
| **Título** | Una sesión real y datos parciales |
| **Mensaje principal** | Las conversaciones funcionan, pero el objetivo de 1 s no se cumplió ni se demostró |
| **Texto visible** | Dental (n = 8): mediana **2,850 s**, promedio **2,989 s** · Otros 4 agentes (parciales): medianas **3,11 a 3,98 s**, máximo **8,90 s** · Ventas y cobranza retail: sin métricas · «Medidas por el worker, transcritas por el equipo» · **Objetivo de 1 s: no cumplido** |
| **Evidencia o imagen** | Gráfico de barras de medianas por agente con una línea en 1 s (datos en la tabla siguiente) y la captura dental `E2E-2026-11-20-voxentra-clinica-dental/capturas/05-cierre-simulado.png` |
| **Responsable / tiempo** | David · **1:30** |
| **Notas del expositor** | No promediar las sesiones. Mencionar el bucle de eventos (136 ms), el error de decodificación de audio y, en reclutamiento, la interrupción y los 8,9 s; sin causa determinada. La dental fue antes del PR #22 |

Datos del gráfico (medianas de E2E en segundos; **[R]**): Dental 2,8500 · Cobranza financiera 3,3598 · Soporte 3,4567 · Reclutamiento 3,1135 (con un turno interrumpido; 3,2450 sin él) · Postventa 3,9832 · Ventas y cobranza retail: «sin métricas». Línea de referencia: 1,0.

## Diapositiva 10 — Limitaciones y riesgos

| Campo | Contenido |
|---|---|
| **Título** | Lo que falta, dicho primero |
| **Mensaje principal** | Declaramos las limitaciones antes de que las pregunten |
| **Texto visible** | Seis agentes: evidencia preliminar, **no aprobación integral** · Log del worker sin archivar · Voces sin validar · Sin telefonía, guion oficial ni comparación de costos · Dental: dato inventado y reserva sin aclarar (sesión anterior al PR #22; **no repetida**) · Reorientación sin aprobación |
| **Evidencia o imagen** | Captura dental `04-direccion-y-telefono.png` y la tabla de incidencias |
| **Responsable / tiempo** | David · **1:30** |
| **Notas del expositor** | No minimizar la interrupción ni el error de audio. No afirmar que los cambios del PR #22 corrigieron I-01 ni I-03. Mencionar que el PR #8 se fusionó sin revisiones |

## Diapositiva 11 — Gestión y contribuciones

| Campo | Contenido |
|---|---|
| **Título** | Quién hizo qué, con respaldo |
| **Mensaje principal** | Atribuimos contribuciones solo con commits y pull requests verificables |
| **Texto visible** | Fernando: pipeline, métricas, seguridad, CI · David: ElevenLabs y sus pruebas · Juan: Chirp 3, personas y voces, interfaz · Los merges no cuentan como autoría · Scrum parcial; CoreStream: solo reporte agregado |
| **Evidencia o imagen** | `Fase 3/08_Contribuciones/MATRIZ_CONTRIBUCIONES.md` (tabla resumida) |
| **Responsable / tiempo** | Fernando · **0:50** |
| **Notas del expositor** | No atribuir tareas de Fase 3 a David sin documento (pendiente que las documente). El PR #18 de Juan sigue abierto y no está integrado. Nombrar la revisión cruzada pendiente |

## Diapositiva 12 — Conclusiones y trabajo futuro

| Campo | Contenido |
|---|---|
| **Título** | Conclusiones y próximos pasos |
| **Mensaje principal** | MVP técnicamente demostrable, con brechas claras y un camino concreto |
| **Texto visible** | MVP de voz funcional y demostrable [C] · Objetivo de 1 s no cumplido · Próximos pasos: archivar el log, probar las rutas pendientes de los siete agentes, validar voces, resolver aprobaciones · Gracias; preguntas |
| **Evidencia o imagen** | Ninguna adicional; fondo del catálogo |
| **Responsable / tiempo** | Fernando · **0:50** |
| **Notas del expositor** | Cerrar con los pendientes académicos (aprobación de la reorientación, retroalimentación del informe final, rúbrica). Abrir preguntas. Si hay retraso, recortar esta diapositiva primero |

---

## Control de tiempo

- Aviso a los **12:50** (inicio de la diapositiva 11) para el cierre.
- Si la comisión interrumpe con una pregunta, ese tiempo cuenta dentro de los 20 minutos: responder breve y volver.
- Recorte en orden: diapositiva 12, apoyo de la 11, segunda mitad de la 3. **Nunca recortar las preguntas ni la declaración de limitaciones (10).**

## Imágenes por preparar antes de armar las diapositivas

1. Esquema del problema (diapositiva 2) y línea de tiempo (diapositiva 3).
2. Gráfico de medianas (diapositiva 9).
3. Captura de terminal de `231 passed` y `94 passed` (diapositiva 8).
4. Mosaico de las seis capturas derivadas (diapositiva 6).
5. Una carpeta local con todas las capturas (ver plan de contingencia).
