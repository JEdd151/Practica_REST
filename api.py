from fastapi import FastAPI, UploadFile, File, Form, Depends
from typing import Optional
#from pydantic import BaseModel
#import shutil
#import os
#import uuid
import orm.repo as repo 
from sqlalchemy.orm import Session
from orm.config import generador_sesion 


app = FastAPI()

#========================G E T==========================

@app.get("/")
def holaMundo():
    print("Invocando '/'")
    mensaje = {
        "mensaje": "hola mundo"
    }
    return mensaje

#get("/alumnos”)
@app.get("/alumnos")
def lista_alumnos(sesion : Session = Depends (generador_sesion)):
    print("Api consultando la tabla alumnos")
    return repo.alumnos(sesion)

#get("/alumnos/{id})
@app.get("/alumnos/{id}")
def alumnos_id(id : int, sesion: Session = Depends (generador_sesion)):
    print("Api consultando alumnos por id")
    return repo.alumnos_id(sesion, id)

#get("/alumnos/{id}/calificaciones")
@app.get("/alumnos/{id}/calificaciones")
def calificaciones_por_id_alumno(id : int, sesion: Session = Depends (generador_sesion)):
    print("Api consultando calificaciones por alumno")
    return repo.calificaciones_por_id_alumno(sesion, id)

#get("/alumnos/{id}/fotos")
@app.get("/alumnos/{id}/fotos")
def fotos_por_id_alumno (id : int, sesion: Session = Depends(generador_sesion)):
    print("Api consultando fotos por id de alumno")
    return repo.fotos_por_alumno(sesion, id)

#get("/fotos/{id}”)
@app.get("/fotos/{id}")
def fotos_id (id : int, sesion: Session = Depends (generador_sesion)):
    print("Api consultando fotos por id")
    return repo.fotos_id(sesion, id)

#get("/calificaciones/{id}”)
@app.get("/calificaciones/{id}")
def calificaciones (id:int, sesion:Session = Depends(generador_sesion)):
    print("Api consultando calificaciones por id")
    return repo.calificaciones_por_id(sesion, id)

@app.get("/fotos")
def lista_fotos (sesion : Session = Depends (generador_sesion)):
    print("Api consultando la tabla fotos")
    return repo.fotos(sesion)

#@app.get("/calificaciones")
#def calificaciones (sesion:Session = Depends(generador_sesion)):
#    print("Api consultando calificaciones")
#    return repo.calificaciones(sesion)


#========================D E L E T E============================

#delete("/fotos/{id}”)
@app.delete("/fotos/{id}")
def eliminar_fotos(id : int, sesion: Session = Depends (generador_sesion)):
    return repo.borrar_fotos_alumno(sesion, id)

#delete("/calificaciones/{id}”)
@app.delete("/calificaciones/{id}")
def eliminar_calificaciones(id : int, sesion = Depends (generador_sesion)):
    return repo.borrar_calificacion_alumno(sesion, id)

#delete("/alumnos/{id}/calificaciones")
@app.delete("/alumnos/{id}/calificaciones")
def eliminar_calificaciones_por_alumno(id : int, sesion = Depends (generador_sesion)):
    return repo.borrar_calificaciones_por_alumno(sesion, id)

#delete("/alumnos/{id}/fotos")
@app.delete("/alumnos/{id}/fotos")
def eliminar_fotos_por_alumno(id : int, sesion = Depends (generador_sesion)):
    return repo.borrar_fotos_por_alumno(sesion, id)

#delete("/alumnos/{id})
@app.delete("/alumnos/{id}")
def eliminar_alumos(id : int, sesion: Session = Depends (generador_sesion)):
    repo.borrar_calificacion_alumno(sesion, id)
    repo.borrar_fotos_alumno(sesion, id)
    repo.borrar_alumnos_por_id(sesion, id)
    
    mensaje = {
        "mensaje" : "alumno eliminado"
    }
    
    return mensaje
