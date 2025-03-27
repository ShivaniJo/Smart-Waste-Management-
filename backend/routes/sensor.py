from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, database

router = APIRouter(prefix="/sensors", tags=["Sensors"])

@router.post("/", response_model=schemas.SensorResponse)
def create_sensor(sensor: schemas.SensorCreate, db: Session = Depends(database.get_db)):
    db_sensor = models.Sensor(**sensor.dict())
    db.add(db_sensor)
    db.commit()
    db.refresh(db_sensor)
    return db_sensor

@router.get("/", response_model=list[schemas.SensorResponse])
def get_all_sensors(db: Session = Depends(database.get_db)):
    return db.query(models.Sensor).all()

@router.get("/{sensor_id}", response_model=schemas.SensorResponse)
def get_sensor(sensor_id: int, db: Session = Depends(database.get_db)):
    sensor = db.query(models.Sensor).filter(models.Sensor.id == sensor_id).first()
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return sensor
