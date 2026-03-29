import streamlit as st

st.set_page_config(page_title="Para Você ❤️", layout="centered")

st.markdown("""
<style>
.stApp {
    background-color: black;
}

.title {
    text-align: center;
    font-size: 32px;
    color: #ff4da6;
    margin-top: 60px;
    font-weight: bold;
}

/* coração */
.heart {
    text-align: center;
    font-size: 22px;
    line-height: 22px;
    margin-top: 80px;
}

/* animação */
.heart span {
    opacity: 0;
    display: inline-block;
    animation: aparecer 0.5s forwards;
}

@keyframes aparecer {
    to {
        opacity: 1;
    }
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">Para você 🌹</div>', unsafe_allow_html=True)

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

html_heart = "<div class='heart'>"

delay = 0

for line in heart_pattern:
    for char in line:
        if char == "❤️":
            html_heart += f"<span style='animation-delay:{delay}s'>❤️</span>"
            delay += 0.03
        else:
            html_heart += " "
    html_heart += "<br>"

html_heart += "</div>"

st.markdown(html_heart, unsafe_allow_html=True)
