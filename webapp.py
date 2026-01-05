import streamlit as st
import edge_tts
import asyncio
import os

# --- PAGE CONFIGURATION (Tab ka naam aur icon) ---
st.set_page_config(page_title="Meri AI Awaaz", page_icon="🎙️")

# --- HEADER ---
st.title("🎙️ AI Text-to-Speech Converter")
st.write("Apna text likho, awaaz select karo aur **Audio Download** karo! (Free & Unlimited)")

# --- SIDEBAR (Settings) ---
st.sidebar.header("⚙️ Settings")

# 1. Voice Selection
gender = st.sidebar.radio("Awaaz kiski chahiye?", ["Ladki (Female)", "Ladka (Male)"])
if gender == "Ladki (Female)":
    VOICE = "hi-IN-SwaraNeural"
else:
    VOICE = "en-IN-PrabhatNeural"

# 2. Speed Control
speed_val = st.sidebar.slider("Bolne ki Speed", -50, 50, 0)
rate_str = f"{speed_val:+d}%" # Format karega like +10% or -10%

# --- MAIN AREA ---
text_input = st.text_area("Yahan wo likho jo bulwana hai (Hindi/English):", height=150)

# Function to generate audio
async def text_to_speech(text, voice, rate):
    output_file = "generated_audio.mp3"
    communicate = edge_tts.Communicate(text, voice, rate=rate)
    await communicate.save(output_file)
    return output_file

# --- ACTION BUTTON ---
if st.button("🔊 Audio Banao"):
    if not text_input:
        st.warning("Arre bhai, pehle kuch likho toh sahi!")
    else:
        with st.spinner('Ruko zara, awaaz ban rahi hai... ⏳'):
            # Async function ko run karna
            output = asyncio.run(text_to_speech(text_input, VOICE, rate_str))
            
            # Success Message
            st.success("✅ Ban gayi! Niche play karo ya download karo.")
            
            # Audio Player
            audio_file = open(output, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/mp3')
            
            # Download Button
            st.download_button(
                label="📥 Download MP3",
                data=audio_bytes,
                file_name="meri_awaaz.mp3",
                mime="audio/mp3"
            )
# --- SIDEBAR ADS (Affiliate Marketing) ---
st.sidebar.markdown("---") # Separator line
st.sidebar.header("🚀 Upgrade Your Voice")

st.sidebar.info(
    "Want ultra-realistic, celebrity-like voices? "
    "Try **ElevenLabs** (The World's Best AI Voice)."
)

# Ye button hai tumhare link ke saath
st.sidebar.markdown(
    """
    <a href="https://try.elevenlabs.io/artjufeglrrl" target="_blank" style="text-decoration: none;">
        <button style="
            width: 100%;
            background-color: #FF4B4B;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            font-size: 16px;">
            👉 Try Premium Voices
        </button>
    </a>
    """,
    unsafe_allow_html=True
)

st.sidebar.caption("Support Soundip by using this link! ❤️")
