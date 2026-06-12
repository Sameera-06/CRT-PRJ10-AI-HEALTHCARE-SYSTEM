import streamlit as st

with open("assets/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("📈 Outcome Prediction")
import plotly.graph_objects as go

from utils.prediction import predict_outcome


age = st.slider(
    "Age",
    1,
    100,
    40
)

severity = st.slider(
    "Disease Severity",
    1,
    10,
    5
)

icu = st.selectbox(
    "ICU Required",
    [0,1]
)

oxygen = st.slider(
    "Oxygen Level",
    50,
    100,
    95
)

heart_rate = st.slider(
    "Heart Rate",
    40,
    180,
    80
)

if st.button(
    "Predict Outcome"
):

    features = [
        age,
        severity,
        icu,
        oxygen,
        heart_rate
    ]

    pred,prob = predict_outcome(
        features
    )

    recovery = prob * 100

    st.metric(
        "Recovery Probability",
        f"{recovery:.2f}%"
    )

    if recovery > 70:
        st.success(
            "Good Recovery Expected"
        )
    elif recovery > 40:
        st.warning(
            "Moderate Recovery"
        )
    else:
        st.error(
            "High Risk Patient"
        )

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=recovery,
            title={
                "text":
                "Recovery Probability"
            },
            gauge={
                "axis":{
                    "range":[0,100]
                }
            }
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )