from sqlalchemy import Column, Integer, String
from backend.database.database import Base


class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)

    reservation_id = Column(String, unique=True, nullable=False)

    customer_name = Column(String, nullable=False)

    phone = Column(String, nullable=False)

    reservation_date = Column(String, nullable=False)

    reservation_time = Column(String, nullable=False)

    guest_count = Column(Integer, nullable=False)

    status = Column(String, default="Confirmed")