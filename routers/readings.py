from fastapi import APIRouter
from models import ElectricityReading

router = APIRouter()

@router.post("/")
def ingest_reading(reading: ElectricityReading):
    return {
        "message": "Reading accepted",
        "data": reading
    }