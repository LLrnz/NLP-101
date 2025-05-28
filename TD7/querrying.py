from typing import Set
from TD3.conclu_filter_corpus_without_stop_words import remove_stop_word
from TD7.make_invert_indexes import (
    make_categories_tokenised_II,
    make_category_tokenised_II,
    make_date_II,
    make_image_II,
    make_section_II,
    querry_bimot_II,
    query_date_II,
    query_image_II,
    query_mot_II,
    query_section_II,
)
from utils.corpus_types import ACTION, LOGIC, II, DocID, Query, SubQuery


def generates_all_inverted_indexes(
    tokenised_corpus, stop_word_dict
) -> dict[ACTION, II]:
    res = {}
    filtered_corpus = remove_stop_word(tokenised_corpus, stop_word_dict)
    stemmed_corpus = []  # spacy corpus

    res[ACTION.THEME] = make_categories_tokenised_II(stemmed_corpus, ["theme", "tire"])
    res[ACTION.SECTION] = make_section_II(tokenised_corpus, "rubrique")
    res[ACTION.DATE] = make_date_II(tokenised_corpus)
    res[ACTION.TITLE] = make_category_tokenised_II(filtered_corpus, "titre")
    res[ACTION.EXACT_WORD] = make_category_tokenised_II(tokenised_corpus)
    res[ACTION.HAS_IMAGE] = make_image_II(tokenised_corpus)

    return res


def query_word(query: SubQuery, IIs) -> Set[DocID]:
    II = IIs[ACTION.EXACT_WORD]

    if len(SubQuery) >= 3:
        res = querry_bimot_II(query[1], query[2], II)
    else:
        res = query_mot_II(query[1], II)
    return res


def query_theme(query: SubQuery, IIs) -> Set[DocID]:
    II = IIs[ACTION.THEME]

    if len(SubQuery) >= 3:
        res = querry_bimot_II(query[1], query[2], II)
    else:
        res = query_mot_II(query[1], II)
    return res


def query_title(query: SubQuery, IIs) -> Set[DocID]:
    II = IIs[ACTION.TITLE]

    if len(SubQuery) >= 3:
        res = querry_bimot_II(query[1], query[2], II)
    else:
        res = query_mot_II(query[1], II)
    return res


def query_section(query: SubQuery, IIs) -> Set[DocID]:
    II = IIs[ACTION.SECTION]

    res = query_section_II(query[1], II)
    return res


def query_date_before(query: SubQuery, IIs) -> Set[DocID]:
    II = IIs[ACTION.DATE]

    res = query_date_II(II, date_sup=query[1])


def query_date_afer(query: SubQuery, IIs) -> Set[DocID]:
    II = IIs[ACTION.DATE]

    res = query_date_II(II, date_inf=query[1])
    return res


def query_image(query: SubQuery, IIs) -> Set[DocID]:
    II = IIs[ACTION.HAS_IMAGE]
    has_image = query[1]

    if query[1] is list:
        has_image = query[1][0]
    res = query_image_II(bool(has_image), II)
    return res


def execute_subquery(query: SubQuery, inverted_indexes) -> Set[DocID]:
    match query[0]:
        case ACTION.THEME:
            return query_theme(query, inverted_indexes)
        case ACTION.SECTION:
            return query_section(query, inverted_indexes)
        case ACTION.AVANT:
            return query_date_before(query, inverted_indexes)
        case ACTION.APRES:
            return query_date_afer(query, inverted_indexes)
        case ACTION.TITLE:
            return query_title(query, inverted_indexes)
        case ACTION.EXACT_WORD:
            return query_word(query, inverted_indexes)
        case ACTION.HAS_IMAGE:
            return query_image(query, inverted_indexes)


def execute_logic(
    all_docs: Set[DocID], operator: LOGIC, set1: Set[DocID], set2: Set[DocID] = None
) -> set[DocID]:
    match (operator):
        case LOGIC.AND:
            return set1.intersection(set2)
        case LOGIC.OR:
            return set1.union(set2)
        case LOGIC.BASE:
            return set1


def apply_querry(query: Query, inverted_indexes, doc_set) -> Set[DocID]:
    res = ()
    for q in query:
        docIDs = execute_subquery(q, inverted_indexes)
        res = execute_logic(doc_set, q[0], res, docIDs)
    return res
