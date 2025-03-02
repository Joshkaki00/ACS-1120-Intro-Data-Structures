#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility
import random


class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        super(Listogram, self).__init__()  # Initialize as a new list
        self.types = 0  # Distinct word types
        self.tokens = 0  # Total word occurrences

        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word using binary search."""
        index = self.index_of(word)
        if index is not None:
            word, old_count = self[index]
            self[index] = (word, old_count + count)  # Update tuple
        else:
            self.insert_sorted((word, count))  # Insert in sorted order
            self.types += 1
        self.tokens += count

    def frequency(self, word):
        """Return frequency count of a word, or 0 if not found."""
        for entry in self:
            if entry[0] == word:
                return entry[1]
        return 0

    def __contains__(self, word):
        """Check if word exists in histogram."""
        return any(entry[0] == word for entry in self)

    def index_of(self, target):
        """Return index of word in histogram using binary search, or None if not found."""
        left, right = 0, len(self) - 1
        while left <= right:
            mid = (left + right) // 2
            if self[mid][0] == target:
                return mid
            elif self[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        return None
    
    def insert_sorted(self, item):
        """Insert a word into the list in sorted order."""
        if not self:
            self.append(item)
            return
        for i in range(len(self)):
            if self[i][0] > item[0]:
                self.insert(i, item)
                return
        self.append(item)

    def sample(self):
        """Return a word from histogram, weighted by frequency."""
        dart = random.uniform(0, self.tokens)
        cumulative = 0
        for word, count in self:
            cumulative += count
            if dart < cumulative:
                return word


def print_histogram(word_list):
    print()
    print('Histogram:')
    print('word list: {}'.format(word_list))
    # Create a listogram and display its contents
    histogram = Listogram(word_list)
    print('listogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
    print_histogram_samples(histogram)


def print_histogram_samples(histogram):
    print('Histogram samples:')
    # Sample the histogram 10,000 times and count frequency of results
    samples_list = [histogram.sample() for _ in range(10000)]
    samples_hist = Listogram(samples_list)
    print('samples: {}'.format(samples_hist))
    print()
    print('Sampled frequency and error from observed frequency:')
    header = '| word type | observed freq | sampled freq  |  error  |'
    divider = '-' * len(header)
    print(divider)
    print(header)
    print(divider)
    # Colors for error
    green = '\033[32m'
    yellow = '\033[33m'
    red = '\033[31m'
    reset = '\033[m'
    # Check each word in original histogram
    for word, count in histogram:
        # Calculate word's observed frequency
        observed_freq = count / histogram.tokens
        # Calculate word's sampled frequency
        samples = samples_hist.frequency(word)
        sampled_freq = samples / samples_hist.tokens
        # Calculate error between word's sampled and observed frequency
        error = (sampled_freq - observed_freq) / observed_freq
        color = green if abs(error) < 0.05 else yellow if abs(error) < 0.1 else red
        print('| {!r:<9} '.format(word)
            + '| {:>4} = {:>6.2%} '.format(count, observed_freq)
            + '| {:>4} = {:>6.2%} '.format(samples, sampled_freq)
            + '| {}{:>+7.2%}{} |'.format(color, error, reset))
    print(divider)
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    main()
