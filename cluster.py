<<<<<<< HEAD
import  numpy as np
=======
import numpy as np
>>>>>>> 04d15b8f1a69f01f73570537f6d5b66a2e9af996
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import SpectralClustering

<<<<<<< HEAD
def most_common(lst):
    return max(set(lst), key=lst.count)

def majority_vote(k, prediction, train_truth):
    assignment = []
    for idx in range(k):
        tp_ls = [train_truth[i] for i,item in enumerate(prediction) if item == idx]
        #tp_ls = [print('here') for i,item in enumerate(prediction) if item == idx]
        print(tp_ls)
=======

def most_common(lst):
    return max(set(lst), key=lst.count)


def majority_vote(k, prediction, train_truth):
    assignment = []
    for idx in range(k):
        tp_ls = [train_truth[i] for i, item in enumerate(prediction) if item == idx]
        # tp_ls = [print('here') for i,item in enumerate(prediction) if item == idx]
        # print(tp_ls)
>>>>>>> 04d15b8f1a69f01f73570537f6d5b66a2e9af996
        assignment.append(most_common(tp_ls))

    return assignment

<<<<<<< HEAD
def kmeans(train_matrix,test_matrix, train_truth):
=======

def kmeans(train_matrix, test_matrix, train_truth):
>>>>>>> 04d15b8f1a69f01f73570537f6d5b66a2e9af996
    predicted_test_categories = []
    k = 10
    kmeans = KMeans(n_clusters=k, random_state=0).fit(train_matrix)
    assignment = majority_vote(k, kmeans.predict(train_matrix), train_truth)
    prediction = kmeans.predict(test_matrix)
    predicted_test_categories = [assignment[idx] for idx in prediction]
<<<<<<< HEAD
    
    return predicted_test_categories

def agglomerative(train_matrix,test_matrix, train_truth, linkopt = "ward"): # linkopt = {“ward”, “complete”, “average”}
    predicted_test_categories = []
    k = 5
    prediction = AgglomerativeClustering(n_clusters=k, linkage = linkopt).fit_predict(np.concatenate((train_matrix, test_matrix), axis=0))
    assignment = majority_vote(k, prediction[:train_matrix.shape[0]], train_truth)
    predicted_test_categories = [assignment[idx] for idx in prediction[train_matrix.shape[0]:]]
    
    return predicted_test_categories

def spectral(train_matrix,test_matrix, train_truth):
=======

    return predicted_test_categories


def agglomerative(train_matrix, test_matrix, train_truth, linkopt="ward"):  # linkopt = {“ward”, “complete”, “average”}
    predicted_test_categories = []
    k = 5
    prediction = AgglomerativeClustering(n_clusters=k, linkage=linkopt).fit_predict(
        np.concatenate((train_matrix, test_matrix), axis=0))
    assignment = majority_vote(k, prediction[:train_matrix.shape[0]], train_truth)
    predicted_test_categories = [assignment[idx] for idx in prediction[train_matrix.shape[0]:]]

    return predicted_test_categories


def spectral(train_matrix, test_matrix, train_truth):
>>>>>>> 04d15b8f1a69f01f73570537f6d5b66a2e9af996
    predicted_test_categories = []
    k = 5
    prediction = SpectralClustering(n_clusters=k).fit_predict(np.concatenate((train_matrix, test_matrix), axis=0))
    assignment = majority_vote(k, prediction[:train_matrix.shape[0]], train_truth)
    predicted_test_categories = [assignment[idx] for idx in prediction[train_matrix.shape[0]:]]
<<<<<<< HEAD
    
    return predicted_test_categories



=======

    return predicted_test_categories
>>>>>>> 04d15b8f1a69f01f73570537f6d5b66a2e9af996
