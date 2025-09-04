import streamlit as st
import time
import random
from streamlit.components.v1 import html

# --------------------
# Configuración de la App
# --------------------
st.set_page_config(
    page_title="💕 Sorpresa Especial para Isabella 💕",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --------------------
# CSS Mejorado con tonos pastel y correcciones para fondo
# --------------------
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;600;700&family=Crimson+Text:ital,wght@0,400;0,600;1,400&display=swap');

:root {
    --primary: #ff99cc; /* Rosa pastel más suave */
    --secondary: #ff66b2; /* Rosa un poco más intenso */
    --accent: #ffd1dc; /* Rosa muy claro */
    --text: #4a4a4a; /* Gris oscuro para texto, buen contraste */
    --light-bg: #fff0f5; /* Fondo pastel general */
    --card-bg: #ffffff; /* Fondo blanco para las tarjetas */
    --shadow: rgba(255, 153, 204, 0.2); /* Sombra en tono rosa pastel */
}

body {
    font-family: 'Crimson Text', serif;
    color: var(--text);
    background: linear-gradient(135deg, var(--light-bg) 0%, #ffffff 100%); /* Gradiente suave de pastel a blanco */
    min-height: 100vh;
}

.main-container {
    background: var(--card-bg); /* Blanco puro o un pastel muy claro */
    border-radius: 20px;
    box-shadow: 0 20px 40px var(--shadow);
    padding: 2rem;
    margin: 1rem;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 153, 204, 0.3); /* Borde suave */
}

.header {
    text-align: center;
    margin-bottom: 2rem;
    animation: fadeInDown 1s ease-out;
}

.header h1 {
    font-family: 'Dancing Script', cursive;
    font-size: 3.5rem;
    font-weight: 700;
    background: linear-gradient(45deg, var(--primary), var(--secondary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
}

.header p {
    font-size: 1.2rem;
    color: var(--text);
    opacity: 0.8;
    margin-top: 0.5rem;
    font-style: italic;
}

.card {
    background: linear-gradient(145deg, var(--card-bg), var(--accent)); /* Gradiente suave para tarjetas */
    border-radius: 15px;
    padding: 2rem;
    margin: 1.5rem 0;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    border: 1px solid rgba(255, 153, 204, 0.1);
    transition: all 0.3s ease;
    animation: slideInUp 0.8s ease-out;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 40px rgba(255, 153, 204, 0.2);
}

.big-love {
    text-align: center;
    font-family: 'Dancing Script', cursive;
    font-weight: 700;
    font-size: 4rem;
    margin: 1rem 0;
    background: linear-gradient(45deg, var(--primary), var(--secondary), var(--primary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: pulse 2s infinite, colorShift 4s infinite;
}

.poem {
    color: var(--text); /* Asegura que el texto del poema sea oscuro */
    text-align: center;
    padding: 1rem;
    background: rgba(255, 255, 255, 0.7); /* Fondo más claro para el poema */
    border-radius: 10px;
    border-left: 4px solid var(--primary);
}

.poem pre {
    white-space: pre-wrap;
    font-family: 'Crimson Text', serif;
    font-size: 1.1rem;
    line-height: 1.8;
    margin: 0;
    background: transparent;
    border: none;
    padding: 0;
}

.floating-hearts {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 1000;
}

.heart {
    position: absolute;
    font-size: 20px;
    color: var(--primary);
    animation: float 6s infinite linear;
    opacity: 0.7;
}

.sparkle {
    display: inline-block;
    animation: sparkle 1.5s infinite;
}

.stButton > button {
    background: linear-gradient(45deg, var(--primary), var(--secondary)) !important;
    color: white !important;
    border: none !important;
    border-radius: 25px !important;
    padding: 0.8rem 2rem !important;
    font-size: 1.1rem !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 5px 15px var(--shadow) !important;
    width: 100%;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px var(--shadow) !important;
    filter: brightness(1.1);
}

.stRadio > div { background: transparent !important; }
.stRadio > div > label {
    background: rgba(255, 255, 255, 0.8) !important;
    border-radius: 10px !important;
    padding: 0.8rem !important;
    margin: 0.5rem 0 !important;
    border: 2px solid transparent !important;
    transition: all 0.3s ease !important;
    color: var(--text) !important; /* Asegura el color del texto del radio */
}

.stRadio > div > label:hover {
    border-color: var(--primary) !important;
    background: rgba(255, 153, 204, 0.1) !important; /* Tono pastel para hover */
}

.message-box {
    background: linear-gradient(135deg, rgba(255, 153, 204, 0.1), rgba(255, 102, 178, 0.1)); /* Tonos pastel */
    border-radius: 15px;
    padding: 1.5rem;
    margin: 1rem 0;
    border-left: 4px solid var(--primary);
    animation: slideInUp 0.5s ease-out;
    color: var(--text) !important; /* Asegura el color del texto */
}

/* Estilos para el texto de st.success */
.stSuccess {
    background-color: #e0ffe0 !important; /* Verde pastel muy claro */
    color: #3c763d !important; /* Verde oscuro para el texto */
    border-color: #d6e9c6 !important;
}

@keyframes fadeInDown {
    from { opacity: 0; transform: translateY(-30px); }
    to { opacity: 1; transform: translateY(0); }
}
@keyframes slideInUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}
@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.05); }
}
@keyframes colorShift {
    0%, 100% { filter: hue-rotate(0deg); }
    50% { filter: hue-rotate(20deg); }
}
@keyframes float {
    0% { transform: translateY(100vh) rotate(0deg); opacity: 0; }
    10% { opacity: 0.7; }
    90% { opacity: 0.7; }
    100% { transform: translateY(-100px) rotate(360deg); opacity: 0; }
}
@keyframes sparkle {
    0%, 100% { opacity: 0.3; transform: scale(1); }
    50% { opacity: 1; transform: scale(1.2); }
}
</style>
"""

st.markdown(CSS, unsafe_allow_html=True)

# --------------------
# Función de recarga segura
# --------------------
def safe_rerun():
    """Función de recarga compatible con varias versiones de Streamlit."""
    try:
        st.rerun()
    except Exception:
        st.experimental_rerun()

# --------------------
# Animación de corazones flotantes
# --------------------
def create_floating_hearts():
    hearts_html = """
    <div class='floating-hearts' id='hearts-container'></div>
    <script>
    function createHeart() {
        const heartsContainer = document.getElementById('hearts-container');
        if (!heartsContainer) return;

        const heart = document.createElement('div');
        heart.className = 'heart';
        heart.innerHTML = '💕';
        heart.style.left = Math.random() * 100 + '%';
        heart.style.animationDuration = (Math.random() * 3 + 4) + 's';
        heart.style.fontSize = (Math.random() * 10 + 15) + 'px';

        heartsContainer.appendChild(heart);

        setTimeout(() => {
            if (heart.parentNode) {
                heart.parentNode.removeChild(heart);
            }
        }, 7000);
    }
    setInterval(createHeart, 2000);
    for(let i = 0; i < 3; i++) {
        setTimeout(createHeart, i * 1000);
    }
    </script>
    """
    return hearts_html

# --------------------
# Loader con mensajes románticos
# --------------------
if 'loaded' not in st.session_state:
    st.session_state.loaded = False

if not st.session_state.loaded:
    romantic_messages = [
        "Preparando algo especial para ti... 💕",
        "Tejiendo palabras de amor... ✨",
        "Creando magia para Isabella... 🌟",
        "Despertando sonrisas... 💖",
        "Casi listo para sorprenderte... 🎀"
    ]

    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown("<div class='header'><h1>✨ Cargando Sorpresa ✨</h1></div>", unsafe_allow_html=True)

    progress = st.progress(0)
    message_placeholder = st.empty()

    for i in range(101):
        progress.progress(i)
        current_message_index = min(i // 20, len(romantic_messages) - 1)
        current_message = romantic_messages[current_message_index]
        message_placeholder.markdown(f"<div style='text-align:center; color:var(--text); font-size:1.1rem; margin:1rem 0'>{current_message}</div>", unsafe_allow_html=True)
        time.sleep(0.02)

    st.markdown("</div>", unsafe_allow_html=True)
    st.session_state.loaded = True
    safe_rerun()

# --------------------
# Interfaz principal mejorada
# --------------------
html(create_floating_hearts(), height=0)

st.markdown("<div class='main-container'>", unsafe_allow_html=True)
st.markdown("<div class='header'><h1>💕 Sorpresa Especial 💕</h1><p>Un rincón mágico creado solo para Isabella</p></div>", unsafe_allow_html=True)

choice = st.radio("✨ Elige tu momento especial:",
                  ("💖 Declaración de amor gigante",
                   "📝 Poema dedicado",
                   "🎈 Diversión y alegría",
                   "💌 Carta del corazón",
                   "🌟 Sorpresa interactiva"), horizontal=True, label_visibility="collapsed")

# --- Opción 1: Declaración de amor animada ---
if choice == "💖 Declaración de amor gigante":
    enhanced_love_html = f"""
    <div class='card' style='text-align:center; padding:2rem;'>
        <div style='font-family:"Dancing Script", cursive; font-size:2rem; color:var(--text); margin-bottom:1rem'>
            Para la hermosa Isabella <span class='sparkle'>✨</span>
        </div>
        <div class='big-love'>TE AMO INFINITAMENTE</div>
        <svg width='300' height='250' viewBox='0 0 32 29.6' xmlns='http://www.w3.org/2000/svg' style='margin:1rem 0'>
            <defs>
                <linearGradient id='heartGradient' x1='0%' y1='0%' x2='100%' y2='100%'>
                    <stop offset='0%' style='stop-color:#ff99cc;stop-opacity:1' />
                    <stop offset='50%' style='stop-color:#ff66b2;stop-opacity:1' />
                    <stop offset='100%' style='stop-color:#ff99cc;stop-opacity:1' />
                </linearGradient>
            </defs>
            <path d='M23.6,0c-2.7,0-4.9,1.6-6,3.8C16.3,1.6,14.1,0,11.4,0C5.1,0,0,5.1,0,11.4c0,7.1,7.5,11.6,16,18.2 c8.5-6.6,16-11.1,16-18.2C32,5.1,26.9,0,20.6,0z' fill='url(#heartGradient)'>
                <animate attributeName='opacity' values='0.7;1;0.7' dur='2s' repeatCount='indefinite'/>
                <animateTransform attributeName='transform' attributeType='XML' type='scale'
                  values='0.95;1.1;0.95' dur='2s' repeatCount='indefinite'/>
            </path>
        </svg>
        <div style='font-size:1.2rem; color:var(--text); font-style:italic; margin-top:1rem'>
            Eres la luz que ilumina cada uno de mis días 🌟
        </div>
        <div style='margin-top:1.5rem; font-size:1rem; color:var(--secondary)'>
            Con todo mi amor, siempre y para siempre 💕
        </div>
    </div>
    """
    html(enhanced_love_html, height=450)

# --- Opción 2: Poema dedicado con nuevo texto y formato corregido ---
elif choice == "📝 Poema dedicado":
    # Nuevo poema proporcionado
    enhanced_poem = """rubio incendio en la penumbra,

cada rizo es un latido que no sé nombrar.
sonrisa —abismo dulce—

me arroja al centro de lo imposible,

allí donde la piel se vuelve plegaria.
tu piel:

un lenguaje que la noche traduce en deseo.

tu alma:

una constelación que insiste en quedarse,

aun cuando todo lo demás se desvanezca.
te nombro en silencio,

y el mundo es apenas un eco

del resplandor que dejas en mí."""

    poem_html = f"""
    <div class='card'>
        <div style='text-align:center; font-family:"Dancing Script", cursive; font-size:1.8rem; color:var(--primary); margin-bottom:1.5rem'>
            Versos para Isabella ✨
        </div>
        <div class='poem'>
            <pre>{enhanced_poem}</pre>
        </div>
    </div>
    """
    st.markdown(poem_html, unsafe_allow_html=True)


# --- Opción 3: Diversión interactiva ---
elif choice == "🎈 Diversión y alegría":
    st.markdown("<div class='card' style='text-align:center'>", unsafe_allow_html=True)
    st.markdown("<div style='font-family:\"Dancing Script\", cursive; font-size:2rem; margin-bottom:1rem; color:var(--primary)'>¡Momento de Diversión! 🎉</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🎈 Globos", key="balloons"):
            st.balloons()
            st.success("¡Globos de felicidad para ti! 🎈✨")
    with col2:
        if st.button("❄️ Nieve", key="snow"):
            st.snow()
            st.success("¡Nieve mágica cayendo para ti! ❄️💕")
    with col3:
        if st.button("🎊 Sorpresa", key="surprise"):
            st.balloons()
            time.sleep(0.5)
            st.snow()
            st.success("¡Doble sorpresa! ¡Eres increíble! 🌟")

    st.markdown("<hr style='margin: 2rem 0; border-color: var(--shadow);'>", unsafe_allow_html=True)
    
    compliments = [
        "Tu sonrisa ilumina el mundo entero ✨",
        "Eres más hermosa que todas las flores del mundo 🌸",
        "Tu risa es la melodía más dulce que existe 🎵",
        "Eres un rayo de sol en días nublados ☀️",
        "Tu corazón es puro oro 💛",
        "Eres la definición perfecta de belleza y gracia (además karateca, ídola) 👑"
    ]
    if st.button("💫 Mensaje Especial para Ti", key="compliment"):
        selected_compliment = random.choice(compliments)
        st.markdown(f"<div class='message-box' style='text-align:center; font-size:1.2rem'>{selected_compliment}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- Opción 4: Carta personalizada ---
elif choice == "💌 Carta del corazón":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div style='font-family:\"Dancing Script\", cursive; font-size:2rem; color:var(--primary); margin-bottom:1rem'>Carta Especial 💌</div>", unsafe_allow_html=True)

    enhanced_letter = """Mi querida Isabella,

Hoy quiero que sepas lo extraordinaria que eres. No solo por tu belleza exterior, que es innegable, sino por esa luz especial que llevas dentro y que ilumina todo a tu alrededor.

Eres esa persona que hace que los días grises se vuelvan coloridos, que convierte los momentos ordinarios en recuerdos preciosos. Tu manera de ser, tu risa, lo inquieta que eres, tu forma de ver el mundo... todo en ti es mágico.

Si alguna vez dudas de lo maravillosa que eres, recuerda que hay alguien que te ama y admira profundamente, que valora cada detalle tuyo y que se siente afortunado de estar contigo.

Sin lugar a duda eres especial y no porque parezcas goku super saiyan 3, sino por tu esencia. No permitas que nadie te haga sentir lo contrario, porque tu valor es infinito.

Con todo mi cariño y amor,
El ingeniero que te ama💕"""
    st.markdown(f"<div style='font-size:1.1rem; line-height:1.8; color:var(--text)'>{enhanced_letter}</div>", unsafe_allow_html=True)

    st.markdown("<div style='margin-top:2rem; padding-top:1rem; border-top:2px solid var(--primary)'>", unsafe_allow_html=True)
    st.markdown("<div style='font-size:1.1rem; color:var(--secondary); margin-bottom:1rem'>✍️ Crea tu mensaje personalizado:</div>", unsafe_allow_html=True)
    
    user_message = st.text_area("Escribe algo especial para Isabella:", placeholder="Tu mensaje aquí...")
    
    if user_message:
        st.markdown(f"<div class='message-box'><strong>Tu mensaje:</strong><br><em>{user_message}</em></div>", unsafe_allow_html=True)
        
        if st.button("🎊 Mostrar con Celebración", key="celebrate_message"):
            st.balloons()
            st.success("¡Mensaje enviado con amor! 💕")
    st.markdown("</div></div>", unsafe_allow_html=True)

# --- Opción 5: Sorpresa interactiva ---
elif choice == "🌟 Sorpresa interactiva":
    st.markdown("<div class='card' style='text-align:center'>", unsafe_allow_html=True)
    st.markdown("<div style='font-family:\"Dancing Script\", cursive; font-size:2rem; color:var(--primary); margin-bottom:1.5rem'>Sorpresa Especial Interactiva 🌟</div>", unsafe_allow_html=True)

    st.markdown("### 🔮 Pregúntale al Corazón")
    st.markdown("*Haz una pregunta sobre ti misma y descubre algo hermoso...*")
    question = st.text_input("¿Qué quieres saber sobre ti?", placeholder="Por ejemplo: ¿Soy especial?")

    magical_answers = [
        "Absolutamente sí, eres increíblemente especial ✨",
        "Sin duda alguna, tu luz brilla más que las estrellas 🌟",
        "Por supuesto, eres una obra maestra de la naturaleza 🎨",
        "Definitivamente, tu corazón es puro oro 💛",
        "¡Claro que sí! Eres única e irreemplazable 👑",
        "Absolutamente, tu sonrisa puede cambiar el mundo 😊"
    ]

    if question and st.button("🔮 Revelar la Respuesta Mágica"):
        answer = random.choice(magical_answers)
        st.markdown(f"<div class='message-box' style='text-align:center; font-size:1.3rem; background: linear-gradient(135deg, rgba(255, 153, 204, 0.2), rgba(255, 102, 178, 0.2))'><strong>🔮 El corazón responde:</strong><br><br><em>{answer}</em></div>", unsafe_allow_html=True)
        st.balloons()

    st.markdown("<hr style='margin: 2rem 0; border-color: var(--shadow);'>", unsafe_allow_html=True)

    st.markdown("### 💕 Medidor de Amor Especial")
    if st.button("💖 Calcular tu Nivel de Amor Recibido"):
        love_percentage = random.randint(95, 100)
        st.markdown(f"<div class='message-box' style='text-align:center'><h2 style='color:var(--primary); font-family:\"Dancing Script\", cursive'>{love_percentage}% 💕</h2><p style='font-size:1.2rem'>¡Eres amada al {love_percentage}%! Tu corazón merece todo el amor del mundo.</p></div>", unsafe_allow_html=True)
        st.snow()
    st.markdown("</div>", unsafe_allow_html=True)

# --- Pie de página mejorado ---
st.markdown("<div style='text-align:center; margin-top:3rem; padding:2rem; color:var(--secondary); font-style:italic'>", unsafe_allow_html=True)
st.markdown("✨ Creado con amor infinito para Isabella ✨<br>💕 Que cada día te traiga sonrisas y felicidad 💕", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
