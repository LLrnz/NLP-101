word = str
doc = str
doc_index = int

indexed_token = tuple[word, doc_index]

docs = list[doc]
words = list[word]

corpus = dict[doc_index, doc]

incidence_matrix = list[list[bool]]

inverted_index = dict[word, list[doc_index]]
