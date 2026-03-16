# ChatBot Agno

## 📋 Description

## Description

A project that uses Python, Agno, and Llama 3.3 (or another model of your choice) with a graphical interface where you can write a prompt and receive a response from the model.

## ✨ Features

- 🤖 AI-powered conversation chatbot
- 🖥️ User-friendly graphical interface
- 🔧 Support for multiple AI models (Llama 3.3 or your choice)

## 🛠️ Technologies Used

- Python 3.9+
- Agno
- Llama 3.3 (configurable)
- Tkinter (GUI)
- Python Virtual Environment

## Project Structure

input text -> Agno + AI -> output text

.env : Put your API key here (Instructions above!).

main.py : File to run.

requirements.txt : File with all libraries to run the file.

## Instructions to use

1. **Make sure you have python 3.9 or newer, and both tkinter and venv modules installed.**

2. **Clone the repository:**
   ```bash
   git init
   git clone 'https://github.com/HenriqueSM0/chatbot_llama'
   ```

3. **Create a virtual environment:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```

5. **Create an API key in GROQ:**
   
   Put it on .env :

   GROQ_KEY_API = 'your_api_key_here'
   
7. **Add PDF files:**

   Place the PDFs you want to process in the pdfs/ folder

8. **Run the application:**
   ```bash
   python main.py
   ```
