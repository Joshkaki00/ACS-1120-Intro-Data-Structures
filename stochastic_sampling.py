import random
import sys
import time
from collections import Counter
from bisect import bisect
from bs4 import BeautifulSoup


def parse_histogram(file_path):
    """
    Parse a text file into a histogram.
    Preprocess the text to clean non-word content.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        raw_content = file.read()
        # Clean HTML tags using BeautifulSoup
        soup = BeautifulSoup(raw_content, 'html.parser')
        cleaned_text = soup.get_text()
        words = cleaned_text.split()
        histogram = Counter(words)
    return list(histogram.items())


def build_cumulative_distribution(histogram):
    """
    Build cumulative probabilities for weighted sampling.
    """
    cumulative = []
    total_count = sum(count for _, count in histogram)
    running_total = 0
    for word, count in histogram:
        running_total += count
        cumulative.append((running_total / total_count, word))  # Probability and word
    return cumulative


def cumulative_weighted_sample(cumulative_distribution):
    """
    Select a random word using cumulative probabilities.
    """
    dart = random.random()  # Generate a number between 0 and 1
    idx = bisect([prob for prob, _ in cumulative_distribution], dart)
    return cumulative_distribution[idx][1]


def benchmark_sampling(histogram, cumulative_distribution, iterations=100000):
    """
    Benchmark the random and optimized weighted sampling functions.
    """
    print(f"\nBenchmarking for {iterations} iterations...")

    # Benchmark random sampling
    start_time = time.time()
    for _ in range(iterations):
        random_sample(histogram)
    random_time = time.time() - start_time

    # Benchmark cumulative weighted sampling
    start_time = time.time()
    for _ in range(iterations):
        cumulative_weighted_sample(cumulative_distribution)
    weighted_time = time.time() - start_time

    print(f"Random Sampling Time: {random_time:.4f} seconds")
    print(f"Weighted Sampling Time: {weighted_time:.4f} seconds")

def validate_weighted_sampling(cumulative_distribution, histogram, iterations=100000):
    """
    Validate weighted sampling by comparing observed and expected probabilities.
    """
    results = Counter()
    for _ in range(iterations):
        selected_word = cumulative_weighted_sample(cumulative_distribution)
        results[selected_word] += 1

    total = sum(results.values())
    print("\nValidation Results (Cumulative Weighted Sampling):")
    for word, count in histogram:
        expected_probability = count / sum(c for _, c in histogram)
        observed_probability = results[word] / total
        print(f"Word: {word}, Expected: {expected_probability:.2%}, Observed: {observed_probability:.2%}")


if __name__ == "__main__":
    # Check for command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python3 optimized_sample.py <file_path>")
        sys.exit(1)

    # Parse and preprocess histogram from the file
    file_path = sys.argv[1]
    histogram = parse_histogram(file_path)

    # Build cumulative probabilities
    cumulative_distribution = build_cumulative_distribution(histogram)

    # Display random and cumulative weighted sampling results
    print("Random Sampling (ignoring weights):")
    for _ in range(5):
        print(random.choice([word for word, _ in histogram]))

    print("\nCumulative Weighted Sampling:")
    for _ in range(5):
        print(cumulative_weighted_sample(cumulative_distribution))

    # Benchmark and validate sampling methods
    benchmark_sampling(histogram, cumulative_distribution)
    validate_weighted_sampling(cumulative_distribution, histogram)