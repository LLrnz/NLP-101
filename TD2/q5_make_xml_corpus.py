from TD2.q5_write_xml import generateXml
from TD2.q5_genrate_corpus_data import generate_corpus_data
import utils.paths as path

"""Q5. Prends les données scrappées sort un XML du coprus structuré"""


def make_corpus(bulletinsDir: str, outputFile: str):
    corpuses = generate_corpus_data(bulletinsDir)
    generateXml(corpuses, outputFile)


# création du fichier corpus
make_corpus(path.BULLETINS, path.XML_CORPUS)
