from datetime import date
from TD3.conclu_filter_corpus_without_stop_words import make_stop_word_dictionnary
from TD3.q1_1_segmente import read_corpus, segment_corpus
from TD7.make_invert_indexes import (
    make_category_tokenised_II,
    make_date_II,
    querry_bimot_II,
    query_date_II,
)
from TD7.querrying import apply_querry, generates_all_inverted_indexes, get_all_docs_set
from utils.corpus_types import ACTION, LOGIC


def test_query_date_ii():
    corpus = segment_corpus(read_corpus("output/corpus.xml"))
    date_ii = make_date_II(corpus)
    date_inf = date(2011, 4, 24)
    date_sup = date(2012, 4, 24)
    print(query_date_II(date_inf, date_sup, date_ii))


def test_query_bimot():
    corpus = [
        {"fichier": ["1"], "texte": ["j", "aime", "les", "spaghettis"]},
        {"fichier": ["2"], "texte": ["j", "aime", "les", "empanadas"]},
    ]

    II = make_category_tokenised_II(corpus, "texte")

    docs = querry_bimot_II("les", "empanadas", II)
    assert docs == ["2"]


def test_apply_query_title():
    corpus = segment_corpus(read_corpus("output/corpus.xml"))
    IIS = generates_all_inverted_indexes(
        corpus, make_stop_word_dictionnary("output/tf_idf.csv", 1.2)
    )
    all_docs = get_all_docs_set(corpus)

    query = [(LOGIC.BASE, (ACTION.TITLE, "photonics"))]
    res = apply_querry(query, IIS, all_docs)

    assert res == set(["75795"])


def test_apply_query_bimot():
    corpus = segment_corpus(read_corpus("output/corpus.xml"))
    IIS = generates_all_inverted_indexes(
        corpus, make_stop_word_dictionnary("output/tf_idf.csv", 1.2)
    )
    all_docs = get_all_docs_set(corpus)

    query = [(LOGIC.BASE, (ACTION.TITLE, "sondes", "acoustiques"))]
    res = apply_querry(query, IIS, all_docs)

    assert res == set(["75794"])


def test_apply_query_date():
    corpus = segment_corpus(read_corpus("output/corpus.xml"))
    IIS = generates_all_inverted_indexes(
        corpus, make_stop_word_dictionnary("output/tf_idf.csv", 1.2)
    )
    all_docs = get_all_docs_set(corpus)

    query = [
        (LOGIC.BASE, (ACTION.AVANT, date(2012, 12, 26))),
        (LOGIC.AND, (ACTION.APRES, date(2012, 1, 1))),
    ]
    res = apply_querry(query, IIS, all_docs)

    assert len(res) == 107


def test_apply_query_image():
    corpus = segment_corpus(read_corpus("output/corpus.xml"))
    IIS = generates_all_inverted_indexes(
        corpus, make_stop_word_dictionnary("output/tf_idf.csv", 1.2)
    )
    all_docs = get_all_docs_set(corpus)

    query = [(LOGIC.BASE, (ACTION.HAS_IMAGE, True))]
    res = apply_querry(query, IIS, all_docs)

    assert len(res) == 113


def test_apply_query_exact_word():
    corpus = segment_corpus(read_corpus("output/corpus.xml"))
    IIS = generates_all_inverted_indexes(
        corpus, make_stop_word_dictionnary("output/tf_idf.csv", 1.2)
    )
    all_docs = get_all_docs_set(corpus)

    query = [
        (LOGIC.BASE, (ACTION.EXACT_WORD, "savon")),
        (LOGIC.OR, (ACTION.EXACT_WORD, "rémi", "dangla")),
    ]
    res = apply_querry(query, IIS, all_docs)

    assert len(res) == 2
