# Certificación de pruebas sobre `main` — 17 de noviembre de 2026

Estado: ejecución nueva, realizada en un equipo local del equipo; pendiente de revisión humana.

## Objeto probado

- Repositorio técnico `fernandoknvz/alloxentric-real-time-agent`, rama `origin/main`, commit `77ff85c3ad252b52df429380ea916cf84c1725a4` (merge del PR #20).
- Se exportó una copia limpia con `git archive origin/main` a una carpeta temporal. El repositorio técnico y su árbol de trabajo no se modificaron.
- No se usaron credenciales ni proveedores reales. No se ejecutaron E2E ni verificaciones manuales con proveedores.

## Entorno

| Elemento | Valor |
|---|---|
| Sistema | Windows 11 Pro |
| Python / uv | 3.12.6 / 0.12.23 (`uv sync --frozen`, `uv.lock`) |
| Node / pnpm | 24.15.0 / 9.15.9 (`pnpm install --frozen-lockfile`) |

## Resultados

| Verificación | Resultado |
|---|---|
| `uv run --frozen pytest` | **214 aprobadas**, 0 fallidas, 1 advertencia (DeprecationWarning de livekit-agents); 64,2 s |
| `vitest run` | **91 aprobadas** en 14 archivos, 0 fallidas |
| ESLint | 0 errores |
| `tsc --noEmit` | 0 errores |
| `next build` + `generate-csp-headers` | Correcto |
| `out/_headers` | 1 encabezado `Content-Security-Policy`; 0 apariciones de `unsafe-inline` o `unsafe-eval`; `script-src 'self' 'sha256-...'` presente |
| GitHub Actions sobre `main` (77ff85c) | `success`, run `42435613596`, 8-nov-2026 01:45 UTC (consulta con `gh run list`) |

### Pruebas Python por archivo (214)

| Archivo | Pruebas |
|---|---:|
| test_agent_name.py | 14 |
| test_config.py | 6 |
| test_latency_settings.py | 13 |
| test_llm.py | 9 |
| test_llm_gemini.py | 15 |
| test_metrics.py | 40 |
| test_personas.py | 26 |
| test_pipeline.py | 32 |
| test_project_bootstrap.py | 3 |
| test_stt.py | 14 |
| test_tts.py | 14 |
| test_voices.py | 28 |

### Pruebas web por archivo (91)

| Archivo | Pruebas |
|---|---:|
| client-secrets.test.ts | 1 |
| config.test.ts | 8 |
| conversation-panel.test.tsx | 15 |
| csp-headers.test.ts | 5 |
| history.test.ts | 8 |
| livekit-token.test.ts | 4 |
| login.test.ts | 8 |
| netlify-runtime.test.ts | 4 |
| origin.test.ts | 4 |
| personas.test.ts | 17 |
| session.test.ts | 4 |
| vercel-postbuild.test.ts | 5 |
| voice-controls.test.tsx | 2 |
| voice-session.test.tsx | 6 |

## Incidencia de entorno (honestidad de la ejecución)

La primera ejecución de Vitest falló al arrancar con `ERR_PACKAGE_IMPORT_NOT_DEFINED` (`#module-evaluator`), con Node 22.20.0 (el proyecto exige 24.x) y, después, también con Node 24.15.0 usando el layout de enlaces simbólicos por defecto de pnpm en este equipo Windows. Con Node 24.15.0 y `pnpm install --frozen-lockfile --config.node-linker=hoisted` las 91 pruebas pasaron. ESLint, `tsc` y el build pasaron en todas las configuraciones. La causa es probablemente del entorno local (INFERENCIA); el CI en Ubuntu con el layout por defecto concluyó en verde.

## Comparación con resultados históricos

| Corte | Python | Web | Naturaleza |
|---|---:|---:|---|
| PR #16 (30-oct) | 200 | 91 | Histórico, ejecutado por el autor del PR |
| PR #17 (31-oct) | 214 | — | Histórico declarado en el PR |
| PR #18 (4-nov, **abierto**) | 281 | 103 | Rama no integrada; no comparable |
| `main` 77ff85c (17-nov) | **214** | **91** | **Nueva ejecución** |

Limitaciones: ejecución en un solo equipo; no reemplaza una ejecución independiente de otro integrante; no valida rendimiento ni calidad de voz.
