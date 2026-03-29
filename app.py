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

# Inicializa estado
if "step" not in st.session_state:
    st.session_state.step = 0

# Flatten (transforma tudo em lista de posições)
positions = []
for i, line in enumerate(heart_pattern):
    for j, char in enumerate(line):
        if char == "❤️":
            positions.append((i, j))

# Cria estrutura vazia
current = [[" " for _ in line] for line in heart_pattern]

# Preenche até o step atual
for k in range(min(st.session_state.step, len(positions))):
    i, j = positions[k]
    current[i][j] = "❤️"

# Mostra
display = ["".join(row) for row in current]

st.markdown(
    "<div class='heart'>" + "<br>".join(display) + "</div>",
    unsafe_allow_html=True
)

# Avança animação
if st.session_state.step < len(positions):
    st.session_state.step += 1
    time.sleep(0.03)
    st.rerun()
