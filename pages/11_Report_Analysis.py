import streamlit as st

with open("assets/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("📄 Medical Report Analysis")


uploaded_file = st.file_uploader(
    "Upload Medical Report"
)

if uploaded_file:

    st.success(
        "Report Uploaded Successfully"
    )

    st.subheader(
        "AI Findings"
    )

    st.warning(
        "Hemoglobin Level Low"
    )

    st.warning(
        "Possible Risk: Anemia"
    )

    st.success(
        "Consult Hematologist"
    )