import streamlit as st
import time

st.set_page_config(page_title="Para Você ❤️", layout="centered")

# CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
    }
    .title {
        text-align: center;
        font-size: 32px;
        color: #ff4da6;
        margin-top: 60px;
        font-weight: bold;
    }
    .heart {
        text-align: center;
        font-size: 22px;
        line-height: 22px;
        margin-top: 80px;
    }
    </style>
""", unsafe_allow_html=True)

# Título
st.markdown('<div class="title">Para você 🌹</div>', unsafe_allow_html=True)

# Coração base
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

# Placeholder único
placeholder = st.empty()

# Lista vazia inicial
current = [" " * len(line) for line in heart_pattern]

# Animação
for i in range(len(heart_pattern)):
    for j in range(len(heart_pattern[i])):
        if heart_pattern[i][j] == "❤️":
            linha = list(current[i])
            linha[j] = "❤️"
            current[i] = "".join(linha)

            placeholder.markdown(
                "<div class='heart'>" + "<br>".join(current) + "</div>",
                unsafe_allow_html=True
            )

            time.sleep(0.04)
