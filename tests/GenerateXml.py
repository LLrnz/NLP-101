import xml.etree.ElementTree as ET

nameDoc = "67068.htm" 
numberBulletin = "BE France 258"
dateBulletin = "21/06/2011"
rubrique = "Focus"
Title = "Physique : Mathias Fink, un bel exemple de chercheur qui innove"
autor = "Jean-François Desessard"
text = "Le 27 avril dernier, le CNRS décernait pour la première fois la Médaille de l'Innovation, dont Valérie Pécresse, ministre de l'Enseignement Supérieur et de la Recherche est à l'origine de la création. Le CNRS souhaite ainsi honorer des chercheurs et ingénieurs travaillant dans des établissements publics de recherche, des universités, des grandes écoles mais aussi des industriels qui développent des innovations marquantes. Pour cette première édition, cette nouvelle distinction a été attribuée à trois chercheurs réputés : l'économiste Esther Duflo, le roboticien François Pierrot et le physicien Mathias Fink. Directeur de l'Institut Langevin "
contact = "Institut Langevin"
                                        
def generateXml(name , number , date, rubrique , title , autor, text , contact ) :
    corpus = ET.Element("corpus")

    bulletin = ET.SubElement(corpus, "bulletin")

    fichier = ET.SubElement(bulletin, "fichier")
    fichier.text = name

    numero = ET.SubElement(bulletin, "numero")
    numero.text = number

    date = ET.SubElement(bulletin, "date")
    date.text = date

    rubrique = ET.SubElement(bulletin, "rubrique")
    rubrique.text = rubrique

    titre = ET.SubElement(bulletin, "titre")
    titre.text = title

    auteur = ET.SubElement(bulletin, "auteur")
    auteur.text = autor

    texte = ET.SubElement(bulletin, "texte")
    texte.text = text

    image = ET.SubElement(bulletin, "image")
    image.text = "image"

    contact = ET.SubElement(bulletin, "contact")
    contact.text = contact

    tree = ET.ElementTree(corpus)
    tree.write("output.xml" , encoding ="utf-8" , xml_declaration = True) 

    
    
generateXml(nameDoc , numberBulletin , dateBulletin , rubrique , Title , autor , text , contact )



