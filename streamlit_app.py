import streamlit as st
import google.generativeai as genai

# Show title and description.
st.title("ReubenGPT 🤖💬 ")

with st.chat_message('ReubenGPT', avatar = '🤖'):
    st.markdown("Hi, I am ReubenGPT, Reuben's slave. This is not an actual bot. We are a team of 3 actual people working in 8-hour shifts hoping that Reuben will notice us and make us his girlfriends. What do you want to kaypoh about.")

if "model" not in st.session_state:
    try: 
        genai.configure(api_key = st.secrets["key"])
    except:
        genai.configure(api_key = 'AIzaSyDjWpmStS_C3aNUAG9FcZLooJx9_0vbRic') #to change after commit.here forr easyt tests
    st.session_state.model = genai.GenerativeModel("gemini-1.5-flash")

if "chat_session" not in st.session_state:
    st.session_state.chat_session = st.session_state.model.start_chat(
  history=[])
    try:
        st.session_state.response = st.session_state.chat_session.send_message(st.secrets['initial'])
    except:
        st.session_state.response = st.session_state.chat_session.send_message('Hi')

if "convo" not in st.session_state:
    st.session_state.convo = []

prompt = st.chat_input("What do you want to kaypoh?")
if prompt:
    st.session_state.convo.append(prompt)
    # st.text(f"You kaypoh: {prompt}")
    response = st.session_state.chat_session.send_message(prompt)
    st.session_state.convo.append(response.text)
    speaker = 'Kaypoh'
    avatar="🤓" 
    for text in st.session_state.convo:
        with st.chat_message(speaker, avatar = avatar):
            st.markdown(text)
        if speaker == 'ReubenGPT' : 
            speaker = 'Kaypoh'
            avatar="🤓" 
            continue
        if speaker == 'Kaypoh' : 
            speaker = 'ReubenGPT'
            avatar="🤖" 
            continue

