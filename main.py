import sys
from vectorization import *
from naive_bayes import *
from svm import *
from NN.neural_network import *


def main():
    
    """
    Usage: python3 main.py <naive_bayes><svm> <tf_idf>
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
    categories = ["Pop", "Rock", "Country", "Blues", "Jazz", "Rap"]
    
    train_truth = []
    test_truth = []

    train_IDs = []
    test_IDs = []

    # Go thru the track list and set aside tracks for training and testing 
    with open("msd_tagtraum_cd2c.cls") as f:
        i = 0
        for line in f:
            try:
                track, category = line.strip().split(None, 1) # max split once
            except:
                print("Line error", line)
                exit(1)

            # Skip categories we are not considering
            if category not in categories:
                continue
            if i < 30000:
                #if category != 'Rock':
                train_truth.append(category)
                train_IDs.append(track)
            elif i < 32000:
                #if category != 'Rock':
                test_truth.append(category)
                test_IDs.append(track)
            else:
                break
            i += 1

    # vectorize train and test
    train_matrix, test_matrix = vectorization(train_IDs, test_IDs, vect_opts)
    
    # classify based on classifier_opts
    if classifier_opts == "naive_bayes":
        predicted_test_categories = naive_bayes_classifier(train_matrix,
                                                           test_matrix,
                                                           train_truth)
    elif classifier_opts == "svm":
        predicted_test_categories = svm(train_matrix,
                                        test_matrix,
                                        train_truth)
    elif classifier_opts == "ensemble_svm":
        predicted_test_categories = ensemble_svm(train_matrix,
                                                 test_matrix,
                                                 train_truth)
    elif classifier_opts == "nn":
        predicted_test_categories = neural_network(train_matrix,
                                                 test_matrix,
                                                 train_truth)

    else:
        print("Unrecognized classification")
        sys.exit(1)

    #print("Training cateogories", train_truth)
    print("Predicted", predicted_test_categories)
    print("Actual", test_truth)
    ct = 0
    for i in range(len(predicted_test_categories)):
        if  predicted_test_categories[i] == test_truth[i]:
            ct += 1
    print("Accuracy", ct/len(test_truth))

    return predicted_test_categories, test_truth


def evaluation(predicted_test_categories, test_truth):
    pass


if __name__ == "__main__":
    main()
