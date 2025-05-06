import xml.etree.ElementTree as ET
from collections import defaultdict
import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt")

# Charger le fichier XML racinisé ou lemmatisé
tree = ET.parse("output/corpus_filtered_substitued.xml")
root = tree.getroot()

# Dictionnaire inverse : mot → {id_fichier → fréquence}
index_inverse = defaultdict(lambda: defaultdict(int))

# Parcourir tous les bulletins
for bulletin in root.findall("bulletin"):
    id_fichier = bulletin.findtext("fichier", default="inconnu").strip()

    titre = bulletin.findtext("titre", default="")
    texte = bulletin.findtext("texte", default="")
    contenu = f"{titre} {texte}"

    mots = word_tokenize(contenu, language="french")
    for mot in mots:
        mot = mot.lower()
        if mot.isalpha():
            index_inverse[mot][id_fichier] += 1

# Sauvegarder l’index inverse
with open("output/fichier_inverse_titre_texte.csv", "w", encoding="utf-8") as f:
    for mot, docs in sorted(index_inverse.items()):
        doc_freqs = " ".join([f"{doc_id}:{freq}" for doc_id, freq in docs.items()])
        f.write(f"{mot}\t{doc_freqs}\n")

