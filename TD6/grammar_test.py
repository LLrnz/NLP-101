from nltk import CFG, ChartParser

from TD3.conclu_filter_corpus_without_stop_words import (
    make_stop_word_dictionnary,
    remove_stop_word,
)
from TD3.q1_1_segmente import read_corpus, segment_corpus

tokenized_corpus = segment_corpus(read_corpus("output/corpus.xml"))

# tokenized_corpus = remove_stop_word(
#     segment_corpus(read_corpus("output/corpus.xml")),
#     make_stop_word_dictionnary("output/tf_idf.csv", 1.2),
# )

RESERVED_WORDS = [
    "images",
    "image",
    "avec",
    "après",
    "avant",
    "entre",
    "en",
    "au",
    "partir",
    "parus",
    "date",
    "ont",
    "publiés",
    "écrits",
    "ne",
    "pas",
    "ni",
    "mais",
    "ou",
    "soit",
    "et",
    "à",
    "la",
    "fois",
    "le",
    "du",
    "des",
    "d",
    "de",
    "l",
    "évoquent",
    "parlent",
    "traitent",
    "évoquant",
    "parlant",
    "traitant",
    "portant",
    "portent",
    "liés",
    "sur",
    "traite",
    "parle",
    "propos",
    "évoque",
    "impliquant",
    "il",
    "cité",
    "elle",
    "citée",
    "contient",
    "contient",
    "possédant",
    "contenant",
    "contiennent",
    "titre",
    "dans",
    "provenant",
    "dont",
    "est",
    "qui",
    "ont",
    "pour",
    "avoir",
    "tous",
    "la",
    "obtenir",
    "voir",
    "je",
    "nous",
    "t",
    "on",
    "j",
    "chercher",
    "sont",
    "afficher",
    "veux",
    "voudrais",
    "cherche",
    "souhaiter",
    "souhaitons",
    "souhaite",
    "donner",
    "trouve",
    "aimerais",
    "souhaitons",
    "rechercher",
    "liste",
    "quels",
    "dans",
    "quels",
    "dans",
    "quelles",
    "quelles",
    "les",
    "articles",
    "recherches",
    "un",
    "article",
    "des",
    "bulletins",
]


def gen_grammar(tokenized_corpus):

    glossaire = []
    for b in tokenized_corpus:
        for token in b["titre"]:
            glossaire.append(token)
        for token in b["texte"]:
            glossaire.append(token)

    glossaire = set(glossaire)
    glossaire.difference_update(set(RESERVED_WORDS))
    str_glossaire = '"'
    str_glossaire += '" | "'.join(glossaire)
    str_glossaire += '"'

    rubriques = []
    for b in tokenized_corpus:
        rubriques.append(" ".join(b["rubrique"]))

    rubriques = set(rubriques)

    str_rubriques = '"'
    str_rubriques += '" | "'.join(
        rubriques,
    )
    str_rubriques += '"'

    grammar = CFG.fromstring(
        """
    R -> RECHERCHE CDTS
    RECHERCHE -> SUJET VERBE UNK_RECHERCHE | SUJET VERBE OPTRECHERCHE UNK_RECHERCHE | QUESTION VERBE UNK_RECHERCHE | QUESTION UNK_RECHERCHE VERBE | VERBE UNK_RECHERCHE | UNK_RECHERCHE | QUESTION UNK_RECHERCHE VERBE SUJET | OPTRECHERCHE UNK_RECHERCHE | VERBE OPTRECHERCHE UNK_RECHERCHE | QUESTION UNK_RECHERCHE | QUESTION UNK_RECHERCHE VERBE SUJET OBJET | OPTRECHERCHE UNK_RECHERCHE
    SUJET -> 'je' | 'nous' | 't' 'on' | 'j'
    VERBE -> 'chercher' | 'sont' | 'afficher' | 'veux' | 'voudrais' | 'cherche' | 'souhaiter' | 'souhaitons' | 'souhaite' | 'donner' | 'trouve' | 'aimerais' | 'souhaitons' | 'rechercher' | 'liste'
    QUESTION -> 'quels' | 'dans' 'quels' | 'dans' 'quelles' | 'quelles'
    UNK_RECHERCHE ->  ART | RUB
    ART -> 'les' 'articles' | 'articles' | 'des' 'articles' | 'les' 'recherches' | 'un' 'article' | 'les' 'bulletins'
    RUB -> 'les' 'rubriques' | 'rubriques' | 'des' 'rubriques' | 'les' 'rubriques' 'des' 'articles'  
    OBJET -> ART


    CDTS -> CDT ET CDTS | CDT OU CDTS | CDT CDTS | CDT | CDT ETNON CDTS | PREET CDT ET CDTS | PREOU CDT OU CDTS
    CDT -> TITRE | DATE | RUBRIQUE | IMAGE | THEME | MOT | SUB
    OPTRECHERCHE -> 'avoir' | 'tous' | 'avoir tous' | 'la' 'liste' | 'obtenir' | 'voir'

    RUBRIQUE -> TERMRUBRIQUE UNK_RUBRIQUE
    TERMRUBRIQUE -> 'dans' 'la' 'rubrique' | 'de' 'la' 'rubrique' | 'provenant' 'de' 'la' 'rubrique'  | 'dont' 'la' 'rubrique' 'est' |'qui' 'ont' 'pour' 'rubrique'
    UNK_RUBRIQUE -> _rubrique_ | """
        + str_rubriques
        + """

    TITRE -> TERMTITRE THEME_MOT | THEME_MOT POSTTITRE 
    THEME_MOT -> THEME | MOT
    TERMTITRE -> 'dont' 'le' 'titre'
    POSTTITRE -> 'dans' 'le' 'titre'


    MOT -> PREMOT UNK_MOT | UNK_MOT POSTMOT
    PREMOT -> VERBEMOT 'le' 'mot' | VERBEMOT
    VERBEMOT ->  PRENEG NEGVBMOT POSTNEG | VBMOT
    NEGVBMOT -> TERMMOT
    VBMOT -> LEMOTTERMMOT
    LEMOTTERMMOT -> QUIMOT LEMOT | QUIMOT 
    QUIMOT -> 'qui' TERMMOT | TERMMOT
    TERMMOT -> 'contient' | 'contient' | 'possédant' | 'contenant' | 'contiennent'
    LEMOT -> 'le' 'mot' | 'les' 'mots'
    POSTMOT ->  'est' 'cité' | 'est' 'il' 'cité' | 'est' 'elle' 'citée' 
    UNK_MOT -> BIMOT
    

    PRENEG -> 'ne'
    POSTNEG -> 'pas'

    THEME -> VBTHEME UNK_THEME 
    VBTHEME -> 'qui' ISNEGTHEME | ISNEGTHEME | ISNEGTHEME PRE | 'qui' ISNEGTHEME PRE
    PRE -> PREET | PREOU
    ISNEGTHEME ->  PRENEG NEGVBTHEME POSTNEG | VBTH
    NEGVBTHEME -> TERMTHEME
    VBTH -> TERMTHEME
    TERMTHEME -> 'évoquent' | 'parlent' | 'traitent' | 'évoquant' | 'parlant' | 'traitant' | 'portant' | 'portent' | 'liés' | 'sur' | 'traite' | 'parle' | 'à' 'propos' | 'évoque' | 'impliquant' | 'liés' 'à'
    UNK_THEME -> BIMOT
    BIMOT -> PREPNOM BIMOT | PREPNOM
    PREPNOM -> 'sur' PREP NOM | 'sur' NOM | NOM | PREP NOM
    PREP -> 'le' | 'la' | 'les' | 'du' | 'des' | 'd' | 'de' 'la' | 'de' | 'l' | 'de' 'l' | 'en'
    
    

    NOM -> """
        + str_glossaire
        + """
    ET -> 'et' 
    PREET -> 'à' 'la' 'fois'
    OU -> 'ou' | 'soit'
    PREOU ->  'soit'
    ETNON -> 'mais' 'pas' | 'et' 'pas' | 'ni' | 'mais'

    DATE -> TERMDATE CDTDATE | CDTDATE 
    TERMDATE -> 'publiés' | 'parus' | 'écrits' | 'qui' 'date' | 'ont' 'été' 'publiés' | 'qui' 'sont' 'écrits'
    CDTDATE -> 'd' 'après' APRES | 'après' APRES | 'avant' AVANT | 'entre' AVANT 'et' APRES | 'de' PILE | 'en' PILE | 'au' PILE | 'du' PILE | 'à' 'partir' 'de' APRES
    AVANT -> FDATE
    APRES -> FDATE
    PILE -> FDATE
    FDATE -> '_date_'

    IMAGE -> PREIMAGE | IMG
    IMG -> 'image' | 'des' 'images'
    PREIMAGE -> 'avec'

    SUB -> BIMOT

    """
    )

    return ChartParser(grammar)


def is_parsable(grammar, tokens):
    try:
        trees = list(grammar.parse(tokens))
        if not trees:
            return False
        else:
            return True
    except:
        return True


def make_tree(grammar, tokens):
    return list(grammar.parse(tokens))


# tokens = "quels être les article paraître entre le 3 mars 2013 et le 4 mai 2013 évoquer les etats unis ".split()
# print(tokens)
# trees = list(parser.parse(tokens))
# if not trees:
#     print("❌ No parse found. Check token sequence.")
# else:
#     for tree in trees:
#         tree.pretty_print()


#    """
# R -> RECHERCHE CDTS
# RECHERCHE -> SUJET VERBE UNK_RECHERCHE | SUJET VERBE OPTRECHERCHE UNK_RECHERCHE | QUESTION VERBE UNK_RECHERCHE | QUESTION UNK_RECHERCHE VERBE | VERBE UNK_RECHERCHE | UNK_RECHERCHE | QUESTION UNK_RECHERCHE VERBE SUJET | OPTRECHERCHE UNK_RECHERCHE | VERBE OPTRECHERCHE UNK_RECHERCHE | QUESTION UNK_RECHERCHE | QUESTION UNK_RECHERCHE VERBE SUJET OBJET | OPTRECHERCHE UNK_RECHERCHE
# SUJET -> 'je' | 'nous' | 't' 'on' | 'j'
# VERBE -> 'chercher' | 'sont' | 'afficher' | 'veux' | 'voudrais' | 'cherche' | 'souhaiter' | 'souhaitons' | 'souhaite' | 'donner' | 'trouve' | 'aimerais' | 'souhaitons' | 'rechercher' | 'liste'
# QUESTION -> 'quels' | 'dans' 'quels' | 'dans' 'quelles' | 'quelles'
# UNK_RECHERCHE ->  ART | RUB
# ART -> 'les' 'articles' | 'articles' | 'des' 'articles' | 'les' 'recherches' | 'un' 'article' | 'les' 'bulletins'
# RUB -> 'les' 'rubriques' | 'rubriques' | 'des' 'rubriques' | 'les' 'rubriques' 'des' 'articles'
# OBJET -> ART


# CDTS -> CDT ET CDTS | CDT OU CDTS | CDT CDTS | CDT | CDT ETNON CDTS
# CDT -> TITRE | DATE | RUBRIQUE | IMAGE | THEME | MOT
# OPTRECHERCHE -> 'avoir' | 'tous' | 'avoir tous' | 'la' 'liste' | 'obtenir' | 'voir'

# RUBRIQUE -> TERMRUBRIQUE COOR_RUBRIQUE
# TERMRUBRIQUE -> 'dans' 'la' 'rubrique' | 'de' 'la' 'rubrique' | 'provenant' 'de' 'la' 'rubrique'  | 'dont' 'la' 'rubrique' 'est' |'qui' 'ont' 'pour' 'rubrique'
# COOR_RUBRIQUE -> UNK_RUBRIQUE ET COOR_RUBRIQUE | UNK_RUBRIQUE OU COOR_RUBRIQUE | UNK_RUBRIQUE ETNON COOR_RUBRIQUE | UNK_RUBRIQUE | OU UNK_RUBRIQUE OU COOR_RUBRIQUE | ET UNK_RUBRIQUE ET COOR_RUBRIQUE
# UNK_RUBRIQUE -> _rubrique_ | """
#     + str_rubriques
#     + """

# TITRE -> TERMTITRE THEME_MOT | THEME_MOT POSTTITRE
# THEME_MOT -> THEME | MOT
# TERMTITRE -> 'dont' 'le' 'titre'
# POSTTITRE -> 'dans' 'le' 'titre'


# MOT -> PREMOT MOTS | MOTS POSTMOT
# PREMOT -> VERBEMOT 'le' 'mot' | VERBEMOT
# VERBEMOT ->  PRENEG NEGVBMOT POSTNEG | VBMOT
# NEGVBMOT -> TERMMOT
# VBMOT -> LEMOTTERMMOT
# LEMOTTERMMOT -> QUIMOT LEMOT | QUIMOT
# QUIMOT -> 'qui' TERMMOT | TERMMOT
# TERMMOT -> 'contient' | 'contient' | 'possédant' | 'contenant' | 'contiennent'
# LEMOT -> 'le' 'mot' | 'les' 'mots'
# POSTMOT ->  'est' 'cité' | 'est' 'il' 'cité' | 'est' 'elle' 'citée'
# MOTS -> UNK_MOT ET MOTS | UNK_MOT OU MOTS | UNK_MOT ETNON MOTS | UNK_MOT | OU UNK_MOT OU MOTS | ET UNK_MOT ET MOTS
# UNK_MOT -> BIMOT


# PRENEG -> 'ne'
# POSTNEG -> 'pas'

# THEME -> VBTHEME THEMES
# ISNEGTHEME ->  PRENEG NEGVBTHEME POSTNEG | VBTH
# NEGVBTHEME -> TERMTHEME
# VBTH -> TERMTHEME
# VBTHEME -> 'qui' ISNEGTHEME | ISNEGTHEME
# TERMTHEME -> 'évoquent' | 'parlent' | 'traitent' | 'évoquant' | 'parlant' | 'traitant' | 'portant' | 'portent' | 'liés' | 'sur' | 'traite' | 'parle' | 'à' 'propos' | 'évoque' | 'impliquant'
# THEMES -> UNK_THEME ET THEMES | UNK_THEME OU THEMES | UNK_THEME ETNON THEMES | UNK_THEME | OU UNK_THEME OU THEMES | ET UNK_THEME ET THEMES
# UNK_THEME -> BIMOT
# BIMOT -> PREPNOM BIMOT | PREPNOM
# PREPNOM -> 'sur' PREP NOM | 'sur' NOM | NOM | PREP NOM
# PREP -> 'le' | 'la' | 'les' | 'du' | 'des' | 'd' | 'de' 'la' | 'de' | 'l'


# NOM -> """
#     + str_glossaire
#     + """
# ET -> 'et' | 'à' 'la' 'fois'
# OU -> 'ou' | 'soit'
# ETNON -> 'mais' 'pas' | 'et' 'pas' | 'ni' | 'mais'

# DATE -> TERMDATE COOR_DATE | COOR_DATE
# COOR_DATE -> CDTDATE ET COOR_DATE | CDTDATE OU COOR_DATE | CDTDATE ETNON COOR_DATE | CDTDATE | OU CDTDATE OU COOR_DATE | ET CDTDATE ET COOR_DATE
# TERMDATE -> 'publiés' | 'parus' | 'écrits' | 'qui' 'date' | 'ont' 'été' 'publiés' | 'qui' 'sont' 'écrits'
# CDTDATE -> 'd' 'après' APRES | 'après' APRES | 'avant' AVANT | 'entre' AVANT 'et' APRES | 'de' PILE | 'en' PILE | 'au' PILE | 'du' PILE | 'à' 'partir' 'de' APRES
# AVANT -> FDATE
# APRES -> FDATE
# PILE -> FDATE
# FDATE -> '_date_'

# IMAGE -> PREIMAGE | IMG
# IMG -> 'image' | 'des' 'images'
# PREIMAGE -> 'avec'

# """
# )
