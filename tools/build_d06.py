from copy import deepcopy
from fase3_common import *  # noqa: F401,F403
from fase3_docx_lib import Doc
from build_d03 import tbl


def build() -> Path:
    d = Doc(ORIG / "D06_Guia_de_Despliegue_y_Operacion.docx")
    d.capture_templates("1. Qué corre dónde", "4.1 Agente (worker)", "Python: uv run pytest", "Python: uv run pytest", "Python: uv run pytest", "1. El worker está corriendo")
    d01_templates(d)
    cover(d, "D06")
    control_row(d, change=(
        "Actualización de Fase 3 sobre una copia completa de la v1.0 (30-oct). Se actualizaron los conteos de pruebas (214 + 91), la integración continua, el nombre configurable del agente (PR #17) y la referencia al PR #16 fusionado; "
        "se añadieron las secciones 12 a 15 (ensayo de la demostración del 19-nov, verificación previa, qué no declarar y referencias). La v1.0 se conserva sin cambios en Fase 2."))
    d.rep(" (200 pruebas, sin red).", " (214 pruebas al 17-nov sobre main, sin red).")
    d.rep(" (91 pruebas) y ", " (91 pruebas, Node 24.x y pnpm 9.15.9) y ")
    d.rep("pnpm build", "pnpm build")
    d.at(d.par("Web: pnpm typecheck"))
    d.bullet("CI: el workflow .github/workflows/ci.yml repite pytest, Vitest, ESLint, TypeScript y el build en cada PR y push a main (sin secretos ni despliegue). La certificación del 17-nov está en D05 §2.4.")
    d.rep("6.2 Vercel (alternativa, PR #16)", "6.2 Vercel (alternativa; código fusionado con el PR #16)")
    d.rep("Usar la versión del PR #16 (agrupa por ", "Corregido en main desde el PR #16 (agrupa por ")
    t = tbl(d, "Variable", "Dónde", "Obligatoria")
    d.cell_set(t, "LIVEKIT_AGENT_NAME", 3, "Nombre del agente que se despacha: alloxentric-real-time-agent. El worker lo resuelve con la misma variable (PR #17): un worker de desarrollo con otro nombre no atiende los despachos de la demo.")

    d.at_end()
    d.h1("12. Ensayo de la demostración del jueves 19 de noviembre de 2026")
    d.para("[PROPUESTA] Lista de pasos para ensayar y ejecutar la demostración funcional sobre el estado integrado de main (77ff85c). Debe ensayarse al menos una vez antes del 19-nov, con el equipo y la red que se usarán.")
    for i, x in enumerate([
        "Verificar que el checkout técnico está en 77ff85c (o en el commit acordado) y que la CI de ese commit está en verde.",
        "Instalar con uv sync --frozen y pnpm install --frozen-lockfile; ejecutar pytest y pnpm test/lint/typecheck si hay tiempo (D05 §2.4).",
        "Configurar las variables solo en archivos locales ignorados o secretos del hosting; confirmar ADC de Google y claves de LiveKit, LLM y ElevenLabs.",
        "Iniciar el worker (uv run alloxentric-agent dev) con el nombre acordado y confirmar registered worker; precalentamiento de voces activo.",
        "Abrir la Web Demo, ingresar el código temporal, elegir una persona (sugerida: clínica dental, la única con E2E archivado) y conversar al menos 4 turnos, incluyendo una interrupción.",
        "Mostrar la transcripción en vivo, el selector de micrófono, el silencio y el historial local; finalizar la llamada.",
        "Mostrar las métricas del log del worker (solo valores numéricos) y compararlas con D05 §4.6, sin afirmar cumplimiento de 1 s.",
        "Tener un plan B: video grabado del ensayo y capturas sin secretos, por si falla un proveedor o la red.",
    ], start=1):
        d.step(f"{i}.", x)
    d.h1("13. Verificación previa y evidencia de la ejecución")
    d.table_new(["Control", "Resultado esperado", "Fuente"], [
        ["CI de main", "Workflow CI en verde (run 42435613596 sobre 77ff85c)", "gh run list / GitHub Actions"],
        ["Certificación local", "214 Python y 91 web aprobadas; lint, tipos, build y CSP correctos", "D05 §2.4"],
        ["Acceso", "401 sin sesión o con código incorrecto; 403 desde origen ajeno", "TC-07 a TC-09; captura de acceso rechazado"],
        ["Worker", "Registrado en el mismo proyecto de LiveKit y con nombre coincidente", "Log del worker (registered worker)"],
        ["Audio", "Audífonos y micrófono verificados para evitar eco; saludo audible", "Llamada de prueba"],
        ["Evidencia", "Capturas de la conversación y transcripción, sin secretos ni código de acceso", "Fase 3/07_Evidencias/capturas-web-demo-2026-11-17/ (pendientes las de conversación)"],
    ], [3.4, 7.6, 5.6])
    d.h1("14. Qué no declarar en la presentación")
    for x in ["Que se cumple el requisito de 1 s de latencia: las medianas medidas son ≈2,6 a 2,7 s. [CONFIRMADO]",
              "Que existe telefonía con Asterisk, un guion oficial de cobranza, persistencia de negocio o un hosting persistente del worker. [CONFIRMADO]",
              "Que el PR #18 (Anthropic, LiveKit Inference, STT seleccionable) forma parte de la solución: está abierto y sin revisión. [CONFIRMADO]",
              "Que las capturas de la Web Demo son mockups previos al desarrollo: son capturas del producto. [CONFIRMADO]",
              "Que la demostración usa datos reales: todos los escenarios son ficticios y no se debe contactar a personas reales. [CONFIRMADO]"]:
        d.bullet(x)
    d.h1("15. Referencias")
    d.bullet("D01, D03 y D05 v1.1; repositorio técnico en 77ff85c; README y docs/ del repositorio técnico; .github/workflows/ci.yml.")
    out = OUT / "D06_Guia_de_Despliegue_y_Operacion_v1.1_Fase3.docx"
    d.save(out)
    return out


if __name__ == "__main__":
    print(build())
