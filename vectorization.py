import tf_idf
import count_vec
import binary_vec
import lsa
import database
import sys
from main import usage_string

def vectorization(train_lyrics, test_lyrics, vect_opts, output_matrix="dense"):

    if vect_opts == "tf_idf":
        return tf_idf.tf_idf_vectorize(train_lyrics, test_lyrics, output_matrix)
    elif vect_opts == "count":
        return count_vec.count_vectorize(train_lyrics, test_lyrics, output_matrix)
    elif vect_opts == "binary":
        return binary_vec.binary_vectorize(train_lyrics, test_lyrics, output_matrix)
    elif vect_opts == "lsa":
        return lsa.lsa_vectorize(train_lyrics, test_lyrics, output_matrix)
    else:
        print("Unrecognized vectorization")
        print("Error! USAGE: " + usage_string)
        sys.exit(1)
