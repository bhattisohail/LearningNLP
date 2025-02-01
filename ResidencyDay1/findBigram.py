from nltk.tokenize import word_tokenize
from nltk import bigrams
from collections import Counter


def tokenize_words(text):
    """
    Tokenizes the input text into a list of words.

    Args:
        text: The input text string.

    Returns:
        A list of strings, where each string is a word from the input text.
    """
    return word_tokenize(text)


def find_bigrams(text):
    """
    Finds all bigrams in the input text.

    Args:
        text: The input text string.

    Returns:
        A list of tuples, where each tuple represents a bigram (pair of consecutive words).
    """
    words = tokenize_words(text)
    bigram_list = list(bigrams(words))
    return bigram_list


def read_file(file_path):
    """
    Reads the content of a file.

    Args:
        file_path: The path to the file.

    Returns:
        A string containing the content of the file.  Returns an empty string if the file cannot be opened.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return "" 
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return ""


def count_bigrams(bigram_list):
    """
    Counts the occurrences of each bigram in a list of bigrams.

    Args:
        bigram_list: A list of tuples, where each tuple is a bigram.

    Returns:
        A Counter object, where the keys are bigrams and the values are their counts.
    """
    return Counter(bigram_list)


def main():
    """
    Main function to read a file, find bigrams, count them, and print the most common ones.
    """
    file_path = 'Nyt.200811.txt'
    text = read_file(file_path)

    if not text:    # Check if file reading was successful
        return      # Exit early if file reading failed
    
    bigram_list = find_bigrams(text)

    bigram_counts = count_bigrams(bigram_list)
    
    most_common_bigrams = bigram_counts.most_common(10)
    print("The 10 Most Common Bigrams in order are: ")
    for bigram, count in most_common_bigrams:
        print(f"{bigram}: {count}")


if __name__ == "__main__":
    main()