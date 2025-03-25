import re
from bs4 import BeautifulSoup


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
            segementedCorpus += word + "	" + filename + "\n"

    return segementedCorpus


def write_on_output_file(corpus: str, outputFile: str):
    with open(outputFile, "w", encoding="utf-8") as f:
        f.write(corpus)


def clean_text(text: str) -> str:
    text = re.sub(r"[^\w\s']", "", text)
    text = text.replace("'", "' ")
    return text


write_on_output_file(
    segment_corpus(read_corpus("output/test1.xml")), "output/test2.txt"
)
