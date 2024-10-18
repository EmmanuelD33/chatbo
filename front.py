import streamlit as st
from chatbot import predict_class, get_response, intents

st.title("Soporte de REDSISCOM")

#Almacena Historico del chat

if "messages" not in st.session_state:
    st.session_state.messages = []
#Para saber si se ejecuta por primera vez el chat
if "first_message" not in st.session_state:
    st.session_state.first_message = True

#Muestra el historico del chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        #Mostrar los mensajes del historico
        st.markdown(message["content"])

#Verifica si por primera vez se ejecuta el codigo
if st.session_state.first_message:
    with st.chat_message("assistant"):
        st.markdown("Hola, ¿Cómo puedo ayudarte?")

    st.session_state.messages.append({"role": "assistant", "content": "Hola, ¿Cómo puedo ayudarte?"})
    st.session_state.first_message = False

if prompt := st.chat_input("¿Como puedo ayudarte?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    #Implementacion de algoritmo de IA
    insts = predict_class(prompt)
    res = get_response(insts, intents)

    with st.chat_message("assistant"):
        st.markdown(res)
    st.session_state.messages.append({"role": "assistant", "content": res})
