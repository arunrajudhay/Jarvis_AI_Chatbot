# Jarvis_AI_Chatbot

## Introduction
Jarvis AI is an interactive chatbot designed to assist users with a wide range of queries using advanced language processing capabilities. Built on the powerful LLaMA model, this application serves as a helpful AI assistant, providing instant responses and engaging conversations. Whether you're seeking information, exploring new ideas, or just looking to chat, Jarvis is here to help!

## Table of Contents
1. Pre-requisites
2. Key Technologies and Skills
3. Usage
4. Data Scrapping
5. Storing in MySQL
6. Querying
7. Further Improvements

## Pre-requisites :
1. pip install streamlit
2. pip install mysql-connector-python
3. pip install langchain
4. pip install langchain-community
5. pip install fpdf

## Features:
1. User-friendly interface for seamless interaction.
2. Stores conversation history for future reference.
3. Allows downloading of chat transcripts as PDFs.
4. Integrates with a MySQL database to manage user interactions and store past conversations.

## Key Technologies and Skills
1. Python Programming
2. Streamlit
3. MySQL Database Management
4. LangChain
5. FPDF
6. Frontend Development

## Usage
To use this project, follow these steps:
1. Clone the repository
2. Install the required packages
3. Run the Streamlit app
4. Access the app in your browser

## Approach:
1. User Interaction: The chatbot receives input from users through a web interface built with Streamlit. Users can type their queries or messages, initiating interaction.
2. Input Processing: The bot processes the incoming user input to understand intent and context. This involves tokenization and normalization of the text for accurate interpretation.
3. Database Querying: If the user query requires fetching specific information, the bot connects to the MySQL database using mysql.connector. It retrieves relevant data based on the user's request, such as user history or predefined responses.
4. Response Generation: Utilizing the LangChain library, the bot generates contextual responses. It employs pre-trained language models (like those from the Ollama library) to formulate replies based on the input and retrieved data.
5. Output Delivery: The bot presents the generated response back to the user through the Streamlit interface, ensuring the conversation flows naturally.
6. Logging and Feedback: Each interaction is logged for analysis and improvement. The bot collects feedback on responses to enhance future interactions and training of the language model.
7. Session Management: The bot maintains user sessions to provide personalized interactions, allowing users to have continuous conversations without losing context.
8. Performance Monitoring: Implement monitoring to track bot performance, response times, and user satisfaction. This data is used to optimize the chatbot’s effectiveness over time.

## Learning Outcomes of This Project:
1. User Interaction Design - Understanding user needs, designing intuitive interfaces using Streamlit, and enhancing user experience through effective communication.
2. Database Management - Learning to interact with MySQL databases, including data retrieval and manipulation, as well as implementing efficient querying techniques.
3. Response Generation Techniques - Exploring the use of language models for generating contextually relevant responses, including the implementation of the LangChain framework.
4. Session Management - Understanding how to maintain user sessions for personalized interactions and context retention throughout conversations.
5. Performance Evaluation - Assessing chatbot performance through metrics like response time, user satisfaction, and interaction logging for continuous improvement.
6. Feedback Mechanism - Implementing feedback loops to gather user input on chatbot responses, facilitating iterative enhancements and model training.
7.Deployment and Scalability - Learning about deploying web applications and ensuring scalability for handling multiple user interactions concurrently.
