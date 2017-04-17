import sys
from sklearn.feature_extraction.text import CountVectorizer

def binary_vectorize(train_lyrics, test_lyrics, option):
    """
    Binary vectorizer
    Input: two lists of strings and one option
    Output: If "dense" is set, two dense matrices (training and testing)
            If "sparse" is set, one sparse matrix, 
            the length of training, and the length of testing
    Example: tf_idf_vectorize(train_lyrics, test_lyrics, "sparse")
             tf_idf_vectorize(train_lyrics, test_lyrics, "dense")
    """
    corpus = train_lyrics + test_lyrics
    
    vectorizer = CountVectorizer(min_df=1, binary=True)

    if option == "dense":
        dmatrix = vectorizer.fit_transform(corpus).toarray()
        assert(len(dmatrix) == len(train_lyrics) + len(test_lyrics))
        return dmatrix[:len(train_lyrics)], dmatrix[-len(test_lyrics):]
    elif option == "sparse":
        return vectorizer.fit_transform(corpus), len(train_lyrics), len(test_lyrics)
    else:
        print ("Invalid option.\nCheck usage.\n")



