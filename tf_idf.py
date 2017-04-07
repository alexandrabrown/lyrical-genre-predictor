import sys
from sklearn.feature_extraction.text import TfidfVectorizer


def tf_idf_vectorize(train_lyrics, test_lyrics, option):
    """
    TF-IDF vectorizer
<<<<<<< HEAD
    Input: two lists of strings and one option
    Output: If "dense" is set, two dense matrices (training and testing)
=======
    Input: two lists of strings
    Output: If "dense" is set, two dense tf-idf matrices (training and testing)
>>>>>>> 6c5fb85edd7027d913ad8e7b0eec293aa8655805
            If "sparse" is set, one sparse matrix, 
            the length of training, and the length of testing
    Example: tf_idf_vectorize(train_lyrics, test_lyrics, "sparse")
             tf_idf_vectorize(train_lyrics, test_lyrics, "dense")
    """
    corpus = train_lyrics + test_lyrics
    
    vectorizer = TfidfVectorizer(min_df=1)
<<<<<<< HEAD
=======
    vectorizer.fit_transform(corpus)
>>>>>>> 6c5fb85edd7027d913ad8e7b0eec293aa8655805

    if option == "dense":
        dmatrix = vectorizer.fit_transform(corpus).toarray()
        assert(len(dmatrix) == len(train_lyrics) + len(test_lyrics))
        return dmatrix[:len(train_lyrics)], dmatrix[-len(test_lyrics):]
    elif option == "sparse":
        return vectorizer.fit_transform(corpus), len(train_lyrics), len(test_lyrics)
    else:
<<<<<<< HEAD
        print ("Invalid option!")
        print("Error! USAGE: " + usage_string)
        sys.exit(1)

=======
        print ("Invalid option.\nCheck usage.\n")

# def main():
#    print (tf_idf_vectorize([], []))

if __name__ == '__main__':
    sys.exit(int(main() or 0))
>>>>>>> 6c5fb85edd7027d913ad8e7b0eec293aa8655805


