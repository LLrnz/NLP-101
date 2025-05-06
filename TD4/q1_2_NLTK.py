import xml.etree.ElementTree as ET
from nltk.stem.snowball import SnowballStemmer
import nltk

nltk.download('punkt_tab')  # Télécharge le tokenizer de NLTK
# Initialisation du stemmer pour le français
stemmer = SnowballStemmer("french") 

tree = ET.parse("output/filtered_corpus.xml")  
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

def process_xml(input_xml: str, output_xml: str, dictionary: Dict[str, str]):
    """Reads an XML file, substitutes words, and writes the updated XML to a new file."""
    tree = ET.parse(input_xml)
    root = tree.getroot()

    for bulletin in root.findall("bulletin"):
        # Process the 'titre' element
        titre = bulletin.find("titre")
        if titre is not None and titre.text:
            titre.text = substitute_words(dictionary, titre.text)

        # Process the 'texte' element
        texte = bulletin.find("texte")
        if texte is not None and texte.text:
            texte.text = substitute_words(dictionary, texte.text)

    # Write the updated XML to the output file
    tree.write(output_xml, encoding="utf-8", xml_declaration=True)


if __name__ == "__main__":
    # Input files
    input_xml = "output/filtered_corpus.xml"
    tsv_substitutes = "output/nltk.csv"
    output_xml = "output/updated_corpus.xml"

    # Load the substitution dictionary
    substitution_dict = substitues_to_dict(tsv_substitutes)

    # Process the XML file
    process_xml(input_xml, output_xml, substitution_dict)

    print(f"Updated XML file saved to: {output_xml}")