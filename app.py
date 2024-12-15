from flask import Flask, request, render_template
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load the API key from the environment (if you're using dotenv)
load_dotenv()
api_key = os.getenv('API_KEY')
genai.configure(api_key = api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

app = Flask(__name__)

# A list to track questions and answers
history = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_value = request.form['inputValue']
        # Generate AI response
        response = model.generate_content(input_value)
        result = response.text.strip()

        # Add the question and answer to the history
        history.append({'question': input_value, 'answer': result})

    return render_template('index.html', history=history)

if __name__ == '__main__':
    app.run(debug=True)
