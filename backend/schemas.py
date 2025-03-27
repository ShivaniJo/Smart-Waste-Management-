from pydantic import BaseModel
from datetime import datetime

class SensorCreate(BaseModel):
    location: str
    bin_capacity: float
    current_fill: float

class SensorResponse(SensorCreate):
    id: int
    last_updated: datetime

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

class PredictionResponse(BaseModel):
    sensor_id: int
    predicted_fill: float
    timestamp: datetime
