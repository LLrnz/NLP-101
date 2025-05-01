import re
from bs4 import BeautifulSoup

from ... import file_handling as file
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
            key = category.name
            text = clean_text(category.text)
            token_list[i][key] = split_text(text)

    return token_list


def split_text(text: str) -> type.Tokens:
    token_list = []
    for word in text.split(" "):
        if word != "":
            token_list.append(word)


def clean_text(text: str) -> str:
    text = text.lower()
    text = text.replace("'", "' ")
    text = re.sub(r"[\n-]", " ", text)
    text = re.sub(r"[^\w\s']", " ", text)

    return text


def tokens_to_file(toknized_corpus: type.TokenizedCorpus) -> str:
    segmented_corpus = ""

    for bulletin in toknized_corpus:
        for _, tokens in bulletin:
            for token in tokens:
                segementedCorpus += token + "	" + bulletin["fichier"] + "\n"

    return segmented_corpus


def detokenize(toknized_corpus: type.TokenizedCorpus) -> type.Corpus:
    pass  # TODO


# fichier de sortie : tokens.csv
file.write_on_output_file(
    tokens_to_file(segment_corpus(read_corpus(path.XML_CORPUS))[0], path.TOKENS)
)
