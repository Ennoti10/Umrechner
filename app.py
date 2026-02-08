import streamlit as st

# Custom CSS für ansprechendes Theme (dunkles Gradient, moderne Fonts)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Poppins', sans-serif;
    }
    .stApp {
        background-color: transparent;
    }
    h1 {
        color: white !important;
        font-size: 3.5rem !important;
        font-weight: 700 !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .hero-section {
        padding: 4rem 2rem;
        text-align: center;
        color: white;
    }
    .features {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
    }
    .btn-explore {
        background: linear-gradient(45deg, #ff6b6b, #feca57);
        color: white !important;
        padding: 1rem 2rem !important;
        border-radius: 50px !important;
        font-weight: 600 !important;
        font-size: 1.2rem !important;
        box-shadow: 0 8px 32px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section">
    <h1>🚀 UFA - Umrechner Für Alles</h1>
    <p style="font-size: 1.5rem; margin-top: 1rem; opacity: 0.95;">
        Der ultimative Tool für alle Umrechnungen: Währung, Länge, Gewicht, Temperatur & mehr!
    </p>
    <br>
    <a href="#features" class="btn-explore st-button">Jetzt entdecken →</a>
</div>
""", unsafe_allow_html=True)

# Features
st.markdown("#features")
st.markdown("""
<div class="features">
    <h2 style="color: #333; text-align: center;">Warum UFA?</h2>
    <div style="display: flex; justify-content: space-around; flex-wrap: wrap;">
        <div style="flex: 1; min-width: 200px; text-align: center; padding: 1rem;">
            <h3>🌍 Multi-Währung</h3>
            <p>Live-Kurse für 150+ Währungen.</p>
        </div>
        <div style="flex: 1; min-width: 200px; text-align: center; padding: 1rem;">
            <h3>📏 Einheiten</h3>
            <p>cm ↔ m ↔ km, kg ↔ lb & mehr.</p>
        </div>
        <div style="flex: 1; min-width: 200px; text-align: center; padding: 1rem;">
            <h3>⚡ Schnell & Mobil</h3>
            <p>Responsive Design für jedes Gerät.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Call to Action
st.markdown("""
<div style="text-align: center; padding: 3rem; background: rgba(0,0,0,0.2); border-radius: 20px;">
    <h2>Bereit zum Umrechnen?</h2>
    <p>Starte jetzt deine erste Konvertierung!</p>
    <st.button>Umrechner starten</st.button>
</div>
""", unsafe_allow_html=True)

st.cap
