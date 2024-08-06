import streamlit as st
from openaimodels import display_openai_models
from huggingmodels import display_huggingface_models
from gemenimodels import display_gemini_models

# Set page configuration (ensure this is the first Streamlit command)
# st.set_page_config(page_title="Generative AI Project", page_icon=":robot_face:", layout="wide")

# Custom CSS for button styling
st.markdown("""
    <style>
    .stButton button {
        background-color: #4CAF50; /* Green */
        border: none;
        color: white;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
        width: 100%;
        height: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# Create a container for the heading
st.markdown("<h1 style='text-align: center; color: #FFA500;'>✨ Welcome to the World of Generative AI ✨</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #00BFFF;'>🌟 Select any button and Explore Generative AI 🌟</h2>", unsafe_allow_html=True)

# Create a container for the buttons
with st.container():
    col1, col2, col3,   = st.columns(3)

    with col1:
        if st.button('Gemini'):
             st.session_state.selected = 'Gemini'
       

    with col2:
        if st.button('OpenAI'):
            st.session_state.selected = 'OpenAI'
    
    with col3:
        if st.button('HuggingFace'):
            st.session_state.selected = 'HuggingFace'

 
  

# Create a container for the content
content_placeholder = st.container()

# Display content based on button click
with content_placeholder:
    if 'selected' in st.session_state:
        if st.session_state.selected == 'OpenAI':
            display_openai_models()
        elif st.session_state.selected == 'HuggingFace':
            display_huggingface_models()
        elif st.session_state.selected == 'Gemini':
            display_gemini_models()
  