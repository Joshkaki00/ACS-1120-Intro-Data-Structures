import random
from bisect import bisect
import string
from bs4 import BeautifulSoup


def clean_text(raw_content):
    """
    Preprocess raw HTML content to extract text:
    - Remove punctuation, numbers, and convert to lowercase.
    """
    soup = BeautifulSoup(raw_content, 'html.parser')
    text = soup.get_text()
    text = text.translate(str.maketrans("", "", string.punctuation + string.digits)).lower()
    return text.split()


def count_words(words):
    """
    Count word occurrences using only lists and tuples (no dictionaries).
    """
    word_counts = []
    for word in words:
        for i, (existing_word, count) in enumerate(word_counts):
            if existing_word == word:
                word_counts[i] = (existing_word, count + 1)
                break
        else:
            word_counts.append((word, 1))
    return word_counts


def apply_vowel_weighting(histogram):
    """
    Apply additional weighting to words starting with vowels.
    """
    vowels = set("aeiou")
    weighted_histogram = []
    for word, count in histogram:
        weight = 1.5 if word[0] in vowels else 1.0
        weighted_histogram.append((word, count * weight))
    return weighted_histogram


def build_cumulative_distribution(histogram):
    """
    Build a cumulative probability distribution for weighted sampling.
    """
    cumulative = []
    total_count = sum(count for _, count in histogram)
    running_total = 0
    for word, count in histogram:
        running_total += count
        cumulative.append((running_total / total_count, word))
    return cumulative


def random_sample(histogram):
    """
    Perform pure random sampling (ignores weights).
    """
    words = [word for word, _ in histogram]
    return random.choice(words)


def cumulative_weighted_sample(cumulative_distribution):
    """
    Perform weighted sampling using the cumulative distribution.
    """
    dart = random.random()
    idx = bisect([prob for prob, _ in cumulative_distribution], dart)
    return cumulative_distribution[idx][1]


def validate_weighted_sampling(histogram, cumulative_distribution, iterations=10000):
    """
    Validate weighted sampling by comparing observed frequencies with expected probabilities.
    """
    results = []
    for _ in range(iterations):
        results.append(cumulative_weighted_sample(cumulative_distribution))

    total = len(results)
    observed = [(word, results.count(word) / total) for word, _ in histogram]
    print("\nValidation Results (Weighted Sampling):")
    for word, count in histogram:
        expected = count / sum(c for _, c in histogram)
        obs = next((o[1] for o in observed if o[0] == word), 0)
        print(f"Word: {word}, Expected: {expected:.2%}, Observed: {obs:.2%}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python stochastic_sampling.py <file_path>")
        sys.exit(1)

    # Read and preprocess input text
    file_path = sys.argv[1]
    with open(file_path, 'r', encoding='utf-8') as file:
        words = clean_text(file.read())

    # Count words and build histogram
    histogram = count_words(words)

    # Apply vowel weighting
    weighted_histogram = apply_vowel_weighting(histogram)

    # Build cumulative probability distribution
    cumulative_distribution = build_cumulative_distribution(weighted_histogram)

    # Display pure random sampling results
    print("Random Sampling (ignoring weights):")
    for _ in range(5):
        print(random_sample(histogram))

    # Display cumulative weighted sampling results
    print("\nCumulative Weighted Sampling:")
    for _ in range(5):
        print(cumulative_weighted_sample(cumulative_distribution))

    # Validate weighted sampling
    validate_weighted_sampling(histogram, cumulative_distribution)