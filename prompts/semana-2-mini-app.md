# Mini-aplicación de práctica: Trivia de cultura general
## Versión A
**Objetivo:** construir la mini-aplicación con un prompt de una línea.
**Herramienta y modelo:** Copilot con el modelo estandar.
**Prompt:** 
```text
Haz una app web de trivia con FastAPI.

Resultado: Línea base construida; se ejecutaron las pruebas de aceptación posteriormente.

Versión B
Objetivo: construir la misma aplicación con un prompt estructurado, AGENTS.md y pruebas de aceptación.Herramienta y modelo: Copilot con el modelo estandar.Prompt:

Actúa como desarrollador backend con experiencia en FastAPI, Jinja2 y pruebas con pytest. Construir la mini-aplicación web Trivia de cultura general...

Resultado: 6 de 6 pruebas de aceptación aprobadas, Ruff con All checks passed.

Mejora
Objetivo: GET /api/preguntas acepta el parámetro opcional cantidad (entre 1 y 5).Herramienta y modelo: Copilot con el modelo estandar.Prompt:

Actúa como desarrollador backend senior experto en FastAPI... Agrega la funcionalidad de cantidad opcional...

Comparación
Las pruebas de aceptación y de mejora pasaron exitosamente en la versión B gracias a la precisión del prompt estructurado y el contexto de AGENTS.md, a diferencia de la versión A.


---

### Paso 3: Subir los cambios a GitHub (Actividad 6, Paso 4)
Una vez guardados ambos archivos, ejecuta estos comandos en tu terminal de VS Code para guardarlos en tu repositorio oficial y que el pipeline de Integración Continua (CI) quede en verde[cite: 14, 15]:

```cmd
git add prompts
git commit -m "Agrega la plantilla de prompt y los prompts de la mini-aplicación"
git push