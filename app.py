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

# Formato do coração (usando placeholders)
heart_pattern = [
"    xx xx    ",
"   xxxxxx   ",
"   xxxxxx   ",
"    xxxxx    ",
"     xxxx     ",
"      xxx      ",
"       xx       ",
"        x        "
]

# Placeholder pra atualizar
placeholder = st.empty()

# Função para renderizar
def render_heart(step, color="white"):
    rendered = []
    count = 0

    for row in heart_pattern:
        new_row = ""
        for char in row:
            if char == "x":
                if count < step:
                    heart = "🤍" if color == "white" else "❤️"
                    new_row += heart
                else:
                    new_row += " "
                count += 1
            else:
                new_row += " "
        rendered.append(new_row)

    placeholder.markdown(
        '<div class="heart">' + "<br>".join(rendered) + '</div>',
        unsafe_allow_html=True
    )

# Contar total de corações
total_hearts = sum(row.count("x") for row in heart_pattern)

# 1. Aparecendo aos poucos em branco
for i in range(total_hearts + 1):
    render_heart(i, color="white")
    time.sleep(0.15)

# 2. Espera um pouquinho
time.sleep(0.5)

# 3. Todos ficam vermelhos
render_heart(total_hearts, color="red")
