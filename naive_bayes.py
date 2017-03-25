# Import Library of Gaussian Naive Bayes model
# sudo pip3 install -U scikit-learn
# sudo pip3 install -U numpy
# sudo pip3 install -U scipy
# http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html
from sklearn.naive_bayes import MultinomialNB
from tf_idf import tf_idf_vectorize
import sys


def naive_bayes_classifier(train_lyrics, test_lyrics, matrix_option):
    """
    Naive Bayes Classifier
    Input: two lists of strings, and matrix "dense" or "spare" option
    Output: list of predicted categories for test_lyrics
    """

    # train_lyrics = ['how does a bastard orphan son of a whore',
    # 'there may be something there that wasnt there before',
    # 'dude bro man you got to make her understand',
    # 'hello its me i was wondering if after all this time you like to be',
    # 'just take those old records off the shelf']

    # train_categories = ['musical', 'musical', 'musical', 'rock', 'rock']

    # test_lyrics = ['hello shelf its me time', 'orphan dude bro']

    train_matrix, test_matrix = tf_idf_vectorize(train_lyrics, test_lyrics, matrix_option)

    print(train_matrix)
    print(test_matrix)

    classifier = MultinomialNB().fit(train_matrix, train_categories)
    predicted = classifier.predict(test_matrix)

    print(predicted)


if __name__ == '__main__':
    sys.exit(int(main() or 0))
