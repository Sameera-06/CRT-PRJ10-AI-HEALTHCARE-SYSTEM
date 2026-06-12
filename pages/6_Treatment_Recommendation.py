
import streamlit as st

with open("assets/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("💊 Treatment Recommendation")
import streamlit as st



disease = st.selectbox(
    "Select Disease",
    [
        "Diabetes",
        "Heart Disease",
        "Kidney Disease"
    ]
)

if st.button(
    "Generate Recommendation"
):

    if disease == "Diabetes":

        st.success("""
Specialist:
Endocrinologist

Tests:
HbA1c
Fasting Blood Sugar

Medication:
Metformin
""")

    elif disease == "Heart Disease":

        st.success("""
Specialist:
Cardiologist

Tests:
ECG
Echocardiogram

Medication:
Aspirin
Statins
""")

    elif disease == "Kidney Disease":

        st.success("""
Specialist:
Nephrologist

Tests:
Creatinine
Urine Analysis

Medication:
As prescribed by doctor
""")