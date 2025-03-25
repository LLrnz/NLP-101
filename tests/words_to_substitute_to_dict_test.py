from unittest import TestCase

from word_substitute_to_dict import substitues_to_dict


def test_substitues_to_dict():
    expected_dict = {"le": "leee", "un": "hunhunhun", "est": "ne sera jamaaaais"}

    calculated_dict = substitues_to_dict("res/words_to_replace.csv")
    TestCase().assertDictEqual(expected_dict, calculated_dict)
