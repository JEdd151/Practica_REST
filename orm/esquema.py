from pydantic import BaseModel

class AlumnosBase (BaseModel):
    nombre:str
    edad:int
    domicilio:str
    carrera:str
    trimestre:str
    email:str
    password:str
    
class CalificacionesBase (BaseModel):
    uea:str
    calificacion:str

class FotosBase (BaseModel):
    titulo:str
    descripcion:str
    ruta:str