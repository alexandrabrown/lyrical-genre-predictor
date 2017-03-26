import sys
import vectorization


def main():
    
    """
    Usage: python3 main.py <naive_bayes><svm> <tfidf>
    TODO: allow lyrics to be read from an optional filename
    """

    classifier_opts = sys.argv[1]
    vect_opts = sys.argv[2]
    predicted_test_categories, test_truth = classify_songs(classifier_opts, vect_opts)
    evaluation(predicted_test_categories, test_truth)


def classify_songs(classifier_opts, vect_opts):

    """
    Load the IDs
    """
    categories = ["Rock", "Pop", "Country", "Blues", "Jazz", "Rap"]
    
    train_truth = []
    test_truth = []

    train_IDs = []
    test_IDs = []

    with open("msd_tagtraum_cd2c.cls") as f:
        i = 0
        for line in f:
            track, category = line.split()
            if category not in categories:
                continue
            if i < 100:
                train_truth.append(category)
                train_ID.append(track)
            elif i < 125:
                test_truth.append(category)
                test_ID.append(track)
            else:
                break
            i += 1

    # vectorize train and test
    train_matrix, test_matrix = vectorization.vectorize(train_IDs, test_IDs,
                                                        vect_opts)
    
    # classify based on classifier_opts
    if classifier_opts == "naive_bayes":
        predicted_test_categories = naive_bayes_classifier(train_matrix,
                                                           test_matrix,
                                                           train_truth)
    elif classifier_opts == "svm":
        pass

    else:
        print("Unrecognized classification")
        sys.exit(1)

    return predicted_test_categories, test_truth


def evaluation(predicted_test_categories, test_truth):
    pass


if __name__ == "__main__":
    main()
