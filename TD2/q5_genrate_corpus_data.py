from TD2.q3_html_scrapper import (
    extract_author,
    extract_contact,
    extract_id_text_title_and_section,
    extract_number_and_date,
    parseAllHTML,
)
import utils.corpus_types as type


# TODO formaliser type de sortie
def generate_corpus_data(bulletinDir: str) -> type.corpus:
    bulletins = parseAllHTML(bulletinDir)
    corpus = []

    for b in bulletins.values():
        bulletinData = {}
        id, images, text, title, section = extract_id_text_title_and_section(b)
        author = extract_author(b)
        contact = extract_contact(b)
        num, date = extract_number_and_date(b)

        bulletinData["fichier"] = id
        bulletinData["numero"] = num
        bulletinData["date"] = date
        bulletinData["rubrique"] = section
        bulletinData["titre"] = title
        bulletinData["auteur"] = author
        bulletinData["texte"] = text

        imagedict = {}
        for i in images:
            imagedict[i[0]] = i[1]

        bulletinData["images"] = imagedict
        bulletinData["contact"] = contact

        corpus.append(bulletinData)

    return corpus
