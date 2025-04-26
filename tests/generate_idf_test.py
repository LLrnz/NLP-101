from TD3.q2_2_generate_idf import calculate_idf


def test_generate_idf():
    inputSet = (
        ("le", 1),
        ("est", 1),
        ("le", 2),
        ("est", 2),
        ("train", 1),
        ("passager", 2),
    )

    expected = "le 0.0000\nest 0.0000\ntrain 0.3010\npassager 0.3010\n"

    calculated = calculate_idf(inputSet)

    assert expected == calculated
