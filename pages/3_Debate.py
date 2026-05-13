import streamlit as st
import whisper
import tempfile #creates temp files for saving audio recordings
import os #We'll use it to delete temp files after Whisper is done with them.
from gtts import gTTS
from chains.debate_chain import create_debate_chain

st.set_page_config(
    page_title="Debate Mode",
    page_icon="⚔️",
    layout="wide"
)

st.title("⚔️ Debate Mode")
st.subheader("Argue a WWI position — Dr. Hritish Mahajan will challenge you")
st.markdown("---")

if "debate_chain" not in st.session_state:
    st.session_state.debate_chain = create_debate_chain()

if "debate_history" not in st.session_state:
    st.session_state.debate_history = []

if "debate_started" not in st.session_state:
    st.session_state.debate_started = False

if "last_audio_id" not in st.session_state:
    st.session_state.last_audio_id = None

if "recording_key" not in st.session_state:
    st.session_state.recording_key = 0

if "debate_judged" not in st.session_state:
    st.session_state.debate_judged = False

if "whisper_model" not in st.session_state:
    with st.spinner("Loading Whisper speech recognition..."):
        st.session_state.whisper_model = whisper.load_model("base")

if not st.session_state.debate_started:
    st.markdown("### Choose your position")

    positions = [
        "Germany was solely responsible for WWI",
        "The Treaty of Versailles was fair and justified",
        "Britain should have stayed out of WWI",
        "The assassination of Franz Ferdinand was inevitable",
        "WWI could have been prevented"
    ]

    selected = st.selectbox("Pick a position to defend:", positions)

    if st.button("⚔️ Start Debate", use_container_width=True):
        st.session_state.debate_started = True
        st.session_state.debate_topic = selected
        st.session_state.debate_judged = False

        with st.spinner("Dr. Hritish Mahajan is preparing his opening challenge..."):
            response = st.session_state.debate_chain.invoke({
                "input": f"The user will argue this position: '{selected}'. Open the debate with a sharp challenging question."
            })
            st.session_state.debate_history.append({
                "role": "assistant",
                "content": response
            })
        st.rerun()

if st.session_state.debate_started:
    st.markdown(f"### ⚔️ Position: *{st.session_state.debate_topic}*")
    st.markdown("---")

    for message in st.session_state.debate_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if st.session_state.debate_judged:
        st.markdown("---")
        st.markdown("### 🏛️ Debate Complete")
        if st.button("⚔️ Start a New Debate", use_container_width=True):
            st.session_state.debate_started = False
            st.session_state.debate_history = []
            st.session_state.last_audio_id = None
            st.session_state.recording_key = 0
            st.session_state.debate_judged = False
            st.rerun()
    else:
        st.markdown("### 🎤 Your argument")
        audio_data = st.audio_input(
            "Hold to record your argument...",
            key=f"audio_{st.session_state.recording_key}"
        )

        if audio_data:
            audio_hash = hash(audio_data.getvalue())
            if audio_hash != st.session_state.last_audio_id:
                st.session_state.last_audio_id = audio_hash

                with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                    tmp.write(audio_data.getvalue())
                    tmp_path = tmp.name

                with st.spinner("Transcribing your argument..."):
                    result = st.session_state.whisper_model.transcribe(tmp_path)
                    user_text = result["text"]

                os.unlink(tmp_path)

                st.markdown(f"**You said:** {user_text}")

                st.session_state.debate_history.append({
                    "role": "human",
                    "content": user_text
                })

                history = "\n".join([
                    f"{m['role'].upper()}: {m['content']}"
                    for m in st.session_state.debate_history
                ])

                with st.spinner("Dr. Hritish Mahajan is responding..."):
                    response = st.session_state.debate_chain.invoke({
                        "input": f"Debate topic: {st.session_state.debate_topic}\n\nConversation so far:\n{history}\n\nRespond to the user's argument."
                    })

                st.session_state.debate_history.append({
                    "role": "assistant",
                    "content": response
                })

                with st.spinner("Generating audio response..."):
                    tts = gTTS(text=response, lang='en', tld='co.uk')
                    tts_path = tempfile.mktemp(suffix=".mp3")
                    tts.save(tts_path)

                st.audio(tts_path, autoplay=True)

                if "JUDGE" in user_text.upper():
                    st.session_state.debate_judged = True

                st.session_state.recording_key += 1
                st.rerun()