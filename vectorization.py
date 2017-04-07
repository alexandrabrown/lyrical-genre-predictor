<<<<<<< HEAD
import tf_idf
import count_vec
import binary_vec
import database
import sys
from main import usage_string

def vectorization(train_IDs, test_IDs, vect_opts, output_matrix="dense"):
=======
import sys
import tf_idf
import database

def vectorization(train_IDs, test_IDs, vect_opts):
>>>>>>> 6c5fb85edd7027d913ad8e7b0eec293aa8655805
    train_lyrics = []
    test_lyrics = []
    train_lyrics = database.get_track_list(train_IDs)
    test_lyrics = database.get_track_list(test_IDs)

<<<<<<< HEAD
    if vect_opts == "tf_idf":
        return tf_idf.tf_idf_vectorize(train_lyrics, test_lyrics, output_matrix)
    elif vect_opts == "count":
        return count_vec.count_vectorize(train_lyrics, test_lyrics, output_matrix)
    elif vect_opts == "binary":
        return binary_vec.binary_vectorize(train_lyrics, test_lyrics, output_matrix)
    else:
        print("Unrecognized vectorization")
        print("Error! USAGE: " + usage_string)
=======

    if vect_opts == "tf_idf":
        return tf_idf.tf_idf_vectorize(train_lyrics, test_lyrics, "dense")
    else:
        print("Unrecognized vectorization")
>>>>>>> 6c5fb85edd7027d913ad8e7b0eec293aa8655805
        sys.exit(1)
