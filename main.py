from fastapi import FastAPI
from routers.readings import router as readings_router

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