"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template
import random
from markov import load_corpus, preprocess_text, build_markov_chain, generate_sentence

app = Flask(__name__)

# Initialize the Markov chain using a sample text file
FILENAME = "pg84-images.txt"  # Change this to your corpus file
SENTENCE_LENGTH = 20  # Default sentence length

try:
    text = load_corpus(FILENAME)
    words = preprocess_text(text)
    markov_chain = build_markov_chain(words)
except Exception as e:
    markov_chain = None
    print(f"Error initializing Markov chain: {e}")

@app.route("/")
def home():
    """Serve the main HTML page."""
    sentence = generate_sentence(markov_chain, SENTENCE_LENGTH) if markov_chain else "Error: Markov chain could not be initialized."
    return render_template('index.html', sentence=sentence)

@app.route("/generate")
def generate():
    """API endpoint to return a new generated sentence."""
    return generate_sentence(markov_chain, SENTENCE_LENGTH) if markov_chain else "Error: No Markov chain available."

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
