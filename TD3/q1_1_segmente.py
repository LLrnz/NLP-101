import re
from typing import List
from bs4 import BeautifulSoup

import utils.file_handling as file
import utils.corpus_types as type
import utils.paths as path

"""Tokénisation"""


def read_corpus(corpusXMLFile: str) -> BeautifulSoup:
    with open(corpusXMLFile) as fp:
        corpus = BeautifulSoup(fp, "xml")
    return corpus


def segment_corpus(corpus: BeautifulSoup) -> type.TokenizedCorpus:

    token_list = []
    for i, bulletin in enumerate(corpus.find_all("bulletin")):
        token_list.append({})

        for category in bulletin.children:
            if category is not None:
                key = category.name
                text = clean_text(category.text)
                token_list[i][key] = split_text(text)

    return token_list


def split_text(text: str) -> type.Tokens:
    token_list = []
    for word in text.split(" "):
        if word != "":
            token_list.append(word)
    return token_list


def clean_text(text: str) -> str:
    text = text.lower()
    text = text.replace("'", "' ")
    text = re.sub(r"[\n-]", " ", text)
    text = re.sub(r"[^\w\s']", " ", text)

    return text


def tokens_to_file(toknized_corpus: type.TokenizedCorpus) -> str:
    segmented_corpus = ""

    for bulletin in toknized_corpus:
        fichier = bulletin["fichier"][0]
        for _, tokens in bulletin.items():
            for token in tokens:
                segmented_corpus += token + "	" + fichier + "\n"

    return segmented_corpus


def unsplit(text: List[str]) -> str:
    return " ".join(text)


def detokenize(toknized_corpus: type.TokenizedCorpus) -> type.Corpus:
    for bulletin in toknized_corpus:
        for category, tokens in bulletin.items():
            bulletin[category] = unsplit(tokens)

    return toknized_corpus
