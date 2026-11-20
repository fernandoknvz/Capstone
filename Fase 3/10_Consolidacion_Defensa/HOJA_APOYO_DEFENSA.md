# Hoja de apoyo para la defensa — 21-nov-2026

**Estado:** PROPUESTA operativa. Resume el material consolidado; no reemplaza el guion ni las evidencias.

## Secuencia y reloj

| N.º | Tema | Responsable | Tiempo | Acumulado | Mensaje que debe quedar |
|---|---|---:|---:|---:|---|
| 1 | Portada y equipo | Fernando | 0:20 | 0:20 | VOXENTRA es la identidad provisional de una demostración académica. |
| 2 | Problema y objetivo original | Fernando | 1:00 | 1:20 | El objetivo original incluía voz en tiempo real y una respuesta de 1 s. |
| 3 | Evolución del proyecto | Fernando | 1:10 | 2:30 | La reorientación es una decisión del equipo; la aprobación académica está pendiente. |
| 4 | Arquitectura | Fernando | 1:20 | 3:50 | Se conserva el flujo navegador → LiveKit → worker STT/LLM/TTS. |
| 5 | Frontend y siete agentes | Juan | 1:20 | 5:10 | Red Edition cambia presentación, no arquitectura ni comportamiento. |
| 6 | Escenarios y alcance | Juan | 1:00 | 6:10 | Los escenarios y operaciones son ficticios y simulados. |
| 7 | Demostración | Juan; Fernando apoya | 2:30 | 8:40 | Solo la clínica tiene sesión documentada; los otros seis tienen evidencia preliminar. |
| 8 | Pruebas y CI | David | 1:10 | 9:50 | 231 pruebas Python y 94 frontend aprobadas; no certifican calidad conversacional E2E. |
| 9 | Resultado E2E y latencia | David | 1:30 | 11:20 | Medianas reportadas de 2,85 a 3,98 s; máximo 8,90 s; meta de 1 s no cumplida. |
| 10 | Limitaciones y riesgos | David | 1:30 | 12:50 | Hay incidencias abiertas, voces no validadas y falta el log original. |
| 11 | Gestión y contribuciones | Fernando | 0:50 | 13:40 | La autoría se respalda con commits y PR; Scrum fue parcial. |
| 12 | Conclusiones y futuro | Fernando | 0:50 | 14:30 | MVP demostrable, no producto listo para producción. |

**Señales de reloj:** aviso discreto a 12:50; si hay atraso, abreviar las diapositivas 11 y 12, sin reducir el tiempo de preguntas.

## Respuestas críticas

| Pregunta | Respuesta breve respaldada |
|---|---|
| ¿Los siete agentes están aprobados? | **No.** [CONFIRMADO] Hay siete configurados. La clínica tiene una sesión documentada; los otros seis tienen evidencia preliminar de una conversación por agente, sin aprobación integral. |
| ¿Se cumplió la latencia de 1 s? | **No.** [REPORTADO] La sesión dental tuvo mediana 2,850 s; otros cuatro agentes, medianas de 3,11 a 3,98 s; máximo 8,90 s. |
| ¿Las operaciones son reales? | **No.** [CONFIRMADO] No hay reservas, pagos, bloqueos, visitas ni mensajería reales. |
| ¿VOXENTRA es una empresa o marca aprobada? | **No.** [CONFIRMADO] Es un nombre provisional. [PENDIENTE] disponibilidad de marca y aprobación académica. |
| ¿La Red Edition cambió el sistema? | **No.** [CONFIRMADO] Solo cambia la presentación visual; la arquitectura y los controles se conservan. |
| ¿Qué prueban los tests? | [CONFIRMADO] Estructura, compatibilidad y frontend. No prueban por sí solos la voz, la latencia ni la calidad E2E. |
| ¿Por qué el agente dental inventó contacto? | [CONFIRMADO] El modelo generó dirección y teléfono no presentes en su configuración. La sesión no se repitió tras reforzar el prompt. |
| ¿Está listo para una pyme? | **No.** [CONFIRMADO] Es una demostración académica sin integraciones operacionales ni telefonía. |

## Frases obligatorias antes de la demo

1. «Los datos y las empresas son ficticios; todas las operaciones son simuladas».
2. «La clínica dental tiene una sesión documentada; los otros seis agentes tienen evidencia preliminar, sin aprobación integral».
3. «La latencia observada está por encima del objetivo de un segundo».

## No afirmar

- Que los siete agentes están aprobados o certificados E2E.
- Que el cliente o el docente aprobaron la reorientación.
- Que la latencia de 1 s se cumplió.
- Que existen operaciones, grabaciones de audio o integraciones reales.
- Que las métricas fueron verificadas contra el log original; siguen reportadas por el equipo.

## Respaldo inmediato

- Presentación editable y PDF local.
- Capturas sanitizadas y sus hashes; no proyectar el video original.
- Diagrama D01, matrices, métricas y resultados de pruebas.
- Si falla la demo: un reintento; luego mostrar capturas y declarar la limitación.

