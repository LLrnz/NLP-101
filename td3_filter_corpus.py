from TD3.conclu_filter_corpus_without_stop_words import (
    make_stop_word_dictionnary,
    reform_corpus,
    remove_stop_word,
)
from TD3.q1_1_segmente import read_corpus, segment_corpus
from utils.file_handling import write_on_output_file
import utils.paths as path


reform_corpus(
    remove_stop_word(
        segment_corpus(read_corpus("output/corpus.xml")),
        make_stop_word_dictionnary("output/tf_idf.csv", 1.2),
    ),
    path.XML_FILTERED_CORPUS,
)
