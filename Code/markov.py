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


def build_markov_chain(words):
    """Build a Markov chain where each word maps to possible next words."""
    chain = {}
    for i in range(len(words) - 1):
        word, next_word = words[i], words[i + 1]
        if word not in chain:
            chain[word] = []
        chain[word].append(next_word)
    return chain
