from incidence_matrix import make_incidence_matrix, make_inverted_index
from text_normalizer import docs_to_corpus, normalize_docs


DOCS = [
    "Un corbeau tient un fromage dans son bec. Un renard rusé le flatte pour le tromper et lui faire lâcher son repas.",
    "Un renard et un bouc tombent dans un puits. Le renard parvient à tromper le bouc pour s’en sortir, puis l’abandonne au fond.",
    "Un loup cherche un prétexte pour faire de l’agneau innocent son repas.",
    "Un renard invite une cigogne à dîner mais lui sert un repas inadapté ; la cigogne se venge de la même manière.",
    "Un loup se déguise en berger pour tromper les moutons, mais il est vite démasqué et puni.",
]


def test_make_indicende_matrix():

    words = [
        "corbeau",
        "renard",
        "cigogne",
        "bouc",
        "loup",
        "berger",
        "fromage",
        "repas",
        "tromper",
    ]

    expected_matrix = [
        [1, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0],
        [1, 0, 1, 1, 0],
        [1, 1, 0, 0, 1],
    ]

    docs = normalize_docs(DOCS)

    assert make_incidence_matrix(docs, words) == expected_matrix


def test_make_inverted_index():
    corpus = docs_to_corpus(DOCS)

    make_inverted_index(corpus)

    expected_inverted_index = {
        "au": [2],
        "bec": [1],
        "berger": [5],
        "bouc": [2],
        "cherche": [3],
        "cigogne": [4],
        "corbeau": [1],
        "dans": [1, 2],
        "de": [3, 4],
        "déguise": [5],
        "démasqué": [5],
        "dîner": [4],
        "en": [2, 5],
        "est": [5],
        "et": [1, 2],
        "faire": [1, 3],
        "flatte": [1],
        "fond": [2],
        "fromage": [1],
        "il": [5],
        "inadapté": [4],
        "innocent": [3],
        "invite": [4],
        "la": [4],
        "le": [1, 2],
        "les": [5],
        "loup": [3, 5],
        "lui": [1, 4],
        "lâcher": [1],
        "l'abandonne": [2],
        "l'agneau": [3],
        "mais": [4, 5],
        "manière": [4],
        "moutons": [5],
        "même": [4],
        "parvient": [2],
        "pour": [2, 3, 5],
        "prétexte": [3],
        "puis": [2],
        "puits": [2],
        "puni": [5],
        "renard": [1, 2, 4],
        "repas": [1, 3, 4],
        "rusé": [1],
        "se": [4, 5],
        "sert": [4],
        "son": [1, 3],
        "sortir": [2],
        "s'en": [2],
        "tient": [1],
        "tombent": [2],
        "tromper": [1, 2, 5],
        "un": [1, 2, 3, 4, 5],
        "une": [4],
        "venge": [4],
        "vite": [5],
        "à": [2, 4],
    }

    assert make_inverted_index(corpus)
