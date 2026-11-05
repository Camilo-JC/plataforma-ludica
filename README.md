# Plataforma lúdica de cursos para niños

Plataforma web lúdica de Ciencias para niños, desarrollada con FastAPI. El curso
trabaja seres vivos, cuerpo humano y medio ambiente mediante misiones. Cada
misión contiene actividades y entrega una insignia únicamente cuando el
aprendiz completa todas sus actividades.

- **Aprendiz:** Camilo Jose Caballero Gonzalez
- **Curso:** Ciencias (seres vivos, cuerpo humano y medio ambiente)
- **Mecánica:** Misiones e insignias
- **Aplicación publicada:** Pendiente de despliegue en Render

## Ejecutar en su equipo

En Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

En Linux o macOS, cree el entorno con `python3 -m venv .venv` y actívelo con `source .venv/bin/activate`.

Abra http://127.0.0.1:8000 en el navegador. La documentación de la API está en http://127.0.0.1:8000/docs.

## Verificar

```bash
pytest -v
ruff check .
```

## API de misiones

- `GET /api/misiones` lista las misiones de Ciencias.
- `POST /api/misiones/{mision_id}/actividades/{actividad_id}/completar`
  registra una actividad. Envíe `{"participante_id": "un-identificador"}`.
  La respuesta indica si se otorgó la insignia al completar la misión.

El progreso actual se conserva en memoria para este prototipo. Al incorporar
persistencia, el servicio puede conectarse a los modelos SQLModel sin cambiar
el contrato de las rutas.

## Estructura

| Carpeta o archivo | Contenido |
| --- | --- |
| `app/` | Aplicación FastAPI: rutas, servicios, modelos, plantillas y archivos estáticos |
| `app/proyecto.py` | Datos de identificación del proyecto |
| `tests/` | Pruebas automatizadas |
| `specs/` | Especificación, flujo de usuario, plan técnico, tareas y decisiones |
| `prompts/` | Prompts versionados |
| `entregas/` | Respuestas semanales; `entregar.py` genera el PDF |
| `AGENTS.md` | Contexto del proyecto para los agentes de IA |
| `STATE.md` | Estado, decisiones y siguiente paso |
| `render.yaml` | Configuración del despliegue en Render |

## Licencia

MIT. Consulte el archivo LICENSE.
