import re
import argparse
from collections import Counter
from typing import List, Tuple
from bisect import bisect_left


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

    word = word.lower()
    words = [item[0] for item in histogram]
    idx = bisect_left(words, word)
    if idx < len(words) and words[idx] == word:
        return histogram[idx][1]
    return 0


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Generate and analyze word frequency histograms from text files.")
    parser.add_argument("file", help="Path to the input text file.")
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
    print("Generated Histogram:")
    for word, count in hist:
        print(f"{word}: {count}")

    # Check frequency of a word if provided
    if args.word:
        freq = tuple_frequency(args.word, hist)
        print(f"\nFrequency of '{args.word}': {freq}")


if __name__ == "__main__":
    main()