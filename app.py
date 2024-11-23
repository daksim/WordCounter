from flask import Flask, request, jsonify, render_template
import re

app = Flask(__name__)

# Function to count words in a given text
def count_words(text):
    # Updated regex to match words, including those with apostrophes
    words = re.findall(r'\b\w+(?:[-\']\w+)*\b', text)
    return len(words)

@app.route('/')
def home():
    # Render the frontend page
    return render_template('index.html')

@app.route('/count', methods=['POST'])
def count():
    # Get the text from the JSON payload
    data = request.get_json()
    text = data.get('text', '')
    # Count the number of words in the text
    word_count = count_words(text)
    # Return the count as a JSON response
    return jsonify({"count": word_count})

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
