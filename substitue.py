def substitute_words(dictionary, text):

    for key, value in dictionary.items():
        text = text.replace(key, value)
    return text
