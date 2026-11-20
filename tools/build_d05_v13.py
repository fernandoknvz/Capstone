"""D05 v1.3: rebaja de estados de prueba según el respaldo archivado (Etapa 2, 19-nov-2026).

Base: D05 v1.2 (Fase 3/Entregables/_historico). No modifica ninguna métrica original.
"""
from fase3_v2 import *  # noqa: F401,F403


def unbold(p) -> None:
    """set_par hereda el formato del primer run (un encabezado en negrita); se deja el texto normal y solo las etiquetas en negrita."""
    from fase3_docx_lib import TAG_RE
    for r in p.runs:
        if not TAG_RE.fullmatch(r.text.strip() or "x"):
            r.bold = False


def build() -> Path:
    d = Doc(HIST / "D05_Plan_de_Pruebas_y_Resultados_v1.2_Fase3.docx")
    d.capture_templates("1. Propósito y estrategia", "2.1 Resultado", "Define cómo se comprueba", "Requisito de 1 s", "Figura 1.", None)
    cover_v2(d, "18-nov-2026", "D05", "1.3", long_date=False)
    control_row(d, version="1.3", date=DATE_V2, change=(
        "Versión 1.3 (saneamiento probatorio tras la auditoría del 19-nov, hallazgos AUD-08 y AUD-09): se rebajaron TC-02, TC-03, TC-04, TC-07 a TC-10 y TC-17 al respaldo realmente archivado; "
        "se clasificó cada cifra de las secciones 4.1 a 4.3 como reportada y no reproducible; se declaró el método de cálculo de percentiles; se corrigió la hora de la ejecución de CI; "
        "se incorporó la evidencia DART-14-2.5 del 19-oct (E10, sanitizada) y el caso TC-24; se actualizaron nombres de portada. No se modificó ninguna métrica original. "
        "La v1.2 se conserva en Fase 3/Entregables/_historico."))

    # --- 2.4: hora de la ejecución de CI
    t = tbl(d, "Verificación", "Resultado del 17-nov")
    d.cell_set(t, "GitHub Actions sobre main", 1, "Conclusión: success (run 42435613596, 7-nov-2026 hora de Chile; 8-nov 01:45 UTC según la certificación)")

    p = P(d, "Resultado histórico del 30 de octubre de 2026")
    d.set_par(p, p.text.replace("200 pruebas de Python y 91 de la web", "200 de Python y 91 de la web"))

    # --- 4: cómo leer
    p = P(d, "Cómo leer esta sección")
    d.set_par(p, "Cómo leer esta sección. Son mediciones propias, con pocas muestras, desde Chile y con audio sintético o voz humana según el caso. Sirven para elegir entre opciones, no como benchmark. "
                 "En la v1.3 cada cifra se clasifica por su respaldo: VERIFICADA (archivo original en el repositorio y recálculo del 19-nov), PARCIAL (parte respaldada y parte reportada), "
                 "REPORTADA (informada por el equipo sin salida bruta archivada) y NO REPRODUCIBLE (no puede repetirse a partir del repositorio: faltan las salidas originales y repetirla exige credenciales y servicios de pago). "
                 "Quedan VERIFICADAS las secciones 4.4 (E01), 4.6 y 4.7; las secciones 4.1 a 4.3 y 4.5 son [REPORTADO POR EL EQUIPO] y no reproducibles.")
    unbold(p)

    # --- 4.1 Gemini
    d.at(tbl(d, "Modelo", "Thinking por defecto"))
    para_sb(d, "Respaldo (v1.3): [REPORTADO POR EL EQUIPO], NO REPRODUCIBLE. No existen las salidas de las corridas; las cifras figuran transcritas en un comentario de config.py y en el README del repositorio técnico, que son registros secundarios. "
           "Esta tabla mide el tiempo al primer token con un script y no es comparable con el primer token del LLM en sesión real (E01: mediana 0,93 s con gemini-3.1-flash-lite; sección 4.4), que se midió con otra herramienta y condiciones. [INFERENCIA]")

    # --- 4.2 ElevenLabs
    d.at(tbl(d, "Modelo", "Primer audio (HTTP)"))
    para_sb(d, "Respaldo (v1.3): la comparación de modelos de esta tabla es [REPORTADO POR EL EQUIPO] y NO REPRODUCIBLE (sin salidas archivadas; el README del repositorio técnico transcribe solo 0,50–0,52 s frente a 0,48–0,49 s). "
           "En cambio, el primer audio del modelo elegido en sesiones reales está VERIFICADO: mediana 0,314 s en E01 (n=22), 0,318 s el 31-oct (n=7) y 0,293 s el 17-nov (n=10), recalculadas desde los archivos. [CONFIRMADO]")
    p = P(d, "Arranque en frío")
    d.set_par(p, "Arranque en frío: la primera síntesis con cada una de las 12 voces chilenas probadas tardó 3,8 a 6,4 s; desde la segunda bajó a 0,28–0,47 s. [REPORTADO POR EL EQUIPO] Esta cifra no está respaldada por archivos ni por el repositorio técnico, cuyo README indica «4–6 s» para las 7 voces configuradas. "
                 "Por eso el worker precalienta las voces al iniciar (PR #16).")
    unbold(p)

    # --- 4.3 Chirp
    d.at(tbl(d, "Configuración", "Resultado final tras terminar la frase"))
    para_sb(d, "Respaldo (v1.3): [REPORTADO POR EL EQUIPO], NO REPRODUCIBLE. Dos muestras por configuración, sin salidas archivadas; la cifra figura en el README del repositorio técnico. "
           "La prueba real del 16-oct (frase sintética de 4,24 s transcrita correctamente, es-US) de la sección 3 tampoco tiene archivo original. La espera de la transcripción final en sesiones reales sí está VERIFICADA (E01 mediana 1,206 s, n=13; 31-oct 1,126 s, n=5; 17-nov: valores > 0 con media 1,356 s, n=5).")

    # --- 4.4 método de percentiles
    d.at(tbl(d, "Métrica (segundos)", "n", "Mediana"))
    para_sb(d, "Método de cálculo (recalculado el 19-nov-2026 desde E01 y los logs del 31-oct y del 17-nov con un script propio sobre las líneas «turn»; no se modificó ninguna métrica original). "
           "Medianas y medias son las habituales y coinciden con las tablas. El P90 de la tabla anterior (3,33 s) corresponde al método de rango más cercano (el 12.º de 13 valores ordenados); con interpolación lineal sería 3,27 s. "
           "Los P95 de las secciones 4.6 (3,237 s) y 4.7 (5,009 s) usan interpolación lineal entre valores ordenados. Con n = 13, 5 y 8 los percentiles altos no son estadísticamente robustos. "
           "No se calculan sobre muestras combinadas. [CONFIRMADO]")

    # --- 5: catálogo
    p = P(d, "Estado: OK ejecutada y aprobada")
    d.set_par(p, "Estado: OK ejecutada y aprobada · OK* aprobada con observación · No cumple · Auto cubierta por pruebas automáticas · Parcial confirmada solo en parte · Rep. reportada por el equipo sin respaldo archivado · NV no verificable con la evidencia disponible · Pend. pendiente de ejecutar o sin acceso. "
                 "Los estados de TC-02, TC-03, TC-04, TC-07 a TC-10 y TC-17 se rebajaron en la v1.3 porque la evidencia archivada no sostenía el resultado completo (los logs no registran texto de conversación por diseño).")
    t = tbl(d, "ID", "Caso", "Resultado esperado")
    d.cell_set(t, "TC-01", 4, "Sesiones del 30-oct (E01), E2E del 31-oct y 17-nov (clínica dental) y prueba de una frase del 19-oct (E10); latencia sobre el requisito")
    d.cell_set(t, "TC-02", 3, "Parcial")
    d.cell_set(t, "TC-02", 4, "Primer audio 0,3–0,4 s medido en sesiones reales (E01, 31-oct y 17-nov). El saludo con su voz solo está visible en la persona clínica dental (capturas del 17-nov); las otras seis personas no tienen evidencia. test_personas.py (saludo de hasta 30 palabras por persona) y test_voices.py (voz por persona) verifican la configuración, no la reproducción.")
    d.cell_set(t, "TC-03", 3, "Parcial")
    d.cell_set(t, "TC-03", 4, "Funcionamiento confirmado: stt_usage en los logs y texto transcrito visible en Agent Console (19-oct, E10) y en la transcripción en vivo (17-nov, E08). Exactitud NO medida: los logs no guardan texto, no hay frase de referencia ni tasa de error. Prueba del 16-oct con frase sintética de 4,24 s [REPORTADO POR EL EQUIPO]")
    d.cell_set(t, "TC-04", 3, "Parcial / NV")
    d.cell_set(t, "TC-04", 4, "Largo: el prompt exige una o dos frases (máx. 25 palabras) [CONFIRMADO en código]; indicio indirecto de respuestas cortas: ≈23 tokens de salida por respuesta el 31-oct (139 en 6 respuestas) y ≈31 no razonados el 17-nov ((1.050 − 771) en 9) [INFERENCIA]. Coherencia y personaje: NV (sin criterios objetivos ni textos archivados; solo capturas del 17-nov). «Una respuesta superó el largo pedido; prompt endurecido» [REPORTADO POR EL EQUIPO]")
    d.cell_set(t, "TC-07", 3, "Auto + Parcial")
    d.cell_set(t, "TC-07", 4, "login.test.ts (8) y session.test.ts (4); captura del rechazo con el mensaje de error (17-nov, servidor local; Figura 4). La prueba en producción del 30-oct es [REPORTADO POR EL EQUIPO], sin archivo")
    d.cell_set(t, "TC-08", 3, "Auto + Rep.")
    d.cell_set(t, "TC-08", 4, "origin.test.ts (4) y login.test.ts [CONFIRMADO]. La prueba en producción del 30-oct es [REPORTADO POR EL EQUIPO], sin archivo")
    d.cell_set(t, "TC-09", 3, "Auto + Rep.")
    d.cell_set(t, "TC-09", 4, "livekit-token.test.ts (4) y session.test.ts [CONFIRMADO]; el log de Netlify del 17-nov registra un 401 en la consulta de sesión previa al login. La prueba en producción del 30-oct es [REPORTADO POR EL EQUIPO], sin archivo")
    d.cell_set(t, "TC-10", 3, "Auto + Rep.")
    d.cell_set(t, "TC-10", 4, "csp-headers.test.ts (5), vercel-postbuild.test.ts (5) y verificación de out/_headers en el build del 17-nov [CONFIRMADO]. La respuesta de producción es [REPORTADO POR EL EQUIPO], sin archivo")
    d.cell_set(t, "TC-17", 3, "NV")
    d.cell_set(t, "TC-17", 4, "Diseño verificado en código: las personas de cobranza prohíben amenazas y exigen confirmar la identidad antes de hablar de la deuda con terceros; test_personas.py comprueba que el prompt contenga esas reglas, no el comportamiento del LLM. No hay E2E con una persona de cobranza ni textos o criterios objetivos archivados. «Probado con la voz sintética» [REPORTADO POR EL EQUIPO]")
    d.cell_set(t, "TC-14", 4, "Mediana 2,59 s (n=13, 30-oct), 2,74 s (n=5, 31-oct) y 3,26 s (n=8, 17-nov); método de percentiles en 4.4")
    d.add_row(t, ["TC-24", "Validación E2E con una frase desde Agent Console (19-oct, DART-14-2.5).", "El agente recibe audio, transcribe, responde y devuelve audio; sesión cerrada sin errores.", "OK*", "E10 (sanitizada). STT confirmado por la pregunta visible; LLM inferido; audio solo por testimonio del operador; sin latencia; errores de liberación de recursos al apagar el worker (OBS-03). Una sola frase"])

    # --- 7: hallazgos
    t = tbl(d, "Hallazgo", "Cómo se detectó", "Corrección")
    d.add_row(t, ["Estados OK de TC-03, TC-04 y TC-17 (y TC-02, TC-07 a TC-10) por encima de la evidencia archivada", "Auditoría del 19-nov (AUD-08, AUD-09)", "Rebajados en la v1.3; para recuperarlos hacen falta entradas, salidas y criterios objetivos (por ejemplo frases de referencia con tasa de error, o un protocolo de revisión semántica)", "Corregido en este documento; evidencia pendiente"])
    d.add_row(t, ["Cifras de las secciones 4.1 a 4.3 sin salidas brutas archivadas", "Auditoría del 19-nov (AUD-08)", "Etiquetadas como reportadas y no reproducibles; se mantienen sin cambios las cifras", "Corregido en este documento; evidencia pendiente"])
    d.add_row(t, ["Errores de liberación de recursos al apagar el worker (FfiHandle, «Task was destroyed but it is pending»)", "Informe DART-14-2.5 del 19-oct (OBS-03, E10)", "No investigados; los logs sanitizados del 31-oct y del 17-nov registran sesiones cerradas sin errores (errors {}), pero omiten las pilas de avisos, por lo que no permiten confirmar si se repitieron", "Pendiente"])

    # --- 8: limitaciones
    d.at(P(d, "La certificación del 17-nov se hizo en un solo equipo"))
    d.bullet("Los logs no registran texto de conversación por diseño: la exactitud del STT, la coherencia de las respuestas del LLM y la conducta de cobranza no pueden verificarse con ellos. Para esos criterios solo existen capturas de una sesión (17-nov) y de una frase (19-oct).")
    d.bullet("Las cifras de las secciones 4.1 a 4.3 son reportadas y no reproducibles; las del 26-oct tampoco tienen logs. Los estados «Parcial», «Rep.» y «NV» del catálogo indican esa brecha.")

    # --- 9: evidencias
    t = tbl(d, "Código", "Archivo", "Contenido")
    d.add_row(t, ["E10", EV_D25 + "README.md (y DART-14-2.5_informe_sanitizado.md, captura_agent_console_recortada.png)", "Informe DART-14-2.5 del 19-oct (EV-22 del registro consolidado), versión sanitizada (texto sin cambios y captura recortada a la consola). SHA-256 del original FB5A857F5BBEB5B8B8EC61BDC788EEBE6E39851A465EFA77FD79E0E7C89E7AC3 (fuera de Git); hashes de los archivos archivados en SHA256SUMS.txt. Una frase; sin latencia."])

    # --- 11 y 12
    p = P(d, "Las pruebas automáticas están en verde sobre main")
    d.set_par(p, "Las pruebas automáticas están en verde sobre main: 214 de Python y 91 de la web, con lint, tipos, build y CSP verificados, además de la CI. El flujo de voz a voz funciona desde el navegador según tres fuentes de medición (E01, E2E del 31-oct con Gemini y E2E del 17-nov con DeepSeek, esta última aprobada con observaciones, con 9 respuestas generadas y sin errores) y una prueba de una frase del 19-oct (E10), pero la latencia (medianas ≈2,6 a 3,3 s) no cumple el requisito de 1 s (2 de 8 turnos en la última sesión). "
                 "El agendamiento es simulado: no hay reservas reales, integración con Asterisk, persistencia empresarial ni worker persistente, y tampoco validación con el guion oficial. "
                 "La evidencia archivada sostiene que el pipeline funciona y mide su latencia, pero no la exactitud del STT, la coherencia de las respuestas ni la conducta de cobranza (TC-03, TC-04 y TC-17 figuran como parcial o no verificable), ni las comparativas de proveedores de las secciones 4.1 a 4.3, que son reportadas. "
                 "La demostración con la clínica dental valida el pipeline conversacional, no el proceso de cobranza. [CONFIRMADO]")
    p = P(d, "D01 v1.1 (arquitectura y diseño)")
    d.set_par(p, "D01 v1.2 (arquitectura y diseño), D03 v1.2 (requerimientos y casos de uso) y D06 v1.2 (operación), en Fase 3/Entregables.")
    d.at(P(d, "Fase 3/07_Evidencias: E01 (en Fase 2)"))
    d.bullet("Evidencia DART-14-2.5 sanitizada del 19-oct (E10): " + EV_D25 + ". Versiones anteriores de este documento (v1.0, v1.1, v1.2) en Fase 3/Entregables/_historico y Fase 2.")

    out = OUT / "D05_Plan_de_Pruebas_y_Resultados_v1.3_Fase3.docx"
    d.save(out)
    return out


if __name__ == "__main__":
    print(build())
