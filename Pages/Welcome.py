import streamlit as st

st.html("""
        <style>
        .stMainBlockContainer{
                background-color:#32322F;
        }
        img{
                border-radius:19px;
        }
        </style>
        """
)
st.title("🩺 BAYMAX AI Chatbot")

# Create two columns for layout
col1, col2 = st.columns([2, 1])
    
with col1:
        st.markdown("""
        ## Welcome to Your Personal Health Companion! 
        
        _BAYMAX_ AI is here to provide:
        - Personalized health insights
        - Symptom guidance
        - Wellness recommendations
        
        ### How to Get Started
        Simply type your health-related question in the chat box 
        and press Enter.
        
        *Disclaimer: This is an AI assistant and does not replace 
        professional medical advice (maybe).*
        """)
    
with col2:
        # Optional: Add a health-related image or icon
        st.image("https://iili.io/20bN78x.jpg", width=250)
    
    # Chat input
st.link_button("Start Chatting","http://localhost:8501/baymax",icon="💬",type="primary",help="At your service")