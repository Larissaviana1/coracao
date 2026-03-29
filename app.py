import streamlit as st

st.set_page_config(page_title="Para Você ❤️", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
    }
    .title {
        text-align: center;
        font-size: 50px;
        color: white;
        margin-top: 50px;
        font-weight: bold;
    }
    .heart {
        text-align: center;
        font-size: 120px;
        margin-top: 100px;
        animation: pulse 1.5s infinite;
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">para você</div>', unsafe_allow_html=True)
st.markdown('<div class="heart">❤️</div>', unsafe_allow_html=True)
