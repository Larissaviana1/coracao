import streamlit as st
import time

st.set_page_config(page_title="Para Você ❤️", layout="centered")

# CSS com animação de pulsar
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
    .pulse {
        animation: pulse 1.2s infinite;
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.15); }
        100% { transform: scale(1); }
    }
    </style>
""", unsafe_allow_html=True)

# Título
st.markdown('<div class="title">Para você 🌹</div>', unsafe_allow_html=True)

# Formato do coração
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

placeholder = st.empty()

def render_heart(step, color="white", pulse=False):
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

    pulse_class = "pulse" if pulse else ""

    placeholder.markdown(
        f'<div class="heart {pulse_class}">' + "<br>".join(rendered) + '</div>',
        unsafe_allow_html=True
    )

# Total de corações
total_hearts = sum(row.count("x") for row in heart_pattern)

# 1. Aparecendo em branco
for i in range(total_hearts + 1):
    render_heart(i, color="white")
    time.sleep(0.12)

# 2. Pausa
time.sleep(0.5)

# 3. Fica vermelho
render_heart(total_hearts, color="red")
time.sleep(0.5)

# 4. Começa a pulsar ❤️
render_heart(total_hearts, color="red", pulse=True)
