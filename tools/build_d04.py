from copy import deepcopy
from fase3_common import *  # noqa: F401,F403
from fase3_docx_lib import Doc


def build() -> Path:
    d = Doc(ORIG / "D04_Estado_de_Avance_del_Proyecto.docx")
    d.tpl["h1"] = deepcopy(d.par("1. Resumen ejecutivo")._p)
    d.tpl["h2"] = deepcopy(d.par("1. Resumen ejecutivo")._p)
    d01_templates(d)
    d.tpl["bullet"] = d.tpl["body"]
    cover(d, "D04")
    d.set_par(d.par("Qué se ha hecho"), "Qué se ha hecho hasta el 30 de octubre de 2026 (corte original) y estado actualizado al 17 de noviembre de 2026")
    control_row(d, change=(
        "Actualización de Fase 3 sobre una copia completa de la v1.0 (corte 30-oct). Las secciones 1 a 8 conservan su redacción y sus cifras del 30-oct; la nueva sección 9 presenta el estado al 17-nov-2026 "
        "(main 77ff85c): indicadores, línea de tiempo, estado por componente, objetivos, plan, evidencias y próximos pasos hasta la evaluación del 19-nov. La v1.0 se conserva sin cambios en Fase 2."))
    d.at(d.par("A la fecha de corte del informe grupal 2.4"))
    d.para("[CONFIRMADO] Actualización del 17-nov-2026: las secciones 1 a 8 describen el corte del 30-oct (PR #16 abierto en ese momento). La sección 9 recoge el estado verificado al 17-nov; allí el PR #16 figura fusionado.")

    d.at_end()
    d.h1("9. Estado al 17 de noviembre de 2026")
    d.h2("9.1 Indicadores")
    d.table_new(["Indicador", "Corte 30-oct", "Corte 17-nov (main 77ff85c)"], [
        ["Pull Requests fusionados", "15 (#1 a #15); #16 abierto", "19 fusionados (#1 a #17, #19 y #20); #18 abierto sin revisión"],
        ["Pruebas automatizadas", "200 Python y 91 web (rama del PR #16)", "214 Python y 91 web ejecutadas el 17-nov sobre main; CI en verde (run 42435613596)"],
        ["Integración continua", "No existía", "GitHub Actions desde el PR #19 (7-nov); 3 ejecuciones documentadas"],
        ["Medición de latencia", "Mediana 2,59 s (n=13)", "Mediana 2,59 s (E01, n=13) y 2,74 s (E2E 31-oct, n=5); no cumple 1 s"],
        ["Escenarios y Web Demo", "7 personas; Netlify y Vercel (PR #16 abierto)", "7 personas, historial y selector de micrófono integrados (PR #16); nombre del agente configurable (PR #17)"],
        ["Evidencia E2E archivada", "E01 (extracto numérico)", "E01 + logs del worker y de Netlify CLI del 31-oct con SHA-256 verificados"],
        ["Telefonía Asterisk, guion oficial, comparación de costos", "No iniciados", "No iniciados (dependen del cliente)"],
    ], [4.4, 4.6, 7.6])
    d.h2("9.2 Línea de tiempo posterior al 30-oct")
    d.table_new(["Fecha", "Hito", "PR / evidencia"], [
        ["30-oct", "Fusión de agentes por persona, voces chilenas, rediseño web, optimizaciones y despliegue en Vercel.", "PR #16 (fusionado el 30-oct, 20:43)"],
        ["31-oct", "Nombre del agente configurable; sesión E2E de la clínica dental con log del worker.", "PR #17 (fusionado el 31-oct); logs sanitizados con SHA-256"],
        ["4-nov", "Propuesta de LLM Anthropic/Inference, STT seleccionable y optimizaciones.", "PR #18 abierto, sin revisión; no integrado"],
        ["7-nov", "Integración continua con GitHub Actions y documentación de sus ejecuciones.", "PR #19 y #20 (fusionados); runs 42433340255, 42433603292, 42435613596"],
        ["14-nov", "Planilla de evaluación de Fase 2 en el repositorio académico: nota 4,5 y brecha principal en evidencias (sin comentarios textuales del docente).", "Commit 93b6c79 en main del repositorio académico"],
        ["17-nov", "Recuperación documental, certificación de pruebas sobre main y actualización de D01 a D06.", "Rama docs/fase3-recuperacion-documental; Fase 3/07_Evidencias"],
    ], [1.8, 9.2, 5.6])
    d.h2("9.3 Estado por componente")
    d.table_new(["Componente", "Responsable (verificable)", "Implementado", "Probado", "En main", "Observación"], [
        ["Base LiveKit, pipeline, métricas, CI y nombre configurable", "Fernando", "Sí", "Sí", "Sí", "PR #2, #7, #9, #10, #17, #19, #20"],
        ["STT Google Chirp 3", "Juan", "Sí", "Sí", "Sí", "PR #6; 14 pruebas; operativo en E01 y E2E"],
        ["LLM DeepSeek y Gemini", "Fernando; optimización de Juan", "Sí", "Sí", "Sí", "DeepSeek real solo reportado; Gemini operativo en E2E"],
        ["TTS ElevenLabs", "David (ajustes de Juan)", "Sí", "Sí", "Sí", "PR #4; 14 pruebas; operativo en E2E"],
        ["Web Demo, seguridad y 7 personas", "Fernando y Juan", "Sí", "Sí (91 pruebas)", "Sí", "PR #11 a #16; E2E solo con la persona clínica dental"],
        ["STT seleccionable y LLM adicionales", "Juan", "En rama", "En rama (281/103)", "No", "PR #18 abierto; no integrado"],
        ["Telefonía Asterisk", "—", "No", "No", "No", "Depende de accesos de Alloxentric [PENDIENTE]"],
        ["Guion oficial y comparación de costos", "—", "No", "No", "No", "Depende de Alloxentric [PENDIENTE]"],
    ], [4.2, 3.4, 1.8, 2.1, 1.3, 3.8])
    d.para("La autoría se basa en commits y PR; los merges no se cuentan como autoría del contenido fusionado. Las decisiones tomadas en reuniones externas requieren actas para respaldo académico. [PENDIENTE DE VALIDACIÓN]")
    d.h2("9.4 Avance por objetivo específico (17-nov)")
    d.table_new(["Objetivo específico", "Estado 30-oct", "Estado 17-nov", "Justificación"], [
        ["1. Guion, intenciones, requerimientos y protocolo comparativo", "Parcial", "Parcial", "D03 v1.1 actualizado; faltan guion oficial, intenciones y protocolo."],
        ["2. Diseño de integración y flujo conversacional", "Parcial", "Parcial (mejorado)", "D01 v1.1 con casos de uso, actividad, módulos y almacenamiento; falta Asterisk."],
        ["3. Prototipo con voz adecuada al contexto chileno", "Parcial", "Parcial", "Prototipo en main con 7 escenarios ficticios; sin validación auditiva ni guion oficial."],
        ["4. Planificar y gestionar con Scrum", "Parcial", "Parcial", "PR por ticket y CI; siguen pendientes backlog, sprints y actas."],
        ["5. Pruebas funcionales, de integración y de voz, incluida la latencia", "Parcial", "Parcial (mejorado)", "214 + 91 pruebas verificadas el 17-nov, CI y E2E 31-oct; latencia sin cumplir 1 s."],
        ["6. Comparar costo y efectividad", "No iniciado", "No iniciado", "Sin protocolo, tarifas ni datos de referencia."],
    ], [5.2, 2.2, 2.6, 6.6])
    d.h2("9.5 Plan hasta la evaluación del jueves 19-nov")
    d.table_new(["Actividad", "Estado al 17-nov", "Responsable sugerido"], [
        ["Obtener la pauta oficial y confirmar los documentos obligatorios", "Pendiente", "Fernando"],
        ["Ensayar la demostración completa sobre main y preparar respaldo en video", "Pendiente", "Fernando y David"],
        ["Capturar la conversación y la transcripción en vivo (evidencia visual)", "Pendiente", "David"],
        ["Revisión cruzada de D01 a D06 e Informe", "Pendiente", "Los tres integrantes"],
        ["Reunir backlog, actas y registros de CoreStream disponibles", "Pendiente", "David (Scrum Master)"],
        ["Preparar la presentación: problema, solución y arquitectura, demostración", "Pendiente", "Equipo"],
    ], [8.2, 3.2, 5.2])
    d.h2("9.6 Evidencias y pendientes")
    d.para("Disponibles: D01 a D06 v1.1, E01, logs E2E del 31-oct con hash verificado, certificación del 17-nov, capturas de la Web Demo y registro consolidado de evidencias. Pendientes: pauta oficial de Fase 3, actas y registros de CoreStream, guion y flujo de Hites, capturas de conversación real y pruebas con Asterisk. [CONFIRMADO]")
    d.h1("10. Conclusiones y referencias")
    d.para("El proyecto pasó de componentes aislados (10-oct) a un MVP de voz funcional con web, métricas, seguridad y CI (17-nov). El avance académico depende ahora de cerrar la evidencia verificable, ensayar la demostración y declarar con precisión lo no integrado y lo pendiente. [CONFIRMADO]")
    d.bullet("Referencias: repositorio técnico en 77ff85c (PR #1 a #17, #19 y #20; PR #18 abierto), D01, D02, D03, D05 y D06 v1.1, Fase 3/07_Evidencias y Fase 3/MATRIZ_TRAZABILIDAD_PRELIMINAR.md.")
    out = OUT / "D04_Estado_de_Avance_del_Proyecto_v1.1_Fase3.docx"
    d.save(out)
    return out


if __name__ == "__main__":
    print(build())
