import streamlit as st
import time
import random
from streamlit.components.v1 import html

# --------------------
# App config
# --------------------
st.set_page_config(
    page_title="💕 Sorpresa Especial para Isabella 💕", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --------------------
# Enhanced CSS with beautiful animations and gradients
# --------------------
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;600;700&family=Crimson+Text:ital,wght@0,400;0,600;1,400&display=swap');

:root { 
    --primary: #ff6b9d; 
    --secondary: #c44569;
    --accent: #f8b500;
    --text: #2c2c54;
    --light: #fff5f8;
    --shadow: rgba(255, 107, 157, 0.2);
}

body { 
    font-family: 'Crimson Text', serif; 
    color: var(--text); 
    background: linear-gradient(135deg, #ffeef8 0%, #fff5f8 50%, #f0f8ff 100%);
    min-height: 100vh;
}

.main-container {
    background: rgba(255, 255, 255, 0.9);
    border-radius: 20px;
    box-shadow: 0 20px 40px var(--shadow);
    padding: 2rem;
    margin: 1rem;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.3);
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
    background: linear-gradient(145deg, #ffffff, #f8f9fa);
    border-radius: 15px;
    padding: 2rem;
    margin: 1.5rem 0;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    border: 1px solid rgba(255, 107, 157, 0.1);
    transition: all 0.3s ease;
    animation: slideInUp 0.8s ease-out;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 40px rgba(255, 107, 157, 0.2);
}

.big-love { 
    text-align: center; 
    font-family: 'Dancing Script', cursive;
    font-weight: 700; 
    font-size: 4rem; 
    margin: 1rem 0;
    background: linear-gradient(45deg, #ff6b9d, #c44569, #ff6b9d);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: pulse 2s infinite, colorShift 4s infinite;
}

.poem { 
    white-space: pre-wrap; 
    font-size: 1.1rem; 
    line-height: 1.8; 
    color: var(--text);
    text-align: center;
    padding: 1rem;
    background: rgba(255, 255, 255, 0.5);
    border-radius: 10px;
    border-left: 4px solid var(--primary);
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

.love-button {
    background: linear-gradient(45deg, var(--primary), var(--secondary)) !important;
    color: white !important;
    border: none !important;
    border-radius: 25px !important;
    padding: 0.8rem 2rem !important;
    font-size: 1.1rem !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 5px 15px var(--shadow) !important;
}

.love-button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px var(--shadow) !important;
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

.stRadio > div { background: transparent !important; }
.stRadio > div > label { 
    background: rgba(255, 255, 255, 0.8) !important;
    border-radius: 10px !important;
    padding: 0.8rem !important;
    margin: 0.5rem 0 !important;
    border: 2px solid transparent !important;
    transition: all 0.3s ease !important;
}

.stRadio > div > label:hover {
    border-color: var(--primary) !important;
    background: rgba(255, 107, 157, 0.1) !important;
}

.message-box {
    background: linear-gradient(135deg, rgba(255, 107, 157, 0.1), rgba(196, 69, 105, 0.1));
    border-radius: 15px;
    padding: 1.5rem;
    margin: 1rem 0;
    border-left: 4px solid var(--primary);
    animation: slideInUp 0.5s ease-out;
}
</style>
"""

st.markdown(CSS, unsafe_allow_html=True)

# --------------------
# Enhanced safe rerun function
# --------------------
def safe_rerun():
    """Enhanced rerun function with better error handling"""
    try:
        st.rerun()
    except Exception:
        try:
            if hasattr(st, "experimental_rerun"):
                st.experimental_rerun()
        except Exception:
            try:
                st.experimental_set_query_params(_rerun=int(time.time()))
            except Exception:
                pass

# --------------------
# Floating hearts animation
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
    
    // Create hearts periodically
    setInterval(createHeart, 2000);
    
    // Create initial hearts
    for(let i = 0; i < 3; i++) {
        setTimeout(createHeart, i * 1000);
    }
    </script>
    """
    return hearts_html

# --------------------
# Enhanced loader with romantic messages
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
    
    for i in range(0, 101, 4):
        progress.progress(i)
        current_message = romantic_messages[i // 20] if i // 20 < len(romantic_messages) else romantic_messages[-1]
        message_placeholder.markdown(f"<div style='text-align:center; color:var(--text); font-size:1.1rem; margin:1rem 0'>{current_message}</div>", unsafe_allow_html=True)
        time.sleep(0.03)
    
    st.markdown("</div>", unsafe_allow_html=True)
    st.session_state.loaded = True
    safe_rerun()

# --------------------
# Main enhanced UI
# --------------------
html(create_floating_hearts(), height=0)

st.markdown("<div class='main-container'>", unsafe_allow_html=True)
st.markdown("<div class='header'><h1>💕 Sorpresa Especial 💕</h1><p>Un rincón mágico creado especialmente para Isabella</p></div>", unsafe_allow_html=True)

# Enhanced options with emojis and better descriptions
choice = st.radio("✨ Elige tu momento especial:",
                  ("💖 Declaración de amor gigante", 
                   "📝 Poema lírico dedicado", 
                   "🎈 Diversión y alegría", 
                   "💌 Carta del corazón",
                   "🌟 Sorpresa interactiva"))

# --- Enhanced Option 1: Animated love declaration ---
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
                    <stop offset='0%' style='stop-color:#ff6b9d;stop-opacity:1' />
                    <stop offset='50%' style='stop-color:#c44569;stop-opacity:1' />
                    <stop offset='100%' style='stop-color:#ff6b9d;stop-opacity:1' />
                </linearGradient>
            </defs>
            <path d='M23.6,0c-2.7,0-4.9,1.6-6,3.8C16.3,1.6,14.1,0,11.4,0C5.1,0,0,5.1,0,11.4c0,7.1,7.5,11.6,16,18.2
              c8.5-6.6,16-11.1,16-18.2C32,5.1,26.9,0,20.6,0z' fill='url(#heartGradient)'>
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
    html(enhanced_love_html, height=400)

# --- Enhanced Option 2: Beautiful poem with better formatting ---
elif choice == "📝 Poema dedicado":
    enhanced_poem = """Isabella, estrella de mis versos,

Eres melodía que danza en el viento,
cabellos de oro que abrazan la luz,
y en cada rizo vive un secreto
que solo mi corazón puede leer.

Te nombro en el silencio de las tardes,
cuando las palabras se vuelven mariposas
y vuelan hacia ti con alas de seda,
llevando susurros de amor eterno.

Cruzas mi mundo con gracia infinita,
y yo aprendo a escribir tu nombre
en las estrellas, en las olas del mar,
en cada latido que me recuerda
que el amor verdadero existe.

No me pidas que deje de amarte,
porque eres el verso que nunca termino,
la canción que siempre quiero cantar,
el sueño del que nunca quiero despertar.

Ven, quédate en este momento,
donde las palabras se vuelven caricias
y el tiempo se detiene solo para nosotros,
idénticos en este amor que nos une."""

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center; font-family:\"Dancing Script\", cursive; font-size:1.8rem; color:var(--primary); margin-bottom:1.5rem'>Versos para Isabella ✨</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='poem'>{enhanced_poem}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- Enhanced Option 3: Interactive fun with multiple surprises ---
elif choice == "🎈 Diversión y alegría":
    st.markdown("<div class='card' style='text-align:center'>", unsafe_allow_html=True)
    st.markdown("<div style='font-family:\"Dancing Script\", cursive; font-size:2rem; margin-bottom:1rem; color:var(--primary)'>¡Momento de Diversión! 🎉</div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🎈 Globos Mágicos", key="balloons", help="¡Haz clic para una lluvia de globos!"):
            st.balloons()
            st.success("¡Globos de felicidad para ti! 🎈✨")
    
    with col2:
        if st.button("❄️ Nieve de Amor", key="snow", help="¡Copos de nieve especiales!"):
            st.snow()
            st.success("¡Nieve mágica cayendo para ti! ❄️💕")
    
    with col3:
        if st.button("🎊 Sorpresa Total", key="surprise", help="¡La sorpresa más grande!"):
            st.balloons()
            time.sleep(0.5)
            st.snow()
            st.success("¡Doble sorpresa! Eres increíble, Isabella! 🌟")
    
    # Random compliment generator
    compliments = [
        "Tu sonrisa ilumina el mundo entero ✨",
        "Eres más hermosa que todas las flores del mundo 🌸",
        "Tu risa es la melodía más dulce que existe 🎵",
        "Eres un rayo de sol en días nublados ☀️",
        "Tu corazón es puro oro 💛",
        "Eres la definición perfecta de belleza y gracia (ademas karateca, idola) 👑"
    ]
    
    if st.button("💫 Mensaje Especial para Ti", key="compliment"):
        selected_compliment = random.choice(compliments)
        st.markdown(f"<div class='message-box' style='text-align:center; font-size:1.2rem'>{selected_compliment}</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# --- Enhanced Option 4: Personalized letter ---
elif choice == "💌 Carta del corazón":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div style='font-family:\"Dancing Script\", cursive; font-size:2rem; color:var(--primary); margin-bottom:1rem'>Carta Especial 💌</div>", unsafe_allow_html=True)
    
    enhanced_letter = """Mi querida Isabella,

Hoy quiero que sepas lo extraordinaria que eres. No solo por tu belleza exterior, 
que es innegable, sino por esa luz especial que llevas dentro y que ilumina 
todo a tu alrededor.

Eres esa persona que hace que los días grises se vuelvan coloridos, que convierte 
los momentos ordinarios en recuerdos preciosos. Tu manera de ser, tu risa, lo inquieta que eres, 
tu forma de ver el mundo... todo en ti es mágico.

Si alguna vez dudas de lo maravillosa que eres, recuerda que hay alguien que 
te ama y admira profundamente, que valora cada detalle tuyo y que se siente afortunado 
de estar contigo.

Sin lugar a duda eres especial y no porque parezcas goku super saiyan 3,
 sino por tu esencia, No permitas que nadie te haga sentir 
lo contrario, porque tu valor es infinito.

Con todo mi cariño y amor,
El ingeniero que te ama💕"""

    st.markdown(f"<div style='font-size:1.1rem; line-height:1.8; color:var(--text)'>{enhanced_letter}</div>", unsafe_allow_html=True)
    
    # Interactive message creator
    st.markdown("<div style='margin-top:2rem; padding-top:1rem; border-top:2px solid var(--primary)'>", unsafe_allow_html=True)
    st.markdown("<div style='font-size:1.1rem; color:var(--secondary); margin-bottom:1rem'>✍️ Crea tu mensaje personalizado:</div>", unsafe_allow_html=True)
    
    user_message = st.text_area("Escribe algo especial para Isabella:", placeholder="Tu mensaje aquí...")
    
    if user_message:
        st.markdown(f"<div class='message-box'><strong>Tu mensaje:</strong><br><em>{user_message}</em></div>", unsafe_allow_html=True)
        
        if st.button("🎊 Mostrar con Celebración", key="celebrate_message"):
            st.balloons()
            st.success("¡Mensaje enviado con amor! 💕")
    
    st.markdown("</div></div>", unsafe_allow_html=True)

# --- New Option 5: Interactive surprise ---
elif choice == "🌟 Sorpresa interactiva":
    st.markdown("<div class='card' style='text-align:center'>", unsafe_allow_html=True)
    st.markdown("<div style='font-family:\"Dancing Script\", cursive; font-size:2rem; color:var(--primary); margin-bottom:1.5rem'>Sorpresa Especial Interactiva 🌟</div>", unsafe_allow_html=True)
    
    # Magic 8-ball style compliment generator
    st.markdown("### 🔮 Pregúntale al Corazón")
    st.markdown("*Haz una pregunta sobre ti misma y descubre algo hermoso...*")
    
    question = st.text_input("¿Qué quieres saber sobre ti?", placeholder="Por ejemplo: ¿Soy especial?")
    
    magical_answers = [
        "Absolutamente sí, eres increíblemente especial ✨",
        "Sin duda alguna, tu luz brilla más que las estrellas 🌟",
        "Por supuesto, eres una obra maestra de la naturaleza 🎨",
        "Definitivamente, tu corazón es puro oro 💛",
        "¡Claro que sí! Eres única e irreemplazable 👑",
        "Sin lugar a dudas, eres perfecta tal como eres 💕",
        "Absolutamente, tu sonrisa puede cambiar el mundo 😊",
        "Por supuesto, eres más valiosa que todos los tesoros 💎"
    ]
    
    if question and st.button("🔮 Revelar la Respuesta Mágica"):
        answer = random.choice(magical_answers)
        st.markdown(f"<div class='message-box' style='text-align:center; font-size:1.3rem; background: linear-gradient(135deg, rgba(255, 107, 157, 0.2), rgba(196, 69, 105, 0.2))'><strong>🔮 El corazón responde:</strong><br><br><em>{answer}</em></div>", unsafe_allow_html=True)
        st.balloons()
    
    # Love percentage calculator (always high!)
    st.markdown("### 💕 Medidor de Amor Especial")
    if st.button("💖 Calcular tu Nivel de Amor Recibido"):
        # Always generate a high percentage
        love_percentage = random.randint(95, 100)
        st.markdown(f"<div class='message-box' style='text-align:center'><h2 style='color:var(--primary); font-family:\"Dancing Script\", cursive'>{love_percentage}% 💕</h2><p style='font-size:1.2rem'>¡Eres amada al {love_percentage}%! Tu corazón merece todo el amor del mundo.</p></div>", unsafe_allow_html=True)
        st.snow()
    
    st.markdown("</div>", unsafe_allow_html=True)

# --- Enhanced Footer ---
st.markdown("<div style='text-align:center; margin-top:3rem; padding:2rem; color:var(--secondary); font-style:italic'>", unsafe_allow_html=True)
st.markdown("✨ Creado con amor infinito para Isabella ✨<br>💕 Que cada día te traiga sonrisas y felicidad 💕", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
