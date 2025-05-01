import re
from typing import Dict, List, Tuple
from bs4 import BeautifulSoup

from file_handling import write_on_output_file
import corpus_types as type

"""Tokénisation"""


def read_corpus(corpusXMLFile: str) -> BeautifulSoup:
    with open(corpusXMLFile) as fp:
        corpus = BeautifulSoup(fp, "xml")
    return corpus


def segment_corpus(corpus: BeautifulSoup) -> type.TokenizedCorpus:
    segementedCorpus = ""
    token_list = []
    for i, bulletin in enumerate(corpus.find_all("bulletin")):
        token_list.append({})
        filename = bulletin.find("fichier").text

        # TODO tokenizer tout le corpus

        texts = bulletin.find("titre").text
        token_list[i]["titre"] = []
        texts = clean_text(texts)
        for word in texts.split(" "):
            if word != "":
                segementedCorpus += word + "	" + filename + "\n"
                token_list[i]["titre"].append(word)

        texts = bulletin.find("texte").text
        token_list[i]["texte"] = []
        texts = clean_text(texts)
        for word in texts.split(" "):
            if word != "":
                segementedCorpus += word + "	" + filename + "\n"
                token_list[i]["texte"].append(word)

    return segementedCorpus, token_list


def clean_text(text: str) -> str:
    text = text.lower()
    text = text.replace("'", "' ")
    text = re.sub(r"[\n-]", " ", text)
    text = re.sub(r"[^\w\s']", " ", text)

    return text


def detokenize(toknized_corpus: type.TokenizedCorpus) -> type.Corpus:
    pass  # TODO


# fichier de sortie : tokens.csv
write_on_output_file(
    segment_corpus(read_corpus("output/corpus.xml"))[0], "output/tokens.csv"
)
