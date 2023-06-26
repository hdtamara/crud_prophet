from sqlalchemy import Column, Integer,Float,Date,String
from database import Base

class Validacion_Diaria(Base):
    __tablename__="tbl_prophet_validacion_diaria"
    id = Column(Integer(),primary_key=True,index=True,autoincrement=True)
    year = Column(Integer(),nullable=False)
    month = Column(Integer(),nullable=False)
    day = Column(Integer(),nullable=False)
    day_week = Column(Integer(),nullable=False)
    interpolado = Column(Float(),nullable=False)
    state_holiday = Column(Integer(),nullable=False)
    prediccion = Column(Float(),nullable=False)
    pred_regr = Column(Float(),nullable=False)
    promedio = Column(Float(),nullable=False)
    yhat = Column(Float(),nullable=False)
    fecha = Column(Date(),nullable=False)
    service_line_id = Column(String(),nullable=False)
    cost_center_id = Column(String(),nullable=False)

class Prediccion_Diaria(Base):
    __tablename__="tbl_prophet_prediccion_diaria"
    id = Column(Integer(),primary_key=True,index=True,autoincrement=True)
    year = Column(Integer(),nullable=False)
    month = Column(Integer(),nullable=False)
    day = Column(Integer(),nullable=False)
    day_week = Column(Integer(),nullable=False)
    state_holiday = Column(Integer(),nullable=False)
    prediccion = Column(Float(),nullable=False)
    fecha = Column(Date(),nullable=False)
    service_line_id = Column(String(),nullable=False)
    cost_center_id = Column(String(),nullable=False)




