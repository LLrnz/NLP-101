from generate_xml import generateXml
from genrate_corpus_data import generate_corpus_data


def make_corpus(bulletinsDir: str, outputFile: str):
    corpuses = generate_corpus_data(bulletinsDir)
    generateXml(corpuses, outputFile)


make_corpus("res/BULLETINS", "output/test1.xml")
