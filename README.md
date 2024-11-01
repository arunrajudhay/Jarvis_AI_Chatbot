# Jarvis_AI_Chatbot

## Introduction
Jarvis AI is an interactive chatbot designed to assist users with a wide range of queries using advanced language processing capabilities. Built on the powerful LLaMA model, this application serves as a helpful AI assistant, providing instant responses and engaging conversations. Whether you're seeking information, exploring new ideas, or just looking to chat, Jarvis is here to help!

## Table of Contents
1. Pre-requisites
2. Features
3. Key Technologies and Skills
4. Usage
5. Approach
6. Learning Outcomes of This Project
7. Project Demo
8. Contribution
9. Contact

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



## Project Demo

![Screenshot 2024-10-28 004418](https://github.com/user-attachments/assets/590fbefe-4cc5-477e-92e1-eac1f93927b6)

For a detailed walkthrough of the project, you can watch the [Project Demo Video](https://drive.google.com/file/d/1BHVO8bOhrTDuCdL4CoLcw-ZEGUuQMJ5g/view?usp=drive_link).


## Contribution:
Contributions to this chatbot project are highly encouraged! If you find any bugs, have feature requests, or would like to suggest enhancements, please feel free to open an issue or submit a pull request. Your input will help improve the chatbot's functionality and user experience. Thank you for your interest and support!

## Contact:

Email : [ruarunraj2013@gmail.com](mailto:ruarunraj2013@gmail.com)

Linkedin : https://www.linkedin.com/in/arunraj-r-u-27722a146

Thanks for showing interest in this repository !
