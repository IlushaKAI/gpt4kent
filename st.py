import g4f
import streamlit as st


st.title("ChatGPT-like clone")
    


messages = []
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if question := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        stream = g4f.ChatCompletion.create(
            model = g4f.models.gpt_4o,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        answer = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": answer})









