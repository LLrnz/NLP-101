import re
from bs4 import BeautifulSoup

from file_handling import write_on_output_file


def read_corpus(corpusXMLFile: str) -> BeautifulSoup:
    with open(corpusXMLFile) as fp:
        corpus = BeautifulSoup(fp, "xml")
    return corpus


def segment_corpus(corpus: BeautifulSoup) -> str:
    segementedCorpus = ""
    for bulletin in corpus.find_all("bulletin"):

        filename = bulletin.find("fichier").text

        texts = bulletin.find("titre").text
        texts += " " + bulletin.find("texte").text

        texts = clean_text(texts)

        for word in texts.split(" "):
            if word != "":
                segementedCorpus += word + "	" + filename + "\n"

    return segementedCorpus


def clean_text(text: str) -> str:
    text = text.lower()
    text = text.replace("'", "' ")
    text = re.sub(r"[\n-]", " ", text)
    text = re.sub(r"[^\w\s']", " ", text)

    return text


write_on_output_file(
    segment_corpus(read_corpus("output/test1.xml")), "output/test2.txt"
)
