from TD7.make_invert_indexes import make_image_II


def test_make_image_II():
    corpus = [
        {"fichier": 1, "images": {"url": "legende"}},
        {"fichier": 2, "images": {}},
    ]
    ii = make_image_II(corpus)
    assert len(ii[True]) == 1
