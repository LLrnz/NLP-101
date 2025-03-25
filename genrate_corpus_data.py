from html_scrapper import (
    extract_author,
    extract_contact,
    extract_id_text_title_and_section,
    extract_number_and_date,
    parseAllHTML,
)


def generate_corpus_data(bulletinDir: str):
    bulletins = parseAllHTML(bulletinDir)
    corpus = []

    for b in bulletins.values():
        bulletinData = {}
        id, images, text, title, section = extract_id_text_title_and_section(b)
        author = extract_author(b)
        contact = extract_contact(b)
        num, date = extract_number_and_date(b)

        bulletinData["nameDoc"] = id
        bulletinData["numberBulletin"] = num
        bulletinData["dateBulletin"] = date
        bulletinData["rubriqueDoc"] = section
        bulletinData["TitleDoc"] = title
        bulletinData["autorDoc"] = author
        bulletinData["textDoc"] = text

        imagedict = {}
        for i in images:
            imagedict[i[0]] = i[1]

        bulletinData["imageDoc"] = imagedict
        bulletinData["contactDoc"] = contact

        corpus.append(bulletinData)

    return corpus
