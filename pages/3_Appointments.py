import streamlit as st
import pandas as pd

with open("assets/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("📅 Appointment Scheduling")



df = pd.read_csv(
    "data/appointments.csv"
)

appointment_id = st.text_input(
    "Appointment ID"
)

patient = st.text_input(
    "Patient Name"
)

doctor = st.text_input(
    "Doctor Name"
)

date = st.date_input(
    "Appointment Date"
)

status = st.selectbox(
    "Status",
    [
        "Pending",
        "Approved",
        "Completed"
    ]
)

if st.button("Book Appointment"):

    new_row = pd.DataFrame({
        "Appointment ID":[appointment_id],
        "Patient Name":[patient],
        "Doctor Name":[doctor],
        "Date":[date],
        "Status":[status]
    })

    df = pd.concat([df,new_row])

    df.to_csv(
        "data/appointments.csv",
        index=False
    )

    st.success("Appointment Booked")

st.markdown("---")

st.dataframe(df,use_container_width=True)