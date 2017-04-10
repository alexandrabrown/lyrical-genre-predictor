import tf_idf
import count_vec
import binary_vec
import lsa
import database
import sys
from main import usage_string

<<<<<<< HEAD
def vectorization(train_IDs, test_IDs, vect_opts, output_matrix="dense"):
    train_lyrics = []
    test_lyrics = []
    train_lyrics = database.get_track_list(train_IDs)
    test_lyrics = database.get_track_list(test_IDs)
=======
def vectorization(train_lyrics, test_lyrics, vect_opts, output_matrix="dense"):
>>>>>>> 04d15b8f1a69f01f73570537f6d5b66a2e9af996

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
