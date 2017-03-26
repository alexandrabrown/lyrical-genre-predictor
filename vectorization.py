import tf_idf
import database

def vectorization(train_IDs, test_IDs, vect_opts):
    train_lyrics = []
    test_lyrics = []
    train_lyrics = database.get_track_list(train_IDs)
    test_lyrics = database.get_track_list(test_IDs)


    if vect_opts == "tf_idf":
		return tf_idf.tf_idf_vectorize(train_lyrics, test_lyrics, "dense")
		
