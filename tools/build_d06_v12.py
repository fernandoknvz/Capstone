"""D06 v1.2: estado de despliegue y limitaciones de la demostración (Etapa 2, 19-nov-2026).

Base: D06 v1.1 (Fase 3/Entregables/_historico).
"""
from fase3_v2 import *  # noqa: F401,F403


def build() -> Path:
    d = Doc(HIST / "D06_Guia_de_Despliegue_y_Operacion_v1.1_Fase3.docx")
    d.capture_templates("1. Qué corre dónde", None, "Se cargan desde", "Que se cumple el requisito", "Que se cumple el requisito", "1. Clonar el repositorio")
    cover_v2(d, "17 de noviembre de 2026", "D06", "1.2")
    control_row(d, version="1.2", date=DATE_V2, change=(
        "Versión 1.2 (saneamiento tras la auditoría del 19-nov, AUD-12): se declara el estado real de despliegue (worker local, demostración bajo demanda, sin producción permanente), "
        "se documentan las limitaciones de la demostración, se actualiza la referencia a la evidencia E2E del 17-nov y las cifras de latencia de la sección 14; se actualizaron nombres de portada. "
        "La v1.1 se conserva en Fase 3/Entregables/_historico."))

    # --- 1: estado de despliegue
    t = tbl(d, "Pieza", "Dónde corre hoy", "Cómo se inicia")
    d.cell_set(t, "Agente de voz", 3, "Si se apaga, la web carga pero no hay llamadas. No existe worker persistente ni despliegue permanente [PENDIENTE].")
    d.cell_set(t, "Web demo + funciones", 3, "Solo sirve la web y los tokens; no aloja al agente. Se habilita bajo demanda con DEMO_ENABLED; no es una producción permanente.")
    d.at(t)
    para_sb(d, "[CONFIRMADO] Estado de despliegue al 19-nov-2026. La demostración E2E del 17-nov se ejecutó con la Web Demo servida localmente con Netlify CLI y un worker local de desarrollo (nombre alloxentric-real-time-agent-dev), sin hosting persistente del worker. "
           "La Web Demo publicada solo atiende llamadas mientras haya un worker registrado con el mismo nombre y DEMO_ENABLED esté activo; su disponibilidad depende de un equipo del grupo. "
           "No se declara producción permanente: tampoco existen telefonía con Asterisk, base de datos de negocio ni integración con una agenda o CRM.")

    # --- 12: ensayo
    p = P(d, "12. Ensayo de la demostración del jueves 19", nth=1)
    d.set_par(p, "12. Ensayo y ejecución de la demostración")
    p = P(d, "[PROPUESTA] Lista de pasos para ensayar")
    d.set_par(p, "[PROPUESTA] Lista de pasos para ensayar y ejecutar la demostración funcional sobre el estado integrado de main (77ff85c). El ensayo local del 17-nov (E2E con DeepSeek, D05 §4.7) es el primer registro de una sesión completa con la Web Demo; conviene repetirlo con el equipo y la red de la presentación antes de la entrega del 21-nov-2026 (fecha indicada por el equipo).")
    d.at(P(d, "8. Tener un plan B"))
    para_sb(d, "Limitaciones de la demostración (declarar al presentarla):")
    for x in ["El agendamiento de la clínica dental es una simulación conversacional: «queda reservada» es texto del agente, no una reserva; no hay agenda, CRM, base de datos ni Asterisk.",
              "La demostración valida el pipeline conversacional (voz → STT → LLM → TTS → voz) con una persona ficticia; no valida el proceso de cobranza ni el guion oficial.",
              "Solo la persona clínica dental tiene E2E archivado; las otras seis personas no se han validado con logs.",
              "El worker corre en un computador del equipo con credenciales propias; si el proveedor de LLM falla (como Gemini el 17-nov con API_KEY_INVALID) hay que cambiar LLM_PROVIDER y avisar que es una decisión del equipo.",
              "La latencia medida (medianas de 2,6 a 3,3 s) no cumple el requisito de 1 s."]:
        d.bullet(x)

    # --- 13
    t = tbl(d, "Control", "Resultado esperado", "Fuente")
    d.cell_set(t, "Evidencia", 2, "Fase 3/07_Evidencias: capturas de la Web Demo (capturas-web-demo-2026-11-17/), de la conversación (E2E-2026-11-17-clinica-dental-deepseek/capturas/) y de la demostración (Demo_E2E_2026-11-17/); faltan las del cierre y del historial de esa sesión")

    # --- 14
    p = P(d, "Que se cumple el requisito de 1 s")
    d.set_par(p, "Que se cumple el requisito de 1 s de latencia: las medianas medidas son ≈2,6 a 3,3 s (30-oct, 31-oct y 17-nov). [CONFIRMADO]")
    p = P(d, "Que la demostración usa datos reales")
    d.at(p)
    d.bullet("Que la demostración con la clínica dental valida el proceso de cobranza o que el agendamiento es real: es una simulación del pipeline conversacional. [CONFIRMADO]")
    d.bullet("Que existe producción permanente, o que las instrucciones atribuidas a Max (por ejemplo, el cambio de STT o el uso de un LLM) fueron aprobadas formalmente: no hay acta ni aprobación verificable. [CONFIRMADO]")
    d.bullet("Que CoreStream, herramienta de Alloxentric, acredita el avance o los hitos del proyecto: el reporte agregado (EV-20) no contiene tickets y su 4 % de eficiencia no es un porcentaje de avance. [CONFIRMADO]")

    # --- 15
    p = P(d, "D01, D03 y D05 v1.1; repositorio técnico")
    d.set_par(p, "D01 v1.2, D03 v1.2 y D05 v1.3; repositorio técnico en 77ff85c; README y docs/ del repositorio técnico; .github/workflows/ci.yml.")

    out = OUT / "D06_Guia_de_Despliegue_y_Operacion_v1.2_Fase3.docx"
    d.save(out)
    return out


if __name__ == "__main__":
    print(build())
