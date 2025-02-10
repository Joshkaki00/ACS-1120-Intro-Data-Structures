import sys
import random


def rearrange_words():
    # Extract words from command-line arguments (excluding the script name)
    words = sys.argv[1:]
    # Check if any words are provided
    if not words:
        print("Usage: python3 rearrange.py <word1> <word2> ... <wordN>")
        return None
    # Shuffle the list of words
    random.shuffle(words)
    # Join and print the rearranged words
    print(" ".join(words))


if __name__ == "__main__":
    rearrange_words()