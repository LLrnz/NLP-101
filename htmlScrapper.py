import re
from typing import Dict, List, Tuple
from bs4 import BeautifulSoup
import glob

NODATA = "NO_DATA"


def parseHTML(path: str) -> BeautifulSoup:
    HTMLFile = open(path, "r")
    index = HTMLFile.read()

    return BeautifulSoup(index, "lxml")


def parseAllHTML(folder_path: str) -> Dict[str, BeautifulSoup]:
    allHTML = glob.glob(folder_path + "/[0-9]*.htm")
    res = {}

    for html in allHTML:
        res[html] = parseHTML(html)

    return res


def extract_number_and_date(select: BeautifulSoup) -> Tuple[str, str]:

    # number and date are on the same table row (tr) as the cell containing "Origine : "
    # get the cell containing "Origine :"
    node = select.find("span", string="Origine :")
    num = NODATA
    date = NODATA

    # Going through the parents until the table data (td) tag is found
    if node is not None:
        data = node.find_parent()
        while data.name != "td":
            data = data.find_parent()

        # get the sibling node "td" which contains wanted data
        sib = data.findNextSibling()

        # extracting num and date from td text with regex
        num = re.search("[0-9]{0,4}", sib.text)[0]
        date = re.search("[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{4}", sib.text)[0]

    return (num, date)


def extract_id_text_title_and_section(
    select: BeautifulSoup,
) -> Tuple[str, str, str, str]:
    text = ""
    title = NODATA
    section = NODATA
    id = NODATA

    # text is define by having more than 20 words
    texts = select.find_all("span", string=re.compile("(\S+ ){10,}"))

    title = texts[0]

    # going through the parents until td contining all needed data is found
    if title is not None:
        data = title.find_parent()
        while data.name != "td":
            data = data.find_parent()

        section = data.contents[1].contents[0].text
        title = data.contents[1].contents[1].text

        id = data.contents[3].contents[1].text
        id = re.search("\d{5}", id).group(0)

        for c in data.contents[5].children:
            text += c.text

    return (id, text, title, section)


def extract_author(select: BeautifulSoup) -> str:

    # number and date are on the same table row (tr) as the cell containing "Origine : "
    # get the cell containing "Origine :"
    node = select.find("span", string="Rédacteur :")
    author = NODATA

    # Going through the parents until the table data (td) tag is found
    if node is not None:
        data = node.find_parent()
        while data.name != "td":
            data = data.find_parent()

        # get the sibling node "td" which contains wanted data
        sib = data.find_next_sibling()

        # extracting num and date from td text with regex
        author = re.search("- ([\w -]*) -", sib.text).group(1)

    return author


def extract_contact(select: BeautifulSoup) -> str:

    # number and date are on the same table row (tr) as the cell containing "Origine : "
    # get the cell containing "Origine :"
    node = select.find("span", string="Pour en savoir plus, contacts :")
    contact = NODATA

    # Going through the parents until the table data (td) tag is found
    if node is not None:
        data = node.find_parent()
        while data.name != "td":
            data = data.find_parent()

        # get the sibling node "td" which contains wanted data
        sib = data.find_next_sibling()
        contact = sib.text
        contact = re.sub(r"\n", "", contact)

    return contact
