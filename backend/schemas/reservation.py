from pydantic import BaseModel


class CheckAvailabilityRequest(BaseModel):
    reservation_date: str
    reservation_time: str
    guest_count: int


class CreateReservationRequest(BaseModel):
    customer_name: str
    phone: str
    reservation_date: str
    reservation_time: str
    guest_count: int


class FindReservationRequest(BaseModel):
    reservation_id: str | None = None
    phone: str | None = None


class ModifyReservationRequest(BaseModel):
    reservation_id: str | None = None
    phone: str | None = None
    new_date: str
    new_time: str
    new_guest_count: int


class CancelReservationRequest(BaseModel):
    reservation_id: str | None = None
    phone: str | None = None