# sudo pip3 install -U scikit-learn
# sudo pip3 install -U scipy
# http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html
from sklearn.naive_bayes import MultinomialNB


def naive_bayes_classifier(train_matrix, test_matrix, train_categories):
    """
    Naive Bayes Classifier
    Input: two Matrices of vector representations of train/test lyrics,
        and a list of strings of categories for training data
    Output: list of predicted categories for test_lyrics
    """

    classifier = MultinomialNB().fit(train_matrix, train_categories)
    predicted = classifier.predict(test_matrix)

    return predicted
