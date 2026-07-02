import streamlit as st

from frontend.utils.api import find_reservation

st.title("🔍 Find Reservation")

reservation_id = st.text_input("Reservation ID (Optional)")

phone = st.text_input("Phone Number (Optional)")

if st.button("Find Reservation"):

    if not reservation_id and not phone:
        st.warning("Please enter a Reservation ID or Phone Number.")

    else:
        data = {
            "reservation_id": reservation_id if reservation_id else None,
            "phone": phone if phone else None,
        }

        response = find_reservation(data)

        if response.get("success"):

            reservation = response["reservation"]

            st.success("Reservation Found!")

            st.write(f"**Reservation ID:** {reservation['reservation_id']}")
            st.write(f"**Customer Name:** {reservation['customer_name']}")
            st.write(f"**Phone Number:** {reservation['phone']}")
            st.write(f"**Reservation Date:** {reservation['reservation_date']}")
            st.write(f"**Reservation Time:** {reservation['reservation_time']}")
            st.write(f"**Guest Count:** {reservation['guest_count']}")
            st.write(f"**Status:** {reservation['status']}")

        else:
            st.error(response["message"])