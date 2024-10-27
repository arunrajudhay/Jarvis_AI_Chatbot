import streamlit as st
import time
import mysql.connector
import atexit
import tempfile
from fpdf import FPDF
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

# Connect to MySQL database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Arunudhay2024",
    database="chatbot"
)
cursor = db_connection.cursor()

# Set up page configuration with custom icon
st.set_page_config(page_title="Jarvis AI", page_icon="🤖", layout="wide")

# Layout with two columns for logo and image
col1, col2 = st.columns([1, 1])
with col1:
    st.image(r"C:\Users\ruaru\Desktop\igebra.png", width=300)
with col2:
    inner_col1, inner_col2 = st.columns([1, 2])
    with inner_col2:
        st.image(r"C:\Users\ruaru\Desktop\cute.webp", width=270)

# Sidebar setup for additional images and product details
with st.sidebar:
    st.image(r"C:\Users\ruaru\Desktop\school.png", width=180)
    st.markdown("<h3 style='text-align: center; color: black; font-weight: bold;'>MAKING KIDS READY FOR THE AI WORLD</h3>", unsafe_allow_html=True)
    st.image(r"C:\Users\ruaru\Desktop\code.jpg", width=200)
    st.write("igebra.ai is an AI Research, Development and Education Company. AI Ready School is a program of igebra.ai")

    st.markdown("<h3 style='text-align: center; color: #4A90E2; text-decoration: underline;'>IGEBRA's Products</h3>", unsafe_allow_html=True)

    # Products section
    products = [
        {"image": r"C:\Users\ruaru\Desktop\kids.webp", "title": '<a href="https://www.ischoolofai.com/ai-ready-kids" target="_blank">AI READY KIDS</a>', "description": "A Power-Packed Online Course to Make Kids Learn GenAI and Showcase Their Skills."},
        {"image": r"C:\Users\ruaru\Desktop\film.webp", "title": '<a href="https://www.ischoolofai.com/ai-film-school" target="_blank">AI FILM SCHOOL</a>', "description": "Learn the Art and Science of Making Films with AI without Losing the Human Element."},
        {"image": r"C:\Users\ruaru\Desktop\tech.webp", "title": '<a href="https://www.ischoolofai.com/ai-tech-school" target="_blank">AI TECH SCHOOL</a>', "description": "A Result Oriented AI Tech School for Graduates and Professionals."},
        {"image": r"C:\Users\ruaru\Desktop\mark.webp", "title": '<a href="https://www.ischoolofai.com/ai-marketing-school" target="_blank">AI MARKETING SCHOOL</a>', "description": "A Comprehensive AI Marketing School for Young Graduates and Professionals."},
    ]

    for product in products:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(product["image"], width=80)
        with col2:
            st.markdown(f"<h5 style='text-align: center; text-decoration: underline;'>{product['title']}</h5>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align: center; font-size: 12px;'>{product['description']}</p>", unsafe_allow_html=True)

    st.write("")
    st.write("To explore more into the world of AI, kindly visit our website: [Igebra.ai](https://www.igebra.ai/)")

# Center-aligned chatbot title and welcome message
st.markdown("<h1 style='text-align: center; color: #4A90E2;'>Igebra's Interactive ChatBot</h1>", unsafe_allow_html=True)
st.markdown(
    "<h5 style='text-align: center;'>Welcome to "
    "<span style='color: skyblue;'>J</span>"
    "<span style='color: pink;'>A</span>"
    "<span style='color: yellow;'>R</span>"
    "<span style='color: red;'>V</span>"
    "<span style='color: violet;'>I</span>"
    "<span style='color: skyblue;'>S</span>, your helpful AI assistant! Ask anything below.</h5>",
    unsafe_allow_html=True
)

# Initialize session state variables
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "introduction_given" not in st.session_state:
    st.session_state.introduction_given = True
if "past_conversations" not in st.session_state:
    st.session_state.past_conversations = []
if "past_conversations_displayed" not in st.session_state:
    st.session_state.past_conversations_displayed = False

# Function to generate chat bubbles
def chat_bubble(message, user_type="You"):
    bubble_color = "#E0F7FA" if user_type == "You" else "#FFECB3"
    align = "flex-end" if user_type == "You" else "flex-start"
    return f"<div style='display: flex; justify-content: {align}; margin: 10px 0;'><div style='background-color: {bubble_color}; padding: 10px 15px; border-radius: 15px; max-width: 70%; box-shadow: 2px 2px 12px rgba(0,0,0,0.1);'><strong>{user_type}:</strong> {message}</div></div>"

# Set up language model and prompt template
prompt = ChatPromptTemplate.from_messages([("system", "You are a helpful AI assistant. Your name is Jarvis."), ("user", "User query: {query}")])
llm = Ollama(model="llama3.2")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Function to save conversation to MySQL
def save_conversation(user_message, jarvis_response):
    cursor.execute('''INSERT INTO conversations (user_message, jarvis_response) VALUES (%s, %s)''', (user_message, jarvis_response))
    db_connection.commit()

# Function to fetch conversations from MySQL
def fetch_conversations():
    cursor.execute('SELECT user_message, jarvis_response, timestamp FROM conversations ORDER BY timestamp DESC')
    return cursor.fetchall()

# Function to create PDF from chat history
def create_pdf(chat_history):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for user_msg, jarvis_resp, timestamp in chat_history:
        pdf.cell(200, 10, txt=f"{timestamp}: You: {user_msg.encode('latin-1', 'replace').decode('latin-1')}", ln=True)
        pdf.cell(200, 10, txt=f"{timestamp}: Jarvis: {jarvis_resp.encode('latin-1', 'replace').decode('latin-1')}", ln=True)
        pdf.cell(200, 10, ln=True)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        pdf.output(tmp_file.name)
        return tmp_file.name

# Sidebar buttons for chat management
with st.sidebar:
    if st.button("Clear Chat History"):
        st.session_state.chat_history.clear()
        st.session_state.past_conversations.clear()
        st.session_state.past_conversations_displayed = False

    if st.button("View Past Conversations"):
        st.session_state.past_conversations = fetch_conversations()
        st.session_state.past_conversations_displayed = True

    if st.button("Download Chat History"):
        past_conversations = fetch_conversations()
        if past_conversations:
            pdf_path = create_pdf(past_conversations)
            with open(pdf_path, "rb") as pdf_file:
                st.download_button(label="Download PDF", data=pdf_file, file_name="chat_history.pdf", mime="application/pdf")
        else:
            st.write("No chat history available to download.")

# Display chat history in bubbles
for chat in st.session_state.chat_history:
    st.markdown(chat, unsafe_allow_html=True)

# Chat input form
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Please enter your queries here 👇", placeholder="Type your question...", key="input_text")
    submit_button = st.form_submit_button(label="Send")

# Handle user input and AI response generation
if submit_button and user_input:
    user_message = chat_bubble(user_input, user_type="You")
    st.session_state.chat_history.append(user_message)
    st.markdown(user_message, unsafe_allow_html=True)

    typing_placeholder = st.empty()
    typing_placeholder.write("Jarvis is typing...")
    time.sleep(0.5)

    response = chain.invoke({"query": user_input})
    jarvis_message = chat_bubble(response, user_type="Jarvis")
    st.session_state.chat_history.append(jarvis_message)
    save_conversation(user_input, response)

    typing_placeholder.empty()
    st.markdown(jarvis_message, unsafe_allow_html=True)

# Display past conversations if requested
if 'past_conversations_displayed' in st.session_state and st.session_state.past_conversations_displayed:
    st.markdown("<h3 style='text-align: center; color: #4A90E2;'>Past Conversations</h3>", unsafe_allow_html=True)
    for user_msg, jarvis_resp, timestamp in st.session_state.past_conversations:
        st.markdown(f"<strong>You:</strong> {user_msg}<br><strong>Jarvis:</strong> {jarvis_resp}<hr>", unsafe_allow_html=True)

# Close the database connection on app exit
atexit.register(db_connection.close)
