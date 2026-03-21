from fastapi import FastAPI
from db.database import engine, Base
from routers import readings
from routers import auth   # <-- import

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])         # <-- add
app.include_router(readings.router, prefix="/readings", tags=["Readings"])

@app.get("/")
def health():
    return {"status": "ok"}
