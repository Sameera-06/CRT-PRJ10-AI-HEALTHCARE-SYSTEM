import streamlit as st

with open("assets/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("📊 Analytics Dashboard")
import pandas as pd
import plotly.express as px


patients = pd.read_csv(
    "data/patients.csv"
)

doctors = pd.read_csv(
    "data/doctors.csv"
)

appointments = pd.read_csv(
    "data/appointments.csv"
)

col1,col2,col3 = st.columns(3)

col1.metric(
    "Patients",
    len(patients)
)

col2.metric(
    "Doctors",
    len(doctors)
)

col3.metric(
    "Appointments",
    len(appointments)
)

st.markdown("---")

if not appointments.empty:

    fig = px.histogram(
        appointments,
        x="Status",
        title="Appointment Status"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

if not patients.empty:

    fig2 = px.histogram(
        patients,
        x="Gender",
        title="Patients By Gender"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )