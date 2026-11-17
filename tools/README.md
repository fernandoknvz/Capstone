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
| `verify_docs.py` | Verifica integridad, numeración, figuras, secretos y texto obsoleto de los DOCX (solo lectura). |
| `build_fase3_documents.py` | Generador de los resúmenes de referencia de Codex (borradores resumidos; su salida no es un entregable). |

Los diagramas (`Fase 3/03_Diseno/diagramas/`) y las capturas (`Fase 3/07_Evidencias/capturas-web-demo-2026-11-17/`) se incluyen ya generados; los scripts que los produjeron dependían de un entorno temporal y no forman parte del repositorio.
