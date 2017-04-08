from sklearn.naive_bayes import KNeighborsClassifier

def knn_classifier(train_matrix, test_matrix, train_categories, k=3):
    """
    K Nereast Neighbors Classifier
    Input: two Matrices of vector representations of train/test lyrics,
        a list of strings of categories for training data,
        and the value of k
    Output: list of predicted categories for test_lyrics
    """

    classifier = KNeighborsClassifier(n_neighbors=k)
    classifier.fit(train_matrix, train_categories)
    predicted = classifier.predict(test_matrix)

    return predicted
