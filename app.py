import streamlit as st

st.set_page_config(page_title="Para Você ❤️", layout="centered")

# CSS fundo preto
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
        font-size: 22px;
        line-height: 22px;
        margin-top: 80px;
        animation: pulse 1.5s infinite;
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    </style>
""", unsafe_allow_html=True)

# Título
st.markdown('<div class="title">para você</div>', unsafe_allow_html=True)

# Desenho do coração com emojis
heart_pattern = [
"  ❤️❤️   ❤️❤️  ",
" ❤️❤️❤️ ❤️❤️❤️ ",
"❤️❤️❤️❤️❤️❤️❤️ ",
"  ❤️❤️❤️❤️❤️❤️  ",
"   ❤️❤️❤️❤️❤️   ",
"    ❤️❤️❤️❤️    ",
"     ❤️❤️❤️     ",
"      ❤️❤️      ",
"       ❤️       "
]

# Mostrar coração
st.markdown(
    '<div class="heart">' + "<br>".join(heart_pattern) + '</div>',
    unsafe_allow_html=True
)
