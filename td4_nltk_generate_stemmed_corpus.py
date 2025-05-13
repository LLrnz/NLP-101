from TD3.q1_1_segmente import read_corpus, segment_corpus
from TD3.q1_2_substitue import substitue_corpus
from TD3.conclu_filter_corpus_without_stop_words import reform_corpus
from utils.file_handling import write_on_output_file
import utils.paths as path
from TD4.q1_2_get_stemmed_word import init_stemmer, get_stems

# Lecture et segmentation du corpus
tokenized_corpus = segment_corpus(read_corpus(path.XML_FILTERED_CORPUS))

# Initialisation du stemmer
stemmer = init_stemmer()

# Dictionnaire mot → racine
stems_dict = get_stems(tokenized_corpus, stemmer)

# Substitution des mots dans le corpus
substitue_corpus(stems_dict, tokenized_corpus)

# Réécriture du corpus modifié dans un nouveau fichier XML
reform_corpus(tokenized_corpus, path.NLTK_LEMMATIZED_CORPUS)
