import streamlit as st
import pandas as pd

with open("assets/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("🛏 Bed Management")
import plotly.express as px


df = pd.read_csv("data/beds.csv")

st.dataframe(
    df,
    use_container_width=True
)

occupied = len(
    df[df["Status"]=="Occupied"]
)

available = len(
    df[df["Status"]=="Available"]
)

col1,col2 = st.columns(2)

col1.metric(
    "Occupied Beds",
    occupied
)

col2.metric(
    "Available Beds",
    available
)

fig = px.pie(
    df,
    names="Status",
    title="Bed Occupancy"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

future_demand = occupied + 5

st.success(
    f"Predicted Bed Demand Next Week: {future_demand}"
)