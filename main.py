import sys


def main():
    # Add option to take in
    classifier_opts  = sys.argv[1]  
    vect_opts = sys.argv[2]
    train(classifier_opts, vect_opts)
    test()
    
def train(classifier_opts, vect_opts):

    """
    Load the IDs
    """
    train_ID = []
    test_ID = []

    # read training data

    if classifier_opts == "naive_bayes":
        pass
    else:  # Vectorization
        pass
        # train_vecs, test_vec = vectorize(TrainID, TestID, vect_opts)
        # classification method (cosine sim, machine learning, etc)


def test():
    pass


if __name__ == "__main__":
    main()
