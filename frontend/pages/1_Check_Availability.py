import streamlit as st

from frontend.utils.api import check_availability

st.title("📅 Check Table Availability")

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

if st.button("Check Availability"):

    data = {
        "reservation_date": str(reservation_date),
        "reservation_time": reservation_time,
        "guest_count": guest_count,
    }

response = check_availability(data)

st.write(response)   # <-- temporary for debugging

if response.get("available"):
    st.success(response["message"])
else:
    st.error(response.get("message", "Unknown error"))