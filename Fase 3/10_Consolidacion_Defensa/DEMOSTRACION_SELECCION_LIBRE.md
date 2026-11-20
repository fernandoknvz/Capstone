# Demostración en vivo con selección libre (máximo 2:30)

**Estado:** PROPUESTA para ensayo. Corresponde a la diapositiva 7 (responsable: Juan; apoyo y reloj: Fernando). Las frases sugeridas se basan en las conversaciones reales del 20-nov (video) y en la matriz de la Etapa 10B. **Cada agente tiene una sola sesión previa y cubre solo parte de los criterios**: no hay garantía de que responda igual.

## 1. Reglas

1. La comisión elige **cualquiera de los siete agentes**.
2. **Máximo 2:30.** Fernando marca con una señal a los 2:00 y corta a los 2:30.
3. Hablar en **frases cortas y completas, sin pausas largas a mitad de frase** (en reclutamiento el agente tomó el turno mientras el usuario hablaba; la causa no está determinada).
4. **Solo datos ficticios.** Nunca nombres, claves ni números reales.
5. No hablar de latencia como logro. Si la comisión pregunta: mediana de 2,85 s en la sesión dental, objetivo de 1 s no cumplido.
6. No proyectar el video original. El respaldo son las capturas derivadas.

## 2. Procedimiento de selección

1. **(0:00 a 0:20)** Mostrar el catálogo. Juan lee los siete nombres y dice: «La clínica dental tiene una sesión documentada; de los otros seis tenemos evidencia preliminar de una conversación cada uno, sin aprobación integral. Los datos son ficticios. ¿Cuál quieren probar?».
2. La comisión elige. Juan hace clic en **Llamar** y autoriza el micrófono (ya autorizado en el ensayo previo).
3. Ofrecer: «Si prefieren, nos dictan qué decirle al agente». Si la comisión quiere hablar directamente con el agente, se le cede el micrófono por **un solo intercambio** (riesgo de ruido y de pausas).

## 3. Línea de tiempo

| Tiempo | Qué ocurre |
|---|---|
| 0:00 – 0:20 | Selección y clic en «Llamar» |
| 0:20 – 0:35 | Saludo del agente (saludo configurado, por voz) |
| 0:35 – 1:05 | **Pregunta inicial** (de la tabla) y respuesta |
| 1:05 – 1:50 | **Pregunta de seguimiento** y respuesta (cada respuesta puede tardar de 2,5 a 5 s) |
| 1:50 – 2:15 | **Cierre** y resumen del agente |
| 2:15 – 2:30 | «Finalizar conversación» y una frase de límites: «Todo fue simulado; no hay integración con sistemas reales» |

## 4. Guion por agente

Todas las capturas están en `alloxentric-real-time-agent/docs/validation/E2E-2026-11-20-voxentra-siete-agentes/` (la dental, en su propia carpeta). La columna «Probado en la sesión del 20-nov» indica lo que sí se observó; **todo lo demás está pendiente** y se debe decir si la comisión lo pregunta.

| Agente | Pregunta inicial | Seguimiento | Cierre | Probado en la sesión del 20-nov | Pendiente (no sugerir en vivo) | Captura de respaldo |
|---|---|---|---|---|---|---|
| Ventas de telefonía (MóvilAndes) | «Hola, sí, tengo un minuto.» | «Uso unos 30 GB al mes.» | «No, gracias, prefiero quedarme con mi plan. Que tenga buen día.» | Saludo; datos y compañía; plan Libre 50; aceptación del rechazo; cierre «sin gestión simulada» | Objeción de precio o permanencia; cobertura; pedir contratar; entregar RUT o tarjeta | `capturas/01_ventas_movil_andes_derivada.png` y `capturas_video/S1-ventas_cierre_108s.png` |
| Cobranza retail (Casa Aurora) | «Hola, no, soy otra persona.» | «No conozco a esa persona, no vive aquí.» | (El agente se disculpa y cierra; decir «Gracias».) | Ruta del **tercero**: no revela la deuda; cierra por número equivocado (33 s) | Ruta del **titular**; disputar el monto; opciones de pago; datos bancarios | `capturas/02_cobranza_retail_casa_aurora_derivada.png` y `capturas_video/S2-cobranza-retail_cierre_156s.png` |
| Cobranza financiera (Costanera) | «Sí, soy el titular; dígame.» | «¿Qué opciones de pago tengo?» | «Voy a pensarlo. ¿Me puede llamar otro día?» y luego una hora ficticia | Verificación del titular; deuda y CAE; abono de 300.000 y 6 a 10 cuotas; llamada simulada «sin carácter vinculante» | Disputar el aumento activamente; acuerdo legal; datos bancarios | `capturas/03_cobranza_financiera_costanera_derivada.png` y `capturas_video/S3-cobranza-financiera_cierre_291s.png` |
| Soporte de internet (FibraSur) | «Mi router no enciende.» | «Sigue apagado.» y luego «Necesito que me lo cambien.» | «Muchas gracias.» | Pasos de diagnóstico (luz, cable, otro enchufe); «no puedo confirmar un cambio real»; descuento sin información; cierre | Preguntar por un modelo; el reinicio; exigir una visita real | `capturas/04_soporte_fibrasur_derivada.png` y `capturas_video/S4-soporte_cierre_428s.png` |
| Entrevista laboral (Talento Cordillera) | «Sí, comencemos.» | «Trabajé cinco años en atención al cliente.» (luego responder el caso STAR en dos frases) | «Tengo toda la disponibilidad. Mi expectativa de renta es de un millón y medio.» | Experiencia; STAR; metas; disponibilidad; renta («sin confirmar rangos»); cierre con fortalezas y mejora | Ofrecer datos sensibles (RUT, salud); preguntar un salario no informado; pedir una decisión | `capturas/05_reclutamiento_talento_cordillera_derivada.png` y `capturas_video/S5-reclutamiento_cierre_638s.png` |
| Atención postventa (Tienda Brújula) | «Tengo un cargo que no reconozco.» | Dar un nombre y una clave de cuatro dígitos **inventados** | «Sí, bloquéenla. No necesito reemplazo, gracias.» | Verificación simulada; cargo de 189.990; bloqueo simulado con folio ficticio; cierre «nada quedó realizado real» | Consultar el cupo; exigir devolución o garantía real | `capturas/06_postventa_tienda_brujula_derivada.png` y `capturas_video/S6-postventa_cierre_770s.png` |
| Clínica dental (Sonrisa Norte) | «Quisiera agendar una hora para una evaluación.» | «Prefiero en la mañana.» | «El viernes a las 11 está bien. Gracias, eso es todo.» | Sesión del 20-nov (09:13), **anterior al PR #22**: agendamiento simulado, evaluación inicial gratis | Dirección y teléfono (**I-01**: el agente inventó ambos); aclaración de la simulación (**I-03**) | Cinco capturas de `E2E-2026-11-20-voxentra-clinica-dental/capturas/` |

**Sobre la clínica dental:** no sugerir preguntar por la dirección o el teléfono (el incidente I-01 sigue abierto y no se repitió la prueba tras el PR #22). Si la comisión pregunta, mostrar la captura 04, **nombrar el incidente** y no improvisar justificaciones. No es ocultar un problema: la diapositiva 10 ya lo declara.

## 5. Contingencia

| Fallo | Señal | Acción inmediata | Respaldo |
|---|---|---|---|
| El sitio no carga | Página en blanco o error | Recargar una vez; pasar al segundo equipo o celular | Captura del agente elegido |
| Acceso rechazado | «Código de acceso incorrecto» | Reingresar el código; si falla, pasar a las capturas | Capturas |
| No conecta con el agente | Más de **15 s** en «Conectando» o mensaje de error | Cerrar y reintentar **una vez** con la clínica | Capturas |
| Sin audio de salida | La transcripción avanza sin sonido | Revisar salida y volumen (10 s) | Leer la transcripción en pantalla |
| Micrófono bloqueado | El navegador pide permiso o no escucha | Autorizar; elegir el dispositivo | Dictar y mostrar capturas |
| Latencia alta | Más de **5 s** por respuesta | Decirlo: limitación conocida; seguir o pasar a capturas | Capturas |
| El agente interrumpe o se pisa | Corta al presentador | Esperar y repetir en una frase corta; nombrarlo como limitación observada | Capturas |
| Responde fuera de guion o inventa un dato | Dato no definido | Nombrarlo (I-01 es una limitación registrada); no repetir la prueba | Capturas |
| Falla un proveedor (cuota, clave) | Error del worker | No insistir | Capturas y métricas |
| Cae la red | Sin conexión | Pasar a las capturas y a la narrativa | PDF local con las capturas |

**Cómo usar el respaldo:** abrir la captura del agente elegido y decir: «Esta es una sesión real del 20 de noviembre. La captura muestra la transcripción; no prueba el audio ni la latencia. Las operaciones son simuladas». Las capturas están cortadas a la derecha; avisarlo si preguntan.

**Qué no usar nunca:** el video original (muestra el escritorio completo, notificaciones de terceros y la URL del sitio) ni las capturas 05 y 06 de la Etapa 8 (conversaciones simuladas con HTTP).

## 6. Ensayo previo (recomendado)

1. Una hora antes: abrir el sitio autenticado y probar el micrófono con **una sola frase** al agente de la clínica (requiere autorización de llamadas con proveedores).
2. Idealmente (con autorización): una prueba corta con cada uno de los siete agentes, con la tabla de §4, y anotar cuáles responden bien, cuáles interrumpen y cuánto tardan.
3. Copiar a una carpeta local las capturas de la tabla y abrirlas una vez sin conexión.
4. Cronometrar la demostración completa: debe caber en 2:30.
