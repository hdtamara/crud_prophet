from pydantic import BaseModel
from datetime import date


class Validacion_Diaria(BaseModel):
    id : int
    year : int
    month : int
    day : int
    day_week : int
    interpolado : int
    state_holiday : int
    prediccion : float
    pred_regr : float
    promedio : float
    yhat : float
    fecha : date
    service_line_id : int
    cost_center_id : int
    class Config:
        orm_mode =True

class Prediccion_Diaria(BaseModel):
    id : int
    year : int
    month : int
    day : int
    day_week : int
    state_holiday : int
    prediccion : float
    fecha : date
    service_line_id : int
    cost_center_id : int
    class Config:
        orm_mode =True
