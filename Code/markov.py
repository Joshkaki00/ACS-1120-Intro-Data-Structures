#!python

import random
import sys
import time
from linkedlist import LinkedList
from hashtable import HashTable


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
    """Build a Markov chain where each word maps to possible next words using a HashTable."""
    if not words:
        print("Error: No words found in the text.")
        sys.exit(1)
    
    chain = HashTable()
    
    for i in range(len(words) - 1):
        word, next_word = words[i], words[i + 1]
        
        if chain.contains(word):
            chain.get(word).append(next_word)  # Append to existing LinkedList
        else:
            new_list = LinkedList()
            new_list.append(next_word)
            chain.set(word, new_list)  # Store LinkedList in HashTable
    
    return chain


def generate_sentence(chain, length=10):
    """Generate a sentence using the Markov chain."""
    if not chain:
        return "Error: Markov chain is empty."
    
    keys = [key for key in chain.keys()]
    word = random.choice(keys)
    sentence = [word]

    for _ in range(length - 1):
        if chain.contains(word) and chain.get(word).head:
            next_words = []
            current = chain.get(word).head
            while current:
                next_words.append(current.data)
                current = current.next
            word = random.choice(next_words)
            sentence.append(word)
        else:
            break  # Stop if no next word available
    
    return ' '.join(sentence)


def performance_test(filename, sentence_length, iterations=1000):
    """Measure execution time of sentence generation over multiple iterations."""
    text = load_corpus(filename)
    words = preprocess_text(text)
    chain = build_markov_chain(words)
    
    start_time = time.time()
    for _ in range(iterations):
        generate_sentence(chain, sentence_length)
    end_time = time.time()
    
    print(f"Generated {iterations} sentences in {end_time - start_time:.4f} seconds.")


def main():
    """Main function to generate a sentence from a text file using Markov chain."""
    if len(sys.argv) < 3:
        print("Usage: python markov.py <filename> <sentence_length> [performance_test_iterations]")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        length = int(sys.argv[2])
        if length <= 0:
            raise ValueError
    except ValueError:
        print("Error: Sentence length must be a positive integer.")
        sys.exit(1)
    
    if len(sys.argv) == 4:
        try:
            iterations = int(sys.argv[3])
            if iterations <= 0:
                raise ValueError
            performance_test(filename, length, iterations)
            sys.exit(0)
        except ValueError:
            print("Error: Performance test iterations must be a positive integer.")
            sys.exit(1)