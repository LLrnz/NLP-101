import csv
from collections import defaultdict

def build_inverted_index(filepath: str) -> dict:
  
    inverted_index = defaultdict(list)
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            mot, doc_id = line.split("\t")
            if doc_id not in inverted_index[mot]:
                inverted_index[mot].append(doc_id)
    return dict(inverted_index)

# Pas impotant, juste pour affichage visuel du dictionnaire dans le csv

def write_inverted_index_to_csv(inverted_index: dict, output_csv_path: str):
    
    with open("output/inverted_index.csv", "w", newline='', encoding="utf-8") as f_out:
        writer = csv.writer(f_out)
        writer.writerow(["Mot", "Liste_docs"])  # En-têtes des colonnes

        for mot, doc_list in inverted_index.items():
            writer.writerow([mot, str(doc_list)])  # La liste est convertie en chaîne
    print(f"✅ Fichier index inversé créé avec succès ")


inverted_index = build_inverted_index("output/tokens.csv")

# Écrire ce dictionnaire dans le fichier CSV
write_inverted_index_to_csv(inverted_index, "output/inverted_index.csv")
