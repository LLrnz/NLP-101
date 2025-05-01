from typing import List, Tuple
import TD3.q2_2_generate_idf as idf
import TD3.q2_1_tf_coefficient as tf

import utils.corpus_types as type
import utils.paths as path


def read_files(tf_file: str, idf_file: str) -> Tuple[type.IdfDict, type.FreqList]:
    idf_dict = idf.file_to_dict(idf_file)
    tf_list = tf.read_file(tf_file)

    return idf_dict, tf_list


def generate_tf_idf(
    parameters: Tuple[type.IdfDict, type.FreqList],
) -> List[type.TokenTfIdf]:
    idf_dict, tf_list = parameters
    res = []

    for term in tf_list:
        id_doc, word, freq = term
        tdIdfEntry = (id_doc, word, freq * idf_dict[word])
        res.append(tdIdfEntry)

    return res


def write_to_file(tfidf: List[type.TokenTfIdf], outputfile: str):
    with open(outputfile, "w", encoding="utf-8") as f:
        for term in tfidf:
            id_doc, word, tfifd = term
            f.write(f"{id_doc}\t{word}\t{tfifd}\n")


write_to_file(
    generate_tf_idf(read_files(path.ALL_TF, path.ALL_IDF)),
    path.ALL_TF_IDF,
)
