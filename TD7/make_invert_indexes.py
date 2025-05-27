from datetime import date
from typing import List, Set
from TD3.q1_1_segmente import segment_text
from utils.corpus_types import DateII, DocID, ImageII, TokenPositionII

AVANT = 0
APRES = 1
PILE = 2


def make_category_II(corpus, category) -> TokenPositionII:
    res = {}

    for bulletin in corpus:
        for i, token in enumerate(segment_text(bulletin[category])):
            res[token][bulletin["fichier"]].append(i)
    return res


def make_category_tokenised_II(tokenised_corpus, category) -> TokenPositionII:
    res = {}

    for bulletin in tokenised_corpus:
        for i, token in enumerate(bulletin[category]):
            if token not in res.keys():
                res[token] = {}
            if bulletin["fichier"][0] not in res[token].keys():
                res[token][bulletin["fichier"][0]] = []
            res[token][bulletin["fichier"][0]].append(i)
    return res


def querry_bimot_II(mot1, mot2, positionII) -> List[DocID]:
    # TODO check si mot dans le dict
    positions_mot1 = positionII[mot1]
    positions_mot2 = positionII[mot2]

    res = []

    for docid, positions in positions_mot1.items():
        if docid in positions_mot2.keys():
            # est ce qu'il y a mot1.position = mot2.position -1 ?
            for p1 in positions:
                for p2 in positions_mot2[docid]:
                    if p1 == p2 - 1:
                        res.append(docid)
    return res


def make_date_II(corpus) -> DateII:
    dict = {}
    for bulletin in corpus:
        j, m, a = bulletin["date"]
        date_str = date(int(a), int(m), int(j))
        if date_str not in dict.keys():
            dict[date_str] = []
        dict[date_str].append(bulletin["fichier"])

    res = []
    for date_str, docs in dict.items():

        # parsed_date = datetime.strptime(date, "%d/%m/%Y").date()
        res.append((date_str, docs))

    res.sort(key=lambda x: x[0])
    return res


def query_date_II(date_inf, date_sup, dateII) -> set[DocID]:
    indexes = [0, 0]
    bests = [dateII[0][0], dateII[-1][0]]

    for i, date_tup in enumerate(dateII):
        if date_tup[0] >= date_inf:
            if i > 0:
                indexes[0] = i
            else:
                indexes[0] = i
            break

    for i, date_tup in enumerate(reversed(dateII)):
        if date_tup[0] <= date_sup:
            indexes[1] = len(dateII) - i
            break

    res = []
    slice = dateII[indexes[0] : indexes[1]]
    for date, docs in slice:
        for doc in docs:
            res.append(doc[0])

    return res


def make_image_II(corpus) -> ImageII:
    res = {True: [], False: []}
    for bulletin in corpus:
        if bulletin["images"] != {}:
            res[True].append(bulletin["fichier"])
        else:
            res[False].append(bulletin["fichier"])

    return res


def query_image_II(has_image: bool, ii: ImageII) -> Set[DocID]:
    return set(ii[has_image])
