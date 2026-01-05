import streamlit as st
import edge_tts
import asyncio

# --- PAGE CONFIG ---
st.set_page_config(page_title="Soundip Studio", page_icon="🎙️", layout="wide")

# --- TITLE ---
st.title("🎙️ Soundip AI Studio")

# --- SIDEBAR (Sirf Ads aur Branding) ---
st.sidebar.header("🚀 Support Us")
st.sidebar.caption("Soundip - Made by Jay Kevat")
st.sidebar.markdown("---")
st.sidebar.info("Want Ultra-Realistic Voices?")
st.sidebar.markdown(
    """<https://try.elevenlabs.io/jayy" target="_blank">
    <button style="width:100%; background:#ff4b4b; color:white; border:none; padding:10px; border-radius:5px; font-weight:bold;">
    ⚡ Try ElevenLabs (Premium)</button></a>""", 
    unsafe_allow_html=True
)

# --- TABS (Alag Sections) ---
tab1, tab2 = st.tabs(["👤 Single Voice (Emotions)", "🗣️ Conversation (2 People)"])

# ==========================================
# TAB 1: SINGLE VOICE (EMOTIONS)
# ==========================================
with tab1:
    st.subheader("Single Voice Generator")
    
    # Is tab ki settings yahi rahengi (Sidebar mein nahi)
    col1, col2 = st.columns(2)
    with col1:
        voice_choice = st.radio("Awaaz Chuno:", ["👩 Swara (Hindi)", "👨 Prabhat (English/Hindi)"])
        if "Swara" in voice_choice:
            VOICE = "hi-IN-SwaraNeural"
        else:
            VOICE = "en-IN-PrabhatNeural"
            
    with col2:
        mood = st.selectbox(
            "Emotion/Style:",
            ["Normal", "😊 Happy", "😔 Sad", "👻 Scary", "🤖 Robot"]
        )

    # Emotion Logic
    rate_str = "+0%"
    pitch_str = "+0Hz"

    if "Happy" in mood:
        rate_str = "+15%"; pitch_str = "+5Hz"
    elif "Sad" in mood:
        rate_str = "-15%"; pitch_str = "-5Hz"
    elif "Scary" in mood:
        rate_str = "-25%"; pitch_str = "-15Hz"
    elif "Robot" in mood:
        rate_str = "-5%"; pitch_str = "+0Hz"

    # Input
    text_single = st.text_area("Yahan Text Likho:", height=150, key="txt_single")

    if st.button("🔊 Audio Banao (Single)", type="primary"):
        if not text_single:
            st.warning("Kuch likho toh sahi!")
        else:
            async def gen_single():
                communicate = edge_tts.Communicate(text_single, VOICE, rate=rate_str, pitch=pitch_str)
                await communicate.save("single.mp3")
            
            asyncio.run(gen_single())
            st.success(f"✅ Generated in {mood} Mode!")
            st.audio("single.mp3")
            with open("single.mp3", "rb") as f:
                st.download_button("📥 Download MP3", f, file_name="soundip_single.mp3")

# ==========================================
# TAB 2: CONVERSATION (NEW SECTION)
# ==========================================
with tab2:
    st.subheader("Multi-Speaker Conversation")
    st.info("💡 **Kaise use karein:** Likhne se pehle `[Male]:` ya `[Female]:` lagayein.")
    
    # Default Example Script
    example_script = """[Male]: Suno, tumne Soundip try kiya?
[Female]: Haan, ye toh kamaal ka tool hai!
[Male]: Sahi mein, ab video banana kitna aasaan ho gaya hai."""

    text_conv = st.text_area("Script Yahan Likho:", height=200, value=example_script, key="txt_conv")

    if st.button("🎭 Conversation Banao (Mix)", type="secondary"):
        if not text_conv:
            st.warning("Script khali hai!")
        else:
            with st.spinner('Dono ki awaaz mix ho rahi hai...'):
                async def gen_conv():
                    lines = text_conv.split('\n')
                    final_audio = b""
                    
                    for line in lines:
                        if not line.strip(): continue
                        
                        # Default Voice
                        v = "en-IN-PrabhatNeural"
                        t = line
                        
                        # Detect Tag
                        if "[Male]:" in line:
                            v = "en-IN-PrabhatNeural"
                            t = line.replace("[Male]:", "").strip()
                        elif "[Female]:" in line:
                            v = "hi-IN-SwaraNeural"
                            t = line.replace("[Female]:", "").strip()
                        
                        # Create Segment
                        communicate = edge_tts.Communicate(t, v)
                        await communicate.save("temp.mp3")
                        with open("temp.mp3", "rb") as f:
                            final_audio += f.read()
                    
                    return final_audio

                try:
                    audio_data = asyncio.run(gen_conv())
                    st.success("✅ Conversation Ready!")
                    st.audio(audio_data, format='audio/mp3')
                    st.download_button("📥 Download Chat", audio_data, file_name="soundip_chat.mp3")
                except Exception as e:
                    st.error(f"Error: {e}")
