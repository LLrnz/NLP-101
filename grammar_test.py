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

glossaire = []
for b in tokenized_corpus:
    for token in b["titre"]:
        glossaire.append(token)
    for token in b["texte"]:
        glossaire.append(token)

glossaire = set(glossaire)
str_glossaire = '"'
str_glossaire += '" | "'.join(glossaire)
str_glossaire += '"'


grammar = CFG.fromstring(
    """
R -> RECHERCHE CDTS
RECHERCHE -> SUJET VERBE UNK_RECHERCHE | QUESTION VERBE UNK_RECHERCHE | QUESTION UNK_RECHERCHE VERBE | VERBE UNK_RECHERCHE
SUJET -> 'je'
VERBE -> 'chercher' | 'être' | 'afficher' | 'vouloir'
QUESTION -> 'quels' | 'dans quels'
UNK_RECHERCHE -> 'les' 'article' | 'les' 'rubrique' | 'article' | 'rubrique'
CDTS -> CDT ET CDTS | CDT OU CDTS | CDT CDTS | CDT
CDT -> TITRE | DATE | RUBRIQUE | THEME | MOT

RUBRIQUE -> TERMRUBRIQUE UNK_RUBRIQUE
TERMRUBRIQUE -> 'dans' 'la' 'rubrique'
UNK_RUBRIQUE -> 'focus'

TITRE -> TERMTITRE THEME_MOT | THEME_MOT POSTTITRE 
THEME_MOT -> THEME | MOT
TERMTITRE -> 'dont' 'le' 'titre'
POSTTITRE -> 'dans' 'le' 'titre'


MOT -> PREMOT MOTS | MOTS POSTMOT
PREMOT -> VERBEMOT 'le' 'mot' | VERBEMOT
VERBEMOT ->  PRENEG NEGVBMOT POSTNEG | VBMOT
NEGVBMOT -> TERMMOT
VBMOT -> TERMMOT
TERMMOT -> 'contenir'
POSTMOT ->  'être' 'citer'
MOTS -> UNK_MOT ET MOTS | UNK_MOT OU MOTS | UNK_MOT ETNON MOTS | UNK_MOT
UNK_MOT -> BIMOT
BIMOT -> PREPNOM BIMOT | PREPNOM

PRENEG -> 'ne'
POSTNEG -> 'pas'

THEME -> TERMTHEME THEMES 
TERMTHEME -> 'évoquer' | 'qui' 'parler' | 'parler'
THEMES -> UNK_THEME ET THEMES | UNK_THEME OU THEMES | UNK_THEME ETNON THEMES | UNK_THEME
UNK_THEME -> BIMOT
PREPNOM -> 'de' 'le' NOM | 'de' 'la' NOM | 'de' NOM | 'du' NOM | 'd' NOM | NOM

NOM -> """
    + str_glossaire
    + """
ET -> 'et'
OU -> 'ou'
ETNON -> 'mais' 'pas' | 'et' 'pas' | 'ni'

DATE -> TERMDATE CDTDATE
TERMDATE -> 'publier'
CDTDATE -> 'après' APRES | 'avant' AVANT
APRES -> '2020'
AVANT -> '2021'

"""
)

parser = ChartParser(grammar)
tokens = "je vouloir les article qui parler d airbus ou du projet taxibot".split()
print(tokens)
trees = list(parser.parse(tokens))

if not trees:
    print("❌ No parse found. Check token sequence.")
else:
    for tree in trees:
        tree.pretty_print()
