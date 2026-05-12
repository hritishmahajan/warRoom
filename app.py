import streamlit as st
from chains.tutor_chain import create_tutor_chain

st.set_page_config(
    page_title="The War Room",
    page_icon="🪖",
    layout="wide"
)

st.title("🪖 The War Room")
st.subheader("Your Personal WWI History Tutor - Dr. Hritish Mahajan WW1")
st.markdown("---")

if "chain" not in st.session_state:
    st.session_state.chain = create_tutor_chain()

#without this, the chain and chat history will reset every time the user submits a new question,
#which would break the conversation flow.

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# := is the walrus operator, which assigns the value AND checks it in one go.

if prompt := st.chat_input("Ask Dr. Hritish Mahajan about WWI..."):
    st.session_state.messages.append({"role": "human", "content": prompt})
    
    with st.chat_message("human"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Dr. Hritish Mahajan is thinking..."):
            response = st.session_state.chain.invoke({
                "question": prompt,
                "chat_history": st.session_state.messages
})
            answer = response
            
        st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})