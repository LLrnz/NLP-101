from TD3.q1_1_segmente import read_corpus, segment_corpus, tokens_to_file
import utils.file_handling as file
import utils.paths as path

# fichier de sortie : tokens.csv
file.write_on_output_file(
    tokens_to_file(segment_corpus(read_corpus(path.XML_CORPUS))), path.TOKENS
)
