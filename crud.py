from database import SessionLocal,engine
from sqlalchemy.orm import Session
import models
import schemas
from typing import List
from datetime import date

#models.Base.metadata.drop_all(engine)
models.Base.metadata.create_all(engine)

session=SessionLocal()
def add_data(data):
    try:
        session.add(data)
        session.commit()
        return {'codigo':1, 'informacion':'Cargue Exitoso'}
    except Exception as e:
        session.rollback ()
        return {'codigo':0, 'informacion':f'Error en el cargue:{e.args}'}
    finally:
        session.close

def add_validacion_diaria(info:schemas.Validacion_Diaria) -> dict:
    data_val = session.query(models.Validacion_Diaria).filter_by(fecha=info['fecha'],service_line_id=info['service_line_id'])
    if(len(data_val.all())>0):
        data_val.update(info)
        session.commit()
        return {'codigo':1, 'informacion':'Update Exitoso'}
    else:
        data = models.Validacion_Diaria(**info)
        cargue = add_data(data)
        return cargue

def add_prediccion_diaria(info:schemas.Prediccion_Diaria) -> dict:
    data_val = session.query(models.Prediccion_Diaria).filter_by(fecha=info['fecha'],service_line_id=info['service_line_id'])
    if(len(data_val.all())>0):
        data_val.update(info)
        session.commit()
        return {'codigo':1, 'informacion':'Update Exitoso'}
    else:
        data = models.Prediccion_Diaria(**info)
        cargue = add_data(data)
        return cargue


