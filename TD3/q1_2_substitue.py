import csv
from typing import Dict

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
