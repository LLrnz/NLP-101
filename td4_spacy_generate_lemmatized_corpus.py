from TD3.conclu_filter_corpus_without_stop_words import (
    make_stop_word_dictionnary,
    reform_corpus,
    remove_stop_word,
)
from TD3.q1_1_segmente import read_corpus, segment_corpus
from TD3.q1_2_substitue import substitue_corpus
from utils.file_handling import write_on_output_file
import utils.paths as path
from TD4_spacy.q2_get_lemma_word import init_model, get_lemmas
import utils.paths as path

tokenized_corpus = segment_corpus(read_corpus(path.XML_FILTERED_CORPUS))
language = init_model("fr_core_news_sm")

lemmas_dict = get_lemmas(tokenized_corpus, language)

substitue_corpus(lemmas_dict, tokenized_corpus)

reform_corpus(tokenized_corpus, path.SPACY_LEMMATIZED_CORPUS)
