import streamlit as st

from frontend.utils.api import modify_reservation

st.title("✏️ Modify Reservation")

reservation_id = st.text_input("Reservation ID (Optional)")

phone = st.text_input("Phone Number (Optional)")

reservation_date = st.date_input("New Reservation Date")

available_times = [
    "5:00 PM",
    "5:30 PM",
    "6:00 PM",
    "6:30 PM",
    "7:00 PM",
    "7:30 PM",
    "8:00 PM",
    "8:30 PM",
    "9:00 PM",
]

reservation_time = st.selectbox(
    "New Reservation Time",
    available_times,
)

guest_count = st.number_input(
    "Guest Count",
    min_value=1,
    max_value=20,
    value=2,
)

if st.button("Modify Reservation"):

    if not reservation_id and not phone:
        st.warning("Please enter a Reservation ID or Phone Number.")

    else:
        data = {
            "reservation_id": reservation_id if reservation_id else None,
            "phone": phone if phone else None,
            "reservation_date": str(reservation_date),
            "reservation_time": reservation_time,
            "guest_count": guest_count,
        }

        response = modify_reservation(data)

        if response.get("success"):
            st.success(response["message"])

            reservation = response["reservation"]

            st.write(f"**Reservation ID:** {reservation['reservation_id']}")
            st.write(f"**Customer:** {reservation['customer_name']}")
            st.write(f"**Date:** {reservation['reservation_date']}")
            st.write(f"**Time:** {reservation['reservation_time']}")
            st.write(f"**Guests:** {reservation['guest_count']}")
            st.write(f"**Status:** {reservation['status']}")

        else:
            st.error(response["message"])