import csv
from typing import Dict
import utils.corpus_types as type

"""Remplacer les mots d'un texte à partir d'un fichier de correspondances"""

# TODO prendre en entrée un fichier de correspondances
# /!\ toutes les instances du mots doivent être remplacées ?


def substitues_to_dict(tsvSubstituesPath: str) -> Dict[str, str]:
    replacement_dict = {}
    with open(tsvSubstituesPath, encoding="utf-8", newline="\n") as file:
        reader = csv.reader(file, delimiter="	")

        for row in reader:
            print(", ".join(row))
            replacement_dict[row[0]] = row[1]

    return replacement_dict


def substitute_words(dictionary, text):

    for key, value in dictionary.items():
        text = text.replace(" " + key + " ", value)

    return text


def substitute_words(dictionary: Dict[str, str], token_list: type.Token) -> type.Tokens:
    res = []
    for token in token_list:
        res.append(dictionary.get(token,token)) # J'ai rajouté ceci car je pense que Si le mot n'est pas dans le dictionnaire, on le garde tel quel
    return res


"""replace all words present in dict in given corpus (modifies corpus object)"""


def substitue_corpus(
    dictionary: Dict[str, str], tokenized_corpus: type.TokenizedCorpus
):
    for bulletin in tokenized_corpus:
        for category, tokens in bulletin.items():
            bulletin[category] = substitute_words(dictionary, tokens)
