import xml.etree.ElementTree as ET
import csv
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')  # Pour tokeniser correctement en français

#Chargement du dictionnaire de substitution
def charger_substitutions(path_csv):
    dico = {}
    with open(path_csv, encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if len(row) == 2:
                dico[row[0]] = row[1]
    return dico

#Substitution des mots dans un texte
def substituer_texte(texte, dico):
    mots = word_tokenize(texte, language="french")
    texte_transforme = ' '.join([dico.get(mot.lower(), mot) for mot in mots])
    return texte_transforme

# Lecture du XML, transformer, sauvegarder
def filtrer_xml(input_xml, output_xml, dict_path):
    dico = charger_substitutions(dict_path)
    tree = ET.parse(input_xml)
    root = tree.getroot()

    for bulletin in root.findall("bulletin"):
        titre_elem = bulletin.find("titre")
        texte_elem = bulletin.find("texte")

        if titre_elem is not None:
            titre_elem.text = substituer_texte(titre_elem.text or "", dico)
        if texte_elem is not None:
            texte_elem.text = substituer_texte(texte_elem.text or "", dico)

    tree.write(output_xml, encoding="utf-8", xml_declaration=True)

input_xml = "output/filtered_corpus.xml"
output_xml = "output/corpus_filtered_substitued.xml"
dict_path = "output/nltk.csv"  

# Création du fichier XML corpus_filtré_substitué.xml filtré et substitué via nltk 
filtrer_xml(input_xml, output_xml, dict_path)
print("Fichier XML transformé sauvegardé :", output_xml)
