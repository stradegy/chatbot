import streamlit as st
import google.generativeai as genai
from openai import OpenAI


# Show title and description.
st.title("💬 ReubenGPT")
# st.write(
#     "This is a simple chatbot that uses OpenAI's GPT-3.5 model to generate responses. "
#     "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
#     "You can also learn how to build this app step by step by [following our tutorial](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)."
# )

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
# openai_api_key = st.text_input("OpenAI API Key", type="password")

if "model" not in st.session_state:
    genai.configure(api_key = st.secrets["key"])
    st.session_state.model = genai.GenerativeModel("gemini-1.5-flash")

if "chat_session" not in st.session_state:
    st.session_state.chat_session = st.session_state.model.start_chat(
  history=[])
    # st.session_state.chat_session.send_message('Do not use any advanced formatting')


# with st.chat_message("ReubenGPT"):
#     # response = st.write_stream(chat_session.history)
#     # st.session_state.messages.append({"role": "assistant", "content": response})
#     # st.write(f'{chat_session.history}')
#     # st.text(f'neneneere')
#     st.write(str(st.session_state.chat_session.history))

for message in st.session_state.chat_session.history:
    if message.role == 'model':
        with st.chat_message("ReubenGPT"):
            st.markdown(str(message.parts).split('"')[1])
    elif message.role == 'user':
        with st.chat_message("Kaypoh"):
            st.markdown(str(message.parts).split('"')[1])

prompt = st.chat_input("Simi Daiji")
if prompt:
    st.text(f"You kaypoh: {prompt}")
    st.session_state.chat_session.send_message(prompt)



# if not openai_api_key:
#     st.info("Please add your OpenAI API key to continue.", icon="🗝️")
# else:

#     # Create an OpenAI client.
#     client = OpenAI(api_key=openai_api_key)

#     # Create a session state variable to store the chat messages. This ensures that the
#     # messages persist across reruns.
#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     # Display the existing chat messages via `st.chat_message`.
#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

#     # Create a chat input field to allow the user to enter a message. This will display
#     # automatically at the bottom of the page.
#     if prompt := st.chat_input("What is up?"):

#         # Store and display the current prompt.
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         with st.chat_message("user"):
#             st.markdown(prompt)

#         # Generate a response using the OpenAI API.
#         stream = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": m["role"], "content": m["content"]}
#                 for m in st.session_state.messages
#             ],
#             stream=True,
#         )

#         # Stream the response to the chat using `st.write_stream`, then store it in 
#         # session state.
#         with st.chat_message("assistant"):
#             response = st.write_stream(stream)
#         st.session_state.messages.append({"role": "assistant", "content": response})
