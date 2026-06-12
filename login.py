import streamlit as st
import json
import os

# ==========================================
# SESSION CHECK
# ==========================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    st.switch_page("pages/0_Home.py")

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Healthcare Login",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# CSS
# ==========================================

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

[data-testid="stSidebar"]{
    display:none;
}

.stApp{
    background:
    linear-gradient(
        135deg,
        #0f172a,
        #1e3a8a,
        #0f766e
    );
}

.main-title{
    text-align:center;
    font-size:55px;
    font-weight:800;
    color:white;
    margin-top:20px;
}

.subtitle{
    text-align:center;
    font-size:20px;
    color:#cbd5e1;
    margin-bottom:20px;
}

.banner{
    background:linear-gradient(
        90deg,
        #3b82f6,
        #06b6d4,
        #22c55e
    );

    padding:18px;
    border-radius:18px;
    text-align:center;
    color:white;
    font-size:22px;
    font-weight:600;
    margin-bottom:20px;
}

[data-testid="stAlert"]{
    background:rgba(255,255,255,0.08);
    color:white;
    border-radius:15px;
    border:1px solid rgba(255,255,255,0.1);
}

label{
    color:white !important;
    font-weight:600;
}

.stTextInput input{
    background:rgba(255,255,255,0.1) !important;
    color:white !important;
    border:1px solid rgba(255,255,255,0.2) !important;
    border-radius:12px !important;
}

.stButton > button{
    background:
    linear-gradient(
        90deg,
        #14b8a6,
        #22c55e
    ) !important;

    color:white !important;
    font-size:18px !important;
    font-weight:bold !important;
    height:50px !important;
    border:none !important;
    border-radius:12px !important;
    width:100%;
}

.stButton > button:hover{
    transform:translateY(-2px);
}

.stTabs [data-baseweb="tab"]{
    font-size:18px;
    font-weight:bold;
    color:white;
}

.footer{
    text-align:center;
    color:white;
    font-size:16px;
    margin-top:30px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# HEADER
# ==========================================

st.markdown("""
<div class="main-title">
🏥 AI-Powered Healthcare System
</div>

<div class="subtitle">
Intelligent Healthcare Platform for Prediction,
Analytics & Resource Management
</div>
""", unsafe_allow_html=True)

# ==========================================
# BANNER
# ==========================================

st.markdown("""
<div class="banner">
🩺 Empowering Better Healthcare Through AI
</div>
""", unsafe_allow_html=True)

# ==========================================
# FEATURES
# ==========================================

c1, c2, c3 = st.columns(3)

with c1:
    st.info("🧠 AI Disease Prediction")

with c2:
    st.info("📊 Resource Optimization")

with c3:
    st.info("🏥 Smart Healthcare Analytics")

st.write("")

# ==========================================
# LOGIN / REGISTER
# ==========================================

left, center, right = st.columns([1.2, 1.5, 1.2])

with center:

    tab1, tab2 = st.tabs(
        ["🔐 Login", "📝 Register"]
    )

    # ======================================
    # LOGIN
    # ======================================

    with tab1:

        email = st.text_input(
            "Email"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button(
            "Login"
        ):

            if os.path.exists(
                "users.json"
            ):

                with open(
                    "users.json",
                    "r"
                ) as f:

                    users = json.load(f)

                found = False

                for user in users:

                    if (
                        user["email"] == email
                        and
                        user["password"] == password
                    ):

                        found = True

                        st.session_state.logged_in = True
                        st.session_state.username = user["name"]

                        st.success(
                            f"Welcome {user['name']}"
                        )

                        st.switch_page(
                            "pages/0_Home.py"
                        )

                        break

                if not found:

                    st.error(
                        "Invalid Credentials"
                    )

            else:

                st.error(
                    "No Registered Users Found"
                )

    # ======================================
    # REGISTER
    # ======================================

    with tab2:

        name = st.text_input(
            "Full Name"
        )

        new_email = st.text_input(
            "Email Address",
            key="reg_email"
        )

        new_password = st.text_input(
            "Password",
            type="password",
            key="regpass"
        )

        if st.button(
            "Register"
        ):

            if os.path.exists(
                "users.json"
            ):

                with open(
                    "users.json",
                    "r"
                ) as f:

                    users = json.load(f)

            else:

                users = []

            email_exists = any(
                user["email"] == new_email
                for user in users
            )

            if email_exists:

                st.warning(
                    "Email already registered"
                )

            else:

                users.append({

                    "name": name,
                    "email": new_email,
                    "password": new_password

                })

                with open(
                    "users.json",
                    "w"
                ) as f:

                    json.dump(
                        users,
                        f,
                        indent=4
                    )

                st.success(
                    "Registration Successful"
                )

# ==========================================
# FOOTER
# ==========================================

st.markdown("""
<div class="footer">
❤️ Better Healthcare Through AI Innovation
</div>
""", unsafe_allow_html=True)