import xml.etree.ElementTree as ET
from nltk.stem.snowball import SnowballStemmer
import nltk

nltk.download('punkt_tab')  # Télécharge le tokenizer de NLTK
# Initialisation du stemmer pour le français
stemmer = SnowballStemmer("french") 

tree = ET.parse("output/out_bulletinexample.xml")  
root = tree.getroot()

mot_racine = []  # Liste pour stocker les mots racines de chaque bulletin

for bulletin in root.findall("bulletin"):
    titre = bulletin.findtext('titre', default='')
    texte = bulletin.findtext('texte', default='')

    contenu = f"{titre} {texte}"  # Concatène le titre et le texte du bulletin
    # Tokenisation du contenu
    mots = nltk.word_tokenize(contenu, language='french') 
    for mot in mots:
        mot_nettoye = mot.lower()  # Convertit le mot en minuscule
        if mot_nettoye.isalpha():  # Vérifie si le mot ne contient que des lettres
            racine = stemmer.stem(mot_nettoye)
            mot_racine.append((mot_nettoye, racine))  # Ajoute le mot et sa racine sous forme de tuple

# Enregistrement des mots racines dans un fichier nltk.py
with open("output/nltk.csv", "w", encoding="utf-8") as f:
    for mot, racine in mot_racine:
        f.write(f"{mot}\t{racine}\n")  # Écrit chaque mot et sa racine dans le fichier
