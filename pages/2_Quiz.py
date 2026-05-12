import streamlit as st
from chains.quiz_chain import create_quiz_chain

st.set_page_config(
    page_title="WWI Quiz",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 WWI Quiz")
st.subheader("Test your World War 1 knowledge")
st.markdown("---")

if "quiz_chain" not in st.session_state:
    st.session_state.quiz_chain = create_quiz_chain()

if "quiz_messages" not in st.session_state:
    st.session_state.quiz_messages = []

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

for message in st.session_state.quiz_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if not st.session_state.quiz_started:
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🎯 Start Quiz", use_container_width=True):
            st.session_state.quiz_started = True
            with st.chat_message("assistant"):
                with st.spinner("Preparing your first question..."):
                    response = st.session_state.quiz_chain.invoke({
                        "input": "Generate a WWI quiz question for me"
                    })
                st.markdown(response)
                st.session_state.quiz_messages.append({
                    "role": "assistant",
                    "content": response
                })
            st.rerun()
if st.session_state.quiz_started:
    if answer := st.chat_input("Type A, B, C, or D to answer..."):
        st.session_state.quiz_messages.append({
            "role": "human",
            "content": answer
        })
        
        with st.chat_message("human"):
            st.markdown(answer)
        
        with st.chat_message("assistant"):
            with st.spinner("Checking your answer..."):
                history = "\n".join([
                      f"{m['role'].upper()}: {m['content']}" 
                      for m in st.session_state.quiz_messages
])

                response = st.session_state.quiz_chain.invoke({
                    "input": f"Conversation so far:\n{history}\n\nThe user just answered: {answer}. Evaluate their answer based on the last question you asked, explain if correct or not, then generate a brand new WWI quiz question."
})

                
            st.markdown(response)
            st.session_state.quiz_messages.append({
                "role": "assistant",
                "content": response
            })