from datetime import date
from TD3.q1_1_segmente import read_corpus, segment_corpus
from TD7.make_invert_indexes import (
    make_category_tokenised_II,
    make_date_II,
    querry_bimot_II,
    query_date_II,
)


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
