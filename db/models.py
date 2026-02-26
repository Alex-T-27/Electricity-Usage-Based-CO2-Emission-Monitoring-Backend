from sqlalchemy import Column, Integer, String, Float, DateTime
from db.database import Base

class Reading(Base):
    __tablename__ = "readings"

    id = Column(Integer, primary_key=True, index=True)
    sensor_id = Column(String, index=True)
    timestamp = Column(DateTime)
    kwh = Column(Float)
    unit = Column(String)
    co2 = Column(Float)