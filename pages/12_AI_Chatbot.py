import streamlit as st

with open("assets/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("🤖 AI Healthcare Assistant")

from utils.chatbot import (
    get_healthcare_response
)



# ==========================
# PROFESSIONAL UI STYLING
# ==========================

st.markdown("""
<style>

/* Chat Messages */
[data-testid="stChatMessage"]{
    border-radius:18px;
    padding:15px;
    margin-bottom:12px;
    border:1px solid rgba(255,255,255,0.1);
    box-shadow:0 4px 12px rgba(0,0,0,0.15);
}

/* User Messages */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
    background: linear-gradient(
        135deg,
        rgba(34,197,94,0.25),
        rgba(22,163,74,0.15)
    );
}

/* Assistant Messages */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
    background: linear-gradient(
        135deg,
        rgba(59,130,246,0.20),
        rgba(30,64,175,0.15)
    );
}

/* Chat Input */
[data-testid="stChatInput"] {
    border-radius:15px;
}

/* Buttons */
.stButton > button {
    width:100%;
    border-radius:12px;
    font-weight:bold;
    transition:0.3s;
}

.stButton > button:hover {
    transform:translateY(-2px);
}

/* Metrics */
[data-testid="metric-container"]{
    border-radius:15px;
    padding:10px;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# HERO SECTION
# ==========================

st.markdown("""
<div style="
padding:20px;
border-radius:20px;
background:linear-gradient(135deg,#059669,#16a34a);
color:white;
text-align:center;
margin-bottom:20px;
">

<h2>🏥 AI Healthcare Assistant</h2>

<p>
Get symptom guidance, wellness advice,
disease education and healthcare support
powered by Gemini AI.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("""
Ask questions about:

- Symptoms
- Diseases
- Nutrition
- Fitness
- Appointments
- Medicines
- Healthcare Tips
""")

# ==========================
# SIDEBAR
# ==========================

st.sidebar.header(
    "Quick Health Questions"
)

quick_question = st.sidebar.selectbox(
    "Choose",
    [
        "",
        "What are diabetes symptoms?",
        "How to reduce blood pressure?",
        "Heart disease prevention",
        "Healthy diet tips",
        "Weight loss suggestions"
    ]
)

# ==========================
# STATS
# ==========================

if "messages" not in st.session_state:
    st.session_state.messages = []

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Conversations",
        len(st.session_state.messages)
    )

with col2:
    st.metric(
        "AI Model",
        "Gemini"
    )

with col3:
    st.metric(
        "Status",
        "Online"
    )

st.markdown("---")

# ==========================
# QUICK ACTION BUTTONS
# ==========================

col1, col2, col3 = st.columns(3)

with col1:
    symptom_btn = st.button(
        "🩺 Symptoms"
    )

with col2:
    medicine_btn = st.button(
        "💊 Medicines"
    )

with col3:
    diet_btn = st.button(
        "🥗 Diet Tips"
    )

# ==========================
# HANDLE QUICK QUESTIONS
# ==========================

user_prompt = None

if quick_question:
    user_prompt = quick_question

if symptom_btn:
    user_prompt = (
        "What symptoms indicate a serious illness?"
    )

if medicine_btn:
    user_prompt = (
        "Give medication safety tips."
    )

if diet_btn:
    user_prompt = (
        "Suggest a healthy diet plan."
    )

chat_input = st.chat_input(
    "Ask a healthcare question..."
)

if chat_input:
    user_prompt = chat_input

# ==========================
# DISPLAY CHAT HISTORY
# ==========================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )

# ==========================
# PROCESS MESSAGE
# ==========================

if user_prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )

    with st.chat_message(
        "user"
    ):
        st.markdown(
            user_prompt
        )

    with st.spinner(
        "🧠 Gemini is analyzing..."
    ):

        answer = get_healthcare_response(
            user_prompt
        )

    with st.chat_message(
        "assistant"
    ):
        st.markdown(
            answer
        )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

# ==========================
# DISCLAIMER
# ==========================

st.markdown("---")

st.warning("""
⚠️ Medical Disclaimer

This AI assistant provides educational
health information only.

It is not a substitute for professional
medical advice, diagnosis or treatment.

Always consult a qualified healthcare
professional for medical concerns.
""")