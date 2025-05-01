from TD3.q2_3_generate_tf_idf import write_to_file, generate_tf_idf, read_files
import utils.paths as path


write_to_file(
    generate_tf_idf(read_files(path.ALL_TF, path.ALL_IDF)),
    path.ALL_TF_IDF,
)
