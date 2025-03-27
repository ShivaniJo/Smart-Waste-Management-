from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Data model for waste bin
class WasteBin(BaseModel):
    id: Optional[str]  # Auto-generated MongoDB ObjectId
    location: str
    latitude: float
    longitude: float
    current_fill: float
    max_capacity: float
    last_updated: datetime
