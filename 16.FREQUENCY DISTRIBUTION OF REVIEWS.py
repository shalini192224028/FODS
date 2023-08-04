import string
from collections import Counter
import matplotlib.pyplot as plt

def calculate_word_frequency(reviews):
    word_freq = Counter()
    
    for review in reviews:
        # Remove punctuation and convert to lowercase
        clean_review = review.translate(str.maketrans("", "", string.punctuation)).lower()
        words = clean_review.split()
        word_freq.update(words)
    
    return word_freq

# Example customer reviews data (replace this with your actual data)
customer_reviews = [
    "This product is great! I love it.",
    "The quality of the product is poor.",
    "I highly recommend this product to others.",
    "Not satisfied with the purchase.",
    "Amazing product! Will buy again."
]

word_frequency = calculate_word_frequency(customer_reviews)

# Print the word frequency distribution
print("Word Frequency Distribution:")
for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")

# Plot the top N words by frequency
top_words = word_frequency.most_common(10)
words, frequencies = zip(*top_words)

plt.bar(words, frequencies)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top Words Frequency")
plt.xticks(rotation=45)
plt.show()
