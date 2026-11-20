"""Datos y utilidades compartidas por los constructores de la Etapa 2 (versiones 1.2 / 1.3, 19-nov-2026).

Los constructores de esta etapa parten del DOCX vigente inmediatamente anterior, conservado en
Fase 3/Entregables/_historico/ (no se modifica), y escriben la nueva versión en Fase 3/Entregables/.
"""
from __future__ import annotations

from fase3_common import *  # noqa: F401,F403
from fase3_docx_lib import Doc

HIST = OUT / "_historico"
DATE_V2 = "19-nov-2026"
DATE_V2_LONG = "19 de noviembre de 2026"
EV_D25 = "Fase 3/07_Evidencias/DART-14-2.5_E2E-2026-10-19/"

# Convención de portada (Etapa 3): Fernando Patricio Olguea González, David Sepúlveda, Juan Díaz
COVER_NAMES = {
    "Juan Díaz (": "Juan Díaz (Product Owner y desarrollador)",
    "Fernando Patricio Olguea González (": "Fernando Patricio Olguea González (líder de proyecto y desarrollador)",
    "David Alexis Sepúlveda Manque (": "David Sepúlveda (Scrum Master y desarrollador)",
}


def cover_v2(d: Doc, old_date_text: str, code: str, version: str, long_date: bool = True, subtitle_old: str | None = None, subtitle_new: str | None = None) -> None:
    """Actualiza la portada: fecha, código/versión y nombres de los integrantes."""
    d.set_par(d.par(old_date_text), DATE_V2_LONG if long_date else DATE_V2)
    d.set_par(d.par("Código del documento:"), f"Código del documento: {code}  ·  Versión {version} (borrador) · Actualización Fase 3")
    for start, new in COVER_NAMES.items():
        d.set_par(d.par(start), new)
    if subtitle_old and subtitle_new:
        d.set_par(d.par(subtitle_old), subtitle_new)


def tbl(d: Doc, *headers: str):
    for t in d.doc.tables:
        cells = [c.text.strip() for c in t.rows[0].cells]
        if len(cells) >= len(headers) and all(cells[i].startswith(h) for i, h in enumerate(headers)):
            return t
    raise KeyError(headers)


def P(d: Doc, start: str, nth: int = 0):
    """Busca un párrafo por su inicio, también dentro de tablas (llamadas y cuadros)."""
    found = [p for p in d._all_paragraphs() if p.text.strip().startswith(start)]
    if len(found) <= nth:
        raise KeyError(f"Párrafo no encontrado: {start!r}")
    return found[nth]


# --------------------------------------------------------------------------- textos compartidos
CORESTREAM_NOTE = (
    "CoreStream es una herramienta de gestión proporcionada por Alloxentric. El equipo informa que presentó deficiencias durante el desarrollo del proyecto "
    "[REPORTADO POR EL EQUIPO]. El reporte agregado del 19-nov-2026 (EV-20; Fase 3/07_Evidencias/CoreStream/, PDF original sin alteraciones, SHA-256 CBDADA1B...EE869) "
    "registra eficiencia del equipo 4 %, índice de bloqueo 0 %, índice de redirección 0 % y 16 tareas completadas en el período «year». "
    "El reporte incluye a Javier Cerna, quien figura en la herramienta del cliente pero no forma parte del equipo Capstone; consta con 0 tareas y no se le atribuyen responsabilidades ni actividades. "
    "El reporte no contiene tickets individuales, identificadores, estados ni fechas: no permite vincular tareas con hitos, requisitos ni con el identificador DART_14, "
    "y el 4 % de eficiencia no debe interpretarse como porcentaje de avance del proyecto, calidad, cumplimiento de hitos ni rendimiento académico individual. [CONFIRMADO]"
)

REUNION_NOTE = (
    "La reunión inicial del 2-sep-2026 con Max Kreimerman consta en el informe de definición de Fase 1, que cita una transcripción de su intervención. "
    "Esa transcripción y la especificación técnica atribuida a Max (v0.1, 02-09-2026) no están archivadas en este repositorio y su localización está pendiente; "
    "el registro histórico ACTA-01 (Fase 3/07_Evidencias/Reuniones_Cliente/) es una reconstrucción sin convocatoria, lista de asistentes ni acuerdos. "
    "Por ello la reunión y lo que se atribuye a Max se tratan como evidencia indirecta y no como acuerdos confirmados. [REPORTADO POR EL EQUIPO]"
)

CONTRADICCION_LLM = (
    "Contradicción entre fuentes históricas sin resolver: el informe de Fase 1 y D03 atribuyen a Max la indicación de evitar un LLM al inicio, "
    "mientras que el informe DART 14 1.1 del equipo (23-sep-2026) describe una especificación v0.1 de Alloxentric cuya cadena LiveKit → STT → LLM → TTS menciona DeepSeek Flash como referencia, "
    "y la misma especificación nombra a Speechmatics. Ninguna de las dos fuentes está archivada; hasta localizarlas no se afirma cuál refleja lo acordado. [PENDIENTE DE VALIDACIÓN]"
)

GUIA_33 = (
    "La guía oficial 3.3 «Presentación Proyecto APT» (copia sin modificar en Fase 3/Pautas_Oficiales/) indica que la presentación debe: describir los aspectos más relevantes del proyecto y fundamentar las decisiones tomadas; "
    "apoyarse en un recurso audiovisual si el proyecto lo requiere; durar como máximo 20 minutos, incluidas las preguntas de la comisión; usar los campos de la guía del Informe Final como estructura básica "
    "(relevancia, objetivos, metodología, desarrollo, evidencias, intereses y proyecciones); ir acompañada de las evidencias definidas en el proyecto; presentar los resultados e incorporar ajustes a partir de la última retroalimentación del docente sobre el informe final; "
    "y se realiza ante una comisión de docentes y la Dirección de Carrera, con nota individual por integrante que pondera el 30 % de la nota final de la asignatura. [CONFIRMADO]"
)

PAUTAS_PENDIENTES = (
    "Están disponibles las guías 3.1 (diario de reflexión) y 3.3 (presentación), pero no las planillas o pautas de evaluación de Fase 3 (evidencia individual y grupal); "
    "mientras falten, no se declara completa la cobertura de los criterios de evaluación. [PENDIENTE]"
)

DOC_TABLE_V12 = [
    ["Presentación (guía 3.3): aspectos relevantes y decisiones fundamentadas", "Oficial (guía 3.3)", "Informe §2 a §6 y §15; D01 (decisiones AD-01 a AD-16)", "Cubierto; las decisiones atribuidas al cliente se presentan sin aprobación confirmada"],
    ["Presentación (guía 3.3): duración máxima de 20 minutos con preguntas", "Oficial (guía 3.3)", "Guion preliminar (Fase 3/09_Presentacion) y Informe §10", "[PENDIENTE] ajustar el guion a 20 minutos y ensayarlo"],
    ["Presentación (guía 3.3): evidencias y resultados del proyecto", "Oficial (guía 3.3)", "D05 §9 y §10; Informe Anexo A; registro consolidado de evidencias", "Cubierto, con las limitaciones declaradas en cada evidencia"],
    ["Presentación (guía 3.3): ajustes según la última retroalimentación del docente", "Oficial (guía 3.3)", "—", "[PENDIENTE] la retroalimentación del informe final de Fase 2 no está en el repositorio"],
    ["Diario de reflexión de Fase 3 (guía 3.1)", "Oficial (guía 3.1), individual", "—", "[PENDIENTE] a cargo de cada integrante"],
    ["Planillas o pautas de evaluación de Fase 3", "Oficial", "—", "[PENDIENTE] no disponibles; la cobertura de evaluación no puede declararse completa"],
    ["Presentación: demostración funcional completa", "Informada por el equipo", "D06 (puesta en marcha) y D05 §10; guion de demostración del Informe", "Ensayo sobre main pendiente de registro; la demo dental valida el pipeline, no el proceso de cobranza"],
    ["Requerimientos IEEE 830 o historias de usuario", "Referencia, por validar", "D03 §4 a §6 (12 RF, 10 RNF + RNF-11, 8 HU)", "Cubierto; estados actualizados al 17-nov"],
    ["Casos de uso", "Referencia, por validar", "D03 §11", "Cubierto con UC-01 a UC-11; UP-1 a UP-4 pendientes"],
    ["Diagrama de clases", "Referencia, por validar", "D01 §10.3", "Cubierto como módulos y clases reales; el código es mayormente funcional"],
    ["Diagramas de actividad", "Referencia, por validar", "D01 §10.2", "Cubierto (actividad del worker)"],
    ["Modelo de datos", "Referencia, por validar", "D01 §10.5", "Declarado: no existe base de datos; se documenta el almacenamiento real"],
    ["Mockups", "Referencia, por validar", "D05 §10 (capturas del producto)", "No existen mockups previos al desarrollo; se muestran capturas reales, sin presentarlas como mockups"],
    ["Plan de pruebas, casos y resultados", "Referencia, por validar", "D05 v1.3", "Cubierto; estados rebajados según el respaldo archivado"],
    ["Backlogs y actas", "Referencia, por validar", "—", "[PENDIENTE] no están en los repositorios; CoreStream solo entrega un reporte agregado (EV-20)"],
    ["Estados de avance, stakeholders y plan de proyecto", "Referencia, por validar", "D04; D03 §2.3; Fase 1 (plan de trabajo)", "Cubierto parcialmente; backlogs y actas pendientes"],
]


def landscape_group(d: Doc, items: list[tuple], width_cm: float = 22.6) -> None:
    """Varias figuras consecutivas en UNA sola sección horizontal (una por página, sin páginas en blanco)."""
    import copy as _copy
    from docx.oxml.ns import qn as _qn
    from docx.text.paragraph import Paragraph as _P
    final = d.body.find(_qn("w:sectPr"))
    portrait, land = _copy.deepcopy(final), _copy.deepcopy(final)
    for s in (portrait, land):
        for t in s.findall(_qn("w:type")):
            s.remove(t)
    pg = land.find(_qn("w:pgSz"))
    w, h = pg.get(_qn("w:w")), pg.get(_qn("w:h"))
    pg.set(_qn("w:w"), h); pg.set(_qn("w:h"), w); pg.set(_qn("w:orient"), "landscape")
    p1 = d.doc.add_paragraph(); p1._p.get_or_add_pPr().append(portrait); d._place(p1._p)
    for i, (image, caption) in enumerate(items):
        d.figure(image, caption, width_cm)
        if i:
            fig_par = d.cursor.getprevious()
            _P(fig_par, d.doc._body).paragraph_format.page_break_before = True
    p2 = d.doc.add_paragraph(); p2._p.get_or_add_pPr().append(land); d._place(p2._p)


# --------------------------------------------------------------------------- ajustes de maquetación (Etapa 3)
from docx.shared import Pt as _Pt


def para_sb(d: Doc, text: str):
    """Párrafo de cuerpo con 6 pt de espacio previo (para texto que sigue a una tabla)."""
    p = d.para(text)
    p.paragraph_format.space_before = _Pt(6)
    return p


def tidy_tables(d: Doc) -> None:
    """Evita cabeceras de tabla huérfanas: la cabecera y la primera fila de datos se mantienen con la siguiente."""
    for t in d.doc.tables:
        for row in t.rows[:2]:
            for cell in row.cells:
                for p in cell.paragraphs:
                    p.paragraph_format.keep_with_next = True


_orig_save = Doc.save


def _save_tidy(self, out):
    tidy_tables(self)
    _orig_save(self, out)


Doc.save = _save_tidy
