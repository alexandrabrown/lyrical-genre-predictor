# Alexandra Brown, Gabriel Hodge, Noriyuki Kojima, Harry Zhang
# EECS 486 Final Project - W17
# Lyrical Genre Predictor

import sys
from vectorization import *
from naive_bayes import *
from database import *
from sklearn.metrics import *
from svm import *
from preprocess import *
# from NN.neural_network import *

usage_string = "python3 main.py [tf_idf | count | binary] [naive_bayes | svm | neural_network] <optional_filename>"
num_training_tracks = 1000
num_testing_tracks = 100


def main():
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print("Error! USAGE: " + usage_string)
        sys.exit(1)

    vect_opts = sys.argv[1]
    classifier_opts = sys.argv[2]

    filename = None

    # Optional filename as input for lyrics
    if len(sys.argv) == 4:
        filename = sys.argv[3]

    predicted_test_categories, test_truth = classify_songs(classifier_opts,
                                                           vect_opts, filename)

    # Only perform evaluation on tracks where the genre is known
    # If they're coming from the user, they could be anything
    if not filename:
        evaluation(predicted_test_categories, test_truth)


# Based on the options, run a classifier on song lyrics
def classify_songs(classifier_opts, vect_opts, filename):

    """
    Load the IDs
    """
    categories = ["Pop", "Rock", "Country", "Blues", "Rap"]
    category_counts = {"Pop": 0, "Rock": 0, "Country": 0,
                       "Blues": 0, "Rap": 0}
    test_counts = {"Pop": 0, "Rock": 0, "Country": 0,
                   "Blues": 0, "Rap": 0}

    train_truth = []
    test_truth = []

    train_IDs = []
    test_IDs = []

    # Go thru the track list and set aside tracks for training and testing
    with open("msd_tagtraum_cd2c.cls") as f:
        for line in f:
            try:
                track, category = line.strip().split(None, 1)  # max split once
            except:
                print("Line error", line)
                exit(1)

            # Skip categories we are not considering
            if category not in categories:
                continue

            if not track_has_lyrics(track):
                continue

            # Make sure we have enough training data
            if category_counts[category] < num_training_tracks:
                train_truth.append(category)
                train_IDs.append(track)
                category_counts[category] += 1

            # If reading from the database and we haven't
            # reached our testing quota for tracks
            elif not filename and test_counts[category] < num_testing_tracks:
                    test_truth.append(category)
                    test_IDs.append(track)
                    test_counts[category] += 1

            else:

                # Reading from user specified file
                if filename:
                    counts = category_counts.values()
                    if min(counts) == num_training_tracks:
                        test_IDs = read_file(filename, test_IDs)
                        break
                else:
                    counts = test_counts.values()
                    if min(counts) == num_testing_tracks:
                        break

    print(category_counts)
    if not filename:
        print(test_counts)

    # vectorize train and test
    train_matrix, test_matrix = vectorization(train_IDs, test_IDs, vect_opts)

    # classify based on classifier_opts
    if classifier_opts == "naive_bayes":
        predicted_test_categories = naive_bayes_classifier(train_matrix,
                                                           test_matrix,
                                                           train_truth)
    elif classifier_opts == "svm":
        predicted_test_categories = svm(train_matrix, test_matrix, train_truth)

    elif classifier_opts == "neural_network":
        predicted_test_categories = neural_network(train_matrix,
                                                   test_matrix, train_truth)

    else:
        print("Unrecognized classification")
        print("Error! USAGE: " + usage_string)
        sys.exit(1)

    print("Predicted", predicted_test_categories)

    if not filename:
        print("Actual", test_truth)

    return predicted_test_categories, test_truth


# Returns preprocessed list of tokens from input
def preprocess(input):

    tokenList = []

    input = input.strip().lower()

    # skip empty lines
    if not input:
        return tokenList

    tokenList = tokenizeText(input)

    # Remove various punctuation to make output more comprehensible
    tokenList = [token.replace('.', '') for token in tokenList]
    tokenList = [token.replace('"', '') for token in tokenList]
    tokenList = [token.replace(',', '') for token in tokenList]
    tokenList = [token.replace('\'', '') for token in tokenList]

    tokenList = removeStopwords(tokenList)
    tokenList = stemWords(tokenList)

    return tokenList


# Use data from filename as test data for the system
# Each song should be on its own line
def read_file(filename, test_IDs):
    with open(filename) as test_file:
        for track in test_file:
            lyrics = str(preprocess(track))
            print(lyrics)
            test_IDs.append(lyrics)
    return test_IDs


# Evaluate based on the true categories and the predicted categories
def evaluation(predicted_test_categories, test_truth):
    num_correct = 0
    for i in range(len(test_truth)):
        if predicted_test_categories[i] == test_truth[i]:
            num_correct += 1
    print("Correctly predicted " + str(num_correct) + " out of " + str(len(test_truth)))

    microP = precision_score(test_truth, predicted_test_categories, average='micro')
    print("Micro precision ", microP)
    macroP = precision_score(test_truth, predicted_test_categories, average='macro')
    print("Macro precision ", macroP)

    microR = recall_score(test_truth, predicted_test_categories, average='micro') 
    print("Micro recall ", microR)
    macroR = recall_score(test_truth, predicted_test_categories, average='macro')
    print("Macro recall ", macroR)

    f1 = f1_score(test_truth, predicted_test_categories, average='micro')
    print("Micro F1 Score ", f1)
    f1 = f1_score(test_truth, predicted_test_categories, average='macro')
    print("Macro F1 Score ", f1)


if __name__ == "__main__":
    main()
