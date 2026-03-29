import streamlit as st

st.set_page_config(page_title="Para Você ❤️", layout="centered")

# CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
    }
    .title {
        text-align: center;
        font-size: 32px;  /* ↓ diminuí aqui */
        color: #ff4da6;
        margin-top: 60px;
        font-weight: bold;
    }
    .heart {
        text-align: center;
        font-size: 22px;
        line-height: 22px;
        margin-top: 80px;
        animation: pulse 1.5s infinite;
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.12); }
        100% { transform: scale(1); }
    }
    </style>
""", unsafe_allow_html=True)

# Título menor
st.markdown('<div class="title"> Para você 🌹</div>', unsafe_allow_html=True)

# Coração
heart_pattern = [
"    ❤️❤️ ❤️❤️    ",
"   ❤️❤️❤️❤️❤️❤️   ",
"   ❤️❤️❤️❤️❤️❤️   ",
"    ❤️❤️❤️❤️❤️    ",
"     ❤️❤️❤️❤️     ",
"      ❤️❤️❤️      ",
"       ❤️❤️       ",
"        ❤️        "
]

st.markdown(
    '<div class="heart">' + "<br>".join(heart_pattern) + '</div>',
    unsafe_allow_html=True
)
