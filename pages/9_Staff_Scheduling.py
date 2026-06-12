import streamlit as st
import pandas as pd

with open("assets/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("👨‍⚕️ Staff Scheduling")
import os
import plotly.express as px


if not os.path.exists("data/staff.csv"):

    st.error(
        "staff.csv file not found in data folder."
    )

    st.stop()

df = pd.read_csv(
    "data/staff.csv"
)

st.dataframe(
    df,
    use_container_width=True
)

fig = px.histogram(
    df,
    x="Shift",
    color="Role",
    title="Staff Shift Allocation"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

patient_load = st.slider(
    "Patient Load",
    0,
    500,
    100
)

if patient_load > 300:

    st.warning(
        "Additional Staff Required"
    )

else:

    st.success(
        "Current Staff Sufficient"
    )