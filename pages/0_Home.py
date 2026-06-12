import streamlit as st

with open("assets/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ==========================================
# LOGIN PROTECTION
# ==========================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.warning(
        "Please login again."
    )

    st.stop()

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI Healthcare System",
    page_icon="🏥",
    layout="wide"
)

# ==========================================
# LOAD CSS
# ==========================================

with open("assets/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ==========================================
# SIDEBAR USER PANEL
# ==========================================

if st.button(
    "🚪 Logout",
    use_container_width=True
):

    st.session_state.clear()

    st.rerun()

# ==========================================
# TOP BAR
# ==========================================

col1, col2 = st.columns([8, 1])

with col1:

    
        unsafe_allow_html=True


# ==========================================
# MAIN DASHBOARD
# ==========================================

st.title(
    "🏥 AI-Powered Healthcare Prediction & Resource Management System"
)

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Patients", "1,250")

with col2:
    st.metric("Doctors", "85")

with col3:
    st.metric("Appointments", "340")

with col4:
    st.metric("Beds Available", "120")

st.markdown("---")

st.subheader("📊 System Overview")

st.info("""
Use the sidebar to navigate through modules.

Available Modules:

• Patient Management
• Doctor Management
• Appointments
• Analytics Dashboard
""")

st.image(
    "https://images.unsplash.com/photo-1576091160550-2173dba999ef",
    use_container_width=True
)

st.markdown("---")


