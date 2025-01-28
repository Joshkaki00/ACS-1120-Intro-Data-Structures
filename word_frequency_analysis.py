# File: word_frequency_analysis.py

import re
from collections import Counter
from typing import Dict, List, Tuple, Union


def read_file(file_path: str) -> str:
    """
    Reads the content of a text file and returns it as a string.

    :param file_path: Path to the text file.
    :return: The content of the file as a string.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} was not found.")
    except IOError as e:
        raise IOError(f"An error occurred while reading the file: {e}")


def histogram(source_text: Union[str, List[str]]) -> Dict[str, int]:
    """
    Generate a histogram (word frequency count) from the given text or list of words.

    :param source_text: A string of text or a list of words.
    :return: A dictionary where keys are words and values are their frequencies.
    """
    if isinstance(source_text, str):
        # Normalize and split text into words
        words = re.findall(r'\b\w+\b', source_text.lower())
    else:
        # Assume source_text is already a list of words
        words = source_text

    return Counter(words)


def unique_words(histogram: Dict[str, int]) -> int:
    """
    Count the number of unique words in a histogram.

    :param histogram: A dictionary where keys are words and values are their frequencies.
    :return: Total number of unique words.
    """
    return len(histogram)


def frequency(word: str, histogram: Dict[str, int]) -> int:
    """
    Get the frequency of a specific word in the histogram.

    :param word: The word to search for.
    :param histogram: A dictionary where keys are words and values are their frequencies.
    :return: The frequency of the word, or 0 if the word is not found.
    """
    return histogram.get(word.lower(), 0)


# Example usage
if __name__ == "__main__":
    # Example with a file
    file_path = "~/Downloads/Le roman de Joël _ Project Gutenberg.html"  # Replace with your file path

    try:
        # Read text from file
        text = read_file(file_path)

        # Generate histogram
        hist = histogram(text)
        print("Histogram:", hist)

        # Count unique words
        unique_count = unique_words(hist)
        print("Unique Words:", unique_count)

        # Frequency of a specific word
        word_freq = frequency("les", hist)
        print("Frequency of 'les':", word_freq)
    except Exception as e:
        print(f"Error: {e}")