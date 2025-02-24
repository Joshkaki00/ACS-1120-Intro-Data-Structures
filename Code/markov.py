#!python

import sys

def load_corpus(filename):
    """Load text from a file and return as a single string."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)


def preprocess_text(text):
    """Clean and tokenize text into words."""
    text = ''.join(char if char.isalpha() or char.isspace() else ' ' for char in text)  # Remove punctuation
    words = text.lower().split()
    return words
