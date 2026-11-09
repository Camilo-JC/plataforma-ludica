## Objetivo
Agregar el endpoint GET /api/version con su prueba correspondiente.

## Herramienta y modelo
Copilot, modelo Auto.

## Prompt
Lee AGENTS.md. Estamos trabajando en pair programming para el Taller 3 del SENA.
Agrega el endpoint GET /api/version, que devuelva la versión definida en app/proyecto.py (en formato JSON {"version": "0.1.0"}), junto con su prueba correspondiente en tests/test_inicio.py.
Antes de modificar ningún archivo, muéstrame el plan detallando estrictamente qué archivos vas a modificar y espera mi aprobación. No modifiques ni rompas las pruebas anteriores.

## Resultado
El agente propuso modificar únicamente `app/rutas/api.py` y `tests/test_inicio.py`. Al aprobar el plan, se implementó correctamente el endpoint devolviendo la versión desde `proyecto.VERSION`. Las 7 pruebas pasaron en verde y Ruff no arrojó errores.