import streamlit as st
import edge_tts
import asyncio

# --- PAGE SETTINGS ---
st.set_page_config(page_title="Soundip Studio", page_icon="🎙️")

# --- TITLE ---
st.title("🎙️ Soundip AI Studio")
st.markdown("### Simple Free Text-to-Speech (With Emotions)")

# --- SIDEBAR: SETTINGS ---
st.sidebar.header("⚙️ Settings")

# 1. Voice Choose Karo
gender = st.sidebar.radio("Voice:", ["👩 Swara (Hindi)", "👨 Prabhat (English/Hindi)"])
if "Swara" in gender:
    VOICE = "hi-IN-SwaraNeural"
else:
    VOICE = "en-IN-PrabhatNeural"

# 2. Mood Choose Karo (Ye humne rakha hai)
st.sidebar.markdown("---")
mood = st.sidebar.selectbox(
    "Emotion/Style:",
    ["Normal", "😊 Happy", "😔 Sad", "👻 Scary", "🤖 Robot"]
)

# --- EMOTION LOGIC (Background Magic) ---
rate_str = "+0%"
pitch_str = "+0Hz"

if "Happy" in mood:
    rate_str = "+15%"
    pitch_str = "+5Hz"
elif "Sad" in mood:
    rate_str = "-15%"
    pitch_str = "-5Hz"
elif "Scary" in mood:
    rate_str = "-25%"
    pitch_str = "-15Hz"
elif "Robot" in mood:
    rate_str = "-5%"
    pitch_str = "+0Hz"

# --- SIDEBAR ADS (Paise kamane ke liye) ---
st.sidebar.markdown("---")
st.sidebar.caption("Want Pro Voices?")
st.sidebar.markdown(
    """<a href="https://try.elevenlabs.io/artjufeglrrl" target="_blank">
    <button style="width:100%; background:#ff4b4b; color:white; border:none; padding:8px; border-radius:4px;">
    ⚡ Try ElevenLabs (Premium)</button></a>""", 
    unsafe_allow_html=True
)

# --- MAIN AREA ---
text_input = st.text_area("Yahan apna text likho:", height=200, placeholder="Kuch likho... Jaise: Hello friends, welcome to my channel!")

# --- GENERATE BUTTON ---
if st.button("🔊 Generate Audio", type="primary"):
    if not text_input:
        st.warning("Are bhai, pehle kuch likho toh sahi!")
    else:
        async def generate_audio():
            communicate = edge_tts.Communicate(text_input, VOICE, rate=rate_str, pitch=pitch_str)
            await communicate.save("soundip_audio.mp3")

        with st.spinner('Awaaz ban rahi hai...'):
            try:
                asyncio.run(generate_audio())
                
                # Audio Player
                st.audio("soundip_audio.mp3", format='audio/mp3')
                
                # Download Button
                with open("soundip_audio.mp3", "rb") as file:
                    st.download_button(
                        label="📥 Download MP3",
                        data=file,import streamlit as st
import edge_tts
import asyncio

# --- PAGE SETTINGS ---
st.set_page_config(page_title="Soundip Studio", page_icon="🎙️")

# --- TITLE ---
st.title("🎙️ Soundip AI Studio")
st.markdown("### Simple Free Text-to-Speech (With Emotions)")

# --- SIDEBAR: SETTINGS ---
st.sidebar.header("⚙️ Settings")

# 1. Voice Choose Karo
gender = st.sidebar.radio("Voice:", ["👩 Swara (Hindi)", "👨 Prabhat (English/Hindi)"])
if "Swara" in gender:
    VOICE = "hi-IN-SwaraNeural"
else:
    VOICE = "en-IN-PrabhatNeural"

# 2. Mood Choose Karo (Ye humne rakha hai)
st.sidebar.markdown("---")
mood = st.sidebar.selectbox(
    "Emotion/Style:",
    ["Normal", "😊 Happy", "😔 Sad", "👻 Scary", "🤖 Robot"]
)

# --- EMOTION LOGIC (Background Magic) ---
rate_str = "+0%"
pitch_str = "+0Hz"

if "Happy" in mood:
    rate_str = "+15%"
    pitch_str = "+5Hz"
elif "Sad" in mood:
    rate_str = "-15%"
    pitch_str = "-5Hz"
elif "Scary" in mood:
    rate_str = "-25%"
    pitch_str = "-15Hz"
elif "Robot" in mood:
    rate_str = "-5%"
    pitch_str = "+0Hz"

# --- SIDEBAR ADS (Paise kamane ke liye) ---
st.sidebar.markdown("---")
st.sidebar.caption("Want Pro Voices?")
st.sidebar.markdown(
    """<a href="https://try.elevenlabs.io/artjufeglrrl" target="_blank">
    <button style="width:100%; background:#ff4b4b; color:white; border:none; padding:8px; border-radius:4px;">
    ⚡ Try ElevenLabs (Premium)</button></a>""", 
    unsafe_allow_html=True
)

# --- MAIN AREA ---
text_input = st.text_area("Yahan apna text likho:", height=200, placeholder="Kuch likho... Jaise: Hello friends, welcome to my channel!")

# --- GENERATE BUTTON ---
if st.button("🔊 Generate Audio", type="primary"):
    if not text_input:
        st.warning("Are bhai, pehle kuch likho toh sahi!")
    else:
        async def generate_audio():
            communicate = edge_tts.Communicate(text_input, VOICE, rate=rate_str, pitch=pitch_str)
            await communicate.save("soundip_audio.mp3")

        with st.spinner('Awaaz ban rahi hai...'):
            try:
                asyncio.run(generate_audio())
                
                # Audio Player
                st.audio("soundip_audio.mp3", format='audio/mp3')
                
                # Download Button
                with open("soundip_audio.mp3", "rb") as file:
                    st.download_button(
                        label="📥 Download MP3",
                        data=file,
                        file_name="soundip_audio.mp3",
                        mime="audio/mp3"
                    )
                st.success(f"✅ Audio Ready! (Mode: {mood})")
                
            except Exception as e:
                st.error(f"Error: {e}")

# --- FOOTER ---
st.markdown("---")
st.caption("Soundip AI - Simple & Free")
                        file_name="soundip_audio.mp3",
                        mime="audio/mp3"
                    )
                st.success(f"✅ Audio Ready! (Mode: {mood})")
                
            except Exception as e:
                st.error(f"Error: {e}")

# --- FOOTER ---
st.markdown("---")
st.caption("Soundip AI - Simple & Free")
