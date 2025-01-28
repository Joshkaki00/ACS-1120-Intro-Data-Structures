import sys
import random

# Path to the Unix dictionary file
WORDS_FILE_PATH = "/usr/share/dict/words"


def sample_words(file_path, num_words):
    """
    Efficiently selects a sample of random words from the file without loading all words into memory.
    """
    sample = []
    with open(file_path, "r", encoding="utf-8") as file:
        for i, line in enumerate(file, start=1):
            word = line.strip()
            if len(sample) < num_words:
                sample.append(word)
            else:
                # Reservoir sampling: replace with decreasing probability
                j = random.randint(0, i - 1)
                if j < num_words:
                    sample[j] = word
    return sample


def main():
    # Verify correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python3 dictionary_words.py <number_of_words>")
        sys.exit(1)

    # Parse the number of words
    try:
        num_words = int(sys.argv[1])
        if num_words <= 0:
            raise ValueError
    except ValueError:
        print("Error: Please provide a positive integer for the number of words.")
        sys.exit(1)

    # Select words
    sentence = sample_words(WORDS_FILE_PATH, num_words)

    # Print the generated sentence
    print(" ".join(sentence))


if __name__ == "__main__":
    main()