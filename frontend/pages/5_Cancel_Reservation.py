import streamlit as st

from frontend.utils.api import cancel_reservation

st.title("❌ Cancel Reservation")

reservation_id = st.text_input("Reservation ID (Optional)")

phone = st.text_input("Phone Number (Optional)")

if st.button("Cancel Reservation"):

    if not reservation_id and not phone:
        st.warning("Please enter a Reservation ID or Phone Number.")

    else:
        data = {
            "reservation_id": reservation_id if reservation_id else None,
            "phone": phone if phone else None,
        }

        response = cancel_reservation(data)

        if response.get("success"):

            reservation = response["reservation"]

            st.success(response["message"])

            st.write(f"**Reservation ID:** {reservation['reservation_id']}")
            st.write(f"**Customer:** {reservation['customer_name']}")
            st.write(f"**Phone:** {reservation['phone']}")
            st.write(f"**Status:** {reservation['status']}")

        else:
            st.error(response["message"])