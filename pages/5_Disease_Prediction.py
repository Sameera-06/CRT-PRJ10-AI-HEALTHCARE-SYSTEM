import streamlit as st

with open("assets/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("🧠 Disease Prediction")
import plotly.graph_objects as go

from utils.prediction import predict_disease

st.title("🩺 AI Disease Prediction")

st.subheader("Patient Health Inputs")

age = st.slider(
    "Age",
    1,
    100,
    30
)

bmi = st.slider(
    "BMI",
    10,
    50,
    25
)

bp = st.slider(
    "Blood Pressure",
    80,
    200,
    120
)

glucose = st.slider(
    "Glucose",
    50,
    300,
    100
)

cholesterol = st.slider(
    "Cholesterol",
    100,
    400,
    180
)

smoking = st.selectbox(
    "Smoking",
    [0,1]
)

if st.button("Predict Disease Risk"):

    features = [
        age,
        bmi,
        bp,
        glucose,
        cholesterol,
        smoking
    ]

    pred,prob = predict_disease(
        features
    )

    risk = prob * 100

    st.metric(
        "Disease Risk %",
        f"{risk:.2f}%"
    )

    if risk > 70:
        st.error(
            "High Disease Risk"
        )
    elif risk > 40:
        st.warning(
            "Moderate Disease Risk"
        )
    else:
        st.success(
            "Low Disease Risk"
        )

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=risk,
            title={
                'text':
                "Disease Risk"
            },
            gauge={
                'axis':
                {'range':[0,100]}
            }
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )