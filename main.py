import sys
from vectorization import *
from naive_bayes import *
from sklearn.metrics import *

usage_string = "python3 main.py [naive_bayes | svm] [tf_idf | count | binary]"

def main():
    
    """
    TODO: allow lyrics to be read from an optional filename
    """

    if len(sys.argv) != 3:
        print("Error! USAGE: " + usage_string)
        sys.exit(1)

    classifier_opts = sys.argv[1]
    vect_opts = sys.argv[2]
    predicted_test_categories, test_truth = classify_songs(classifier_opts, vect_opts)
    evaluation(predicted_test_categories, test_truth)


def classify_songs(classifier_opts, vect_opts):

    """
    Load the IDs
    """
    categories = ["Pop", "Rock", "Country", "Blues", "Jazz", "Rap"]
    category_counts = {"Pop": 0, "Rock": 0, "Country": 0,
                       "Blues": 0, "Jazz": 0, "Rap": 0}
    
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
            if i < 20000:

                # Make sure we have at least x songs in each genre
                if category_counts[category] < 500:
                    train_truth.append(category)
                    train_IDs.append(track)
                    category_counts[category] += 1

            elif i < 20100:
                test_truth.append(category)
                test_IDs.append(track)
            else:
                break
            i += 1

    print(category_counts)

    # vectorize train and test
    train_matrix, test_matrix = vectorization(train_IDs, test_IDs, vect_opts)
    
    # classify based on classifier_opts
    if classifier_opts == "naive_bayes":
        predicted_test_categories = naive_bayes_classifier(train_matrix,
                                                           test_matrix,
                                                           train_truth)
    elif classifier_opts == "svm":
        pass

    else:
        print("Unrecognized classification")
        print("Error! USAGE: " + usage_string)
        sys.exit(1)

    print("Predicted", predicted_test_categories)
    print("Actual", test_truth)

    return predicted_test_categories, test_truth


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
    print("Macro recall, ", macroR)

    f1 = f1_score(test_truth, predicted_test_categories, average='micro')
    print("Micro F1 Score ", f1)
    f1 = f1_score(test_truth, predicted_test_categories, average='macro')
    print("Macro F1 Score ", f1)



if __name__ == "__main__":
    main()
