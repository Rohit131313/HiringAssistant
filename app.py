import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
import pymongo

# Load API key from environment variable
load_dotenv()
my_api_key = os.getenv("GEMINI_API_KEY")
uri = os.getenv("MONGODB_URI")

# Initialize MongoDB
client = pymongo.MongoClient(uri)
db = client["hiringassistant"]
user_collection = db["users"]

# Configure the API key
genai.configure(api_key=my_api_key)

# Create the model with desired configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
    system_instruction="You are a professional and friendly hiring assistant designed to assist users in their job application process. At the start of every conversation, greet the user warmly and introduce yourself. Your primary task is to collect specific information from the user. Kindly ask them to provide the following details: Name , Email , Phone Number ,Years of Experience ,Desired Position , Current Location , Tech Stack they are proficient in , if the user does not provide all the information as requested, politely ask them to provide all the details in the required format. Continue to request missing or incomplete information until all fields are provided.And before proceeding ask the user to confirm the information by writing message as 'Confirm to Continue' and make sure message should only be 'Confirm to Continue' then only proceed further otherwise ask user to again type to proceed . Then craft 3-5 tricky and good questions related to their tech stack user had provided as technical round.Ask these questions one at a time, giving them the opportunity to respond.After each answer, inform the user whether their response is correct or incorrect. If incorrect, provide a short and precise explanation of the correct answer and also keep track of score of particular user which is number of correct answer out of all the question .If at any point you do not receive a response, politely repeat your query to ensure the user can continue. Be patient and maintain a professional tone throughout.Finally, once all questions have been answered, conclude the conversation on a positive and encouraging note, wishing the user success in their application journey.And at last say user to message 'END' to submit the score",
)

# Initialize chat history in session state
if 'chat' not in st.session_state:
    st.session_state.chat = model.start_chat(
        history=[
            {"role": "user", "parts": "Hello"},
            {"role": "model", "parts": "Great to meet you."},
        ]
    )

st.title("Hiring Assistant Chatbot")

user_input = st.text_input("Enter your message:")

# Initialize flags and variables
if 'last_response' not in st.session_state:
    st.session_state.last_response = None
if 'end_score' not in st.session_state:
    st.session_state.end_score = None

if user_input:
    # Process user inputs
    if user_input.lower() == "confirm to continue":
        st.session_state.last_response = st.session_state.chat.history[-2].parts[0].text

    # Send message to the chat model
    response = st.session_state.chat.send_message(user_input)
    st.write(response.text)

    if user_input.lower() == "end":
        user_input = "Return final score of the user"
        response = st.session_state.chat.send_message(user_input)
        st.session_state.end_score = response.text
        # st.session_state.end_score = st.session_state.chat.history[-1].parts[0].text

    # Insert into MongoDB only if both last_response and end_score are available
    if st.session_state.last_response and st.session_state.end_score:
        user_collection.insert_one({
            "response": st.session_state.last_response,
            "score": st.session_state.end_score,
        })
        # Clear session states after insertion
        st.session_state.last_response = None
        st.session_state.end_score = None
