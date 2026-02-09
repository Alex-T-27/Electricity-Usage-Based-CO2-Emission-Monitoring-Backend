from fastapi import FastAPI

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
