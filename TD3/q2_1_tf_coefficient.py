import csv
from typing import List, Tuple
from bs4 import BeautifulSoup
from collections import Counter
import utils.corpus_types as type
import utils.paths as path

"""Calcule le tf de chaque terme dans chaque doc depuis le fichier de tokens"""


def coefficient_tf(segmentedCorpusFile: str) -> Counter:
    result = []
    with open(segmentedCorpusFile, "r", encoding="utf-8") as fp:
        word_counts = Counter()
        for line in fp:
            line = line.strip()
            if line:  # Evitemement des lignes vides
                parts = line.split("\t")
                if len(parts) == 2:
                    word, id_doc = parts
                    word_counts[word, id_doc] += 1  # Compte des occurences

    return word_counts


def write_coefficient_tf(tf_counts: Counter, outputFile: str):
    with open(outputFile, "w", encoding="utf-8") as f:
        for (word, id_doc), count in tf_counts.items():
            f.write(f"{id_doc}\t{word}\t{count}\n")


def read_file(filepath: str) -> type.FreqList:
    res = []

    with open(filepath, encoding="utf-8", newline="\n") as file:
        reader = csv.reader(file, delimiter="	")
        for row in reader:
            id_doc, word, tf = row
            res.append((id_doc, word, int(tf)))

    return res
