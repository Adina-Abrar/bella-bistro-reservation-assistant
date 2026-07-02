from fastapi import FastAPI

from backend.database.database import Base, engine
from backend.models.reservation import Reservation
from backend.api.reservation import router as reservation_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Bella Bistro Reservation Assistant",
    version="1.0.0"
)

app.include_router(reservation_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Bella Bistro Reservation Assistant!"
    }