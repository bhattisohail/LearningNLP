import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag, ne_chunk
from nltk.chunk import RegexpParser
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

# Ensure all necessary datasets are downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('wordnet')

def tokenize_text(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    return sentences, words

def filter_stop_words(words):
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word.casefold() not in stop_words]
    return filtered_words

def stem_words(words):
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in words]
    return stemmed_words

def lemmatize_words(words):
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    return lemmatized_words

def pos_tagging(words):
    return pos_tag(words)

def chunk_words(pos_tags, grammar):
    chunk_parser = RegexpParser(grammar)
    chunked_tree = chunk_parser.parse(pos_tags)
    return chunked_tree

# Example usage
example_text = """
Muad'Dib learned rapidly because his first training was in how to learn.
And the first lesson of all was the basic trust that he could learn.
It's shocking to find how many people do not believe they can learn,
and how many more believe learning to be difficult."""

sentences, words = tokenize_text(example_text)
print("Tokenized Sentences:", sentences)
print("Tokenized Words:", words)

filtered_words = filter_stop_words(words)
print("Filtered Words (Stopwords Removed):", filtered_words)

string_for_stemming = """
The crew of the USS Discovery discovered many discoveries.
Discovering is what explorers do."""
words_for_stemming = word_tokenize(string_for_stemming)
stemmed_words = stem_words(words_for_stemming)
print("Stemmed Words:", stemmed_words)

sagan_quote = """
If you wish to make an apple pie from scratch,
you must first invent the universe."""
words_in_sagan_quote = word_tokenize(sagan_quote)
print("POS Tags for Sagan Quote:", pos_tagging(words_in_sagan_quote))

jabberwocky_excerpt = """
'Twas brillig, and the slithy toves did gyre and gimble in the wabe:
all mimsy were the borogoves, and the mome raths outgrabe."""
words_in_excerpt = word_tokenize(jabberwocky_excerpt)
print("POS Tags for Jabberwocky Excerpt:", pos_tagging(words_in_excerpt))

string_for_lemmatizing = "The friends of DeSoto love scarves."
words_for_lemmatizing = word_tokenize(string_for_lemmatizing)
lemmatized_words = lemmatize_words(words_for_lemmatizing)
print("Lemmatized Words:", lemmatized_words)

pos_tags = pos_tagging(filtered_words)
print("POS Tags:", pos_tags)

lotr_quote = "It's a dangerous business, Frodo, going out your door."
words_in_lotr_quote = word_tokenize(lotr_quote)
lotr_pos_tags = pos_tagging(words_in_lotr_quote)
print("POS Tags for LOTR Quote:", lotr_pos_tags)
chunk_grammar = "NP: {<DT>?<JJ>*<NN>}"
chunked_tree = chunk_words(lotr_pos_tags, chunk_grammar)
chunked_tree.draw()