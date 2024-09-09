from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
import requests
from dotenv import load_dotenv
import os
import google.generativeai as genai


load_dotenv()


app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
csrf = CSRFProtect(app)

gemini_api_key = os.getenv('GEMINI_API_KEY')
model = os.getenv('MODEL')

genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel(model)

conversation_history = []

@app.route('/fetch', methods=['POST'])
def fetch():
    if request.method == 'POST':
        input_text = request.form['input']

        conversation_history.append(["You", input_text])

        try:
            prompt_message_path = "prompt/content.txt"

            with open(prompt_message_path, 'r', encoding='utf-8') as file:
                prompt = file.read()

            prompt = prompt.format(user_input = input_text)
            response = model.generate_content(prompt)
            ai_response = response.text


            output_text = ai_response
            conversation_history.append(["Bot", output_text ])

        except KeyError:
            error_message = "Unexpected response from Gemini API. Please try again later."
            return render_template('home.html', value=error_message)
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return render_template('home.html', value=error_message)

        # Pass the output to the HTML template for rendering
        return render_template('home.html', value = conversation_history)

    return render_template('home.html', value = conversation_history)


@app.route('/')
def home():
    return render_template('home.html', value=conversation_history)



if __name__ == '__main__':
    app.run(debug=True)
