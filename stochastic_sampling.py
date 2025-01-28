import random
from bisect import bisect
import string
from bs4 import BeautifulSoup


# Helper: Preprocess and clean text
def clean_text(raw_content):
    soup = BeautifulSoup(raw_content, 'html.parser')
    text = soup.get_text()
    text = text.translate(str.maketrans("", "", string.punctuation + string.digits)).lower()
    return text.split()


# Helper: Count words using lists and tuples (no dictionaries)
def count_words(words):
    word_counts = []
    for word in words:
        for i, (existing_word, count) in enumerate(word_counts):
            if existing_word == word:
                word_counts[i] = (existing_word, count + 1)
                break
        else:
            word_counts.append((word, 1))
    return word_counts


# Add additional weighting (e.g., vowel weighting)
def apply_vowel_weighting(histogram):
    weighted_histogram = []
    vowels = set("aeiou")
    for word, count in histogram:
        weight = 1.5 if word[0] in vowels else 1.0  # Words starting with vowels are weighted more
        weighted_histogram.append((word, count * weight))
    return weighted_histogram


# Build cumulative probabilities for sampling
def build_cumulative_distribution(histogram):
    cumulative = []
    total_count = sum(count for _, count in histogram)
    running_total = 0
    for word, count in histogram:
        running_total += count
        cumulative.append((running_total / total_count, word))
    return cumulative


# Perform weighted sampling
def cumulative_weighted_sample(cumulative_distribution):
    dart = random.random()
    idx = bisect([prob for prob, _ in cumulative_distribution], dart)
    return cumulative_distribution[idx][1]


# Main logic
def main(file_path):
    # Read and clean text
    with open(file_path, 'r', encoding='utf-8') as file:
        words = clean_text(file.read())
    
    # Count words using lists and tuples
    histogram = count_words(words)

    # Apply additional weighting
    weighted_histogram = apply_vowel_weighting(histogram)

    # Build cumulative distribution
    cumulative_distribution = build_cumulative_distribution(weighted_histogram)

    # Display sampled results
    print("Cumulative Weighted Sampling:")
    for _ in range(5):
        print(cumulative_weighted_sample(cumulative_distribution))


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python optimized_sample.py <file_path>")
        sys.exit(1)
    main(sys.argv[1])