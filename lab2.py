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

# 1. Tokenization
example_text = """
Muad'Dib learned rapidly because his first training was in how to learn.
And the first lesson of all was the basic trust that he could learn.
It's shocking to find how many people do not believe they can learn,
and how many more believe learning to be difficult."""

sentences = sent_tokenize(example_text)
words = word_tokenize(example_text)

print("Tokenized Sentences:", sentences)
print("Tokenized Words:", words)

# 2. Filtering Stop Words
stop_words = set(stopwords.words("english"))
filtered_words = [word for word in words if word.casefold() not in stop_words]
print("Filtered Words (Stopwords Removed):", filtered_words)

# 3. Stemming
string_for_stemming = """
The crew of the USS Discovery discovered many discoveries.
Discovering is what explorers do."""
words = word_tokenize(string_for_stemming)
print("Words for Stemming:", words)
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in words]
print("Stemmed Words:", stemmed_words)

sagan_quote = """
If you wish to make an apple pie from scratch,
you must first invent the universe."""
words_in_sagan_quote = word_tokenize(sagan_quote)
nltk.pos_tag(words_in_sagan_quote)

jabberwocky_excerpt = """
'Twas brillig, and the slithy toves did gyre and gimble in the wabe:
all mimsy were the borogoves, and the mome raths outgrabe."""
words_in_excerpt = word_tokenize(jabberwocky_excerpt)
nltk.pos_tag(words_in_excerpt)
print("POS Tags for Jabberwocky Excerpt:", nltk.pos_tag(words_in_excerpt))

# 4. Lemmatization
lemmatizer = WordNetLemmatizer()
string_for_lemmatizing = "The friends of DeSoto love scarves."
words = word_tokenize(string_for_lemmatizing)
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
print("Lemmatized Words:", lemmatized_words)

# 5. POS Tagging
pos_tags = pos_tag(filtered_words)
print("POS Tags:", pos_tags)

# 6. Chunking
lotr_quote = "It's a dangerous business, Frodo, going out your door."
words_in_lotr_quote = word_tokenize(lotr_quote)
lotr_pos_tags = nltk.pos_tag(words_in_lotr_quote)
print("POS Tags for LOTR Quote:", lotr_pos_tags)
chunk_grammar = "NP: {<DT>?<JJ>*<NN>}"
chunk_parser = nltk.RegexpParser(chunk_grammar)
chunked_tree = chunk_parser.parse(lotr_pos_tags)
chunked_tree.draw()