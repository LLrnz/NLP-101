import xml.etree.ElementTree as ET
from xml.dom import minidom

nameDoc = "67068" 
numberBulletin = "258"
dateBulletin = "21/06/2011"
rubriqueDoc = "Focus"
TitleDoc = "Physique : Mathias Fink, un bel exemple de chercheur qui innove"
autorDoc = "Jean-François Desessard"
textDoc = ("Le 27 avril dernier, le CNRS décernait pour la première fois la Médaille de l'Innovation, dont Valérie Pécresse, ministre de l'Enseignement Supérieur et de la Recherche est à l'origine de la création. Le CNRS souhaite ainsi honorer des chercheurs et ingénieurs travaillant dans des établissements publics de recherche, des universités, des grandes écoles mais aussi des industriels qui développent des innovations marquantes. Pour cette première édition, cette nouvelle distinction a été attribuée à trois chercheurs réputés : l'économiste Esther Duflo, le roboticien François Pierrot et le physicien Mathias Fink. Directeur de l'Institut Langevin")
imageDoc = {"image1" : "img1" , "image2": "img2", "image3": "img3" , "image4": "img4", "image5": "img5"} 
contactDoc = "Institut Langevin"

imageDoc.values()

def prettify(elem):
    """Fonction d'indentation du fichier XML.
    """
    rough_string = ET.tostring(elem, encoding = 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")   
                                        
def generateXml(name , number , date, rubrique , title , autor, text , images , contact ) :
    corpus = ET.Element("corpus")

    bulletin = ET.SubElement(corpus, "bulletin")

    fichier = ET.SubElement(bulletin, "fichier")
    fichier.text = name

    numero = ET.SubElement(bulletin, "numero")
    numero.text = number

    date_elem = ET.SubElement(bulletin, "date")
    date_elem.text = date

    rubrique_elem = ET.SubElement(bulletin, "rubrique")
    rubrique_elem.text = rubrique

    titre = ET.SubElement(bulletin, "titre")
    titre.text = title

    auteur = ET.SubElement(bulletin, "auteur")
    auteur.text = autor

    texte = ET.SubElement(bulletin, "texte")
    texte.text = text

    images_elem = ET.SubElement(bulletin, "images")
   
    # Possibility of many images
    for key, value in images.items():
        image_elem = ET.SubElement(images_elem, "image")
        image_elem.text = value
            
    contact_elem = ET.SubElement(bulletin, "contact")
    contact_elem.text = contact

    xml_str = prettify(corpus)
    with open("output.xml", "w" , encoding="utf-8") as f:
        f.write(xml_str)
        
generateXml(nameDoc , numberBulletin , dateBulletin , rubriqueDoc , TitleDoc , autorDoc , textDoc , imageDoc, contactDoc )



