from sklearn.neighbors import NearestCentroid

def rocchio_classifier(train_matrix, test_matrix, train_categories):
    """
    Rocchio (Nearest Centroid) Classifier
    Input: two Matrices of vector representations of train/test lyrics,
        and a list of strings of categories for training data
    Output: list of predicted categories for test_lyrics
    """

    classifier = NearestCentroid()
    classifier.fit(train_matrix, train_categories)
    predicted = classifier.predict(test_matrix)

    return predicted
