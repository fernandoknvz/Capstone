# Pruebas - versión de trabajo

## Capas de prueba

1. Unitarias Python sin red.
2. Unitarias/integración frontend con proveedores simulados.
3. Scripts manuales contra proveedores reales.
4. E2E desde navegador.
5. Telefonía Asterisk: pendiente.

## Resultados históricos separados

- PR #16: 200 Python y 91 web declaradas.
- PR #17: 214 Python declaradas.
- PR #18: 281 Python y 103 web declaradas, **rama no integrada**.
- CI: incorporado por PR #19 y documentado por PR #20.

Falta ejecutar una certificación reproducible sobre el corte final de `main` y archivar sus logs. No se deben combinar los conteos de ramas distintas.
