from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db.models import User
from dependency import get_current_user   # <-- import the guard
from models import ElectricityReading
from services.readings_service import save_reading, get_readings, get_reading_by_id

router = APIRouter()


@router.post("/")
def ingest(
    reading: ElectricityReading,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)   # <-- protected
):
    saved = save_reading(db, reading)
    return {
        "id": saved.id,
        "sensor_id": saved.sensor_id,
        "kwh": saved.kwh,
        "co2_emissions": saved.co2
    }


@router.get("/")
def fetch_readings(
    sensor_id: str | None = None,
    limit: int | None = None,
    offset: int = 0,
    sort: str = "desc",
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)   # <-- protected
):
    return get_readings(db, sensor_id, limit, offset, sort)


@router.get("/{reading_id}")
def fetch_reading(
    reading_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)   # <-- protected
):
    reading = get_reading_by_id(db, reading_id)
    if reading is None:
        raise HTTPException(status_code=404, detail="Reading not found")
    return reading
