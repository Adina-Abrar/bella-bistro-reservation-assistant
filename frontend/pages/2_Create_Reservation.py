import streamlit as st

from frontend.utils.api import create_reservation

st.title("➕ Create Reservation")

customer_name = st.text_input("Customer Name")

phone = st.text_input(
    "Phone Number",
    placeholder="03XXXXXXXXX"
)

reservation_date = st.date_input("Reservation Date")

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
    "Reservation Time",
    available_times,
)

guest_count = st.number_input(
    "Guest Count",
    min_value=1,
    max_value=20,
    value=2,
)

if st.button("Create Reservation"):

    if not customer_name:
        st.warning("Please enter your name.")

    elif not phone:
        st.warning("Please enter your phone number.")

    elif not phone.isdigit():
        st.warning("Phone number should contain only digits.")

    elif len(phone) != 11:
        st.warning("Phone number must be exactly 11 digits.")

    elif not phone.startswith("03"):
        st.warning("Phone number must start with 03.")

    else:
        data = {
            "customer_name": customer_name,
            "phone": phone,
            "reservation_date": str(reservation_date),
            "reservation_time": reservation_time,
            "guest_count": guest_count,
        }

        response = create_reservation(data)

        if response.get("success"):
            st.success(response["message"])
            st.info(f"Reservation ID: {response['reservation_id']}")
        else:
            st.error(response.get("message", "Something went wrong."))