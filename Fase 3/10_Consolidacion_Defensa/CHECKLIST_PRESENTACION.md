# Checklist de presentación y plan de contingencia (21-nov-2026)

**Estado:** PROPUESTA. Marque cada punto con fecha y responsable. Los puntos con (⚠) requieren autorización o una decisión del equipo antes de ejecutarlos.

> **Referencias (Etapa 10E):** contenido de las diapositivas en `PRESENTACION_FINAL_12_DIAPOSITIVAS.md`; demostración y contingencia en `DEMOSTRACION_SELECCION_LIBRE.md`; estado y riesgos en `CIERRE_FASE3_VERIFICACION.md`. Pendiente del usuario: ubicación del extracto `Texto pegado(10).txt`.

## 1. Antes de la defensa (hoy, 20-nov)

### Académico
- [ ] (⚠) Consultar al docente guía: reorientación a VOXENTRA, formato de la demostración con selección libre y si debe incorporarse algún ajuste del informe final.
- [ ] Conseguir la retroalimentación del informe final (Fase 2) y revisar qué ajustes pide la guía 3.3.
- [ ] Obtener la rúbrica de Fase 3 si existe.
- [ ] Confirmar hora, sala o enlace, y quiénes integran la comisión.
- [ ] Revisión cruzada de `ANEXO_EVOLUCION_VOXENTRA.md` por los tres integrantes.
- [ ] David: documentar sus actividades de Fase 3 con respaldo, para poder mencionarlas.
- [ ] Cada integrante: leer todo el material (la nota es individual) y ensayar las preguntas de `PREGUNTAS_DEFENSA.md`.
- [ ] Cada integrante: validar y reescribir su diario individual (3.1) en sus propias palabras; resolver las marcas pendientes.

### Evidencia
- [ ] Archivar el registro del worker del 20-nov, sanitizado (sin identificadores de sala, participante ni worker) y con su hash.
- [ ] Copiar la evidencia E2E del 20-nov al repositorio académico (hoy solo está en el técnico, sin seguimiento).
- [ ] Tener a mano las capturas del 20-nov (cinco), la tabla de métricas y los resultados de pytest (231) y vitest (94).
- [ ] Verificar que ningún material proyectado contenga identificadores de sesión, direcciones IP, URL personales o claves.

### Demostración
- [ ] (⚠) Repetir una prueba corta con voz de los siete agentes antes de la defensa (requiere autorización explícita de llamadas con proveedores), cubriendo las rutas no probadas: objeción y cobertura (ventas), titular (cobranza retail), datos bancarios, cupo y datos sensibles. Anotar cuáles responden bien y cuáles interrumpen.
- [ ] Ensayo con el sitio publicado: acceso, selección de agente, micrófono, audio de salida y cierre.
- [ ] Verificar cuotas y claves vigentes de Google, ElevenLabs, DeepSeek y LiveKit.
- [ ] Confirmar qué worker atiende la demostración (publicado, no un worker de desarrollo) y que está encendido.
- [ ] Confirmar el código de acceso temporal y que la sesión no expira durante la defensa.
- [ ] Decidir qué hacer con I-01 e I-03: probar los prompts actuales o declararlos como limitación (no cambiar código sin autorización).
- [ ] **Plan alternativo con capturas reales:** copiar a una carpeta local de la defensa las capturas derivadas de `docs/validation/E2E-2026-11-20-voxentra-siete-agentes/` (`capturas/` y `capturas_video/`) y de `E2E-2026-11-20-voxentra-clinica-dental/capturas/`; abrirlas una vez para confirmar que cargan sin conexión (tabla en `ESTRUCTURA_PRESENTACION.md`).
- [ ] **No llevar ni proyectar el video original** (muestra el escritorio, notificaciones de terceros y la URL del sitio).
- [ ] Obtener el log completo del worker del 20-nov (el extracto que cita el paquete no se recibió).
- [ ] Una persona del equipo debe escuchar el video y anotar su valoración de las voces.
- [ ] Decidir si se menciona la insignia de la interfaz («sin prueba real documentada») frente a la evidencia preliminar.

## 2. Una hora antes

- [ ] Cargar el sitio en una pestaña **ya autenticada** y dejar el catálogo visible.
- [ ] Probar el micrófono y el volumen con una sola frase al agente de la clínica (autorizada).
- [ ] Cerrar notificaciones, mensajería y pestañas con datos personales; usar un perfil de navegador limpio (sin favoritos ni avatar personal).
- [ ] Tener las diapositivas, el PDF de respaldo y las capturas en una carpeta local, sin depender de la red.
- [ ] Cargar la batería o conectar el equipo; segundo equipo o celular con el sitio listo, si es posible.
- [ ] Cronómetro visible para el equipo (14:30 de exposición, aviso a los 12:50).
- [ ] Repartir roles: quien habla, quien opera la demo, quien lleva el reloj.

## 3. Durante la defensa

- [ ] Decir al inicio: VOXENTRA es un nombre provisional de la demostración.
- [ ] Decir antes de la demo: la clínica tiene una sesión documentada y los otros seis agentes, evidencia preliminar sin aprobación integral; los datos son ficticios y las respuestas pueden tardar de 2,5 a 5 segundos.
- [ ] No prometer ni afirmar: latencia de 1 s cumplida, siete agentes probados, reservas o mensajes reales, aprobación del cliente o del docente, audio grabado.
- [ ] Citar las métricas como «medidas por el worker y transcritas por el equipo».
- [ ] Si una pregunta no tiene respuesta documentada, decirlo.

## 4. Plan de contingencia

| Fallo | Señal | Acción inmediata | Respaldo |
|---|---|---|---|
| El sitio no carga | Página en blanco o error | Recargar una vez; probar el segundo equipo o el celular | Mostrar capturas del catálogo y de la sesión del 20-nov |
| Acceso rechazado | «Código de acceso incorrecto» | Reingresar el código; verificar que el servicio esté activo | Capturas |
| El agente no responde o no conecta | Más de 20 s en «Conectando» o mensaje de error | Cerrar y reintentar una vez con la clínica | Explicar el límite y mostrar la sesión documentada |
| Sin audio de salida | Transcripción sin sonido | Revisar el dispositivo de salida y el volumen | Leer la transcripción en pantalla |
| Micrófono bloqueado | El navegador pide permiso o no escucha | Autorizar el micrófono; elegir el dispositivo correcto | Dictar el flujo mostrando las capturas |
| Latencia excesiva | Más de 5 s por respuesta | Decirlo: es una limitación conocida (mediana de 2,85 s, objetivo de 1 s no cumplido) | Continuar o pasar a capturas |
| El agente responde fuera de guion o inventa un dato | Dato no definido (ver I-01) | Nombrarlo como limitación registrada y no repetir la prueba | Capturas |
| Agente elegido falla o se interrumpe | Respuesta incoherente, corte al usuario o silencio | Decir que cada agente tiene una sola sesión previa; proponer la clínica | Captura derivada del agente elegido (ver tabla del plan alternativo) |
| Caída de red | Sin conexión | Pasar a las capturas y a la narrativa | PDF local |
| Fallo de un proveedor (cuota, clave) | Error del worker | No insistir; seguir con el material estático | Capturas y métricas |

**Respaldo audiovisual:** hoy **no existe ninguna grabación de audio** de ninguna sesión. Si el equipo quiere un respaldo con voz, debe grabar una pantalla con audio de una sesión de ensayo (con datos ficticios y con el consentimiento de quienes hablen). Esa grabación sería una **evidencia nueva** y no debe presentarse como la sesión del 20-nov.

## 5. Material a llevar

- [ ] Diapositivas (PDF y archivo editable).
- [ ] Capturas derivadas del 20-nov (dental: cinco; seis agentes: una captura y un cierre por agente), de la Etapa 8 (catálogo) y del E2E del 17-nov, recortadas y con hash.
- [ ] Hoja de métricas: dental (mediana 2,850 s; promedio 2,989 s) y cuatro agentes con datos parciales (medianas de 3,11 a 3,98 s; sin promedio combinado); objetivo de 1 s no cumplido ni demostrado.
- [ ] Resultado de pytest (231) y vitest (94).
- [ ] Diagrama de arquitectura (D01).
- [ ] Matriz de contribuciones.
- [ ] Anexo de evolución y lista de aprobaciones pendientes.
- [ ] Informe v1.2 y entregables D01 a D06 (con la advertencia de que citan cifras previas).
- [ ] Respuestas de `PREGUNTAS_DEFENSA.md` (una hoja por integrante).

## 6. Después de la defensa

- [ ] Registrar la retroalimentación de la comisión.
- [ ] Archivar la evidencia faltante y actualizar los entregables si corresponde.
- [ ] Decidir el cierre de los pendientes del anexo.
