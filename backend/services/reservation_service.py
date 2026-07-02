from sqlalchemy.orm import Session

from backend.models.reservation import Reservation


def check_availability(
    db: Session,
    reservation_date: str,
    reservation_time: str,
):
    """
    Check whether a reservation already exists
    for the requested date and time.
    """

    existing_reservation = (
        db.query(Reservation)
        .filter(
            Reservation.reservation_date == reservation_date,
            Reservation.reservation_time == reservation_time,
            Reservation.status == "Confirmed",
        )
        .first()
    )

    if existing_reservation:
        return {
            "available": False,
            "message": "No tables are available for the requested time."
        }

    return {
        "available": True,
        "message": "Table is available."
    }