import streamlit as st

with open("assets/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("📑 Reports")
import pandas as pd


report_type = st.selectbox(
    "Select Report",
    [
        "Disease Statistics",
        "Bed Occupancy",
        "Doctor Performance",
        "Resource Usage"
    ]
)

if st.button(
    "Generate Report"
):

    report = pd.DataFrame({

        "Metric":[
            "Sample 1",
            "Sample 2",
            "Sample 3"
        ],

        "Value":[
            100,
            200,
            300
        ]

    })

    st.dataframe(report)

    csv = report.to_csv(
        index=False
    )

    st.download_button(
        "Download CSV",
        csv,
        "report.csv",
        "text/csv"
    )