from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

@app.get("/")
def root():
    return {
        "service": "Environment Telemetry & Emission Backend",
        "status": "running"
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/readings")
def ingest_reading(reading: ElectricityReading):
    return {
        "message": "Reading accepted",
        "data": reading
    }
