from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.dependencies import get_db
from backend.schemas.reservation import CheckAvailabilityRequest
from backend.services.reservation_service import check_availability

router = APIRouter()


@router.post("/check-availability")
def check_table_availability(
    request: CheckAvailabilityRequest,
    db: Session = Depends(get_db)
):
    return check_availability(
        db=db,
        reservation_date=request.reservation_date,
        reservation_time=request.reservation_time,
    )