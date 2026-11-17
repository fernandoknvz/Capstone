from pathlib import Path
from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "Fase 3" / "Entregables"
OUT.mkdir(parents=True, exist_ok=True)

PROJECT = "Alloxentric Real Time Agent"
DATE = "17 de noviembre de 2026"
TECH_HEAD = "77ff85c3ad252b52df429380ea916cf84c1725a4"
RECOVERY_HEAD = "7369bbc0bc2b22fb8e25c9b84eac33d2c7a5b561"


def shade(cell, fill):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = tc_pr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tc_pr.append(shd)
    shd.set(qn("w:fill"), fill)


def borders(table):
    tbl_pr = table._tbl.tblPr
    old = tbl_pr.find(qn("w:tblBorders"))
    if old is not None:
        tbl_pr.remove(old)
    node = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        item = OxmlElement(f"w:{edge}")
        item.set(qn("w:val"), "single")
        item.set(qn("w:sz"), "4")
        item.set(qn("w:color"), "D9D9D9")
        node.append(item)
    tbl_pr.append(node)


def cell_margin(cell, value=100):
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_mar = tc_pr.first_child_found_in("w:tcMar")
    if tc_mar is None:
        tc_mar = OxmlElement("w:tcMar")
        tc_pr.append(tc_mar)
    for side in ("top", "left", "bottom", "right"):
        elem = tc_mar.find(qn(f"w:{side}"))
        if elem is None:
            elem = OxmlElement(f"w:{side}")
            tc_mar.append(elem)
        elem.set(qn("w:w"), str(value))
        elem.set(qn("w:type"), "dxa")


def set_cell_text(cell, text, bold=False, color="000000", size=8.5, align=None):
    cell.text = ""
    p = cell.paragraphs[0]
    if align is not None:
        p.alignment = align
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.05
    r = p.add_run(str(text))
    r.bold = bold
    r.font.name = "Arial"
    r._element.get_or_add_rPr().rFonts.set(qn("w:ascii"), "Arial")
    r._element.get_or_add_rPr().rFonts.set(qn("w:hAnsi"), "Arial")
    r.font.size = Pt(size)
    r.font.color.rgb = RGBColor.from_string(color)


def add_table(doc, headers, rows, widths=None):
    table = doc.add_table(rows=1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    borders(table)
    for i, header in enumerate(headers):
        cell = table.rows[0].cells[i]
        shade(cell, "1F4E78")
        set_cell_text(cell, header, bold=True, color="FFFFFF", size=8.5, align=WD_ALIGN_PARAGRAPH.CENTER)
        cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        cell_margin(cell)
        if widths:
            cell.width = Cm(widths[i])
    for ridx, row in enumerate(rows):
        cells = table.add_row().cells
        for i, value in enumerate(row):
            if ridx % 2:
                shade(cells[i], "EDF3F8")
            align = WD_ALIGN_PARAGRAPH.CENTER if len(str(value)) < 25 and i > 0 else WD_ALIGN_PARAGRAPH.LEFT
            set_cell_text(cells[i], value, size=8.2, align=align)
            cells[i].vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            cell_margin(cells[i])
            if widths:
                cells[i].width = Cm(widths[i])
    doc.add_paragraph().paragraph_format.space_after = Pt(0)
    return table


def configure(doc):
    sec = doc.sections[0]
    sec.top_margin = Cm(2.2)
    sec.bottom_margin = Cm(2.0)
    sec.left_margin = Cm(2.2)
    sec.right_margin = Cm(2.2)
    styles = doc.styles
    normal = styles["Normal"]
    normal.font.name = "Arial"
    normal._element.rPr.rFonts.set(qn("w:ascii"), "Arial")
    normal._element.rPr.rFonts.set(qn("w:hAnsi"), "Arial")
    normal.font.size = Pt(10)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.15
    for name, size, before, after in (("Title", 22, 0, 14), ("Heading 1", 15, 14, 6), ("Heading 2", 12, 10, 4), ("Heading 3", 10.5, 8, 3)):
        style = styles[name]
        style.font.name = "Arial"
        style._element.rPr.rFonts.set(qn("w:ascii"), "Arial")
        style._element.rPr.rFonts.set(qn("w:hAnsi"), "Arial")
        style.font.size = Pt(size)
        style.font.bold = True
        style.font.color.rgb = RGBColor(0, 0, 0)
        style.paragraph_format.space_before = Pt(before)
        style.paragraph_format.space_after = Pt(after)
        style.paragraph_format.keep_with_next = True


def add_cover(doc, title, subtitle, code, version, responsible, status):
    p = doc.add_paragraph(style="Title")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run(title)
    p2 = doc.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p2.add_run(subtitle)
    r.bold = True
    r.font.size = Pt(13)
    doc.add_paragraph()
    meta = [
        ("Proyecto", PROJECT),
        ("Asignatura", "Capstone de Ingeniería en Informática"),
        ("Documento", code),
        ("Versión", version),
        ("Fecha de corte", DATE),
        ("Responsable de consolidación", responsible),
        ("Estado", status),
    ]
    add_table(doc, ["Campo", "Valor"], meta, [5.0, 11.0])
    doc.add_paragraph("Fuentes principales: documentos históricos D01-D06 y E01; repositorio técnico en " + TECH_HEAD + "; PR #16-#20; evidencia E2E del 31 de octubre; recuperación documental " + RECOVERY_HEAD + ".")
    doc.add_page_break()


def add_control(doc, sources, implemented, pending, limitations):
    doc.add_heading("Control del documento", level=1)
    add_table(doc, ["Elemento", "Detalle"], [
        ("Fuentes", sources),
        ("Funcionalidades implementadas", implemented),
        ("Funcionalidades pendientes", pending),
        ("Limitaciones conocidas", limitations),
        ("Estado de revisión", "Borrador preparado para revisión de Fernando, David y Juan. No publicado."),
    ], [4.5, 11.5])


def para(doc, text, bold_lead=None):
    p = doc.add_paragraph()
    if bold_lead and text.startswith(bold_lead):
        p.add_run(bold_lead).bold = True
        p.add_run(text[len(bold_lead):])
    else:
        p.add_run(text)
    return p


def bullet(doc, text):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_after = Pt(3)
    p.add_run(text)


def finish(doc, filename):
    for sec in doc.sections:
        footer = sec.footer.paragraphs[0]
        footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
        footer.text = f"{PROJECT} | Borrador Fase 3 | {DATE}"
        for run in footer.runs:
            run.font.name = "Arial"
            run.font.size = Pt(8)
            run.font.color.rgb = RGBColor(89, 89, 89)
    path = OUT / filename
    doc.save(path)
    return path


def new_doc(title, subtitle, code, version, responsible, status="Borrador para revisión humana"):
    doc = Document()
    configure(doc)
    add_cover(doc, title, subtitle, code, version, responsible, status)
    return doc


def architecture():
    d = new_doc("Arquitectura de software Fase 3", "Estado integrado y evolución pendiente", "D01 Fase 3", "1.1", "Juan Díaz; revisión técnica sugerida: Fernando Olguea")
    add_control(d, "D01 v1.0; código en origin/main; PR #16-#20; matriz de trazabilidad.", "Pipeline voz a voz, Web Demo, seguridad, métricas y CI.", "Asterisk, worker persistente, persistencia de negocio y protocolo económico.", "PR #18 no integrado; escenario real del cliente y pauta Fase 3 pendientes.")
    d.add_heading("Resumen arquitectónico", level=1)
    para(d, "La solución integrada permite una conversación de voz desde un navegador. LiveKit Cloud transporta el audio y despacha un worker Python. El worker transcribe con Google Chirp 3, genera texto con Gemini o DeepSeek y sintetiza audio con ElevenLabs. La Web Demo y sus funciones serverless gestionan acceso y tokens, pero no ejecutan el worker.")
    d.add_heading("Componentes integrados en main", level=1)
    add_table(d, ["Componente", "Tecnología", "Responsabilidad", "Evidencia"], [
        ("Web Demo", "Next.js y React", "Acceso, persona, llamada, transcripción e historial local", "PR #11-#16"),
        ("LiveKit Cloud", "WebRTC y Agents", "Sala, audio y despacho del agente", "PR #2/#7 y E2E 31-oct"),
        ("Worker", "Python 3.12 y livekit-agents 1.8.4", "Orquestación y observabilidad", "agent.py y pipeline.py"),
        ("STT", "Google Chirp 3", "Transcripción streaming", "PR #6, E01 y E2E"),
        ("LLM", "Gemini o DeepSeek", "Respuesta conversacional streaming", "PR #3/#5, E01 y E2E"),
        ("TTS", "ElevenLabs", "Síntesis streaming", "PR #4, E01 y E2E"),
        ("CI", "GitHub Actions", "pytest, Vitest, lint, TypeScript y build", "PR #19/#20"),
    ], [3.0, 3.5, 6.2, 3.3])
    d.add_heading("Flujo de una sesión", level=1)
    for text in [
        "La persona inicia sesión en la Web Demo y selecciona una persona desde una lista cerrada.",
        "La función serverless valida sesión, origen y persona, y emite un token con despacho explícito.",
        "LiveKit despacha el job al worker configurado por nombre.",
        "El worker crea la sesión con STT, LLM y TTS, reproduce el saludo y procesa turnos.",
        "Las métricas registran tiempos y uso numérico sin almacenar texto de conversación.",
    ]:
        bullet(d, text)
    d.add_heading("Seguridad y privacidad", level=1)
    para(d, "El código integrado mantiene secretos fuera de Git, usa cookie segura y firmada, valida origen, restringe persona y despacho, aplica CSP y desactiva la grabación de la sesión con record=False. Siguen pendientes rate limiting, límites de gasto, identidad individual de evaluadores y validación normativa para cobranza real.")
    d.add_heading("Trabajo no integrado", level=1)
    para(d, "El PR #18 contiene Anthropic, LiveKit Inference, STT seleccionable y optimizaciones adicionales. Está abierto, sin revisión registrada y no forma parte de la arquitectura vigente de main.")
    d.add_heading("Limitaciones", level=1)
    for x in ["Sin Asterisk ni llamadas telefónicas reales.", "Sin almacenamiento persistente de cartera o resultados.", "Sin hosting persistente demostrado del worker.", "Sin guion oficial ni protocolo de costo y efectividad.", "Latencia medida superior al objetivo declarado de un segundo."]:
        bullet(d, x)
    return finish(d, "D01_Fase3_Arquitectura_Software_v1.1.docx")


def risks():
    d = new_doc("Plan de riesgos Fase 3", "Riesgos técnicos académicos y operacionales", "D02 Fase 3", "1.1", "Fernando Olguea; revisión sugerida: David Sepúlveda y Juan Díaz")
    add_control(d, "D02 v1.0; PR #16-#20; E01; E2E 31-oct; auditoría del 17-nov.", "Controles web, métricas, CI y evidencia E2E sanitizada.", "Asterisk, límites de gasto, licencias, pauta Fase 3 y decisión DART.", "Valoraciones sujetas a revisión del equipo y a fuentes aún no disponibles.")
    d.add_heading("Criterio de valoración", level=1)
    para(d, "La prioridad combina probabilidad e impacto sobre entrega académica, seguridad, costo, alcance y calidad. Un riesgo materializado describe un problema observado; no equivale a una causa cerrada.")
    add_table(d, ["ID", "Riesgo", "Nivel", "Estado", "Respuesta y evidencia"], [
        ("R-01", "Latencia mayor a un segundo", "Crítico", "Materializado", "E01 y E2E; informar sin afirmar cumplimiento; definir umbral formal."),
        ("R-02", "Pauta oficial Fase 3 no disponible", "Crítico", "Activo", "Solicitar pauta; no inventar criterios."),
        ("R-03", "DART presentado como cambio aprobado", "Crítico", "Activo", "Mantener Alloxentric como nombre oficial; DART solo propuesta."),
        ("R-04", "Asterisk no implementado", "Alto", "Activo", "Acordar alcance o realizar spike con acceso del cliente."),
        ("R-05", "Guion y criterios del cliente no adjuntos", "Alto", "Activo", "Obtener acta o marcar pendiente."),
        ("R-06", "Gasto de APIs sin límites", "Alto", "Activo", "Demo supervisada, DEMO_ENABLED y límites antes de acceso abierto."),
        ("R-07", "Voces/licencias no confirmadas", "Alto", "Activo", "Confirmar titularidad y licencia; no uso productivo."),
        ("R-08", "Evidencia insuficiente o dispersa", "Alto", "En mitigación", "Rama documental, hashes, matriz y registro de evidencias."),
        ("R-09", "PR #18 confundido con main", "Alto", "Activo", "Rotular siempre como PR abierto/no integrado."),
        ("R-10", "Worker local no disponible en la presentación", "Alto", "Activo", "Ensayo, responsable, respaldo audiovisual y plan de contingencia."),
        ("R-11", "Secretos o datos personales en evidencia", "Alto", "Mitigado parcialmente", "Logs sanitizados y escaneo; repetir antes de publicar."),
        ("R-12", "Revisión humana tardía", "Alto", "Activo", "Revisión cruzada antes de PPT o integración."),
    ], [1.4, 5.2, 2.0, 2.5, 6.0])
    d.add_heading("Riesgos que no pueden cerrarse documentalmente", level=1)
    para(d, "No se consideran cerrados Asterisk, la aprobación de DART, la licencia de voces, los límites de gasto, el protocolo económico ni la pauta Fase 3. Requieren decisión externa o evidencia nueva.")
    return finish(d, "D02_Fase3_Plan_Riesgos_v1.1.docx")


def requirements():
    d = new_doc("Levantamiento de requerimientos Fase 3", "Requerimientos confirmados propuestos y pendientes", "D03 Fase 3", "1.1", "Juan Díaz; validación sugerida: equipo y contraparte")
    add_control(d, "D03 v1.0; Fase 1 y 2; código main; PR #16-#20.", "MVP de voz web, proveedores principales, controles web y observabilidad.", "Asterisk, guion oficial, comparación económica, pauta Fase 3.", "Varias decisiones se conocen por documentación del equipo sin acta de cliente adjunta.")
    d.add_heading("Reglas de clasificación", level=1)
    add_table(d, ["Clase", "Uso"], [("Confirmado", "Respaldado por documentos académicos, repositorio integrado o evidencia archivada."), ("Propuesto", "Diseño o evolución sin aprobación académica o del cliente adjunta."), ("Pendiente", "Falta definición, acceso o fuente verificable."), ("No integrado", "Existe en una rama o PR abierto, no en main.")], [3.5, 12.5])
    d.add_heading("Requerimientos funcionales", level=1)
    add_table(d, ["ID", "Requerimiento", "Fuente", "Estado", "Verificación"], [
        ("RF-01", "Mantener conversación de voz en tiempo real", "Fase 1", "Implementado", "E2E 31-oct"),
        ("RF-02", "Transportar audio mediante LiveKit", "Fase 1", "Implementado", "PR #2/#7"),
        ("RF-03", "Transcribir audio", "Fase 1; cambio posterior", "Implementado con Chirp 3", "PR #6, E01"),
        ("RF-04", "Generar respuesta conversacional", "Decisión posterior", "Implementado con Gemini/DeepSeek", "PR #3/#5"),
        ("RF-05", "Sintetizar voz mediante ElevenLabs", "Fase 1", "Implementado", "PR #4, E2E"),
        ("RF-06", "Acceder desde una Web Demo controlada", "Propuesta equipo", "Implementado", "PR #11-#16"),
        ("RF-07", "Usar guion oficial de cobranza", "Fase 1", "Pendiente", "Sin evidencia"),
        ("RF-08", "Realizar llamada por Asterisk", "Fase 1", "Pendiente", "Sin prueba"),
        ("RF-09", "Comparar costo y efectividad", "Fase 1", "Pendiente", "Sin protocolo"),
        ("RF-10", "Elegir STT/LLM adicionales", "PR #18", "No integrado", "Pruebas de rama"),
    ], [1.5, 6.0, 3.0, 2.8, 3.0])
    d.add_heading("Requerimientos no funcionales", level=1)
    add_table(d, ["ID", "Requerimiento", "Estado y resultado"], [
        ("RNF-01", "Respuesta no mayor a un segundo", "No cumple: E01 mediana 2,5941 s; muestra E2E 31-oct mediana 2,7411 s."),
        ("RNF-02", "Secretos fuera de Git", "Implementado en diseño; evidencia recuperada escaneada sin secretos."),
        ("RNF-03", "Trazabilidad de cambios", "Ramas, PR y matriz disponibles; revisiones formales incompletas en algunos PR."),
        ("RNF-04", "Privacidad de la prueba", "record=False y métricas numéricas; políticas de proveedores pendientes."),
        ("RNF-05", "Reproducibilidad", "Lockfiles y CI existen; certificación local final pendiente."),
        ("RNF-06", "Disponibilidad operacional", "Worker persistente no demostrado."),
    ], [2.0, 6.0, 8.0])
    d.add_heading("Evolución DART", level=1)
    para(d, "DART y el caso de cobranza para pymes se documentan exclusivamente como propuesta de evolución. No reemplazan el nombre académico Alloxentric Real Time Agent y no constituyen un requerimiento aprobado.")
    return finish(d, "D03_Fase3_Levantamiento_Requerimientos_v1.1.docx")


def progress():
    d = new_doc("Estado de avance Fase 3", "Avance integrado evidencia disponible y brechas", "D04 Fase 3", "1.1", "Fernando Olguea; revisión sugerida: equipo completo")
    add_control(d, "D04 v1.0; historial de ambos repositorios; PR #1-#20; auditoría 17-nov.", "MVP web voz-a-voz, pruebas automatizadas, métricas, seguridad y CI.", "Asterisk, costos, persistencia, guion oficial y pauta Fase 3.", "E2E limitada; algunos acuerdos de cliente no tienen acta adjunta.")
    d.add_heading("Resumen", level=1)
    para(d, "El proyecto alcanzó un MVP web de voz a voz integrado en main. El progreso técnico supera lo presentado en Fase 2, pero la latencia no cumple el objetivo declarado, la telefonía no está implementada y parte importante de la evidencia estaba fuera del repositorio académico. La recuperación documental corrige la dispersión, no las brechas técnicas.")
    add_table(d, ["Hito", "Estado", "Referencia", "Limitación"], [
        ("Pipeline LiveKit", "Integrado", "PR #2/#7", "Sin Asterisk"),
        ("STT/LLM/TTS", "Integrado", "PR #3-#6", "Aprobaciones externas parciales"),
        ("Métricas", "Integrado y medido", "PR #9, E01", "Muestra no estadística"),
        ("Web Demo", "Integrada", "PR #11-#16", "Worker local"),
        ("Personas", "Integradas", "PR #16", "Una persona con log E2E recuperado"),
        ("Aislamiento worker", "Integrado", "PR #17", "Mismo proyecto LiveKit"),
        ("CI", "Integrado", "PR #19/#20", "PR #19 sin aprobación independiente"),
        ("Proveedores alternativos", "PR abierto", "PR #18", "No es main"),
        ("Documentación académica", "Recuperada", RECOVERY_HEAD[:7], "Revisión humana pendiente"),
    ], [5.0, 3.0, 3.0, 5.0])
    d.add_heading("Contribuciones verificables", level=1)
    add_table(d, ["Integrante", "Contribuciones verificables"], [
        ("Fernando", "Entorno, LiveKit, DeepSeek, Gemini, pipeline, métricas, Web Demo inicial, seguridad, incidentes y CI."),
        ("David", "ElevenLabs TTS, pruebas, script de validación y reflexión académica."),
        ("Juan", "Chirp 3, personas, latencia, rediseño web, historial, Vercel, PR #18 y D01-D06/E01."),
    ], [3.5, 12.5])
    d.add_heading("Brechas para cierre", level=1)
    for x in ["Obtener pauta oficial y validar alcance académico.", "Revisar los siete entregables Fase 3.", "Certificar pruebas sobre el corte final de main.", "Preparar demostración y contingencia.", "Acordar tratamiento de Asterisk, costo/efectividad y latencia."]:
        bullet(d, x)
    return finish(d, "D04_Fase3_Estado_Avance_v1.1.docx")


def tests():
    d = new_doc("Plan de pruebas y resultados Fase 3", "Resultados históricos evidencia recuperada y pruebas pendientes", "D05 Fase 3", "1.1", "David Sepúlveda; revisión técnica sugerida: Juan Díaz")
    add_control(d, "D05 v1.0; E01; E2E 31-oct; PR #16-#20; workflow CI.", "Pruebas unitarias, web, seguridad, CI y E2E web.", "Asterisk, certificación final, seis personas y muestra estadística.", "Resultados de ramas distintas no son acumulables; PR #18 no integrado.")
    d.add_heading("Estrategia", level=1)
    add_table(d, ["Nivel", "Objetivo", "Estado"], [
        ("Unitarias Python", "Configuración, proveedores, pipeline, métricas y personas sin red", "Históricamente aprobadas"),
        ("Frontend", "Sesión, token, seguridad, UI e historial", "Históricamente aprobadas"),
        ("Integración real", "Comprobar proveedores con scripts manuales", "Resultados parciales"),
        ("E2E web", "Conversación completa y latencia", "Evidencia 30-oct y 31-oct"),
        ("Telefonía", "Llamada real Asterisk", "No ejecutada"),
    ], [3.5, 8.5, 4.0])
    d.add_heading("Resultados automatizados históricos", level=1)
    add_table(d, ["Corte", "Python", "Web", "Clasificación"], [
        ("PR #16", "200", "91", "Rama luego integrada"),
        ("PR #17", "214", "No informado", "Integrado en main"),
        ("PR #18", "281", "103", "PR abierto; no integrado"),
        ("PR #19/#20", "Workflow CI", "Workflow CI", "Integrado; ejecuciones documentadas"),
    ], [4.0, 3.5, 3.5, 5.0])
    d.add_heading("Métricas E01 del 30 de octubre", level=1)
    add_table(d, ["Indicador", "Resultado"], [("Sesiones", "5"), ("Turnos del agente", "22"), ("Turnos con E2E", "13"), ("Mediana E2E", "2,5941 s"), ("Mínimo", "0,4775 s; turno interrumpido"), ("Máximo", "4,0839 s"), ("Sobre 3 s", "3 turnos")], [7.0, 9.0])
    d.add_heading("E2E del 31 de octubre", level=1)
    add_table(d, ["Indicador", "Resultado"], [("Sesiones", "1"), ("Turnos con E2E", "5"), ("Media", "2,3302 s"), ("Mediana", "2,7411 s"), ("Rango", "1,1912-3,3519 s"), ("Errores de sesión", "0")], [7.0, 9.0])
    para(d, "La muestra del 31 de octubre corresponde a clínica dental, un hablante, frases no controladas, sin grabación y sin reloj externo. No constituye validación estadística ni prueba del caso oficial de cobranza.")
    d.add_heading("Conclusión de pruebas", level=1)
    para(d, "El flujo voz-a-voz está funcionalmente demostrado desde navegador. No existe evidencia de cumplimiento del objetivo de un segundo, telefonía Asterisk ni comparación económica. Se requiere una certificación final reproducible del commit de main antes de la presentación.")
    return finish(d, "D05_Fase3_Plan_Pruebas_Resultados_v1.1.docx")


def deployment():
    d = new_doc("Guía de despliegue y operación Fase 3", "Puesta en marcha verificación y contingencia", "D06 Fase 3", "1.1", "Juan Díaz; revisión operativa sugerida: David Sepúlveda")
    add_control(d, "D06 v1.0; README técnico; workflow CI; PR #16-#20.", "Worker local, Web Demo, Netlify/Vercel y LiveKit Cloud.", "Worker persistente, cuenta de servicio operativa, límites y Asterisk.", "No se desplegó durante esta consolidación; comandos requieren credenciales del equipo.")
    d.add_heading("Distribución de componentes", level=1)
    add_table(d, ["Componente", "Ubicación operacional", "Observación"], [
        ("Worker Python", "Equipo de un integrante", "Debe estar ejecutándose y registrado."),
        ("Web Demo", "Netlify o Vercel", "Aloja interfaz y funciones, no el worker."),
        ("LiveKit", "LiveKit Cloud", "Salas y despacho."),
        ("STT/LLM/TTS", "Servicios gestionados", "Consumen credenciales y cuota."),
    ], [4.0, 5.0, 7.0])
    d.add_heading("Puesta en marcha controlada", level=1)
    for x in [
        "Verificar que el checkout técnico corresponda a 77ff85c o al commit aprobado para la demostración.",
        "Instalar dependencias reproducibles con uv y pnpm a partir de los lockfiles.",
        "Configurar variables en archivos locales ignorados o secretos del hosting; nunca en Git.",
        "Validar ADC de Google y las credenciales de LiveKit, LLM y ElevenLabs.",
        "Ejecutar la suite automatizada y conservar el log de la certificación.",
        "Iniciar el worker con nombre de desarrollo o demostración acordado y verificar su registro.",
        "Habilitar la demo solo durante la ventana supervisada y ejecutar una llamada de prueba.",
    ]:
        bullet(d, x)
    d.add_heading("Lista previa a la presentación", level=1)
    add_table(d, ["Control", "Resultado esperado"], [
        ("Worker", "Registrado en el mismo proyecto y con nombre coincidente."),
        ("Web", "Sitio y rutas API responden sin 5xx."),
        ("Acceso", "401 sin sesión, 403 desde origen ajeno."),
        ("Audio", "Micrófono correcto, audífonos y saludo audible."),
        ("Métricas", "Logger INFO activo y ruta de archivo definida."),
        ("Contingencia", "Capturas o video sin secretos y guion alternativo."),
    ], [6.0, 10.0])
    d.add_heading("Después de la demostración", level=1)
    para(d, "Deshabilitar sesiones nuevas, detener el worker si no se necesita, revisar consumo, archivar únicamente métricas y logs sanitizados, y rotar cualquier secreto expuesto. DEMO_ENABLED=false no corta sesiones ya abiertas.")
    d.add_heading("Limitaciones operacionales", level=1)
    para(d, "No existe evidencia de worker persistente, rate limiting propio, tope de duración, llamadas simultáneas ni Asterisk. La guía no autoriza producción ni uso con datos reales.")
    return finish(d, "D06_Fase3_Guia_Despliegue_Operacion_v1.1.docx")


def academic_report():
    d = new_doc("Informe de avance Fase 3", "Consolidación documental y trazabilidad", "Informe académico Fase 3", "0.9", "Fernando Olguea, David Sepúlveda y Juan Díaz")
    add_control(d, "Fases 1 y 2; D01-D06/E01; repositorios académico y técnico; evidencia E2E; matriz de trazabilidad.", "MVP web voz-a-voz, observabilidad, seguridad, personas, despliegue web y CI.", "Pauta Fase 3, Asterisk, persistencia, costos, guion oficial y aprobación DART.", "Borrador académico sin pauta oficial; exige revisión del equipo y docente.")
    sections = [
        ("Introducción", "Este informe consolida el avance académico y técnico del proyecto Alloxentric Real Time Agent para la presentación de Fase 3. El corte documental es el 17 de noviembre de 2026. La solución mantiene su nombre académico; DART se registra únicamente como propuesta de evolución pendiente de autorización."),
        ("Problema abordado", "Alloxentric requiere explorar un agente de cobranza por voz en tiempo real con mayor flexibilidad. El proyecto busca construir y evaluar un prototipo que conecte audio, transcripción, generación de respuesta y síntesis, dejando pendiente la comparación formal con la solución actual."),
        ("Objetivos", "El objetivo general heredado es desarrollar y evaluar un prototipo de bot de cobranza por voz basado en LiveKit. Los objetivos específicos abarcan requerimientos, arquitectura, implementación, gestión, pruebas y comparación económica. No existe un ajuste académico aprobado que los reemplace."),
        ("Alcance", "El alcance implementado comprende una conversación de voz desde navegador, proveedores STT/LLM/TTS, Web Demo, métricas y CI. No comprende Asterisk, campañas productivas, cartera real, persistencia empresarial ni operación con datos personales reales."),
        ("Metodología", "El equipo declaró Scrum y aplica ramas por ticket, Pull Requests y seguimiento en GitHub/CoreStream. La evidencia de ceremonias, backlog y actas sigue incompleta. La consolidación utiliza trazabilidad requerimiento-implementación-prueba-evidencia."),
        ("Arquitectura", "El navegador se conecta a LiveKit Cloud. Un worker Python recibe el job y orquesta Google Chirp 3, Gemini o DeepSeek y ElevenLabs. Las funciones serverless controlan sesión y token; no alojan al worker."),
        ("Tecnologías", "Python 3.12, LiveKit Agents 1.8.4, Google Cloud Speech-to-Text Chirp 3, Gemini, DeepSeek, ElevenLabs, Next.js, React, Netlify/Vercel y GitHub Actions."),
        ("Desarrollo implementado", "Main contiene el pipeline de voz, configuración, métricas, siete personas, Web Demo, controles de acceso, historial local, Vercel y CI. El PR #18 contiene proveedores y selección de STT adicionales, pero continúa abierto y no se considera integrado."),
        ("Pruebas", "El repositorio contiene pruebas Python y web sin red, scripts manuales, CI y evidencia E2E. Los conteos históricos deben asociarse a su corte: 200/91 en PR #16; 214 Python en PR #17; 281/103 solo en PR #18."),
        ("Resultados", "E01 contiene 13 turnos E2E medibles con mediana 2,5941 s. La sesión del 31 de octubre contiene cinco turnos medibles con media 2,3302 s y mediana 2,7411 s. El flujo funciona, pero no cumple el objetivo declarado de un segundo."),
        ("Riesgos", "Los riesgos críticos son la latencia, la falta de pauta Fase 3 y presentar DART como cambio aprobado. También permanecen Asterisk, gasto de APIs, licencias, evidencia dispersa y disponibilidad del worker."),
        ("Limitaciones", "Las muestras son pequeñas, no existe telefonía real, no hay protocolo económico ni persistencia de negocio, y varios acuerdos del cliente no tienen acta adjunta."),
        ("Contribuciones individuales", "Fernando aportó coordinación, arquitectura, pipeline, métricas, Web Demo inicial, seguridad y CI. David implementó TTS ElevenLabs, pruebas y validación manual. Juan implementó Chirp 3, personas, optimizaciones, rediseño web, Vercel y la documentación D01-D06/E01."),
        ("Conclusiones", "El equipo dispone de un MVP técnicamente funcional y demostrable. La principal tarea de Fase 3 es consolidar evidencia verificable y presentar con precisión qué está integrado, qué fue medido y qué continúa pendiente."),
        ("Trabajo futuro", "Obtener la pauta, validar alcance con docente y cliente, certificar pruebas sobre main, ampliar E2E, resolver Asterisk, definir costos y efectividad, confirmar licencias y decidir formalmente la evolución DART."),
        ("Referencias y anexos", "Referencias principales: repositorio académico fernandoknvz/Capstone; repositorio técnico fernandoknvz/alloxentric-real-time-agent; PR #1-#20; D01-D06; E01; logs E2E sanitizados del 31 de octubre; matriz de trazabilidad preliminar."),
    ]
    for title, text in sections:
        d.add_heading(title, level=1)
        para(d, text)
    d.add_heading("Anexos disponibles", level=2)
    for x in ["Matriz de trazabilidad preliminar.", "Registro consolidado de evidencias.", "Logs E2E sanitizados con hashes.", "Documentos históricos de Fase 1 y Fase 2."]:
        bullet(d, x)
    return finish(d, "Informe_Avance_Fase3_v0.9.docx")


if __name__ == "__main__":
    outputs = [architecture(), risks(), requirements(), progress(), tests(), deployment(), academic_report()]
    for output in outputs:
        print(output)
