from pydantic import BaseModel, Field
from datetime import datetime

class ElectricityReading(BaseModel):
    sensor_id: str = Field(min_length=3)
    timestamp: datetime
    kwh: float = Field (gt=0)
    unit: str



