import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag, ne_chunk
from nltk.chunk import RegexpParser
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

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

def chink_words(pos_tags, grammar):
    chunk_parser = RegexpParser(grammar)
    chunked_tree = chunk_parser.parse(pos_tags)
    return chunked_tree

def named_entity_recognition(pos_tags, binary=False):
    tree = ne_chunk(pos_tags, binary=binary)
    return tree

def create_concordance(text, word):
    nltk_text = nltk.Text(word_tokenize(text))
    nltk_text.concordance(word)

def create_dispersion_plot(text, words):
    nltk_text = nltk.Text(word_tokenize(text))
    nltk_text.dispersion_plot(words)

def create_frequency_distribution(words):
    freq_dist = FreqDist(words)
    freq_dist.plot(20, cumulative=False)
    return freq_dist

def find_collocations(text):
    nltk_text = nltk.Text(word_tokenize(text))
    nltk_text.collocations()

def process_text(text):
    print("Tokenizing text...")
    sentences, words = tokenize_text(text)
    print("Tokenized Sentences:", sentences)
    print("Tokenized Words:", words)

    print("Filtering stop words...")
    filtered_words = filter_stop_words(words)
    print("Filtered Words (Stopwords Removed):", filtered_words)

    return filtered_words

def process_and_print_pos_tags(text):
    words = word_tokenize(text)
    pos_tags = pos_tagging(words)
    print(f"POS Tags for text: {pos_tags}")
    return pos_tags

def draw_tree(tree, title):
    print(f"Drawing tree for {title}...")
    tree.draw()

example_text = """
Muad'Dib learned rapidly because his first training was in how to learn.
And the first lesson of all was the basic trust that he could learn.
It's shocking to find how many people do not believe they can learn,
and how many more believe learning to be difficult."""

filtered_words = process_text(example_text)

string_for_stemming = """
The crew of the USS Discovery discovered many discoveries.
Discovering is what explorers do."""
print("Stemming words...")
stemmed_words = stem_words(word_tokenize(string_for_stemming))
print("Stemmed Words:", stemmed_words)

sagan_quote = """
If you wish to make an apple pie from scratch,
you must first invent the universe."""
process_and_print_pos_tags(sagan_quote)

jabberwocky_excerpt = """
'Twas brillig, and the slithy toves did gyre and gimble in the wabe:
all mimsy were the borogoves, and the mome raths outgrabe."""
process_and_print_pos_tags(jabberwocky_excerpt)

string_for_lemmatizing = "The friends of DeSoto love scarves."
print("Lemmatizing words...")
lemmatized_words = lemmatize_words(word_tokenize(string_for_lemmatizing))
print("Lemmatized Words:", lemmatized_words)

pos_tags = pos_tagging(filtered_words)
print("POS Tags:", pos_tags)

lotr_quote = "It's a dangerous business, Frodo, going out your door."
lotr_pos_tags = process_and_print_pos_tags(lotr_quote)

# Named Entity Recognition
ner_tree = named_entity_recognition(lotr_pos_tags)
draw_tree(ner_tree, "LOTR Quote")

# Concordance
create_concordance(example_text, "learn")

# Dispersion Plot
create_dispersion_plot(example_text, ["learn", "believe", "trust"])

# Frequency Distribution
freq_dist = create_frequency_distribution(filtered_words)
print("Most common words:", freq_dist.most_common(10))

# Collocations
find_collocations(example_text)

quote = """
Men like Schiaparelli watched the red planet—it is odd, by-the-bye, that
for countless centuries Mars has been the star of war—but failed to
interpret the fluctuating appearances of the markings they mapped so well.
All that time the Martians must have been getting ready.

During the opposition of 1894 a great light was seen on the illuminated
part of the disk, first at the Lick Observatory, then by Perrotin of Nice,
and then by other observers. English readers heard of it first in the
issue of Nature dated August 2.
"""
def extract_ne(quote):
    print("Extracting named entities...")
    words = word_tokenize(quote)
    tags = nltk.pos_tag(words)
    tree = nltk.ne_chunk(tags, binary=True)
    named_entities = set(
        " ".join(i[0] for i in t)
        for t in tree
        if hasattr(t, "label") and t.label() == "NE"
    )
    print("Named Entities:", named_entities)
    return named_entities

print(extract_ne(quote))
