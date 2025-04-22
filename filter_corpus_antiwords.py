import csv
from typing import Dict, List

from file_handling import write_on_output_file


def make_stop_word_dictionnary(tfidf_file: str, threshold: float) -> List[str]:
    res = []
    with open(tfidf_file, encoding="utf-8", newline="\n") as file:
        reader = csv.reader(file, delimiter="\t")
        for row in reader:
            _, word, tfidf = row
            if float(tfidf) <= threshold:
                res.append(word)
    return res


def remove_stop_word(xml_corpus_file: str, stopwords: List[str]) -> str:

    with open(xml_corpus_file, "r", encoding="utf-8") as file:
        corpus = file.read()

        for word in stopwords:
            corpus = corpus.replace(" " + word + " ", " ")

        return corpus


write_on_output_file(
    remove_stop_word(
        "output/test1.xml", make_stop_word_dictionnary("output/tfidf.csv", 1.2)
    ),
    "output/filtered_corpus.xml",
)
