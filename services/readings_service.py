from db.database import SessionLocal
from db.models import Reading

EMISSION_FACTOR = 0.233

def calculate_co2(kwh: float) -> float:
    return kwh * EMISSION_FACTOR


def save_reading(reading):
    db = SessionLocal()

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
    db.close()

    return db_reading


def get_all_readings():
    db = SessionLocal()
    readings = db.query(Reading).all()
    db.close()

    return readings


def get_reading_by_id(reading_id: int):
    db = SessionLocal()
    reading = db.query(Reading).filter(Reading.id == reading_id).first()
    db.close()

    return reading


def get_readings_by_sensor(sensor_id: str): 
    db = SessionLocal()
    reading = db.query(Reading).filter(Reading.sensor_id == sensor_id).all()
    db.close()

    return reading