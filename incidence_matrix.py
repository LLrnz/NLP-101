from indexation_types import docs, words, incidence_matrix, corpus, inverted_index
from text_normalizer import tokenize


def make_incidence_matrix(normalized_docs: docs, terms: words) -> incidence_matrix:
    im = [[0 for _ in range(len(normalized_docs))] for _ in range(len(terms))]
    for i, d in enumerate(normalized_docs):
        for j, w in enumerate(terms):
            if w in d:
                im[j][i] = 1
    return im


def make_inverted_index(corpus: corpus) -> inverted_index:
    inverted_index = {}
    indexed_tokens = []

    for i, d in corpus.items:
        for t in tokenize(d):
            indexed_tokens.append((t, i))

    indexed_tokens.sort(key=lambda tup: tup[0])

    for t, i in indexed_tokens:
        if t in inverted_index.keys:
            if i not in inverted_index[t]:
                inverted_index[t] = inverted_index[t].append(i)
        else:
            inverted_index[t] = i

    return inverted_index
