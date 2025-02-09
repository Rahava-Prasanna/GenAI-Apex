import streamlit as st
import requests
import google.generativeai as genai
import os

# Set API Keys
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")  

# Configure Google Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# Hugging Face API URL for Stable Diffusion
HF_API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"

# Function to Generate Images with Hugging Face
def generate_huggingface_image(prompt):
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    payload = {"inputs": prompt}
    
    response = requests.post(HF_API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.content  # Returns raw image data
    else:
        return None  # If failed, return None

# Streamlit UI
st.title("AI Interior Designer (Gemini + Hugging Face)")

st.sidebar.header("Room Customization")
room_type = st.sidebar.selectbox("Select Room Type:", ["Living Room", "Bedroom", "Kitchen", "Office"])
style = st.sidebar.selectbox("Choose Design Style:", ["Modern", "Minimalist", "Bohemian", "Classic", "Industrial"])
color_scheme = st.sidebar.color_picker("Pick a Primary Color", "#ffffff")

# AI Design Plan (Google Gemini)
if st.sidebar.button("Generate Design Plan"):
    prompt = f"Suggest an interior design for a {room_type} in {style} style with a {color_scheme} color scheme."
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    st.subheader("AI Design Recommendation")
    st.write(response.text)

# AI Image Generation (Hugging Face)
if st.sidebar.button("Generate AI Room Image"):
    image_prompt = f"A {style} {room_type} with {color_scheme} walls, stylish furniture, and elegant lighting."
    
    image_data = generate_huggingface_image(image_prompt)
    
    if image_data:
        st.image(image_data, caption="AI-Generated Interior Design (Hugging Face)")
    else:
        st.error("Error generating image with Hugging Face API.")

# AI Chatbot (Google Gemini)
st.subheader("Chat with AI Designer")
user_query = st.text_input("Ask me anything about interior design:")
if user_query:
    model = genai.GenerativeModel("gemini-1.5-flash")
    chat_response = model.generate_content(user_query)
    st.write(chat_response.text)