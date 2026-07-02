import streamlit as st

st.set_page_config(
    page_title="Bella Bistro Reservation Assistant",
    page_icon="🍽️",
    layout="wide",
)

st.title("🍽️ Bella Bistro Reservation Assistant")

st.write(
    """
Welcome to the Bella Bistro Reservation System.

Use the navigation on the left to:

- 📅 Check Availability
- ➕ Create Reservation
- 🔍 Find Reservation
- ✏️ Modify Reservation
- ❌ Cancel Reservation
"""
)