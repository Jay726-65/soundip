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
import streamlit as st
import edge_tts
import asyncio

# --- PAGE SETTINGS ---
st.set_page_config(page_title="Soundip AI Studio", page_icon="🎙️")

# --- HEADER & STYLE ---
st.title("🎙️ Soundip AI Studio")
st.markdown("### Unlimited Free AI Text-to-Speech with Emotions")
st.markdown("---")

# --- SIDEBAR: SETTINGS ---
st.sidebar.header("🎛️ Voice Settings")

# 1. Voice Selection
gender = st.sidebar.radio("Step 1: Choose Voice", ["👩 Swara (Hindi Female)", "👨 Prabhat (English/Hindi Male)"])
if "Swara" in gender:
    VOICE = "hi-IN-SwaraNeural"
else:
    VOICE = "en-IN-PrabhatNeural"

# 2. Emotion Selection (The Magic 🪄)
st.sidebar.markdown("---")
mood = st.sidebar.selectbox(
    "Step 2: Choose Emotion/Style",
    ["Normal (Seedha)", "😊 Happy (Khush)", "😔 Sad (Dukhi)", "😠 Angry (Gussa)", "👻 Scary (Daraawana)", "🤖 Robot"]
)

# --- LOGIC: APPLYING EMOTIONS ---
# Hum pitch aur rate ko hack karke emotions banayenge
rate_str = "+0%"
pitch_str = "+0Hz"

if "Happy" in mood:
    rate_str = "+15%"   # Thoda tez (Excited)
    pitch_str = "+5Hz"  # Thoda upar (Cheer)
elif "Sad" in mood:
    rate_str = "-15%"   # Dheere (Low energy)
    pitch_str = "-5Hz"  # Bhari awaaz
elif "Angry" in mood:
    rate_str = "+20%"   # Bohot tez (Aggressive)
    pitch_str = "+2Hz"  # Thoda sharp
elif "Scary" in mood:
    rate_str = "-25%"   # Bohot slow
    pitch_str = "-15Hz" # Bohot bhari (Monster)
elif "Robot" in mood:
    rate_str = "-5%"
    pitch_str = "+0Hz"
else:
    # Normal
    rate_str = "+0%"
    pitch_str = "+0Hz"

# Display Settings for Nerd Users
st.sidebar.caption(f"🔧 Technical: Rate {rate_str} | Pitch {pitch_str}")

# --- AFFILIATE / SUPPORT ---
st.sidebar.markdown("---")
st.sidebar.info("Want human-like breathing & laughing voices?")
st.sidebar.markdown(
    """<a href="https://try.elevenlabs.io/artjufeglrrl" target="_blank"><button style="width:100%; background:#ff4b4b; color:white; border:none; padding:8px; border-radius:4px;">⚡ Try ElevenLabs (Premium)</button></a>""", 
    unsafe_allow_html=True
)

# --- MAIN AREA ---
text_input = st.text_area("✍️ Type your text here (Hindi/English):", height=150, placeholder="Kuch likho... Jaise: Aaj main bohot khush hoon!")

async def text_to_speech(text, voice, rate, pitch):
    output_file = "generated_audio.mp3"
    communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
    await communicate.save(output_file)
    return output_file

# --- GENERATE BUTTON ---
if st.button("🔊 Generate Audio", type="primary"):
    if not text_input:
        st.warning("Pehle kuch likho toh sahi! 😅")
    else:
        with st.spinner('Generating Audio... (Soundip AI)'):
            try:
                # Async function call
                output = asyncio.run(text_to_speech(text_input, VOICE, rate_str, pitch_str))
                
                # Success
                st.success(f"✅ Generated in '{mood}' Mode!")
                
                # Player
                audio_file = open(output, 'rb')
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format='audio/mp3')
                
                # Download
                st.download_button(
                    label="📥 Download MP3",
                    data=audio_bytes,
                    file_name="soundip_audio.mp3",
                    mime="audio/mp3"
                )
            except Exception as e:
                st.error(f"Error aa gaya: {e}")

# Footer
st.markdown("---")
st.markdown("<center>Made with ❤️ by <b>Jay Kevat (Soundip)</b></center>", unsafe_allow_html=True)
