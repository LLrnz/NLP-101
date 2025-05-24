import csv
from index_inverse import build_inverted_index

def search_in_inverted_index_dict(inverted_index: dict[str, list[str]], mot_cle: str) -> set:
  
    if mot_cle in inverted_index:
        return set(inverted_index[mot_cle])
    else:
        return set()

# Charge ton dictionnaire d'index inversé
inverted_index = build_inverted_index("output/tokens.csv")

# Recherche d'un mot
mot_cle = "innove"
result = search_in_inverted_index_dict(inverted_index, mot_cle)

print(f"Documents contenant le mot '{mot_cle}': {result}")