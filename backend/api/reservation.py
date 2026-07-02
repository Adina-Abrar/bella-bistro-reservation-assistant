from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.dependencies import get_db

from backend.schemas.reservation import (
    CheckAvailabilityRequest,
    CreateReservationRequest,
    FindReservationRequest,
    ModifyReservationRequest,
    CancelReservationRequest,
)

from backend.services.reservation_service import (
    check_availability,
    create_reservation,
    find_reservation,
    modify_reservation,
    cancel_reservation,
)

# ADD THIS LINE
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


@router.post("/create-reservation")
def create_new_reservation(
    request: CreateReservationRequest,
    db: Session = Depends(get_db),
):
    return create_reservation(
        db=db,
        customer_name=request.customer_name,
        phone=request.phone,
        reservation_date=request.reservation_date,
        reservation_time=request.reservation_time,
        guest_count=request.guest_count,
    )


@router.post("/find-reservation")
def find_existing_reservation(
    request: FindReservationRequest,
    db: Session = Depends(get_db),
):
    return find_reservation(
        db=db,
        reservation_id=request.reservation_id,
        phone=request.phone,
    )


@router.put("/modify-reservation")
def modify_existing_reservation(
    request: ModifyReservationRequest,
    db: Session = Depends(get_db),
):
    return modify_reservation(
        db=db,
        reservation_id=request.reservation_id,
        phone=request.phone,
        reservation_date=request.reservation_date,
        reservation_time=request.reservation_time,
        guest_count=request.guest_count,
    )

@router.put("/cancel-reservation")
def cancel_existing_reservation(
    request: CancelReservationRequest,
    db: Session = Depends(get_db),
):
    return cancel_reservation(
        db=db,
        reservation_id=request.reservation_id,
        phone=request.phone,
    )