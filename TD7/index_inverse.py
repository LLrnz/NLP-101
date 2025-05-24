import csv
from collections import defaultdict

# Créer l'index inversé
inverted_index = defaultdict(list)

# Lire le fichier des tokens
with open("output/tokens.csv", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        mot, doc_id = line.split("\t")
        if doc_id not in inverted_index[mot]:
            inverted_index[mot].append(doc_id)

# Création du fichier CSV inverted_index pour l'index inversé de tokens!
with open("output/inverted_index.csv", "w", newline='', encoding="utf-8") as f_out:
    writer = csv.writer(f_out)
    writer.writerow(["Mot", "Liste_docs"])  # En-têtes des colonnes

    for mot, doc_list in inverted_index.items():
        writer.writerow([mot, str(doc_list)])  # Convertir la liste en chaîne de caractères

print("*** Fichier index inversé créé avec succès ! ***")
