import re
from htmlScrapper import (
    extract_author,
    extract_contact,
    extract_number_and_date,
    extract_id_text_title_and_section,
    parseAllHTML,
    parseHTML,
)

BULLETINS_DIR = "res/BULLETINS"


def test_extract_number_and_date():

    bulletin = parseHTML(BULLETINS_DIR + "/67068.htm")

    num, date = extract_number_and_date(bulletin)

    # Check if name is coherent
    # assert re.match("[A-Z]+ [\w]+ numéro [0-9]+", num)
    assert "BE France numéro 258" == num

    # Check if date is coherent
    assert re.match("[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{4}", date)


def test_extract_number_and_date_all():

    bulletins = parseAllHTML(BULLETINS_DIR + "res/BULLETINS")

    for filename, b in bulletins.items():
        num, date = extract_number_and_date(b)

        # Check if name is coherent
        assert re.match("[A-Z]+ [\w]+ numéro [0-9]+", num)

        # Check if date is coherent
        assert re.match("[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{4}", date)


def test_extract_id_text_title_and_section():
    bulletin = parseHTML(BULLETINS_DIR + "/67068.htm")
    id, text, title, section = extract_id_text_title_and_section(bulletin)

    # check if  id is coherent
    # assert re.match("\d{5}", id)
    assert id == "67068"
    # # Check if text is coherent
    # assert re.match("(\S+ ){25,}", text)
    assert (
        text
        == """Le 27 avril dernier, le CNRS décernait pour la première fois la Médaille de l'Innovation, dont Valérie Pécresse, ministre de l'Enseignement Supérieur et de la Recherche est à l'origine de la création. Le CNRS souhaite ainsi honorer des chercheurs et ingénieurs travaillant dans des établissements publics de recherche, des universités, des grandes écoles mais aussi des industriels qui développent des innovations marquantes. Pour cette première édition, cette nouvelle distinction a été attribuée à trois chercheurs réputés : l'économiste Esther Duflo, le roboticien François Pierrot et le physicien Mathias Fink. Directeur de l'Institut Langevin "Ondes et Images", créé en janvier 2009 au sein de l'Ecole de Physique et de Chimie Industrielles de la Ville de Paris (ESPCI), Mathias Fink est un remarquable exemple de ces chercheurs qui innovent. Les travaux de son équipe ont en effet abouti à la création de quatre start-ups, qui totalisent 230 personnes, dans des domaines aussi variés que la médecine, les télécommunications, le multimédia ou encore les objets tactiles."J'aime transformer des idées de physique très fondamentale en produits innovants", précise d'emblée Mathias Fink. Mais pour y parvenir, il fallait trouver le "terrain" propice. Et c'est à la fin des années 1980, à l'occasion d'une rencontre avec Georges Charpak, le prix Nobel de Physique 1992, qu'il va le découvrir, au coeur de la Montagne Sainte Geneviève, en plein Paris. Alors physicien au sein d'un des plus grands laboratoires français de physique du solide, Mathias Fink souhaite faire de l'innovation autour du concept de renversement du temps. De la "belle physique" comme la qualifient les connaisseurs, qui plus est qui intéresse quatre grands industriels du secteur aéronautique (Dassault, Aerospatial, Snecma, Turboméca), prêts à financer des travaux. Mais à cette époque, le milieu de la recherche est encore peu enclin à travailler avec l'industrie, d'autant plus si celle-ci est "militaro-industrielle". Aussi Mathias Fink se retrouve isolé. Georges Charpak lui propose alors de rencontrer Pierre-Gilles de Gennes, alors directeur de l'ESPCI, et Jacques Lewiner, le directeur scientifique. "C'est un endroit sympathique", lui précise Georges Charpak. "Je les ai rencontré. L'endroit était en effet très sympathique. Ils m'ont alors dit : vous voulez Innovez ? Alors venez", résume Mathias Fink qui ajoute : "cela a été la chance de ma carrière".Vous êtes chercheur : amusez-vousC'est ainsi que dès 1990, ce physicien crée le Laboratoire Ondes et Acoustique, dans une école qu'il qualifie d'"unique". "Innover est particulièrement bien vu à l'ESPCI, et l'on vous donne le feu vert du moment que l'idée proposée est très originale", précise-t-il. Autre particularité de cette école vraiment pas comme les autres Grandes Ecoles, la pluridisciplinarité qui y règne. Ne cherchez pas, vous n'y trouverez pas comme ailleurs un département de physique, un département de chimie et un département de biologie. "Ici, on vous dit dès le départ : vous êtes chercheur, amusez-vous", souligne-t-il avec une pointe d'humour. Et c'est en s'amusant que lui et son équipe ont développé les fameux miroirs à retournement temporel qui permettent d'échantillonner et d'enregistrer un champ acoustique incident puis de le réémettre dans une chronologie inversée. Mathias Fink et ses collaborateurs se sont rendus compte en effet que faire revivre à une onde sa vie passée permettait de focaliser cette onde à sa source d'une façon très efficace. Ils commencèrent alors à travailler d'abord sur les ultrasons, puis sur les ondes sismiques et les micro-ondes.Cette équipe aurait pu se limiter à publier d'excellents papiers dans des publications réputées comme Physical Review. Mais ces chercheurs ont compris très vite qu'au-delà de cette "belle physique", il y avait des applications potentielles. Ainsi le renversement du temps permettait de brûler une tumeur, mais aussi de détruire un composant électronique, ou encore de voir derrière un mur ou d'envoyer des informations à un endroit précis dans une pièce. "Progressivement, nous avons donc développé un certain nombre d'instruments originaux qui ont fini par déboucher sur la création de plusieurs start-ups", indique-t-il. A partir du concept de renversement du temps, Mathias Fink et son équipe ont découvert qu'il était possible de créer des images d'une autre façon. Aussi sont-ils parvenus à fabriquer des imageurs du corps humain grâce auxquels il est possible d'obtenir 10.000 images par seconde du corps humain. "Nous avons pu alors découvrir que le corps humain était parcouru d'ondes que jamais personne n'avait observé jusqu'alors", s'enthousiasme-t-il.La pluridisciplinarité, clé de la réussite de l'Institut Langevin "Ondes et Images"Le renversement du temps aurait-il des effets sur l'âge de ceux qui le pratiquent ? Au-delà de la boutade, Mathias Fink, âgé aujourd'hui de 65 ans, pourrait le laisser croire, tant son enthousiasme reste intact. Ainsi, en 2009 a-t-il concrétisé le rapprochement de son laboratoire avec un autre laboratoire de l'ESPCI, celui d'Optique Physique, en créant l'Institut Langevin "Ondes et Images", dont il est le directeur, Arnaud Tourin et Rémi Carminatti en étant les deux directeurs adjoints. Cette Unité Mixte de Recherche (CNRS/ESPCI ParisTech/UPMC/Université Paris-Diderot), qui compte une centaine de personnes, a pour coeur de métier la physique des ondes. Les recherches qui y sont menées s'étendent des concepts fondamentaux aux applications les plus poussées de l'imagerie multi-ondes (acousto-optique, photo-acoustique, élastographie par ultrasons ou IRM) aux techniques originales de focalisation (retournement temporel, filtre inverse, contrôle de front d'ondes), en passant par la création d'entreprises mettant en oeuvre ces nouvelles technologies dans les domaines du biomédical, des télécommunications, de la domotique, etc. "L'aventure se poursuit, toujours dans la pluridisciplinarité, qui est la clé de notre réussite. Aussi faut-il impérativement la préserver", conclut-il."""
    )

    assert title == "Physique : Mathias Fink, un bel exemple de chercheur qui innove"

    assert section == "Focus"


def test_extract_id_text_title_and_section_all():

    bulletins = parseAllHTML(BULLETINS_DIR + "res/BULLETINS")

    for filename, b in bulletins.items():
        id, text, title, section = extract_id_text_title_and_section(b)

        # check if  id is coherent
        assert re.match("\d{5}", id)

        # Check if text is coherent
        assert re.match("(\S+ ){200,}", text)

        # Check if title is coherent
        assert re.match("(\S+ ){4,20}", title)

        # Check if section is coherent
        assert re.match("(\S+[ ]*){1,5}", section)


def test_extract_author():

    bulletin = parseHTML(BULLETINS_DIR + "/67068.htm")

    author = extract_author(bulletin)

    assert author == "Jean-François Desessard"


def test_extract_author_all():

    bulletins = parseAllHTML(BULLETINS_DIR + "res/BULLETINS")

    for filename, b in bulletins.items():
        author = extract_author(b)

        # Check if name is coherent
        assert re.match("[\w -]*", author)


def test_extract_contact():

    bulletin = parseHTML(BULLETINS_DIR + "/67068.htm")

    contact = extract_contact(bulletin)

    assert (
        contact
        == """Institut Langevin "Ondes et Images" - Mathias Fink - email : mathias.fink@espci.fr - http://www.institut-langevin.espci.fr"""
    )
