"""Reglas de negocio para misiones e insignias de Ciencias."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Actividad:
    id: str
    titulo: str


@dataclass(frozen=True)
class Mision:
    id: str
    titulo: str
    tema: str
    insignia: str
    actividades: tuple[Actividad, ...]


MISIONES = (
    Mision(
        id="seres-vivos",
        titulo="Exploradores de la vida",
        tema="Seres vivos",
        insignia="Insignia de explorador de la vida",
        actividades=(
            Actividad("clasificar-seres-vivos", "Clasificar seres vivos"),
            Actividad("ciclo-de-vida", "Reconocer un ciclo de vida"),
        ),
    ),
    Mision(
        id="cuerpo-humano",
        titulo="Mi cuerpo por dentro",
        tema="Cuerpo humano",
        insignia="Insignia de anatomía",
        actividades=(
            Actividad("sistemas-del-cuerpo", "Relacionar sistemas del cuerpo"),
            Actividad("habitos-saludables", "Elegir hábitos saludables"),
        ),
    ),
    Mision(
        id="medio-ambiente",
        titulo="Guardianes del planeta",
        tema="Medio ambiente",
        insignia="Insignia de guardián del planeta",
        actividades=(
            Actividad("separar-residuos", "Separar residuos"),
            Actividad("cuidar-el-agua", "Proponer acciones para cuidar el agua"),
        ),
    ),
)


class MisionNoEncontradaError(ValueError):
    """Se lanza cuando una misión o actividad no existe."""


class ServicioMisiones:
    """Gestiona el progreso de participantes y el otorgamiento de insignias."""

    def __init__(self) -> None:
        self._actividades_completadas: dict[tuple[str, str], set[str]] = {}

    def listar(self) -> tuple[Mision, ...]:
        return MISIONES

    def completar_actividad(
        self, participante_id: str, mision_id: str, actividad_id: str
    ) -> tuple[Mision, bool]:
        mision = next((item for item in MISIONES if item.id == mision_id), None)
        if mision is None:
            raise MisionNoEncontradaError("La misión no existe.")

        actividades_validas = {actividad.id for actividad in mision.actividades}
        if actividad_id not in actividades_validas:
            raise MisionNoEncontradaError("La actividad no existe en la misión.")

        clave = (participante_id, mision_id)
        completadas = self._actividades_completadas.setdefault(clave, set())
        completadas.add(actividad_id)
        insignia_ganada = completadas >= actividades_validas
        return mision, insignia_ganada


servicio_misiones = ServicioMisiones()
