#!python

import random
import sys
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
    text = ''.join(char if char.isalpha() or char.isspace() else ' ' for char in text)
    words = text.lower().split()
    return words


def build_markov_chain(words):
    """Build a Markov chain using a HashTable with LinkedLists storing word frequencies."""
    if not words:
        print("Error: No words found in the text.")
        sys.exit(1)
    
    chain = HashTable()
    
    for i in range(len(words) - 1):
        word, next_word = words[i], words[i + 1]
        
        if chain.contains(word):
            linked_list = chain.get(word)
            node = linked_list.find(lambda node: node.data == next_word)  # Find node by data
            if node:
                node.count += 1  # Increment frequency count
            else:
                linked_list.append(next_word, 1)  # Store new word with count = 1
        else:
            new_list = LinkedList()
            new_list.append(next_word, 1)  # Initialize first occurrence
            chain.set(word, new_list)
    
    return chain


def weighted_random_choice(linked_list):
    """Select a word from a LinkedList using weighted probability."""
    word_counts = []
    total_count = 0
    
    current = linked_list.head
    while current:
        word_counts.append((current.data, current.count))
        total_count += current.count
        current = current.next
    
    if not word_counts:
        return None
    
    rand_val = random.uniform(0, total_count)
    cumulative = 0
    
    for word, count in word_counts:
        cumulative += count
        if rand_val <= cumulative:
            return word
    
    return word_counts[-1][0]  # Fallback (should never be hit)


def generate_sentence(chain, length=10):
    """Generate a sentence using the Markov chain with weighted random selection."""
    if not chain:
        return "Error: Markov chain is empty."
    
    keys = [key for key in chain.keys()]
    word = random.choice(keys)
    sentence = [word]
    
    for _ in range(length - 1):
        if chain.contains(word):
            linked_list = chain.get(word)
            next_word = weighted_random_choice(linked_list)
            if not next_word:
                break
            sentence.append(next_word)
            word = next_word
        else:
            break  # Stop if no next word is available
    
    return ' '.join(sentence)


def main():
    """Main function to generate a sentence from a text file using Markov chain."""
    if len(sys.argv) != 3:
        print("Usage: python markov.py <filename> <sentence_length>")
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        length = int(sys.argv[2])
        if length <= 0:
            raise ValueError
    except ValueError:
        print("Error: Sentence length must be a positive integer.")
        sys.exit(1)
    
    text = load_corpus(filename)
    words = preprocess_text(text)
    chain = build_markov_chain(words)
    sentence = generate_sentence(chain, length)
    print(sentence)


if __name__ == "__main__":
    main()

