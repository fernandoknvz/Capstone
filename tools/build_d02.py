from fase3_common import *  # noqa: F401,F403
from fase3_docx_lib import Doc
from build_d03 import tbl


def build() -> Path:
    d = Doc(ORIG / "D02_Plan_de_Respuesta_a_Riesgos.docx")
    d.capture_templates("1. Propósito y método", "", "", "", "", None) if False else None
    d.capture_templates("1. Propósito y método", None, "Se registran 20", "R-01 · Latencia", "Figura 1.", None) if False else None
    # plantillas: encabezados y viñetas de este documento; cuerpo y leyenda de D01
    from copy import deepcopy
    d.tpl["h1"] = deepcopy(d.par("1. Propósito y método")._p)
    d.tpl["h2"] = deepcopy(d.par("1. Propósito y método")._p)
    d.tpl["bullet"] = deepcopy(next(p._p for p in d.doc.paragraphs if p.style.name == "List Bullet"))
    d01_templates(d)
    cover(d, "D02")
    control_row(d, change=(
        "Actualización de Fase 3 sobre una copia completa de la v1.0 (30-oct). Se mantienen los 20 riesgos, fichas y protocolos originales y se añade la sección 9 con la revaloración al 17-nov, "
        "los riesgos R-21 y R-22 (propuestos) y la actualización de las lecciones. La v1.0 se conserva sin cambios en Fase 2."))
    d.rep("Los identificadores corresponden al registro de la sección 3.", "Los identificadores corresponden al registro de la sección 3. Figura del 30-oct (20 riesgos); R-21 y R-22 se agregan en la sección 9.")
    d.at(d.par("Se registran 20 riesgos"))
    d.para("[CONFIRMADO] Actualización del 17-nov-2026: el registro, las fichas y los protocolos de las secciones 3 a 8 conservan su redacción del 30-oct. La sección 9 incorpora la revaloración al 17-nov y dos riesgos nuevos (R-21 y R-22); con ellos el registro suma 22 riesgos.")

    d.at_end()
    d.h1("9. Actualización al 17 de noviembre de 2026")
    d.para("Revaloración basada en evidencia verificable del repositorio técnico (main 77ff85c), de la CI y de las sesiones E2E. Las valoraciones nuevas son [PROPUESTA] hasta que el equipo las apruebe.")
    d.table_new(["Riesgo", "Estado al 30-oct", "Cambio verificado al 17-nov", "Estado propuesto"], [
        ["R-01 Latencia de voz a voz > 1 s", "Materializado (mediana 2,59 s)", "El E2E del 31-oct confirma el orden de magnitud: mediana 2,74 s (n=5), 1 turno sobre 3 s. Sin mejora medida; las alternativas de STT están en el PR #18 (abierto, no integrado).", "Materializado; sin cambio"],
        ["R-03 Retraso de un componente", "Mitigado", "Los PR #16 y #17 se fusionaron el 30 y 31-oct; el pipeline completo está en main.", "Mitigado"],
        ["R-11 Falla del despliegue web", "Materializado", "Pruebas de regresión y CI (PR #19) cubren el empaquetado y la CSP; el build y la verificación de out/_headers pasaron el 17-nov.", "Materializado; control reforzado"],
        ["R-12 Worker no disponible", "Activo", "Sigue ejecutándose en un equipo del equipo. El nombre configurable (PR #17) evita despachos cruzados, pero no resuelve el hosting persistente.", "Activo; crítico para la demostración del 19-nov"],
        ["R-17 Evidencias y registros Scrum insuficientes", "Activo", "Se recuperaron D01-D06, E01, logs E2E sanitizados con SHA-256 y un registro consolidado de evidencias; siguen sin adjuntar backlog, actas y registros de CoreStream.", "Activo; parcialmente mitigado"],
        ["R-18 Desviaciones sin aprobación formal", "Activo", "Persisten sin acta el cambio de STT, el uso de LLM y la autorización de Gemini; se añadió el PR #18 como nueva desviación propuesta.", "Activo"],
        ["R-19 Tiempo insuficiente", "Activo (crítico)", "La evaluación de Fase 3 es el jueves 19-nov-2026; quedan pocos días para ensayo, capturas de conversación y presentación.", "Activo (crítico)"],
    ], [4.0, 2.6, 7.2, 3.0])
    d.h2("9.1 Riesgos nuevos")
    d.table_new(["ID", "Riesgo", "Categoría", "Prob.", "Impacto", "Nivel", "Estado"], [
        ["R-21", "Documentación obligatoria de Fase 3 no confirmada: no existe la pauta oficial en los repositorios y solo se conoce la lista informada por el equipo.", "Planificación / alcance", "Alta", "Alto", "Crítico", "Activo [PROPUESTA]"],
        ["R-22", "Presentar como implementado lo que no está integrado (PR #18, Asterisk, persistencia, cobranza oficial) o cambiar el alcance del proyecto sin autorización.", "Gestión / integridad académica", "Media", "Alto", "Alto", "Activo [PROPUESTA]"],
    ], [1.3, 6.0, 2.4, 1.2, 1.4, 1.4, 2.8])
    d.table_new(["ID", "Señal de alerta", "Respuesta propuesta", "Responsable sugerido"], [
        ["R-21", "El docente pide un documento que no está en la lista; la pauta cambia.", "Pedir la pauta por escrito; usar la tabla de D03 §12 como lista de verificación y completar los elementos [PENDIENTE] según prioridad.", "Fernando (coordinación)"],
        ["R-22", "Una diapositiva o un documento afirma algo sin prueba ni evidencia en la matriz de trazabilidad.", "Revisión cruzada de la presentación contra la matriz; rótulo explícito «no integrado» o «pendiente»; mantener el nombre Alloxentric Real Time Agent.", "David (revisión) y Juan"],
    ], [1.3, 5.0, 7.6, 2.6])
    d.h2("9.2 Lecciones de las últimas semanas")
    for x in ["Un nombre de agente compartido provocó despachos cruzados entre workers de desarrollo; se corrigió con el nombre configurable (PR #17). [CONFIRMADO]",
              "Un PR (#19) se fusionó sin aprobación independiente; la CI y el PR #20 documentan las ejecuciones, pero el control humano quedó incompleto. [CONFIRMADO]",
              "Las pruebas locales pueden fallar por el entorno (Node 22, layout de pnpm en Windows); el CI en Ubuntu sirve como referencia reproducible. [CONFIRMADO]",
              "Las cifras de pruebas deben citarse con su corte (200/91, 214, 281/103) para no mezclar ramas distintas. [CONFIRMADO]"]:
        d.bullet(x)
    d.h1("10. Conclusiones y referencias")
    d.para("Los riesgos críticos siguen siendo la latencia, la dependencia del cliente para guion y telefonía, y el tiempo. Se suman dos riesgos de cierre académico (R-21 y R-22) que se controlan con la pauta oficial y una revisión cruzada de lo que se afirma en la presentación. [PROPUESTA]")
    d.bullet("Referencias: D01, D03, D05 y D06 v1.1; repositorio técnico en 77ff85c; Fase 3/07_Evidencias; Fase 3/MATRIZ_TRAZABILIDAD_PRELIMINAR.md.")
    out = OUT / "D02_Plan_de_Respuesta_a_Riesgos_v1.1_Fase3.docx"
    d.save(out)
    return out


if __name__ == "__main__":
    print(build())
