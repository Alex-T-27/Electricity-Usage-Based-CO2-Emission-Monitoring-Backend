from db.database import SessionLocal
from db.models import Reading
from sqlalchemy import asc, desc
from sqlalchemy.orm import Session

EMISSION_FACTOR = 0.233

def calculate_co2(kwh: float) -> float:
    return kwh * EMISSION_FACTOR


def save_reading(db: Session, reading):

    co2_value = calculate_co2(reading.kwh)

    db_reading = Reading(
        sensor_id=reading.sensor_id,
        timestamp=reading.timestamp,
        kwh=reading.kwh,
        unit=reading.unit,
        co2=co2_value
    )

    db.add(db_reading)
    db.commit()
    db.refresh(db_reading)

    return db_reading



def get_reading_by_id(db: Session, reading_id: int):
    reading = db.query(Reading).filter(Reading.id == reading_id).first()
    return reading


def get_readings(
    db: Session,
    sensor_id: str | None = None,
    limit: int | None = None,
    offset: int = 0,
    sort: str = "desc"
):
    query = db.query(Reading)

    if sensor_id:
        query = query.filter(Reading.sensor_id == sensor_id)

    if sort == "asc":
        query = query.order_by(asc(Reading.timestamp))
    else:
        query = query.order_by(desc(Reading.timestamp))

    return query.offset(offset).limit(limit).all()
