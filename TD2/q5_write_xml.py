import xml.etree.ElementTree as ET
from xml.dom import minidom

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
    return reparsed.toprettyxml(indent="  ")


# TODO formaliser type entrée
def generateXml(corpus_data, outputFile):
    """Fonction de génération du fichier XML à partir des données du corpus."""
    corpus = ET.Element("corpus")

    for bullentin_data in corpus_data:
        bulletin = ET.SubElement(corpus, "bulletin")

        fichier = ET.SubElement(bulletin, "fichier")
        fichier.text = bullentin_data["nameDoc"]

        numero = ET.SubElement(bulletin, "numero")
        numero.text = bullentin_data["numberBulletin"]

        date_elem = ET.SubElement(bulletin, "date")
        date_elem.text = bullentin_data["dateBulletin"]

        rubrique_elem = ET.SubElement(bulletin, "rubrique")
        rubrique_elem.text = bullentin_data["rubriqueDoc"]

        titre = ET.SubElement(bulletin, "titre")
        titre.text = bullentin_data["TitleDoc"]

        auteur = ET.SubElement(bulletin, "auteur")
        auteur.text = bullentin_data["autorDoc"]

        texte = ET.SubElement(bulletin, "texte")
        texte.text = bullentin_data["textDoc"]

        images_elem = ET.SubElement(bulletin, "images")

        # Prise en compte des différentes images
        for key, value in bullentin_data["imageDoc"].items():
            image = ET.SubElement(images_elem, "image")
            image_elem = ET.SubElement(image, "urlImage")
            image_elem.text = key
            image_elem = ET.SubElement(image, "legendeImage")
            image_elem.text = value

        contact_elem = ET.SubElement(bulletin, "contact")
        contact_elem.text = bullentin_data["contactDoc"]

    xml_str = prettify(corpus)
    with open(outputFile, "w", encoding="utf-8") as f:
        f.write(xml_str)
