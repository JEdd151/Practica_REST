import orm.modelos as modelos
from sqlalchemy.orm import Session
import orm.esquema as esquema

#Funciones para manejar alumnos 
def alumnos (sesion:Session):
    print("SELECT * FROM Alumnos")
    return sesion.query(modelos.Alumno).all()
    

def alumnos_id (sesion:Session,id_alumnos:int):
    print("SELECT * FROM Alumnos WHERE id = ", id_alumnos)
    return sesion.query(modelos.Alumno).filter(modelos.Alumno.id == id_alumnos).first ()


def fotos (sesion:Session):
    print("SELECT * FROM fotos")
    return sesion.query(modelos.Foto).all()


def fotos_id (sesion:Session, id_fotos:int):
    print (f"SELECT * FROM fotos WHERE id={id_fotos}")
    return sesion.query(modelos.Foto).filter(modelos.Foto.id == id_fotos).first()


def fotos_por_alumno (sesion:Session, id_al:int):
    print (f"SELECT * FROM fotos WHERE id_alumnos={id_al}")
    return sesion.query(modelos.Foto).filter(modelos.Foto.id_alumno == id_al).all()

def calificaciones (sesion:Session):
    print("SELECT * FROM calificaciones")
    return sesion.query(modelos.Calificacion).all()


def calificaciones_por_id(sesion:Session, id_fo:int):
    print (f"SELECT * FROM calificaciones WHERE id={id_fo}")
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id == id_fo).first()

def calificaciones_por_id_alumno(sesion:Session, id_al:int):
    print(f"SELECT * FROM calificaciones WHERE id_alumnos={id_al}")
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id_alumno == id_al).all()



    
def borrar_calificacion_alumno(sesion:Session, id_al:int):
    print(f"DELETE FROM calificaciones WHERE id_alumnos={id_al}")
    
    calific_del = calificaciones_por_id_alumno(sesion, id_al)
    
    if calific_del:
        for e in calific_del:
            sesion.delete(e)
        sesion.commit()
    else:
        print(f"No hay calificaciones para el alumno {id_al}")

def borrar_fotos_alumno(sesion:Session, id_al:int):
    print (f"DELETE FROM app.fotos WHERE id_alumnos={id_al}")
    
    fotos_del = fotos_por_alumno(sesion, id_al)
    
    if fotos_del:
        for e in fotos_del:
            sesion.delete(e)
        sesion.commit()
    else:
        print(f"No hay fotos para el alumno {id_al}")


def borrar_alumnos_por_id (sesion:Session, id_alumno:int):
    print(f"DELETE FROM alumnos WHERE id_alumnos={id_alumno}")
    alumnos = alumnos_id (sesion, id_alumno)
    
    if alumnos:
        sesion.delete(alumnos)
        sesion.commit()
        
        mensaje = {
            "mensaje":f"Alumno con ID {id_alumno} eliminado"
        }
        return mensaje
    else: 
        print(f"No se encuantra ningun alumno con ID {id_alumno}")
        mensaje = {
            "mensaje":f"No se encontro ningun alumno con ID {id_alumno}"
        }
        
        return mensaje
    

#--------------------Practica REST-2----------------------

#post("/alumnos”)
def guardar_alumnos (sesion:Session, alum_nuevo:esquema.AlumnosBase):
    alumno_bd = modelos.Alumno()
    
    alumno_bd.nombre = alum_nuevo.nombre
    alumno_bd.edad = alum_nuevo.edad
    alumno_bd.domicilio = alum_nuevo.domicilio
    alumno_bd.carrera = alum_nuevo.carrera
    alumno_bd.email = alum_nuevo.email
    
    sesion.add(alumno_bd)
    sesion.commit()
    sesion.refresh(alumno_bd)
    return alumno_bd  

#post("/alumnos/{id}/calificaciones")
def guardar_calificaciones(sesion:Session, id:int, calif_esquema:esquema.CalificacionesBase):
    alum_bd = alumnos_id(sesion, id)
    
    if alum_bd is not None:
        calfi_bd = modelos.Calificacion(
            id_alumno = id,
            uea = calif_esquema.uea,
            calificacion = calif_esquema.calificacion
        )
        sesion.add(calfi_bd)
        sesion.commit()
        sesion.refresh(calfi_bd)
        
        print(calif_esquema)
        return calif_esquema
    else:
        respuesta = {
            "mensaje" : "No hay relacion"
        }
        return respuesta

#post("/alumnos/{id}/fotos")
def guardar_foto(sesion:Session, id:int, foto_esquema:esquema.FotosBase):
    alum_bd = alumnos_id(sesion, id)
    
    if alum_bd is not None:
        foto_bd = modelos.Foto (
            id_alumno = id,
            titulo = foto_esquema.titulo,
            descripcion = foto_esquema.descripcion,
            ruta = foto_esquema.ruta
        )
        sesion.add(foto_bd)
        sesion.commit()
        sesion.refresh(foto_bd)
        
        print(foto_esquema)
        return foto_esquema
    else:
        respuesta = {
            "mensaje" : "No hay relacion"
        }
        return respuesta



#put("/alumnos/{id})
def actualizar_alumno (sesion:Session, id:int, alumno_esquema:esquema.AlumnosBase):
    almn_bd = alumnos_id(sesion, id)
    if almn_bd is not None:
        almn_bd.nombre = alumno_esquema.nombre,
        almn_bd.edad = alumno_esquema.edad,
        almn_bd.domicilio = alumno_esquema.domicilio,
        almn_bd.carrera = alumno_esquema.carrera,
        almn_bd.trimestre = alumno_esquema.trimestre,
        almn_bd.email = alumno_esquema.email,
        almn_bd.password = alumno_esquema.password
        
        sesion.commit()
        sesion.refresh(almn_bd)
        
        print(alumno_esquema)
        return alumno_esquema
    else:
        respuesta = {
            "mensaje":"No existe el alumno"
        }
        return respuesta
    
#put("/calificaciones/{id}")
def actualizar_calificaciones(sesion:Session, id:int, calificacion_esquema:esquema.CalificacionesBase):
    calif_bd = calificaciones_por_id(sesion, id)
    if calif_bd is not None:
        calif_bd.uea = calificacion_esquema.uea
        calif_bd.calificacion = calificacion_esquema.calificacion
        
        sesion.commit()
        sesion.refresh(calif_bd)
        
        print(calificacion_esquema)
        return calificacion_esquema
    else:
        respuesta = {
            "mensaje":"No existe la calificacion"
        }
        return respuesta

#put("/fotos/{id}")
def actualizar_foto(sesion:Session, id:int, foto_esquema:esquema.FotosBase):
    foto_bd = fotos_id(sesion, id)
    if foto_bd is not None:
        foto_bd.titulo = foto_esquema.titulo
        foto_bd.descripcion = foto_esquema.descripcion
        foto_bd.ruta = foto_esquema.ruta
        
        sesion.commit()
        sesion.refresh(foto_bd)
        
        print(foto_esquema)
        return foto_esquema
    else:
        respuesta = {
            "mensaje":"No existe la foto"
        }
        return respuesta