import streamlit as st
import pandas as pd

with open("assets/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("📦 Resource Allocation")
import plotly.express as px
import os



if not os.path.exists(
    "data/hospital_resources.csv"
):

    st.error(
        "hospital_resources.csv not found."
    )

    st.stop()

try:

    df = pd.read_csv(
        "data/hospital_resources.csv"
    )

except Exception as e:

    st.error(
        f"Error loading file: {e}"
    )

    st.stop()

st.dataframe(
    df,
    use_container_width=True
)

fig = px.bar(
    df,
    x="Resource",
    y="Available",
    title="Hospital Resources Availability"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

resource = st.selectbox(
    "Select Resource",
    df["Resource"]
)

if st.button(
    "Forecast Demand"
):

    st.success(
        f"Predicted demand for {resource}: +15%"
    )