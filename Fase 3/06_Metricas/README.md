# Métricas - versión de trabajo

## E01, 30-oct-2026

- Cinco sesiones y 22 turnos del agente.
- Trece turnos contienen `e2e_latency_s`.
- Mediana histórica documentada: 2,59 s.
- Mínimo: 0,48 s, correspondiente a un turno interrumpido.
- Máximo: 4,08 s.
- Tres turnos superan 3 s.

## E2E, 31-oct-2026

- Una sesión de clínica dental.
- Siete turnos del agente; cinco con E2E disponible.
- Media E2E: 2,33 s.
- Mediana E2E: 2,74 s.
- Rango: 1,19-3,35 s.
- P95 estimado: 3,24 s, sin robustez estadística por `n=5`.

## Interpretación

Las etapas se solapan y no deben sumarse. `e2e_latency_s` es la referencia. Ninguna de estas muestras demuestra el cumplimiento del objetivo de un segundo.
