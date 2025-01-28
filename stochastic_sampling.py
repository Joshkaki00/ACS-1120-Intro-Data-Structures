import random
import sys
from collections import Counter


def parse_histogram(file_path):
    """
    Parse a text file into a histogram.
    Each word in the file contributes to the frequency count.
    """
    histogram = Counter()
    with open(file_path, 'r') as file:
        words = file.read().split()
        for word in words:
            histogram[word] += 1
    return list(histogram.items())


def random_sample(histogram):
    """
    Select a random word from the histogram ignoring frequencies.
    """
    words = [word for word, _ in histogram]
    return random.choice(words)
