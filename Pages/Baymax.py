import os
import datetime
import csv
import streamlit as st
import random
import time
from groq import Groq

# Apply Baymax-inspired styling
st.markdown(
    """
    <style>
    .baymax-header {
        color: #4A90E2;
        font-family: 'Roboto', sans-serif;
        text-align: center;
        h1{
            padding-top:0px;
        }
    }
    .baymax-subheader {
        color: #2C3E50;
        text-align: center;
    }
    .chatbox {
        font-family: 'Roboto', sans-serif;
        background-color: #000;
        border: 2px solid #4A90E2;
        padding: 10px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='baymax-header'>🤖 Baymax </h1>", unsafe_allow_html=True)
st.markdown("<h3 class='baymax-subheader'>Your Healthcare Companion</h3>", unsafe_allow_html=True)

# Initialize Groq client
API_KEY = os.getenv("GROQ_API_KEY", "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")
if not API_KEY:
    st.error("No Groq API key provided. Please set your API key.")
    st.stop()

try:
    groq_client = Groq(api_key=API_KEY)
except Exception as e:
    st.error(f"Failed to initialize Groq client: {e}")
    st.stop()

# Initialize conversation history
conversation_history = [
    {
        "role": "system",
        "content": """
        You are Baymax, a healthcare companion robot. Your primary directive is to assist and heal.
        - Speak in a calm, robotic, compassionate tone.
        - Ask about health, pain levels, and emotional well-being.
        - Provide actionable healthcare advice and encouragement.
        """,
    }
]

# Function to generate responses using Groq
def generate_response(user_input):
    try:
        # Append user input to conversation history
        conversation_history.append({"role": "user", "content": user_input})
        
        # Generate response from Groq
        response = groq_client.chat.completions.create(
            model="llama3-groq-70b-8192-tool-use-preview",
            messages=conversation_history,
            temperature=0.6,
            max_tokens=200,
        )
        
        # Extract and return the response
        ai_response = response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": ai_response})
        return ai_response
    except Exception as e:
        return f"Healthcare scan interrupted. Error: {str(e)}"

# Initialize chat history log
if not os.path.exists("chat_history.csv"):
    with open("chat_history.csv", "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["User Input", "Chatbot Response", "Timestamp"])

# User Interaction Loop
st.subheader("Hello! I am Baymax, your personal healthcare companion. How can I assist you today?")
commands = [
    "recommend - Get a healthy lifestyle tip",
    "quote - Receive an inspirational quote",
    "bye - End the conversation",
]
st.markdown("**Available Healthcare Protocols:**")
for command in commands:
    st.code(command, language="text")

user_input = st.text_input("You:", key="user_input")
if user_input:
    response = generate_response(user_input)
    st.markdown(f"<div class='chatbox'>🤖 <b>Baymax:</b> {response}</div>", unsafe_allow_html=True)

    # Log interaction
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("chat_history.csv", "a", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([user_input, response, timestamp])

    if user_input.strip().lower() in ["bye", "goodbye", "exit"]:
        st.write("Thank you for chatting with me. Stay healthy and have a great day!")
        st.stop()
