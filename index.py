import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types


# Load environment variables
load_dotenv()

# Function to generate AI response
def generate_response(user_input):
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        st.error("GEMINI_API_KEY not found in environment variables.")
        return "Error: API Key not found."

    client = genai.Client(api_key=api_key)
    model = "gemini-2.0-flash"
    
    contents = [

        types.Content(
            role="user",
            parts=[types.Part.from_text(text=user_input)],
        ),
    ]
    
    generate_content_config = types.GenerateContentConfig(
        temperature=1,
        top_p=0.95,
        top_k=40,
        max_output_tokens=8192,
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(
                text="Provide responses only for unit conversion questions. If not a unit conversion question, kindly ask them to provide a valid query."
            ),
        ],
    )

    response_text = ""
    for chunk in client.models.generate_content_stream(
        model=model, contents=contents, config=generate_content_config
    ):
        response_text += chunk.text

    return response_text

# ---- STREAMLIT UI ----
st.set_page_config(page_title="AI Unit Converter", page_icon="⚡", layout="centered")

# Custom CSS for improved UI
st.markdown("""
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f8f9fa;
    }
    .chat-container {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }
    .user-message {
        text-align: right;
        background-color: #007bff;
        color: white;
        padding: 10px;
        border-radius: 10px;
        max-width: 60%;
        margin-left: auto;
        margin-top:10px;
    }
    .bot-message {
        text-align: left;
        color:black;
        margin-top:10px;
        background-color: #e9ecef;
        padding: 10px;
        border-radius: 10px;
        max-width: 60%;
    }
    </style>
""", unsafe_allow_html=True)

# Chat UI
st.title("⚡ AI Unit Converter")
st.write("Ask me any unit conversion question!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You: ", placeholder="Enter your unit conversion question...")

if st.button("Ask AI", use_container_width=True):
    if user_input.strip():
        response = generate_response(user_input)
        
        # Save chat history
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("AI", response))

# Display Chat History
st.subheader("Chat History")
chat_container = st.container()
with chat_container:
    for role, text in st.session_state.chat_history:
        if role == "You":
            st.markdown(f"<div class='user-message'>{text}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='bot-message'>{text}</div>", unsafe_allow_html=True)
