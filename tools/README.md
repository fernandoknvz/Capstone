# Herramientas de generación documental (Fase 3)

Scripts que producen y verifican los entregables de `Fase 3/Entregables/` a partir de copias de los documentos originales de `Fase 2/Evidencias Proyecto/Evidencias Documentacion/` (los originales nunca se modifican).

## Requisitos

- Python 3.12 con `python-docx` (`py -m pip install python-docx`).
- Solo para `word_finalize.py`: Windows con Microsoft Word y `pywin32` (`py -m pip install pywin32`). Actualiza el índice, guarda el DOCX y exporta un PDF de revisión.

## Uso (desde esta carpeta)

| Script | Función |
|---|---|
| `build_d01.py` a `build_d06.py`, `build_informe.py` | Generan cada DOCX en `Fase 3/Entregables/`. Usan `fase3_common.py` (datos compartidos) y `fase3_docx_lib.py` (edición que conserva el formato). |
| `word_finalize.py <docx> <carpeta_pdf>` | Actualiza el índice con Word y exporta un PDF. |
| `build_etapa2.py [carpeta_pdf]` | Genera los entregables vigentes (19-nov): D01 v1.2, D02 v1.2, D03 v1.2, D04 v1.2, D05 v1.3, D06 v1.2 e Informe v1.2 (este último con `build_informe.py`, que desde la Etapa 2 produce la v1.2; la v1.1 se conserva como DOCX en `_historico`). Parte de las versiones anteriores en `Fase 3/Entregables/_historico/` mediante `build_d03_v12.py`, `build_d04_v12.py`, `build_d05_v13.py`, `build_d06_v12.py` y `fase3_v2.py`. Con `carpeta_pdf` actualiza índices con Word y exporta PDF de revisión. |
| `archive_dart25.py <docx>` | Archiva la versión sanitizada del informe DART-14-2.5 (texto sin cambios y captura recortada) en `Fase 3/07_Evidencias/DART-14-2.5_E2E-2026-10-19/`. |
| `verify_etapa2.py` | Verifica coherencia de los entregables vigentes: identidad de portada, versiones citadas, rutas de evidencia, estados de TC, CoreStream, hashes y secretos (solo lectura). |
| `visual_check.py <carpeta_pdf>` | Revisión automática de los PDF exportados con Word: páginas en blanco, texto o tablas fuera de margen, imágenes deformadas e índices frente a la página real (requiere PyMuPDF). |
| `build_d01_d02_v12.py` | D01 v1.2 y D02 v1.2 (solo portada y referencias cruzadas). |
| `build_diarios_fase3.py` | (Solo copia local; no publicado por contener los textos de los diarios.) Completa los tres diarios de reflexión individual de Fase 3 sobre la pauta oficial 3.1 (parte siempre de la copia oficial en `Pautas_Oficiales/`; escribe en `Fase 3/Evidencias Individuales/`). |
| `verify_diarios.py` | (Solo copia local; no publicado junto con los diarios.) Verifica los tres diarios: identificación, preguntas oficiales, marcas pendientes y solapamiento entre integrantes (solo lectura). |
| `verify_docs.py` | Verifica integridad, numeración, figuras, secretos y texto obsoleto de los DOCX (solo lectura). |
| `build_fase3_documents.py` | Generador de los resúmenes de referencia de Codex (borradores resumidos; su salida no es un entregable). |

Los diagramas (`Fase 3/03_Diseno/diagramas/`) y las capturas (`Fase 3/07_Evidencias/capturas-web-demo-2026-11-17/`) se incluyen ya generados; los scripts que los produjeron dependían de un entorno temporal y no forman parte del repositorio.
