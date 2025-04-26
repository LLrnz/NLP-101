import csv
import xml.etree.ElementTree as ET
from typing import Dict, List

from file_handling import write_on_output_file
from TD2.q5_write_xml import prettify
from TD3.q1_1_segmente import read_corpus, segment_corpus
from TD3.q1_2_substitue import substitute_words

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
    tokenized_corpus: List[Dict[str, List[str]]], stopwords: List[str]
) -> Dict[str, List[str]]:
    new_corpus = []

    for i, b in enumerate(tokenized_corpus):
        new_corpus.append({})
        for category, token_list in b.items():
            for stop_word in stopwords:
                token_list = list(filter(lambda word: word != stop_word, token_list))
            new_corpus[i][category] = token_list

    return new_corpus


def reform_corpus(tokenized_corpus: List[Dict[str, List[str]]]) -> str:

    corpus = ET.Element("corpus")

    for bullentin_data in tokenized_corpus:
        bulletin = ET.SubElement(corpus, "bulletin")

        titre = ET.SubElement(bulletin, "titre")
        titre.text = bullentin_data["titre"]

        texte = ET.SubElement(bulletin, "texte")
        texte.text = bullentin_data["texte"]

    # xml_str = prettify(corpus)
    return corpus.text


write_on_output_file(
    reform_corpus(
        remove_stop_word(
            segment_corpus(read_corpus("output/corpus.xml"))[1],
            make_stop_word_dictionnary("output/tf_idf.csv", 1.2),
        )
    ),
    "output/filtered_corpus.xml",
)
