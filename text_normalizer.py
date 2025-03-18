import re
from indexation_types import docs, corpus, doc, words


def normalize_text(text: str) -> str:
    text = text.lower()
    "".join(e for e in text if (e.isalnum() or e == " "))
    return text


def normalize_docs(docs: docs) -> docs:
    for d in docs:
        d = normalize_text(d)
    return docs


def docs_to_corpus(docs: docs) -> corpus:
    c = {}
    for i, d in enumerate(docs):
        c[i] = d
    return c


def tokenize(doc: doc) -> words:
    normalize_text(doc)
    return doc.split(" ")
