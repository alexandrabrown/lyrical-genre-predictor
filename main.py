import sys
import vectorization

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
    test_genres = ["Rock", "Pop", "Country", "Blues", "Jazz", "Rap"]
    ground_truth = {}

    train_ID = []
    test_ID = []

    with open("msd_tagtraum_cd2c.cls") as f:
        i = 0
        for line in f:
            track, genre = line.split()
            if genre not in test_genres:
                continue
            if i < 100:
                ground_truth[track] = genre
                train_ID.append(track)
            elif i < 125:
                ground_truth[track] = genre
                test_ID.append(track)
            else:
                break
            i += 1

    # read training data

    if classifier_opts == "naive_bayes":
        pass
    else:  # Vectorization
        train_matrix, test_matrix = vectorization.vectorize(train_ID, test_ID, vect_opts)
        # classification method (cosine sim, machine learning, etc)


def test():
    pass


if __name__ == "__main__":
    main()
