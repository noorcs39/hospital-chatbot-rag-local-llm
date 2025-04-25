import streamlit as st
from rag_pipeline import ask_question

st.title("🏥 Hospital System Chatbot Designed by Noor Uddin")
query = st.text_input("Ask something:")

if query:
    response = ask_question(query)
    st.write(response)
