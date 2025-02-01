from collections import Counter;
from nltk import bigrams, word_tokenize;

# Tokenize by word
def tokenize_words(text):
    return word_tokenize(text)

def find_bigrams(text):
    words = tokenize_words(text)
    bigram_list = list(bigrams(words))
    return bigram_list

def count_bigrams(bigram_list):
    return Counter(bigram_list)

# Read the file
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    file_path = 'Nyt.200811.txt'
    text = read_file(file_path)

    bigram_list = find_bigrams(text)
    # Debug print first 20 bigrams
    print("First 20 Bigrams:")
    for bigram in bigram_list[:20]:
        print(bigram)

    bigram_counts = count_bigrams(bigram_list)
    
    most_common_bigrams = bigram_counts.most_common(10)
    print("10 Most Common Bigrams:")
    for bigram, count in most_common_bigrams:
        print(f"{bigram}: {count}")

if __name__ == "__main__":
    main()