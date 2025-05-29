from datetime import date, datetime
import re


def replace_dates(text):
    mois = {
        "janvier": "01",
        "février": "02",
        "mars": "03",
        "avril": "04",
        "mai": "05",
        "juin": "06",
        "juillet": "07",
        "août": "08",
        "septembre": "09",
        "octobre": "10",
        "novembre": "11",
        "décembre": "12",
    }

    patterns = [
        (
            r"\b(\d{1,2})/(\d{1,2})/(\d{4})",
            lambda m: f"{int(m.group(1)):02d}/{int(m.group(2)):02d}/{m.group(3)}",
        ),
        (
            r"\b(?:mois d'|mois de )(\w+)\s+(\d{4})",
            lambda m: f"00/{mois.get(m.group(1).lower(), '00')}/{m.group(2)}",
        ),
        (r"\bl'année (\d{4})", lambda m: f"00/00/{m.group(1)}"),
        (
            r"\ble (\d{1,2}) (\w+)\s+(\d{4})",
            lambda m: f"{int(m.group(1)):02d}/{mois.get(m.group(2).lower(), '00')}/{m.group(3)}",
        ),
        (
            r"\b(?:mois de|mois d')(\w+)",
            lambda m: f"00/{mois.get(m.group(1).lower(), '00')}/0000",
        ),
        (
            r"\b (\d{4})",
            lambda m: f"00/00/{m.group(1)}",
        ),
    ]

    found_dates = []
    modified_text = text

    for pattern, fmt_func in patterns:

        def replacer(match):
            formatted = fmt_func(match)
            found_dates.append(formatted)
            return " _date_"

        modified_text = re.sub(pattern, replacer, modified_text)

    return modified_text, found_dates


def find_begin_end(pile: date):
    begin = date.min
    end = date.max
    if pile[3] == "0" and pile[4] == "0":
        begin = date(int(pile[6:10]), 1, 1)
        end = date(int(pile[6:10]), 12, 31)

    elif pile[0] == "0" and pile[1] == "0":
        begin = date(int(pile[6:10]), int(pile[3:5]), 1)
        end = date(int(pile[6:10]), int(pile[3:5]), 31)

    else:
        begin = pile
        end = pile

    return (begin, end)
