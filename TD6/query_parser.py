# import nltk


from datetime import date, datetime
from typing import List
from TD3.q1_1_segmente import clean_text, split_text
from TD6.date_finder import find_begin_end, replace_dates
from TD6.grammar_test import make_tree
from utils.corpus_types import ACTION, LOGIC
from nltk.tree import Tree


def parse_query(grammar, str):
    query = clean_text(str)
    query, dates = replace_dates(query)
    query = split_text(query)
    tree = make_tree(grammar, query)
    dates.reverse()
    res = translate_grammar_tree(tree[0], dates)

    return res


def translate_grammar_tree(tree: Tree, reversed_date_list):
    logic_chain = []
    base_action = None
    last_action = None
    first_condition = True

    def extract_bimot_terms(node: Tree) -> list[str]:
        terms = []
        for subtree in node.subtrees():
            if subtree.label() == "BIMOT":
                for subsub in subtree.subtrees():
                    if subsub.label() == "NOM":
                        terms.append(subsub[0])
        return terms

    def extract_terminals(tree: Tree, labels: list[str]) -> list[str]:
        terms = []
        for subtree in tree.subtrees():
            if subtree.label() in labels:
                terms.extend(subtree.leaves())
        return terms

    def recursive_parse(node: Tree, date_list: List[date]):
        nonlocal base_action, last_action, first_condition

        if node.label() == "RECHERCHE":
            base_action = ACTION.THEME
            last_action = base_action

        elif node.label() == "THEME":
            terms = extract_bimot_terms(node)
            if terms:
                logic_type = LOGIC.BASE if first_condition else LOGIC.AND
                logic_chain.append((logic_type, (ACTION.THEME, *terms)))
                first_condition = False
                last_action = ACTION.THEME

        elif node.label() == "TITRE":
            terms = extract_bimot_terms(node)
            if terms:
                logic_type = LOGIC.BASE if first_condition else LOGIC.AND
                logic_chain.append((logic_type, (ACTION.TITLE, *terms)))
                first_condition = False
                last_action = ACTION.TITLE

        elif node.label() == "MOT":
            terms = extract_bimot_terms(node)
            if terms:
                logic_type = LOGIC.BASE if first_condition else LOGIC.AND
                logic_chain.append((logic_type, (ACTION.EXACT_WORD, *terms)))
                first_condition = False
                last_action = ACTION.EXACT_WORD

        elif node.label() == "RUBRIQUE":
            terms = extract_terminals(node, ["_rubrique_"])
            if terms:
                logic_type = LOGIC.BASE if first_condition else LOGIC.AND
                logic_chain.append((logic_type, (ACTION.SECTION, *terms)))
                first_condition = False
                last_action = ACTION.SECTION

        elif node.label() == "DATE":
            for subtree in node.subtrees():
                if subtree.label() in {"AVANT", "APRES", "PILE"}:
                    date = subtree.leaves()[0]
                    action_type = {
                        "AVANT": ACTION.AVANT,
                        "APRES": ACTION.APRES,
                        "PILE": ACTION.PILE,
                    }[subtree.label()]
                    logic_type = LOGIC.BASE if first_condition else LOGIC.AND

                    if action_type == ACTION.PILE:
                        begin, end = find_begin_end(date_list.pop())
                        logic_chain.append((logic_type, (ACTION.AVANT, end)))
                        logic_chain.append((logic_type, (ACTION.APRES, begin)))

                    else:
                        logic_chain.append(
                            (
                                logic_type,
                                (
                                    action_type,
                                    datetime.strptime(date_list.pop(), "dd/mm/YYYY"),
                                ),
                            )
                        )
                    first_condition = False
                    last_action = action_type

        elif node.label() == "IMAGE":
            logic_type = LOGIC.BASE if first_condition else LOGIC.AND
            logic_chain.append((logic_type, (ACTION.HAS_IMAGE,)))
            first_condition = False
            last_action = ACTION.HAS_IMAGE

        elif node.label() == "SUB":
            terms = extract_bimot_terms(node)
            if terms and last_action:
                logic_chain.append((LOGIC.AND, (last_action, *terms)))

        elif node.label() == "CDTS":
            for child in node:
                recursive_parse(child, date_list)

        elif node.label() == "CDT":
            for child in node:
                recursive_parse(child, date_list)

        else:
            for child in node:
                if isinstance(child, Tree):
                    recursive_parse(child, date_list)

    recursive_parse(tree, reversed_date_list)
    return logic_chain
