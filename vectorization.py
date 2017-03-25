import tf_idf
import load_from_db

def vectorization(train_ID, test_ID, vect_opts):
    train_lyrics = []
    test_lyrics = []
    for id in train_ID:
        train_lyrics.append(load_from_db.get_track(id))
    for id in test_ID:
        test_lyrics.append(load_from_db.get_track(id))


    if vect_opts == "tf_idf":
		return tf_idf.tf_idf_vectorize(train_lyrics, test_lyrics, "dense")
		
