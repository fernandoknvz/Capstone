"""Datos y utilidades compartidas por los constructores de documentos Fase 3."""
from __future__ import annotations

import copy
from pathlib import Path

from docx.oxml import parse_xml
from docx.oxml.ns import qn

from fase3_docx_lib import Doc

ROOT = Path(__file__).resolve().parents[1]
ORIG = ROOT / "Fase 2" / "Evidencias Proyecto" / "Evidencias Documentacion"
OUT = ROOT / "Fase 3" / "Entregables"
FIG = ROOT / "Fase 3" / "03_Diseno" / "diagramas"
SHOT = ROOT / "Fase 3" / "07_Evidencias" / "capturas-web-demo-2026-11-17"
SHOT_DS = ROOT / "Fase 3" / "07_Evidencias" / "E2E-2026-11-17-clinica-dental-deepseek" / "capturas"
EV_DS = "Fase 3/07_Evidencias/E2E-2026-11-17-clinica-dental-deepseek/"
DATE_DS = "18-nov-2026"

DATE = "17 de noviembre de 2026"
CUT = "17-nov-2026"
TECH_HEAD = "77ff85c"
TECH_HEAD_FULL = "77ff85c3ad252b52df429380ea916cf84c1725a4"
AUTHOR = "Equipo (consolidación asistida con Claude Code); revisión pendiente de Juan, Fernando y David"

W_NS = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'


def landscape_figure(d: Doc, image: Path, caption: str, width_cm: float = 22.6) -> None:
    """Inserta la figura en su propia página horizontal y vuelve a vertical."""
    final = d.body.find(qn("w:sectPr"))
    portrait = copy.deepcopy(final)
    for t in portrait.findall(qn("w:type")):
        portrait.remove(t)
    land = copy.deepcopy(final)
    for t in land.findall(qn("w:type")):
        land.remove(t)
    pg = land.find(qn("w:pgSz"))
    w, h = pg.get(qn("w:w")), pg.get(qn("w:h"))
    pg.set(qn("w:w"), h)
    pg.set(qn("w:h"), w)
    pg.set(qn("w:orient"), "landscape")
    # El párrafo con sectPr cierra la sección vertical previa
    p1 = d.doc.add_paragraph()
    p1._p.get_or_add_pPr().append(portrait)
    d._place(p1._p)
    d.figure(image, caption, width_cm)
    p2 = d.doc.add_paragraph()
    p2._p.get_or_add_pPr().append(land)
    d._place(p2._p)


def control_row(d: Doc, code_table_first: str = "Versión", change: str = "", version: str = "1.1", date: str = CUT) -> None:
    t = d.table(code_table_first)
    d.add_row(t, [f"{version} (borrador)", date, AUTHOR, change])


def cover(d: Doc, code: str, version: str = "1.1", date: str = DATE) -> None:
    d.retitle_cover(
        f"{date}",
        f"Código del documento: {code}  ·  Versión {version} (borrador) · Actualización Fase 3",
        "Estado: Borrador para revisión del equipo (sin aprobación; no publicado)",
    )


# --------------------------------------------------------------------------- casos de uso (compartido D01/D03/Informe)
USE_CASES = [
    ("UC-01", "Ingresar con código de acceso", "Evaluador", "Ingresa el código temporal; el servidor compara su hash, valida el origen y entrega una cookie de sesión de 30 min.", "RF-09 · HU-01", "login.test.ts (8), session.test.ts (4); TC-07, TC-08"),
    ("UC-02", "Seleccionar agente (persona)", "Evaluador", "Elige 1 de 7 agentes; el navegador envía solo el identificador, validado contra una lista cerrada.", "RF-10 · HU-03", "personas.test.ts (17), test_personas.py (26); TC-06"),
    ("UC-03", "Conversar por voz con el agente", "Evaluador", "Inicia la conversación; el agente saluda y sostiene el diálogo voz → STT → LLM → TTS → voz.", "RF-01 a RF-04 · HU-01", "test_pipeline.py (32), voice-session.test.tsx (6); E2E 31-oct; TC-01, TC-02, TC-03"),
    ("UC-04", "Ver transcripción en vivo", "Evaluador", "La pantalla muestra lo que dijo la persona y lo que respondió el agente, sin líneas duplicadas.", "RF-11 · HU-01", "conversation-panel.test.tsx (15); TC-11"),
    ("UC-05", "Interrumpir al agente", "Evaluador", "La persona puede hablar mientras el agente responde; la sesión detiene la reproducción.", "RF-06", "Capacidad de la sesión LiveKit; E01 registra turnos interrumpidos; TC-15 pendiente"),
    ("UC-06", "Elegir micrófono y silenciar", "Evaluador", "Selecciona el dispositivo de entrada y silencia/reactiva el micrófono durante la llamada.", "RF-11 · HU-04", "conversation-panel.test.tsx; TC-12 y TC-13 (verificación real pendiente)"),
    ("UC-07", "Consultar, descargar y borrar historial local", "Evaluador", "Lista conversaciones guardadas en el navegador, descarga una como texto o borra todo.", "RF-11 · HU-05", "history.test.ts (8); TC-18"),
    ("UC-08", "Finalizar conversación y cerrar acceso", "Evaluador", "Termina la llamada y cierra la sesión de acceso.", "RF-09", "voice-controls.test.tsx (2), voice-session.test.tsx (6)"),
    ("UC-09", "Iniciar y registrar el worker del agente", "Equipo técnico", "Ejecuta el worker con el nombre acordado; se registra en LiveKit y atiende los despachos.", "RNF-09", "test_project_bootstrap.py (3), test_agent_name.py (14); guía D06"),
    ("UC-10", "Revisar métricas de latencia y uso", "Equipo técnico", "Lee las líneas de log numéricas por turno y por sesión.", "RF-08", "test_metrics.py (40); E01 y E2E 31-oct"),
    ("UC-11", "Ejecutar verificación automática (CI)", "Equipo técnico", "GitHub Actions ejecuta pytest, Vitest, ESLint, TypeScript y build en cada PR y push a main.", "RNF-08", ".github/workflows/ci.yml; runs 42433340255, 42433603292, 42435613596"),
]
PENDING_UC = [
    ("UP-1", "Atender llamada telefónica (Asterisk)", "Alloxentric / equipo", "RF-07 · HU-08", "Sin código ni pruebas; depende de accesos del cliente"),
    ("UP-2", "Ejecutar el guion oficial de cobranza con reconocimiento de intenciones", "Alloxentric / equipo", "RF-05 · HU-06", "Los escenarios actuales son ficticios y no equivalen al guion oficial"),
    ("UP-3", "Comparar costo y efectividad por llamada", "Alloxentric", "RF-12 · HU-07", "Solo existen contadores de uso; falta protocolo y tarifas"),
    ("UP-4", "Persistir resultados de negocio", "Alloxentric / equipo", "Sin requisito en D03", "No existe base de datos ni persistencia (solo localStorage y logs)"),
]


def use_case_tables(d: Doc) -> None:
    d.table_new(["ID", "Caso de uso", "Actor", "Descripción", "Requisito / HU", "Verificación"],
                [list(r) for r in USE_CASES], [1.6, 2.9, 1.8, 5.0, 2.2, 3.7])
    d.para("[PENDIENTE] Casos de uso sin implementación en el código (se muestran fuera del límite del sistema en la Figura):")
    d.table_new(["ID", "Caso de uso pendiente", "Actor", "Requisito / HU", "Estado"],
                [list(r) for r in PENDING_UC], [1.6, 5.0, 2.6, 2.6, 5.8])


E2E_TABLE = [
    ["Sesiones / duración aproximada", "1 / 87,2 s"],
    ["Turnos del agente", "7 (5 con e2e_latency_s)"],
    ["Media · mediana E2E", "2,330 s · 2,741 s"],
    ["Mínimo · máximo E2E", "1,191 s · 3,352 s"],
    ["P95 estimado", "3,237 s (n=5; sin robustez estadística)"],
    ["Mediana por etapa (calculada del log)", "Espera de transcripción final 1,126 s (n=5) · primer token del LLM 1,093 s (n=6) · primer audio TTS 0,318 s (n=7)"],
    ["Turnos sobre 3 s · interrumpidos", "1 de 5 con E2E (3,352 s) · 1 de 7"],
    ["Errores de sesión", "0"],
    ["Persona probada", "Clínica dental (1 de 7); voz humana de un hablante"],
    ["Configuración", "main a d80c419 (PR #16 y #17); Chirp 3 · gemini-3.1-flash-lite · eleven_v4_turbo; record=False"],
    ["Uso registrado", "Gemini 2.493 tokens de entrada y 139 de salida · ElevenLabs 640 caracteres y 42,8 s · Chirp 3 72,0 s de audio"],
]

# Sesión E2E del 17-nov-2026 con DeepSeek (fuente: registro y log sanitizado en EV_DS; recalculado del log el 18-nov)
E2E_DS_TABLE = [
    ["Sesión · duración", "Job AJ_zm9g5TDNqgG5 · 145,9 s (solicitud 22:41:56 a desconexión del cliente 22:44:22)"],
    ["Turnos del agente", "10: 1 saludo estático (sin LLM) + 9 respuestas generadas por el LLM"],
    ["Media · mediana E2E", "2,961 s · 3,264 s (n=8; los turnos 1 y 3 no tienen emparejamiento con un turno de la persona)"],
    ["Mínimo · máximo E2E", "0,557 s (turno interrumpido) · 5,499 s"],
    ["P95 estimado", "5,009 s (n=8; sin robustez estadística)"],
    ["Objetivo de 1 s", "NO CUMPLIDO: 2 de 8 turnos medidos (turnos 2 y 5); 4 de 8 sobre 3 s"],
    ["Medias por etapa", "Primer token del LLM 1,830 s (n=9; mediana 1,788 s) · primer audio TTS 0,293 s (n=10) · espera de transcripción final 1,356 s (n=5, solo valores > 0) · fin de turno 1,097 s (n=8)"],
    ["Errores de sesión", "0 (errors: {})"],
    ["Persona probada", "Clínica dental (1 de 7); voz humana de un hablante; worker local de desarrollo"],
    ["Configuración", "Commit fe88e268, con el mismo árbol Git que main 77ff85c (ed9ad04e68eff160b850308e486cf3c51cf9d060, verificado el 18-nov; no consta que el árbol de trabajo local estuviera limpio durante el ensayo); Chirp 3 · deepseek-flash · eleven_v4_turbo; record=False"],
    ["Uso registrado", "DeepSeek 5.308 tokens de entrada y 1.050 de salida (771 de razonamiento) · ElevenLabs 890 caracteres y 66,6 s · Chirp 3 134,0 s de audio"],
    ["Alcance funcional", "Agendamiento SIMULADO: sin reservas reales, sin Asterisk, sin persistencia empresarial; el texto «queda reservada» es conversacional"],
]

CERT_TABLE = [
    ["pytest (uv run --frozen pytest)", "214 aprobadas, 0 fallidas, 1 advertencia (DeprecationWarning de livekit-agents); 64 s", "Python 3.12 (uv, uv.lock)"],
    ["Vitest (pnpm test)", "91 aprobadas en 14 archivos, 0 fallidas", "Node 24.15.0, pnpm 9.15.9"],
    ["ESLint (pnpm lint)", "0 errores", "Node 24.15.0"],
    ["TypeScript (pnpm typecheck)", "0 errores", "Node 24.15.0"],
    ["Build (next build + generate-csp-headers)", "Correcto", "Node 24.15.0"],
    ["Verificación de out/_headers", "1 encabezado CSP; sin 'unsafe-inline' ni 'unsafe-eval'; script-src con hashes sha256", "Misma comprobación del workflow CI"],
    ["GitHub Actions sobre main (77ff85c)", "Conclusión: success (run 42435613596, 7-nov-2026)", "Consulta con gh run list"],
]


def caption_template(d: Doc) -> None:
    """Toma el estilo de leyenda de figura (centrado, cursiva gris) de D01 para documentos sin figuras."""
    from docx import Document
    src = Document(str(ORIG / "D01_Arquitectura_de_la_Solucion.docx"))
    for par in src.paragraphs:
        if par.text.startswith("Figura 1."):
            d.tpl["caption"] = copy.deepcopy(par._p)
            return
    raise KeyError("leyenda")


def d01_templates(d: Doc) -> None:
    """Plantillas de cuerpo y leyenda tomadas de D01 (mismo estilo en todos los documentos)."""
    from docx import Document
    src = Document(str(ORIG / "D01_Arquitectura_de_la_Solucion.docx"))
    for par in src.paragraphs:
        if par.text.startswith("Este documento describe") and "body" not in d.tpl:
            d.tpl["body"] = copy.deepcopy(par._p)
        if par.text.startswith("Figura 1.") and "caption" not in d.tpl:
            d.tpl["caption"] = copy.deepcopy(par._p)
