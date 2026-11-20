# Anexo académico final de la Fase 3 — Alloxentric Real Time Agent y la demostración VOXENTRA

**Estado:** BORRADOR de cierre para revisión del equipo. Es un anexo **complementario**: no sustituye ni modifica los siete entregables vigentes (D01 v1.2, D02 v1.2, D03 v1.2, D04 v1.2, D05 v1.3, D06 v1.2 e Informe consolidado v1.2) ni las versiones de `Entregables/_historico/`. Amplía y consolida `ANEXO_EVOLUCION_VOXENTRA.md`.

**Proyecto:** Alloxentric Real Time Agent · Capstone (PTY4614 / 001V) · Duoc UC, sede Plaza Oeste · Docente guía: Luis Bravo Yáñez.
**Integrantes (según las portadas oficiales):** Fernando Patricio Olguea González (líder de proyecto y desarrollador), David Sepúlveda (Scrum Master y desarrollador) y Juan Díaz (Product Owner y desarrollador).
**Corte:** 20-nov-2026. Defensa: 21-nov-2026.

**Clasificación de la evidencia:** **[CONFIRMADO]** verificado en archivos o con ejecución propia · **[REPORTADO POR EL EQUIPO]** informado, sin archivo original archivado · **[INFERENCIA]** deducido · **[PENDIENTE]** falta información.

> **Aviso.** VOXENTRA es un **nombre provisional** de una demostración académica. **No es una empresa constituida**, ni un producto comercial, ni un reemplazo académico autorizado del objetivo original. No se afirma que el cliente ni el docente hayan aprobado la reorientación.

## 1. Contexto del proyecto original

- [REPORTADO] Según el informe de Fase 1, en la reunión inicial del 2-sep-2026 el representante de Alloxentric explicó que su plataforma de bots de voz, hecha para gran escala, tiene poca elasticidad de costos cuando baja el volumen de llamadas, y pidió un prototipo de bot de cobranza por voz.
- [CONFIRMADO] Objetivo general heredado (Informe v1.2, §3): desarrollar y evaluar un prototipo de bot de cobranza por voz basado en LiveKit, con transcripción, ElevenLabs y telefonía Asterisk; comparar costo y efectividad con la solución actual y responder en no más de 1 s. **No existe un ajuste académico aprobado que reemplace ese objetivo.**
- [PENDIENTE] La transcripción del 2-sep y la especificación v0.1 no están archivadas; ACTA-01 es una reconstrucción sin convocatoria ni asistentes.

## 2. Evolución demostrativa hacia VOXENTRA

| Hito | Estado |
|---|---|
| Fase 1 (sep) y Fase 2 (oct): componentes aislados y primeras pruebas | [CONFIRMADO] en los informes |
| 17-nov: MVP integrado en `main` (`77ff85c`), 214 + 91 pruebas, E2E dental con DeepSeek | [CONFIRMADO] (D05 v1.3) |
| 19/20-nov: PR #21 (identidad visible VOXENTRA) y PR #22 (siete agentes ficticios), fusionados | [CONFIRMADO] |
| Decisión del equipo de continuar el MVP de forma autónoma como demostración para pymes | [REPORTADO]; sin acta, fecha ni lista de participantes |
| Aprobación del docente guía | **[PENDIENTE]**; no hay evidencia |
| Conocimiento o conformidad del cliente original | **[PENDIENTE]**; no se afirma |
| Reutilización del código y la identidad de Alloxentric; disponibilidad de la marca VOXENTRA | **[PENDIENTE]**; no verificado |

**Dificultades de coordinación documentadas** (solo lo que el expediente sostiene): falta de actas y de transcripción archivada; decisiones atribuidas al cliente sin aprobación formal verificable; contradicción no resuelta sobre usar o no un LLM; REG-04 con «cumplimiento no acreditado»; ausencia de protocolo de latencia y de guion oficial de cobranza; CoreStream con solo un reporte agregado [REPORTADO el juicio sobre sus deficiencias]. **El expediente no documenta reuniones incumplidas ni una negativa del cliente**; si el equipo quiere sostenerlo, debe aportar correos, convocatorias o tickets.

## 3. Arquitectura implementada

[CONFIRMADO] en el código (`main`):

| Capa | Componente |
|---|---|
| Voz en tiempo real | LiveKit Agents; worker en Python |
| STT | Google Chirp 3 (`chirp_3`, `es-US`) |
| LLM | Gemini (por defecto) o DeepSeek (`deepseek-flash`), según `LLM_PROVIDER` |
| TTS | ElevenLabs (`eleven_v4_turbo`), una voz por agente |
| Frontend | Next.js estático; acceso por código; sesión por cookie; token de LiveKit emitido por el servidor con despacho forzado; solo viaja el id del agente |
| Seguridad | CSP sin `unsafe-inline` ni `unsafe-eval`; sin grabación de audio |
| Calidad | Pruebas automatizadas y CI (GitHub Actions) |
| **No existe** | Telefonía Asterisk, persistencia de negocio, integración con calendarios, mensajería, pagos ni sistemas empresariales |

Los proveedores efectivos de las sesiones del 20-nov son [REPORTADO]: el extracto del log del worker **aún no está incorporado** (ver §7). La versión desplegada del frontend y del worker **no está acreditada**.

## 4. Siete escenarios configurados

[CONFIRMADO] (PR #21 y #22): empresas y personas ficticias, sin marcas comerciales reales ni nombres de integrantes. Cada agente tiene guion, saludo, voz y reglas comunes (hablar breve, no inventar disponibilidad ni condiciones, aclarar lo simulado, no pedir datos reales).

| Agente (visible) | Empresa ficticia | Id técnico | Estado de validación |
|---|---|---|---|
| Clínica dental | Clínica Dental Sonrisa Norte | `clinica-dental` | **Aprobado con observaciones** (sesión previa al PR #22) |
| Ventas de telefonía | MóvilAndes | `claro-ventas` | Evidencia parcial favorable; no aprobado integralmente |
| Cobranza retail | Casa Aurora | `falabella-cobranza` | Evidencia parcial favorable (solo la ruta del tercero) |
| Cobranza financiera | Financiera Costanera | `ripley-cobranza` | Evidencia parcial favorable |
| Soporte de internet | FibraSur | `soporte-internet` | Evidencia favorable con observaciones |
| Entrevista laboral | Talento Cordillera | `entrevista-rrhh` | Evidencia favorable con observaciones |
| Atención postventa | Tienda Brújula | `hites-servicio` | Evidencia favorable con observaciones |

Los ids técnicos de tres agentes conservan nombres históricos de marcas; no se muestran al usuario y no se renombraron para no romper el despacho.

## 5. Metodología de validación

1. **Pruebas automatizadas** (Python y frontend), sin red ni credenciales: verifican estructura, sincronización de agentes, ausencia de marcas reales y aislamiento de secretos.
2. **Sesiones E2E manuales** con proveedores reales desde la versión publicada, con un probador humano y la transcripción en pantalla. La aplicación no graba audio.
3. **Criterios por agente** de la matriz de la Etapa 10B: saludo, consulta principal, pregunta inesperada, pedido fuera de alcance y cierre, más restricciones, incidencias, métricas y criterios no verificables.
4. **Regla de dictamen:** un agente **no se aprueba porque haya respondido**. Cada criterio se marca *observado*, *parcial* o *no evaluable*; los no evaluables **no se convierten en aprobados**.
5. **Tratamiento de la evidencia:** hashes SHA-256; originales sin modificar; copias derivadas recortadas para publicar; el video de pantalla (con el escritorio completo) no se publica.
6. **Límites del método:** una sola sesión por agente; un solo probador; registro del worker parcial; sin evaluación auditiva.

## 6. Resultados de las pruebas

| Resultado | Valor | Estado |
|---|---|---|
| Pruebas de Python | 231 aprobadas (1 advertencia del SDK) | [CONFIRMADO] (ejecución del 20-nov sobre el árbol equivalente a `main`) |
| Pruebas del frontend | 94 aprobadas en 14 archivos; `tsc` sin errores | [CONFIRMADO] |
| Agentes configurados | 7 | [CONFIRMADO] |
| Conversaciones E2E del 20-nov | 7 (1 dental documentada y 6 con evidencia preliminar) | [CONFIRMADO] en capturas y video |
| Operaciones empresariales | **Todas simuladas** | [CONFIRMADO] |

Los seis agentes restantes saludaron con el texto configurado, respondieron de forma coherente con su guion, aclararon la simulación y no se observaron datos inventados ni datos reales solicitados [CONFIRMADO en video]. **Ninguno se declara aprobado integralmente**: cada sesión cubre solo parte de los criterios.

## 7. Métricas verificadas y reportadas

### 7.1 Verificadas [CONFIRMADO]

| Dato | Valor | Cómo se verificó |
|---|---|---|
| Pruebas automáticas | 231 y 94 | Ejecución propia |
| Hashes del paquete de evidencias | 8 de 8 coinciden | `sha256sum` sobre el contenido extraído |
| Mensajes y duración de cuatro sesiones | Reclutamiento 23 · 3:14; soporte 16 · 1:55; cobranza financiera 14 · 1:54; cobranza retail 5 · 0:33 | Historial local de la interfaz (video) |
| Cálculo de estadísticos | Coincide con el informe preliminar | Recálculo desde `metricas_parciales.csv` (**el cálculo**, no la fuente) |

### 7.2 Reportadas [REPORTADO POR EL EQUIPO]

Los valores de latencia provienen de `metricas_parciales.csv` y de las cifras de la sesión dental transcritas por el equipo. **El extracto original del worker (`Texto pegado(10).txt`) no estaba disponible en esta revisión**; cuando se reciba, solo podrán pasar a [CONFIRMADO] los datos verificables directamente en el extracto, y no se afirmará que es el log completo.

| Agente | Turnos con E2E | Mediana E2E | Rango E2E |
|---|---|---|---|
| Dental (n = 8, previo al PR #22) | 8 | **2,8500 s** (promedio **2,9890 s**) | 2,6067 – 4,1406 s |
| Cobranza financiera | 5 | 3,3598 s | 2,9463 – 5,0845 s |
| Soporte | 6 | 3,4567 s | 2,9634 – 5,1822 s |
| Reclutamiento | 8 (1 interrumpido) | 3,1135 s (3,2450 s sin el interrumpido) | 0,6608 – 8,9018 s |
| Postventa | 6 | 3,9832 s | 2,4520 – 4,6312 s |
| Ventas y cobranza retail | — | sin métricas | — |

**No se calcula un promedio de las sesiones** (distinto número de turnos, extracto parcial, un turno interrumpido y un valor atípico). **El objetivo de 1 s no se cumplió ni se demostró** en ninguna sesión. Los componentes (EOT, TTFT, TTFB) no son aditivos y no se atribuye causa a la latencia.

## 8. Incidencias

| Incidencia | Evidencia |
|---|---|
| Dental I-01: dirección y teléfono generados por el modelo (no están en el prompt) | [CONFIRMADO] en captura; **abierta; no repetida tras el PR #22** |
| Dental I-02: saludo distinto del configurado | [CONFIRMADO]; causa no determinada |
| Dental I-03: reserva y mensajería afirmadas antes de aclarar la simulación | [CONFIRMADO]; **abierta; no repetida tras el PR #22** |
| Dental I-05: mensaje inicial del usuario incompleto en las capturas | [CONFIRMADO]; no se reconstruyó |
| Reclutamiento: el agente interrumpió al usuario; E2E de 8,9018 s | Interrupción [CONFIRMADO en video]; latencia [REPORTADO] |
| Avisos de bloqueo del bucle de eventos (136 ms en la sesión dental y otros), transcripciones tardías, `eot prediction timed out`, `Task was destroyed but it is pending!`, error de decodificación de audio | [REPORTADO]; sin causa determinada |
| La insignia de la interfaz sigue diciendo «sin prueba real documentada» en los seis agentes | [CONFIRMADO] |

La sesión dental (09:13) fue **anterior** al PR #22 (09:41). Las seis sesiones posteriores son **consistentes** con los prompts del PR #22 [INFERENCIA], pero **no se infiere la versión desplegada** y eso no valida la corrección de I-01 ni I-03.

## 9. Limitaciones

- Seis agentes con evidencia preliminar, **sin aprobación integral**; rutas no probadas: objeción y cobertura (ventas), titular (cobranza retail), acuerdo legal y datos bancarios (cobranza financiera), modelo y reinicio (soporte), datos sensibles (reclutamiento), cupo y devoluciones (postventa).
- Log del worker no archivado; voces sin validación auditiva; versión desplegada no acreditada.
- Latencia sobre el objetivo; muestras pequeñas de una sola sesión por agente.
- Sin telefonía, guion oficial de cobranza, comparación de costos ni integraciones empresariales.
- Reorientación, uso del nombre VOXENTRA y reutilización del código sin aprobación documentada.
- **Requisitos de la guía 3.3 sin evidencia** (ver §10).

## 10. Requisitos de la guía oficial sin evidencia en el expediente

| Requisito (guía 3.3) | Estado |
|---|---|
| Incorporar los ajustes de la **última retroalimentación del docente sobre el informe final** | **Sin evidencia**: la retroalimentación no consta en el expediente |
| Usar como orientación los campos de la **guía del Informe Final** | **Sin evidencia**: la guía no está en el expediente (se usó la estructura del Informe v1.2 como aproximación [INFERENCIA]) |
| Rúbrica o planilla de evaluación de Fase 3 | **Sin evidencia** |
| Máximo 20 minutos incluyendo preguntas | Plan definido (14:30 + 5:30); **sin ensayo cronometrado** |
| Apoyo audiovisual | Contenido definido; **las diapositivas aún no existen** |
| Evidencias que acompañen la presentación | Disponibles con las limitaciones de §9 |
| Fundamentar las decisiones | Cubierto en la narrativa; las decisiones atribuidas al cliente carecen de acta y la reorientación carece de aprobación |

## 11. Conclusiones y trabajo futuro

**Conclusiones**

1. El equipo dispone de un MVP técnicamente funcional y demostrable de agentes de voz en tiempo real, con 231 + 94 pruebas automáticas aprobadas y siete escenarios ficticios configurados.
2. La clínica dental tiene una sesión documentada (aprobada con observaciones) y los otros seis agentes, evidencia preliminar favorable, sin aprobación integral.
3. El objetivo de latencia de 1 s no se cumplió ni se demostró; las operaciones son simuladas.
4. La reorientación es una decisión del equipo con aprobación académica pendiente; el objetivo original no se reemplaza.

**Trabajo futuro (propuesta, sin compromiso)**

1. Incorporar el extracto del worker, sanitizado y con hash, y reclasificar solo lo verificable.
2. Completar las rutas no probadas de los siete agentes y repetir la prueba dental con el prompt actual.
3. Validar de oído las voces y decidir el criterio para cambiar el estado visible de cada agente.
4. Resolver la aprobación del docente, la verificación de la marca y el permiso de reutilización.
5. Medir latencia con un protocolo definido.
6. Si hubiera interés comercial, abordar integraciones reales como un proyecto distinto.

## 12. Referencias de evidencia

- Repositorio técnico: `docs/validation/E2E-2026-11-20-voxentra-clinica-dental/`, `docs/validation/E2E-2026-11-20-voxentra-siete-agentes/`, `docs/validation/ETAPA-10B-siete-agentes-2026-11-20.md` y `docs/validation/ETAPA-8-voxentra-frontend-2026-11-19/` (las dos primeras, sin seguimiento a la fecha).
- Repositorio académico: `Fase 3/Entregables/`, `Fase 3/07_Evidencias/`, `Fase 3/08_Contribuciones/MATRIZ_CONTRIBUCIONES.md` y `Fase 3/10_Consolidacion_Defensa/`.
- Fuera de Git: paquete `VOXENTRA_evidencias_E2E_20nov.zip` y video de la sesión (solo hashes; el video no es publicable).
