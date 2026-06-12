import streamlit as st
import pandas as pd

with open("assets/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )
import os

st.title("📋 Electronic Health Records (EHR)")

st.markdown("""
Manage and view patient medical records, prescriptions,
diagnostic reports, and treatment history.
""")

# ==========================================
# LOAD DATA
# ==========================================

if not os.path.exists("data/medical_records.csv"):

    st.error(
        "medical_records.csv file not found in data folder."
    )

    st.stop()

try:

    df = pd.read_csv(
        "data/medical_records.csv"
    )

except Exception as e:

    st.error(
        f"Error loading records: {e}"
    )

    st.stop()

# ==========================================
# SEARCH
# ==========================================

search_patient = st.text_input(
    "🔍 Search Patient Name"
)

if search_patient:

    filtered_df = df[
        df["Patient Name"]
        .str.contains(
            search_patient,
            case=False,
            na=False
        )
    ]

else:

    filtered_df = df

# ==========================================
# METRICS
# ==========================================

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Total Records",
        len(df)
    )

with col2:

    st.metric(
        "Unique Patients",
        df["Patient Name"].nunique()
    )

with col3:

    st.metric(
        "Doctors",
        df["Doctor"].nunique()
    )

st.markdown("---")

# ==========================================
# RECORDS TABLE
# ==========================================

st.subheader(
    "📑 Medical Records"
)

st.dataframe(
    filtered_df,
    use_container_width=True
)

# ==========================================
# PATIENT DETAILS
# ==========================================

st.markdown("---")

st.subheader(
    "👤 Patient Details"
)

patient = st.selectbox(
    "Select Patient",
    df["Patient Name"].unique()
)

patient_data = df[
    df["Patient Name"] == patient
]

if not patient_data.empty:

    record = patient_data.iloc[0]

    col1, col2 = st.columns(2)

    with col1:

        st.write(
            f"**Patient ID:** {record['Patient ID']}"
        )

        st.write(
            f"**Age:** {record['Age']}"
        )

        st.write(
            f"**Gender:** {record['Gender']}"
        )

        st.write(
            f"**Blood Group:** {record['Blood Group']}"
        )

    with col2:

        st.write(
            f"**Disease:** {record['Disease']}"
        )

        st.write(
            f"**Doctor:** {record['Doctor']}"
        )

        st.write(
            f"**Visit Date:** {record['Visit Date']}"
        )

st.markdown("---")

# ==========================================
# PRESCRIPTION
# ==========================================

st.subheader(
    "💊 Prescription"
)

st.info(
    record["Prescription"]
)

# ==========================================
# LAB REPORT
# ==========================================

st.subheader(
    "🧪 Lab Report"
)

st.success(
    record["Lab Report"]
)