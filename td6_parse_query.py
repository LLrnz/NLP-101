import nltk

from TD3.conclu_filter_corpus_without_stop_words import (
    make_stop_word_dictionnary,
    remove_stop_word,
)
from TD3.q1_1_segmente import read_corpus, segment_corpus
from TD6.query_parser import generate_grammar


tokenized_corpus = segment_corpus(read_corpus("output/corpus.xml"))

grammar = generate_grammar(tokenized_corpus)


sent = "je chercher article sur changement climatique après 2012".split()

parser = nltk.RecursiveDescentParser(grammar)

print(parser.parse_one(sent))
for tree in parser.parse(sent):
    print(tree)
