import csv
import xml.etree.ElementTree as ET
from typing import Dict, List

from utils.file_handling import write_on_output_file
from TD2.q5_write_xml import generate_XML_no_images, generateXml, prettify
from TD3.q1_1_segmente import detokenize, read_corpus, segment_corpus
from TD3.q1_2_substitue import substitute_words

import utils.corpus_types as type

"""Forme le dico stop words (avec seuil depuis tf_idf.csv), filtre le corpus dans filtered_corpus.xml"""


def make_stop_word_dictionnary(tfidf_file: str, threshold: float) -> Dict[str, str]:
    res = {}
    with open(tfidf_file, encoding="utf-8", newline="\n") as file:
        reader = csv.reader(file, delimiter="\t")
        for row in reader:
            _, word, tfidf = row
            if float(tfidf) <= threshold:
                res[word] = " "
    return res


# TODO formaliser strucutre données tokens
def remove_stop_word(
    tokenized_corpus: type.TokenizedCorpus, stopwords: List[str]
) -> type.TokenizedCorpus:

    for i, b in enumerate(tokenized_corpus):

        for category in ["titre", "texte"]:
            token_list = b[category]
            for stop_word in stopwords:
                token_list = list(filter(lambda word: word != stop_word, token_list))
            tokenized_corpus[i][category] = token_list

    return tokenized_corpus


def reform_corpus(tokenized_corpus: type.TokenizedCorpus, outputfile: str) -> str:
    corpus = detokenize(tokenized_corpus)
    generate_XML_no_images(corpus, outputfile)
