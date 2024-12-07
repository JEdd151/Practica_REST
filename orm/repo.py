import orm.modelos as modelos
from sqlalchemy.orm import Session


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
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id == id_fo).all()

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

