import re
import time
import argparse
from collections import Counter
from typing import List, Tuple, Dict, Union


# Histogram using list of tuples
def list_based_histogram(source_text: str) -> List[Tuple[str, int]]:
    """
    Generate a histogram as a list of tuples from source text.
    :param source_text: The content of the text file.
    :return: A sorted list of tuples representing word frequencies.
    """
    # Normalize text: lowercase, remove punctuation
    words = re.findall(r'\b\w+\b', source_text.lower())

    # Count word frequencies using Counter and convert to list of tuples
    hist = Counter(words).items()

    # Return sorted list of tuples for optimized read operations
    return sorted(hist)


def tuple_frequency(word: str, histogram: List[Tuple[str, int]]) -> int:
    """
    Retrieve the frequency of a word from the tuple-based histogram.
    :param word: The word to search for.
    :param histogram: The histogram as a sorted list of tuples.
    :return: Frequency count of the word.
    """
    from bisect import bisect_left

    word = word.lower()
    words = [item[0] for item in histogram]
    idx = bisect_left(words, word)
    if idx < len(words) and words[idx] == word:
        return histogram[idx][1]
    return 0


def save_histogram_to_file(histogram: List[Tuple[str, int]], filename: str):
    """
    Save the histogram to a plain text file.
    :param histogram: The histogram as a sorted list of tuples.
    :param filename: The file to save the histogram to.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        for word, count in histogram:
            file.write(f"{word} {count}\n")


def load_histogram_from_file(filename: str) -> List[Tuple[str, int]]:
    """
    Load a histogram from a plain text file.
    :param filename: The file containing the histogram.
    :return: A list of tuples representing word frequencies.
    """
    histogram = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            word, count = line.split()
            histogram.append((word, int(count)))
    return histogram


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Generate and analyze word frequency histograms from text files.")
    parser.add_argument("file", help="Path to the input text file.")
    parser.add_argument("-s", "--save", help="Path to save the histogram file.", default="histogram.txt")
    parser.add_argument("-w", "--word", help="Word to check frequency for.")
    args = parser.parse_args()

    # Read text file
    try:
        with open(args.file, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found.")
        return

    # Generate histogram
    hist = list_based_histogram(content)
    print("Generated Histogram:", hist)

    # Save histogram if save path is provided
    if args.save:
        save_histogram_to_file(hist, args.save)
        print(f"Histogram saved to '{args.save}'.")

    # Check frequency of a word if provided
    if args.word:
        freq = tuple_frequency(args.word, hist)
        print(f"Frequency of '{args.word}': {freq}")


if __name__ == "__main__":
    main()