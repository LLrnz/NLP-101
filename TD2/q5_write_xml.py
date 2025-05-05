import xml.etree.ElementTree as ET
from xml.dom import minidom

import utils.corpus_types as type

# Corpus de test comportant plusieurs bulletins
corpus_data = [
    {
        "nameDoc": "67068",
        "numberBulletin": "258",
        "dateBulletin": "21/06/2011",
        "rubriqueDoc": "Focus",
        "TitleDoc": "Physique : Mathias Fink, un bel exemple de chercheur qui innove",
        "autorDoc": "Jean-François Desessard",
        "textDoc": "Le 27 avril dernier, le CNRS décernait pour la première fois la Médaille de l'Innovation, dont Valérie Pécresse, ministre de l'Enseignement Supérieur et de la Recherche est à l'origine de la création. Le CNRS souhaite ainsi honorer des chercheurs et ingénieurs travaillant dans des établissements publics de recherche, des universités, des grandes écoles mais aussi des industriels qui développent des innovations marquantes. Pour cette première édition, cette nouvelle distinction a été attribuée à trois chercheurs réputés : l'économiste Esther Duflo, le roboticien François Pierrot et le physicien Mathias Fink. Directeur de l'Institut Langevin",
        "imageDoc": {
            "image1": "img1",
            "image2": "img2",
            "image3": "img3",
            "image4": "img4",
            "image5": "img5",
        },
        "contactDoc": "Institut Langevin",
    },
    {
        "nameDoc": "67069",
        "numberBulletin": "259",
        "dateBulletin": "22/06/2011",
        "rubriqueDoc": "Science",
        "TitleDoc": "Un autre article scientifique important",
        "autorDoc": "Auteur inconnu",
        "textDoc": "Un autre texte scientifique pertinent...",
        "imageDoc": {"image1": "imgA", "image2": "imgB"},
        "contactDoc": "Université X",
    },
    {
        "nameDoc": "70009",
        "numberBulletin": "200",
        "dateBulletin": "22/06/2012",
        "rubriqueDoc": "Mathématique",
        "TitleDoc": "Un autre article scientifique important",
        "autorDoc": "Andrea",
        "textDoc": "Un autre texte scientifique pertinent...",
        "imageDoc": {"image1": "imgA", "image2": "imgB", "image3": "imgC"},
        "contactDoc": "Université de compiègne",
    },
]


def prettify(elem):
    """Fonction d'indentation du fichier XML."""
    rough_string = ET.tostring(elem, encoding="utf-8")
    reparsed = minidom.parseString(rough_string)
    return reparsed  # .toprettyxml(indent="  ")


def generateXml(corpus_data: type.Corpus, outputFile: str):
    """Fonction de génération du fichier XML à partir des données du corpus."""
    corpus = ET.Element("corpus")

    for bullentin_data in corpus_data:
        bulletin = ET.SubElement(corpus, "bulletin")

        fichier = ET.SubElement(bulletin, "fichier")
        fichier.text = bullentin_data["fichier"]

        numero = ET.SubElement(bulletin, "numero")
        numero.text = bullentin_data["numero"]

        date_elem = ET.SubElement(bulletin, "date")
        date_elem.text = bullentin_data["date"]

        rubrique_elem = ET.SubElement(bulletin, "rubrique")
        rubrique_elem.text = bullentin_data["rubrique"]

        titre = ET.SubElement(bulletin, "titre")
        titre.text = bullentin_data["titre"]

        auteur = ET.SubElement(bulletin, "auteur")
        auteur.text = bullentin_data["auteur"]

        texte = ET.SubElement(bulletin, "texte")
        texte.text = bullentin_data["texte"]

        images_elem = ET.SubElement(bulletin, "images")

        # Prise en compte des différentes images
        for key, value in bullentin_data["images"].items():
            image = ET.SubElement(images_elem, "image")
            image_elem = ET.SubElement(image, "urlImage")
            image_elem.text = key
            image_elem = ET.SubElement(image, "legendeImage")
            image_elem.text = value

        contact_elem = ET.SubElement(bulletin, "contact")
        contact_elem.text = bullentin_data["contact"]

    # xml_str = prettify(corpus)

    with open(outputFile, "wb") as f:
        ET.ElementTree(corpus).write(f, encoding="utf-8")


def generate_XML_no_images(corpus_data: type.Corpus, outputFile: str):
    """Fonction de génération du fichier XML à partir des données du corpus."""
    corpus = ET.Element("corpus")

    for bullentin_data in corpus_data:
        bulletin = ET.SubElement(corpus, "bulletin")

        fichier = ET.SubElement(bulletin, "fichier")
        fichier.text = bullentin_data["fichier"]

        numero = ET.SubElement(bulletin, "numero")
        numero.text = bullentin_data["numero"]

        date_elem = ET.SubElement(bulletin, "date")
        date_elem.text = bullentin_data["date"]

        rubrique_elem = ET.SubElement(bulletin, "rubrique")
        rubrique_elem.text = bullentin_data["rubrique"]

        titre = ET.SubElement(bulletin, "titre")
        titre.text = bullentin_data["titre"]

        auteur = ET.SubElement(bulletin, "auteur")
        auteur.text = bullentin_data["auteur"]

        texte = ET.SubElement(bulletin, "texte")
        texte.text = bullentin_data["texte"]

        images_elem = ET.SubElement(bulletin, "images")
        images_elem.text = bullentin_data["images"]

        contact_elem = ET.SubElement(bulletin, "contact")
        contact_elem.text = bullentin_data["contact"]

    # xml_str = prettify(corpus)

    with open(outputFile, "wb") as f:
        ET.ElementTree(corpus).write(f, encoding="utf-8")
