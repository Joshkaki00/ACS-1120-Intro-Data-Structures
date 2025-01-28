import re
import time
from collections import Counter
from tkinter import Tk, filedialog
from typing import Dict, List, Union


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
        words = re.findall(r'\b\w+\b', source_text.lower())  # Tokenize words
    else:
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


def main():
    """
    Main function to interactively select a file, process it for word frequency,
    and display the analysis results.
    """
    # Use tkinter to open a file dialog
    root = Tk()
    root.withdraw()  # Hide the main Tkinter window
    file_path = filedialog.askopenfilename(
        title="Select a Text File",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not file_path:
        print("No file selected. Exiting.")
        return

    try:
        # Step 1: Read the selected file
        text = read_file(file_path)

        # Step 2: Generate histogram
        hist = histogram(text)
        print(f"Histogram for '{file_path}':\n{hist}\n")

        # Step 3: Count unique words
        unique_count = unique_words(hist)
        print(f"Unique Words: {unique_count}")

        # Step 4: Frequency of a specific word
        word = input("Enter a word to check its frequency (or press Enter to skip): ").strip()
        if word:
            word_freq = frequency(word, hist)
            print(f"Frequency of '{word}': {word_freq}")
        else:
            print("Skipped word frequency check.")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()