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
st.markdown('<div class="title"> Para você 🌹</div>', unsafe_allow_html=True)

# Estrutura do coração
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

# Placeholder para animação
placeholder = st.empty()

# Construção animada
current_lines = [" " * len(line) for line in heart_pattern]

for i, line in enumerate(heart_pattern):
    new_line = list(current_lines[i])

    for j, char in enumerate(line):
        if char == "❤️":
            new_line[j] = "❤️"
            current_lines[i] = "".join(new_line)

            placeholder.markdown(
                '<div class="heart">' + "<br>".join(current_lines) + '</div>',
                unsafe_allow_html=True
            )

            time.sleep(0.05)  # velocidade da animação

        else:
            new_line[j] = " "

    current_lines[i] = "".join(new_line)
