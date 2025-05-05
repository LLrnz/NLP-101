from TD3.q2_2_generate_idf import calculate_idf, read_word_docid_file
from utils.file_handling import write_on_output_file
import utils.paths as path

write_on_output_file(calculate_idf(read_word_docid_file(path.TOKENS)), path.ALL_IDF)
