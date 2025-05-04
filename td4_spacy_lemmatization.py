from TD3.conclu_filter_corpus_without_stop_words import (
    make_stop_word_dictionnary,
    remove_stop_word,
)
from TD3.q1_1_segmente import read_corpus, segment_corpus
from utils.file_handling import write_on_output_file
import utils.paths as path
from TD4_spacy.q2_get_lemma_word import init_model, get_lemmas
import utils.paths as path

tokenized_corpus = segment_corpus(read_corpus(path.XML_FILTERED_CORPUS))
language = init_model("fr_core_news_sm")

write_on_output_file(str(get_lemmas(tokenized_corpus, language)), path.SPACY_LEMMAS)
