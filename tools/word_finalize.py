"""Actualiza el índice/campos con Word (COM), guarda el DOCX y exporta un PDF de revisión.

Uso: py word_finalize.py <docx> <carpeta_pdf>
Requiere Microsoft Word instalado. El PDF es solo para revisión visual.
"""
import sys
from pathlib import Path

import win32com.client


def finalize(docx: Path, pdf_dir: Path) -> int:
    pdf_dir.mkdir(parents=True, exist_ok=True)
    word = win32com.client.DispatchEx("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0
    try:
        doc = word.Documents.Open(str(docx.resolve()), ReadOnly=False, AddToRecentFiles=False)
        doc.Repaginate()
        for toc in doc.TablesOfContents:
            toc.Update()
        doc.Fields.Update()
        for sec in doc.Sections:
            for f in sec.Footers(1).Range.Fields:
                f.Update()
        doc.Repaginate()
        pages = doc.ComputeStatistics(2)
        doc.Save()
        pdf = pdf_dir / (docx.stem + ".pdf")
        doc.ExportAsFixedFormat(str(pdf.resolve()), 17)  # wdExportFormatPDF
        doc.Close(False)
        return pages
    finally:
        word.Quit()


if __name__ == "__main__":
    n = finalize(Path(sys.argv[1]), Path(sys.argv[2]))
    print("páginas:", n)
