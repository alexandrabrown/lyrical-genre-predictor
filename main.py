import sys
def main():
    # Add option to take in
    classifier_opts  = sys.argv[1]  
    vect_opts = sys.argv[2]
    train(clasifier_opts, vect_opts)
    test()
    
def train(classifier_opts, vect_opts):

    """
    Load the data
    """
    TrainID = []
    TestID = []
    
    if clasifier_opts == "naive_bayes":
        
    else:
        vec = tf_idf()       
    
 
    """
    Train the classifier
    """
    

    """
    Test
    """
  
if __name__ == "__main__":
  main()
