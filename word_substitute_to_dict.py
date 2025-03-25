import csv
from typing import Dict


def substitues_to_dict(tsvSubstituesPath: str) -> Dict[str, str]:
    replacement_dict = {}
    with open(tsvSubstituesPath, encoding="utf-8", newline="\n") as file:
        reader = csv.reader(file, delimiter="	")

        for row in reader:
            print(", ".join(row))
            replacement_dict[row[0]] = row[1]

    return replacement_dict


print(substitues_to_dict("res/words_to_replace.csv"))
