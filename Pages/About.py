import streamlit as st
st.title("About.")
st.divider()
st.write("This project aims to create an AI-powered mental health assistant that can understand and respond to user queries about mental health symptoms. Using NLP techniques, the system will extract key information from user input and employ Logistic Regression to provide informed responses. The web interface, built with Streamlit, allows users to easily interact with the bot and receive tailored guidance.")

st.subheader("Project Breakdown:")

st.subheader("Dataset:")
st.markdown("""
The dataset for this project consists of labeled intents and symptoms:
- **Intents**: The user’s purpose behind the input, such as “mental health query,” “symptom checker,” or “greeting.”
- **Entities**: Specific details extracted from user input like symptoms, mood, stress level, or medical conditions.
- **Text**: User input text, such as "I feel anxious" or "I have a headache."
""")
st.subheader("Streamlit Interface:")
st.markdown("""
The chatbot interface is built using **Streamlit**. It includes:
- A text input box for users to describe their symptoms or mental health-related concerns.
- A response window where the bot displays potential diagnoses (in the case of the symptom checker) or mental health advice (for the mental health assistant).
- The interface uses the trained models to generate responses based on the user’s input.
""")

st.subheader("Conclusion:")
st.markdown("""
In this project, we developed an AI-based **Mental Health Assistant** and **Symptom Checker Bot** that can understand and respond to user input based on intents and extracted symptoms. The system was trained using NLP techniques and Logistic Regression, and its interface was built using Streamlit for an interactive and user-friendly experience.

This project can be expanded by adding more data, using advanced NLP techniques, and incorporating deep learning algorithms to enhance the accuracy and depth of the responses.
""")