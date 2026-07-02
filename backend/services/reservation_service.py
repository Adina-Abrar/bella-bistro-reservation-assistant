from sqlalchemy.orm import Session

from backend.models.reservation import Reservation
from backend.utils.generate_reservation_id import generate_reservation_id


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


def create_reservation(
    db: Session,
    customer_name: str,
    phone: str,
    reservation_date: str,
    reservation_time: str,
    guest_count: int,
):
    availability = check_availability(
        db=db,
        reservation_date=reservation_date,
        reservation_time=reservation_time,
    )

    if not availability["available"]:
        return availability

    reservation_id = generate_reservation_id()
    new_reservation = Reservation(
        reservation_id=reservation_id,
        customer_name=customer_name,
        phone=phone,
        reservation_date=reservation_date,
        reservation_time=reservation_time,
        guest_count=guest_count,
)
    db.add(new_reservation)
    db.commit()
    db.refresh(new_reservation)

    return {
        "success": True,
        "message": "Reservation created successfully.",
        "reservation_id": reservation_id,
    }


def find_reservation(
    db: Session,
    reservation_id: str = None,
    phone: str = None,
):
    """
    Find a reservation using either the reservation ID
    or the customer's phone number.
    """

    if reservation_id:
        reservation = (
            db.query(Reservation)
            .filter(Reservation.reservation_id == reservation_id)
            .first()
        )

    elif phone:
        reservation = (
            db.query(Reservation)
            .filter(Reservation.phone == phone)
            .first()
        )

    else:
        return {
            "success": False,
            "message": "Please provide a reservation ID or phone number."
        }

    if not reservation:
        return {
            "success": False,
            "message": "Reservation not found."
        }

    return {
        "success": True,
        "reservation": {
            "reservation_id": reservation.reservation_id,
            "customer_name": reservation.customer_name,
            "phone": reservation.phone,
            "reservation_date": reservation.reservation_date,
            "reservation_time": reservation.reservation_time,
            "guest_count": reservation.guest_count,
            "status": reservation.status,
        }
    }

def modify_reservation(
    db: Session,
    reservation_id: str = None,
    phone: str = None,
    reservation_date: str = None,
    reservation_time: str = None,
    guest_count: int = None,
):
    """
    Modify an existing reservation.
    """
    if reservation_id:
        reservation = (
            db.query(Reservation)
            .filter(Reservation.reservation_id == reservation_id)
            .first()
        )

    elif phone:
        reservation = (
            db.query(Reservation)
            .filter(Reservation.phone == phone)
            .first()
        )

    else:
        return {
            "success": False,
            "message": "Please provide a reservation ID or phone number."
        }
    
    if not reservation:
        return {
            "success": False,
            "message": "Reservation not found."
        }
    
    # Check availability only if date or time is being changed
    if reservation_date or reservation_time:

        new_date = reservation_date or reservation.reservation_date
        new_time = reservation_time or reservation.reservation_time

        # Only check if the customer is changing to a different slot
        if (
            new_date != reservation.reservation_date
            or new_time != reservation.reservation_time
        ):
            availability = check_availability(
                db=db,
                reservation_date=new_date,
                reservation_time=new_time,
            )

            if not availability["available"]:
                return availability
            
    # Update only the fields provided by the customer
    if reservation_date:
        reservation.reservation_date = reservation_date

    if reservation_time:
        reservation.reservation_time = reservation_time

    if guest_count is not None:
        reservation.guest_count = guest_count
    db.commit()
    db.refresh(reservation)

    return {
        "success": True,
        "message": "Reservation updated successfully.",
        "reservation": {
            "reservation_id": reservation.reservation_id,
            "customer_name": reservation.customer_name,
            "phone": reservation.phone,
            "reservation_date": reservation.reservation_date,
            "reservation_time": reservation.reservation_time,
            "guest_count": reservation.guest_count,
            "status": reservation.status,
        },
    }


def cancel_reservation(
    db: Session,
    reservation_id: str = None,
    phone: str = None,
):
    """
    Cancel an existing reservation.
    """

    if reservation_id:
        reservation = (
            db.query(Reservation)
            .filter(Reservation.reservation_id == reservation_id)
            .first()
        )

    elif phone:
        reservation = (
            db.query(Reservation)
            .filter(Reservation.phone == phone)
            .first()
        )

    else:
        return {
            "success": False,
            "message": "Please provide a reservation ID or phone number."
        }

    if not reservation:
        return {
            "success": False,
            "message": "Reservation not found."
        }
    
    if reservation.status == "Cancelled":
        return {
        "success": False,
        "message": "This reservation has already been cancelled."
    }
    
    reservation.status = "Cancelled"
    db.commit()
    db.refresh(reservation)
    return {
        "success": True,
        "message": "Reservation cancelled successfully.",
        "reservation": {
            "reservation_id": reservation.reservation_id,
            "customer_name": reservation.customer_name,
            "phone": reservation.phone,
            "reservation_date": reservation.reservation_date,
            "reservation_time": reservation.reservation_time,
            "guest_count": reservation.guest_count,
            "status": reservation.status,
        },
    }