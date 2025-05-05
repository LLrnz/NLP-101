import csv
import math
from typing import Counter

from utils.file_handling import write_on_output_file
import utils.corpus_types as type
import utils.paths as path


"""Calcul l'didf depuis le fichier de tokens"""


def read_is_word_freq_dict(filepath: str) -> type.TokenFreqDictByDocs:
    freqDict = {}

    with open(filepath, encoding="utf-8", newline="\n") as file:
        reader = csv.reader(file, delimiter="	")

        for row in reader:
            docId, word, freq = row
            freqDict[docId][word] = freq

    return freqDict


def read_word_docid_file(filepath: str) -> type.TokensAndDocIDsSet:
    wordDocID = []
    with open(filepath, encoding="utf-8", newline="\n") as file:
        reader = csv.reader(file, delimiter="	")

        for row in reader:
            word, docID = row
            wordDocID.append((word, docID))
        return set(wordDocID)


def calculate_idf(wordDocId: type.TokensAndDocIDsSet) -> str:
    res = ""
    docCnt = Counter(tup[1] for tup in wordDocId)
    nbDocs = len(docCnt)

    wordCnt = Counter(tup[0] for tup in wordDocId)

    for tup in wordCnt.keys():
        word = tup  # [0]
        nbDocsWhereWordIsFound = wordCnt[word]
        idf = math.log10(nbDocs / nbDocsWhereWordIsFound)
        res += word + " " + f"{idf:.4f}" + "\n"

    return res


def file_to_dict(filepath: str) -> type.IdfDict:
    idf = {}

    with open(filepath, encoding="utf-8", newline="\n") as file:
        reader = csv.reader(file, delimiter=" ")
        for row in reader:
            word, w_idf = row
            idf[word] = float(w_idf)

    return idf
