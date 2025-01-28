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


def weighted_sample(histogram):
    """
    Select a random word based on the weights from the histogram.
    """
    total_count = sum(count for _, count in histogram)  # Total frequency
    dart = random.randint(1, total_count)  # Random point on the number line
    fence = 0

    for word, count in histogram:
        fence += count
        if fence >= dart:
            return word


def validate_weighted_sampling(histogram, iterations=10000):
    """
    Validate the weighted sampling function by running it multiple times
    and analyzing the frequency of each word.
    """
    results = Counter()
    for _ in range(iterations):
        selected_word = weighted_sample(histogram)
        results[selected_word] += 1

    total = sum(results.values())
    print("\nValidation Results:")
    for word, count in histogram:
        expected_probability = count / sum(c for _, c in histogram)
        observed_probability = results[word] / total
        print(f"Word: {word}, Expected: {expected_probability:.2%}, Observed: {observed_probability:.2%}")


if __name__ == "__main__":
    # Check for command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python3 sample.py <file_path> or <word_list>")
        sys.exit(1)

    # Parse input (file or inline word list)
    if len(sys.argv) == 2:  # File input
        file_path = sys.argv[1]
        histogram = parse_histogram(file_path)
    else:  # Inline word list
        words = sys.argv[1:]
        histogram = Counter(words).items()

    # Display random and weighted sampling results
    print("Random Sampling (ignoring weights):")
    for _ in range(5):
        print(random_sample(histogram))

    print("\nFrequency-Weighted Sampling:")
    for _ in range(5):
        print(weighted_sample(histogram))

    # Validate weighted sampling probabilities
    validate_weighted_sampling(histogram)