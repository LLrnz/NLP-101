from TD5.correcteur_orthographique import charger_lexique, saisir_phrase, traiter_phrase


def test_correcteur():
    lexique = charger_lexique("TD5/lexique.csv")
    phrase = "je mange une banane"
    mots, lemmes = traiter_phrase(phrase, lexique)

    expected = [
        "[je] (non trouvé)",
        "manger",
        "[une] (non trouvé)",
        "[banane] (non trouvé)",
    ]

    assert len(lemmes) == len(expected)
    assert all([a == b for a, b in zip(lemmes, expected)])


def test_correcteur_2():
    lexique = charger_lexique("TD5/lexique.csv")
    phrase = "c'eut été les étés"
    mots, lemmes = traiter_phrase(phrase, lexique)

    expected = [
        "[c] (non trouvé)",
        "[eut] (non trouvé)",
        "être",
        "[les] (non trouvé)",
        "été",
    ]

    assert len(lemmes) == len(expected)
    assert all([a == b for a, b in zip(lemmes, expected)])
