# Gemini Chatbot with Flask

## Overview

This project implements a chatbot using the Gemini API and Flask.

## Key Links

1. [Gemini API Documentation](https://ai.google.dev/api?lang=python)
2. [Gemini AI Studio](https://aistudio.google.com/)

## Installation Steps

1. **Clone the Repository**
   ```bash
   `git clone https://github.com/williyam-m/Chatbot-Flask-App-Using-Gemini-API.git`
   ```
2. **Create a Virtual Environment**
    ```bash
   `python -m venv venv`
   ```
3. **Activate the Virtual Environment**

   - **On Windows:**
     ```bash
     `venv\Scripts\activate`
     ```
   - **On Linux/macOS:**
     ```bash
     `source venv/bin/activate`
     ```
4. **Install Required Packages**
    ```bash
   `pip install -r requirements.txt`
    ```
5. **Configure Environment Variables**

   Create a `.env` file in the root directory of the project with the following content:

   ```ini
   SECRET_KEY=<flask key>
   GEMINI_API_KEY=<gemini api key>
   MODEL=<model name>
   ```
6. **Run the Application**
 
   ```bash
   python app.py
   ```