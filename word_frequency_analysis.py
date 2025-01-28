import re
from collections import Counter
from typing import Dict, List, Tuple, Union


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