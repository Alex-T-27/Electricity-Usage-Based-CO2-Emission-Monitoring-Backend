from fastapi import APIRouter
from models import ElectricityReading
from services.readings_service import save_reading
from services.readings_service import get_all_readings
from services.readings_service import get_reading_by_id
from services.readings_service import get_readings_by_sensor
from fastapi import HTTPException

router = APIRouter()

@router.post("/")
def ingest(reading: ElectricityReading):
    saved = save_reading(reading)

    return {
        "id": saved.id,
        "sensor_id": saved.sensor_id,
        "kwh": saved.kwh,
        "co2_emissions": saved.co2
    }


@router.get("/")
def fetch_readings(sensor_id: str | None = None):

    if sensor_id:
        return get_readings_by_sensor(sensor_id)

    return get_all_readings()

@router.get("/{reading_id}")
def fetch_reading(reading_id: int):
    reading = get_reading_by_id(reading_id)

    if reading is None:
        raise HTTPException(status_code=404, detail="Reading not found")

    return reading

