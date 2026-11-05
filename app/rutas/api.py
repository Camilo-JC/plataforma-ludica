"""Endpoints de la API REST, documentados en /docs."""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app import proyecto
from app.servicios.misiones import MisionNoEncontradaError, servicio_misiones

router = APIRouter()


class Salud(BaseModel):
    estado: str


class DatosProyecto(BaseModel):
    aprendiz: str
    curso: str
    mecanica: str
    version: str


class ActividadRespuesta(BaseModel):
    id: str
    titulo: str


class MisionRespuesta(BaseModel):
    id: str
    titulo: str
    tema: str
    insignia: str
    actividades: list[ActividadRespuesta]


class CompletarActividad(BaseModel):
    participante_id: str


class ProgresoRespuesta(BaseModel):
    mision_id: str
    actividad_id: str
    insignia_ganada: bool
    insignia: str


@router.get("/salud", response_model=Salud, tags=["Sistema"])
def salud():
    """Indica si la aplicación está en funcionamiento."""
    return Salud(estado="ok")


@router.get("/api/proyecto", response_model=DatosProyecto, tags=["Proyecto"])
def datos_proyecto():
    """Devuelve los datos de identificación del proyecto."""
    return DatosProyecto(
        aprendiz=proyecto.APRENDIZ,
        curso=proyecto.CURSO,
        mecanica=proyecto.MECANICA,
        version=proyecto.VERSION,
    )


@router.get("/api/misiones", response_model=list[MisionRespuesta], tags=["Misiones"])
def listar_misiones():
    """Lista las misiones de Ciencias y sus actividades."""
    return servicio_misiones.listar()


@router.post(
    "/api/misiones/{mision_id}/actividades/{actividad_id}/completar",
    response_model=ProgresoRespuesta,
    tags=["Misiones"],
)
def completar_actividad(
    mision_id: str, actividad_id: str, solicitud: CompletarActividad
):
    """Registra una actividad y otorga la insignia al completar la misión."""
    try:
        mision, insignia_ganada = servicio_misiones.completar_actividad(
            solicitud.participante_id, mision_id, actividad_id
        )
    except MisionNoEncontradaError as error:
        raise HTTPException(status_code=404, detail=str(error)) from error

    return ProgresoRespuesta(
        mision_id=mision.id,
        actividad_id=actividad_id,
        insignia_ganada=insignia_ganada,
        insignia=mision.insignia,
    )
