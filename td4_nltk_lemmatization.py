import csv
from TD3.q1_1_segmente import read_corpus, segment_corpus
from utils.file_handling import write_on_output_file
import utils.paths as path
from TD4.q1_2_get_stemmed_word import init_stemmer, get_stems

# Lecture et segmentation du corpus XML
tokenized_corpus = segment_corpus(read_corpus(path.XML_FILTERED_CORPUS))

# Initialisation du stemmer
stemmer = init_stemmer()

# Extraction des stems (racines)
stems_dict = get_stems(tokenized_corpus, stemmer)

# Sauvegarde dans un fichier CSV
with open(path.NLTK_LEMMAS, mode="w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerow(["mot", "racine"])
    for mot, racine in stems_dict.items():
        writer.writerow([mot, racine])

print(f"Fichier lémentisé NLTK généré : {path.NLTK_LEMMAS}")