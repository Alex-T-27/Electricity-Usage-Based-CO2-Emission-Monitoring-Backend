from fastapi import FastAPI
from routers.readings import router as readings_router
from db.database import engine
from db.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Environment Telemetry API",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "service": "Environment Telemetry Backend",
        "status": "running"
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(
    readings_router,
    prefix="/readings",
    tags=["readings"]
)