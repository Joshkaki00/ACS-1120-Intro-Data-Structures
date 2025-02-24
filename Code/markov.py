#!python

import random
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


def generate_sentence(chain, length=10):
    """Generate a sentence using the Markov chain."""
    if not chain:
        return "Error: Markov chain is empty."

    # Select starting word using random index
    keys = list(chain.keys())
    word = keys[random.randint(0, len(keys) - 1)]
    sentence = [word]

    for _ in range(length - 1):
        if word in chain and chain[word]:
            next_words = chain[word]
            word = next_words[random.randint(0, len(next_words) - 1)]
            sentence.append(word)
        else:
            break  # Stop if no next word available
    return ' '.join(sentence)


def main():
    """Main function to generate a sentence from a text file using Markov chain."""
    if len(sys.argv) != 3:
        print("Usage: python markov.py <filename> <sentence_length>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        length = int(sys.argv[2])
    except ValueError:
        print("Error: Sentence length must be an integer.")
        sys.exit(1)

    text = load_corpus(filename)
    words = preprocess_text(text)
    chain = build_markov_chain(words)
    sentence = generate_sentence(chain, length)
    print(sentence)


if __name__ == "__main__":
    main()