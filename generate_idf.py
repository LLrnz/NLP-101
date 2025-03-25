import csv
import math
from typing import Counter, Dict, List, Set, Tuple

from file_handling import write_on_output_file


def read_is_word_freq_dict(filepath: str) -> Dict[int, Dict[str, int]]:
    freqDict = {}

    with open(filepath, encoding="utf-8", newline="\n") as file:
        reader = csv.reader(file, delimiter="	")

        for row in reader:
            docId, word, freq = row
            freqDict[docId][word] = freq

    return freqDict


def read_word_docid_file(filepath: str) -> Set[Tuple[str, int]]:
    wordDocID = []
    with open(filepath, encoding="utf-8", newline="\n") as file:
        reader = csv.reader(file, delimiter="	")

        for row in reader:
            word, docID = row
            wordDocID.append((word, docID))
        return set(wordDocID)


def calculate_idf(wordDocId: Set[Tuple[str, int]]) -> str:
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


write_on_output_file(
    calculate_idf(read_word_docid_file("output/test2.txt")), "output/test3.csv"
)
