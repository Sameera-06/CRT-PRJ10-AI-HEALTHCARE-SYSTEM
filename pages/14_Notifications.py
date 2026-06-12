import streamlit as st

with open("assets/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("🔔 Notifications")



notifications = [

    "Appointment Reminder",

    "Medicine Reminder",

    "Lab Report Available",

    "Emergency Alert"

]

for item in notifications:

    st.info(item)