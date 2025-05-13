import re


def saisir_phrase():
    return input("Entrez une phrase : ")


# 2.a : Extraction des mots et conversion en minuscules


def extraire_mots(phrase):
    return re.findall(r"\b\w+\b", phrase.lower())


# 2.b : Charger le lexique et associer directement un mot à son lemme
def charger_lexique(nom_fichier):
    lexique = {}
    with open(nom_fichier, "r", encoding="utf-8") as f:
        for ligne in f:
            mot, lemme = ligne.strip().split()
            lexique[mot.lower()] = lemme.lower()
    return lexique


# 2.c : Recherche de mots par préfixe commun
def prefixe_commun(mot, lexique, min_prefixe=2):  # seuil configurable
    max_communes = 0
    candidats = []
    for mot_lexique in lexique:
        communes = 0
        for a, b in zip(mot, mot_lexique):
            if a == b:
                communes += 1
            else:
                break
        if communes >= min_prefixe:
            if communes > max_communes:
                max_communes = communes
                candidats = [mot_lexique]
            elif communes == max_communes:
                candidats.append(mot_lexique)
    return candidats


# 2.d : Usage de l’algorithme de Levenshtein pour départager les candidats
def levenshtein(a, b):
    if len(a) < len(b):
        return levenshtein(b, a)
    if len(b) == 0:
        return len(a)
    previous_row = list(range(len(b) + 1))
    for i, c1 in enumerate(a):
        current_row = [i + 1]
        for j, c2 in enumerate(b):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]


# Étape 2.e : Si aucun mot n’est trouvé, indiquer que le mot est inconnu
def corriger_mot(mot, lexique):
    candidats = prefixe_commun(mot, lexique, min_prefixe=2)  # ← seuil 2 lettres
    if not candidats:
        return f"[{mot}] (non trouvé)"
    meilleur = min(candidats, key=lambda x: levenshtein(mot, x))
    return lexique[meilleur]


# -------------------------------------------------------------
# Traitement global d’une phrase : application  des étapes 2.a à 2.e
# -------------------------------------------------------------
def traiter_phrase(phrase, lexique):
    mots = extraire_mots(phrase)  # 2.a
    lemmes = []
    for mot in mots:
        if mot in lexique:  # 2.b
            lemmes.append(lexique[mot])
        else:
            lemmes.append(corriger_mot(mot, lexique))  # 2.c → 2.d → 2.e
    return mots, lemmes
