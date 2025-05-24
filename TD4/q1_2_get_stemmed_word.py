from typing import Dict
import utils.corpus_types as type
from nltk.stem.snowball import SnowballStemmer


def init_stemmer() -> SnowballStemmer:
    return SnowballStemmer("french")


def get_stems(
    corpus: type.TokenizedCorpus, stemmer: SnowballStemmer
) -> Dict[str, str]:
    res = {}
    for bulletin in corpus:
        for _, tokenList in bulletin.items():
            for token in tokenList:
                # Vérification que le token est une chaîne de caractères alphabétiques
                if token.isalpha():
                    res[token] = stemmer.stem(token)
    return res
