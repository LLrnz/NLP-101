from TD3.q2_1_tf_coefficient import coefficient_tf, write_coefficient_tf
import utils.paths as path

tf_counts = coefficient_tf(path.TOKENS)
write_coefficient_tf(tf_counts, path.ALL_TF)
