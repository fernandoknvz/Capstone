# Guion de defensa (21-nov-2026)

**Estado:** PROPUESTA. Es un borrador para que cada integrante lo reescriba con sus propias palabras; no es un texto para leer. Tiempos según `ESTRUCTURA_PRESENTACION.md` (exposición 14:30, preguntas 5:30, total 20:00 incluyendo preguntas).

## Reglas comunes

1. **Cada uno responde por todo el proyecto.** La nota es individual; las preguntas pueden ir a cualquiera, sin importar quién presentó la diapositiva.
2. **Decir siempre el nivel de certeza.** Para las métricas del 20-nov: «medidas por el worker y transcritas por el equipo; el registro original aún no está archivado».
3. **Declarar los límites antes de que los pregunten:** objetivo de 1 s no cumplido; seis agentes con evidencia preliminar pero sin aprobación integral; log del worker no archivado; operaciones simuladas.
4. **Nombres:** el proyecto se llama *Alloxentric Real Time Agent*; *VOXENTRA* es el nombre provisional de la demostración, no una empresa.
5. **Nunca decir:** que el cliente o el docente aprobaron la reorientación; que el cliente incumplió reuniones; que los siete agentes están probados; que el objetivo de latencia se cumplió; que hay audio grabado; que existen reservas, mensajes, pagos o visitas reales.
6. **Si no se sabe:** «No tenemos ese dato documentado; lo que sí está documentado es…». No improvisar cifras ni atribuciones.
7. Quien sostiene el reloj: Fernando (aviso al minuto 12:50 para cerrar).

---

## Guion de Fernando — 5:30 (diapositivas 1, 2, 3, 4, 11 y 12)

**Diapositiva 1 — Portada (0:20)**
«Buenas tardes. Somos Fernando, David y Juan, y presentamos el Proyecto APT *Alloxentric Real Time Agent*, que en esta fase mostramos como una demostración que llamamos VOXENTRA. Aclaro desde ya que VOXENTRA es un nombre provisional de la demostración, no una empresa.»

**Diapositiva 2 — Problema y objetivo original (1:00)**
«El proyecto nació de un problema planteado por Alloxentric: su plataforma de bots de voz, hecha para gran escala, tiene poca elasticidad de costos cuando baja el volumen de llamadas. Según nuestro informe de Fase 1, nos pidieron explorar una alternativa: un prototipo de bot de cobranza por voz con LiveKit, transcripción, ElevenLabs y telefonía Asterisk, que comparara costo y efectividad y respondiera en menos de un segundo. Dejo claro que la transcripción de esa reunión no está archivada en nuestro expediente; lo presentamos como lo reportó el equipo en Fase 1.»

**Diapositiva 3 — Evolución y decisión (1:10)**
«Construimos un pipeline de voz funcional con proveedores intercambiables, una demo web y pruebas automáticas. No logramos la telefonía Asterisk, el guion oficial de cobranza ni la comparación de costos. Nuestro expediente tampoco tiene actas ni aprobaciones formales de las decisiones atribuidas al cliente. Con ese contexto, el equipo propuso continuar el MVP de forma autónoma y presentarlo como una demostración de agentes de voz para pymes. **Esa reorientación es una decisión del equipo; no tenemos aprobación del cliente y la aprobación académica está pendiente.** [Ajustar con el docente antes de la defensa.]»

**Diapositiva 4 — Arquitectura (1:20)**
«La arquitectura se conservó. En LiveKit corre un worker en Python: Google Chirp 3 transcribe, un modelo de lenguaje, Gemini o DeepSeek según configuración, genera la respuesta, y ElevenLabs la sintetiza. El navegador solo envía el identificador del agente; el servidor emite el token y fija el despacho, el prompt nunca viaja al cliente. La política de seguridad del sitio no usa permisos amplios para scripts en línea y la aplicación no graba audio. En la sesión que mostraremos se informó DeepSeek como modelo.»

**Diapositiva 11 — Gestión y contribuciones (0:50)**
«Atribuimos contribuciones solo con commits y pull requests verificables; un merge no cuenta como autoría. Usamos una adaptación parcial de Scrum, y la herramienta de gestión del cliente, CoreStream, solo nos entrega un reporte agregado sin tickets. Una revisión cruzada de nuestros entregables quedó pendiente: el PR documental se fusionó sin revisiones registradas y lo reconocemos.»

**Diapositiva 12 — Conclusiones y trabajo futuro (0:50)**
«Hoy tenemos un MVP técnicamente funcional y demostrable, con 231 pruebas de Python y 94 del frontend aprobadas. Su brecha principal es la latencia: no alcanzamos el segundo. Como trabajo futuro: archivar el registro de la sesión, probar uno a uno los otros seis agentes, validar las voces y resolver la aprobación de la reorientación. Gracias; quedamos atentos a sus preguntas.»

**Apoyo en la demo (diap. 7):** operar el reloj y el respaldo (capturas), sin hablar de latencia como logro.

---

## Guion de Juan — 4:50 (diapositivas 5, 6 y 7)

**Diapositiva 5 — Frontend y siete agentes (1:20)**
«Mantuvimos la navegación de la demo y cambiamos solo lo visible: nombre provisional VOXENTRA, identidad Red Edition con fondo oscuro y acentos rojos, y un aviso permanente que dice que son datos ficticios y que no hay operaciones reales ni integración con sistemas de empresas. Detrás hay siete agentes, cada uno con su empresa ficticia, su guion, su saludo y su voz. El navegador envía solo el identificador y el servidor lo valida. Por compatibilidad no cambiamos los identificadores internos, aunque algunos conservan nombres históricos que el usuario no ve.»

**Diapositiva 6 — Escenarios y alcance (1:00)**
«Reemplazamos las marcas reales por empresas ficticias: por ejemplo MóvilAndes, Casa Aurora, Financiera Costanera, FibraSur, Talento Cordillera y Tienda Brújula, además de la Clínica Dental Sonrisa Norte. Cada tarjeta muestra su estado: la clínica dental tiene una prueba real documentada. De los otros seis tenemos evidencia preliminar de una conversación por agente, grabada el 20 de noviembre, pero **sin aprobación integral**: cada sesión cubre solo parte de lo que queríamos probar, y la insignia de la pantalla todavía dice que no tienen prueba documentada. Todo lo que ocurre dentro de la conversación (agendar, enviar un mensaje, cobrar, abrir un reclamo) es simulado.»

**Diapositiva 7 — Demostración (2:30)**
«Les propongo que ustedes elijan un agente. Antes de empezar quiero decir tres cosas: la clínica tiene una sesión documentada y los otros agentes, evidencia preliminar de una conversación cada uno; las respuestas pueden tardar entre dos y cuatro segundos; y los datos son ficticios. [Pausa: la comisión elige.] [Conversar 60 a 90 segundos con el flujo: saludo, consulta, una pregunta inesperada, un pedido fuera de alcance, cierre.] Si algo falla, lo decimos y mostramos las capturas de la sesión documentada.»

Si la conversación falla: «Esto es parte de lo que reportamos como limitación; les mostramos una sesión real del 20 de noviembre con captura de pantalla, que no prueba el audio». [Abrir la captura del agente elegido según `ESTRUCTURA_PRESENTACION.md`.]

**Datos de apoyo de Juan (para preguntas):** su trabajo verificable incluye la integración de Chirp 3, personas y voces, el rediseño de la interfaz, el historial local y el PR #18, que **sigue abierto y no está integrado**.

---

## Guion de David — 4:10 (diapositivas 8, 9 y 10)

**Diapositiva 8 — Pruebas y CI (1:10)**
«Las pruebas automáticas corren sin red ni credenciales: 231 pruebas de Python y 94 del frontend están aprobadas; las ejecutamos de nuevo el 20 de noviembre. Incluyen que los siete agentes existan con los mismos identificadores en Python y TypeScript, que los guiones no mencionen marcas reales ni nombres de personas del equipo y que cada agente se declare ficticio. Hay también integración continua en GitHub Actions. **Estas pruebas no miden la calidad de la voz ni la conducta del modelo.** Mi aporte técnico documentado es la integración de ElevenLabs y sus pruebas.»

**Diapositiva 9 — Sesión E2E y latencia (1:30)**
«Documentamos una sesión real con la clínica dental el 20 de noviembre: 2 minutos 15 segundos y 8 turnos. La latencia de extremo a extremo tuvo una mediana de 2,850 segundos y un promedio de 2,989; el mínimo fue 2,61 y el máximo 4,14. De los otros agentes tenemos métricas parciales de cuatro: medianas de 3,1 a 4,0 segundos, con un valor máximo de 8,9; no las promediamos porque son extractos parciales de una sola sesión por agente. **El objetivo de 1 segundo no se cumplió y no está demostrado en ninguna sesión.** Estas métricas las transcribió el equipo desde el registro del worker; el archivo original no está archivado todavía. Los registros también señalan bloqueos breves del bucle de eventos, un error de decodificación de audio y, en reclutamiento, una vez que el agente interrumpió al usuario; no determinamos la causa.»

**Diapositiva 10 — Limitaciones y riesgos (1:30)**
«Lo que falta, claramente: los otros seis agentes tienen evidencia preliminar, no aprobación integral; no hemos escuchado ni validado las voces; falta archivar el registro del worker; no hay telefonía ni guion oficial de cobranza ni comparación de costos. En la sesión dental el agente dio una dirección y un teléfono que no estaban en su configuración, y afirmó una reserva antes de aclarar que era simulada. Esa sesión fue anterior a los prompts reforzados del 20 de noviembre y no la repetimos, así que **no podemos decir que esos incidentes estén corregidos**. En las otras seis sesiones los agentes sí aclararon la simulación, pero eso no prueba lo mismo para la clínica. También quedan pendientes la aprobación de la reorientación y la verificación del nombre VOXENTRA.»

**Para completar [PENDIENTE]:** David debe agregar y documentar lo que hizo en Fase 3 (hoy no hay actividad suya atribuida en los documentos); sin respaldo no debe mencionarlo.

---

## Cierre y preguntas (5:30)

- Fernando agradece y abre las preguntas.
- Reparto de respuestas: arquitectura, decisiones, cliente y aprobaciones → Fernando; frontend, agentes y demostración → Juan; pruebas, métricas, riesgos y TTS → David. **Cualquiera puede completar.**
- Si una pregunta no se puede responder con evidencia, decir qué falta y cuándo se resolvería.

## Ensayo recomendado

Dos ensayos cronometrados: uno sin demo (para verificar los 14:30) y otro con la demo completa. Registrar quién se pasa de tiempo y recortar la diapositiva 12 primero.
