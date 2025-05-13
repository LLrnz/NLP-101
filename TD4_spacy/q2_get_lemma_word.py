from typing import Dict
import utils.corpus_types as type
import spacy


def init_model(model: str) -> spacy.language:
    return spacy.load(model)


def get_lemmas(
    corpus: type.TokenizedCorpus, language: spacy.language
) -> Dict[str, str]:
    res = {}
    for bulletin in corpus:
        for _, tokenList in bulletin.items():
            for token in tokenList:
                doc = language(token)
                lemma = doc[0].lemma_
                res[token] = lemma

    return res


# def lemmatize(
#     corpus: type.TokenizedCorpus, language: spacy.language
# ) -> type.TokenizedCorpus:
#     res = []
#     for bulletin in corpus:
#         lemmatize_bulletin = {}
#         for category, tokenList in bulletin.items():
#             lemmas = language(tokenList)
#             lemmatize_bulletin[category] = lemmas

#     res.append(lemmatize_bulletin)
#     return res
