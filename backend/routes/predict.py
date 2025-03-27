from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models, schemas, database
import numpy as np
import pickle

router = APIRouter(prefix="/predict", tags=["Prediction"])

# Load trained ML model
with open("ml/model.pkl", "rb") as file:
    model = pickle.load(file)

@router.post("/", response_model=schemas.PredictionResponse)
def predict_waste(sensor_id: int, db: Session = Depends(database.get_db)):
    sensor = db.query(models.Sensor).filter(models.Sensor.id == sensor_id).first()
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")

    features = np.array([[sensor.current_fill / sensor.bin_capacity]])
    prediction = model.predict(features)

    new_prediction = models.Prediction(sensor_id=sensor.id, predicted_fill=prediction[0])
    db.add(new_prediction)
    db.commit()
    db.refresh(new_prediction)

    return new_prediction
