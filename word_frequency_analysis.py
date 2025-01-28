import re
from collections import Counter
from typing import Dict, List, Union


def read_file(file_path: str) -> str:
    """
    Reads the content of a text file and returns it as a string.
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
    """
    if isinstance(source_text, str):
        words = re.findall(r'\b\w+\b', source_text.lower())
    else:
        words = source_text

    return Counter(words)


def unique_words(histogram: Dict[str, int]) -> int:
    """
    Count the number of unique words in a histogram.
    """
    return len(histogram)


def frequency(word: str, histogram: Dict[str, int]) -> int:
    """
    Get the frequency of a specific word in the histogram.
    """
    return histogram.get(word.lower(), 0)


def most_frequent_words(histogram: Dict[str, int], n: int = 10) -> List[Tuple[str, int]]:
    """
    Get the top 'n' most frequent words from the histogram.
    """
    return Counter(histogram).most_common(n)


def least_frequent_words(histogram: Dict[str, int], n: int = 10) -> List[Tuple[str, int]]:
    """
    Get the 'n' least frequent words from the histogram.
    """
    return sorted(histogram.items(), key=lambda item: item[1])[:n]


# Example usage
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Analyze word frequencies in a text.")
    parser.add_argument("file_path", type=str, help="Path to the text file.")
    args = parser.parse_args()

    try:
        # Read text from file
        text = read_file(args.file_path)

        # Generate histogram
        hist = histogram(text)
        print("Histogram:", hist)

        # Count unique words
        unique_count = unique_words(hist)
        print("Unique Words:", unique_count)

        # Frequency of a specific word
        word = "les"  # Replace with desired word
        word_freq = frequency(word, hist)
        print(f"Frequency of '{word}':", word_freq)

        # Most frequent words
        print("Most Frequent Words:", most_frequent_words(hist, 10))

        # Least frequent words
        print("Least Frequent Words:", least_frequent_words(hist, 10))

    except Exception as e:
        print(f"Error: {e}")