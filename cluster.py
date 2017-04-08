import  numpy as np
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import SpectralClustering

def most_common(lst):
    return max(set(lst), key=lst.count)

def majority_vote(k, prediction, train_truth):
    assignment = []
    for idx in range(k):
        tp_ls = [train_truth[i] for i,item in enumerate(prediction) if item == idx]
        #tp_ls = [print('here') for i,item in enumerate(prediction) if item == idx]
        print(tp_ls)
        assignment.append(most_common(tp_ls))

    return assignment

def kmeans(train_matrix,test_matrix, train_truth):
    predicted_test_categories = []
    k = 10
    kmeans = KMeans(n_clusters=k, random_state=0).fit(train_matrix)
    assignment = majority_vote(k, kmeans.predict(train_matrix), train_truth)
    prediction = kmeans.predict(test_matrix)
    predicted_test_categories = [assignment[idx] for idx in prediction]
    
    return predicted_test_categories

def agglomerative(train_matrix,test_matrix, train_truth, linkopt = "ward"): # linkopt = {“ward”, “complete”, “average”}
    predicted_test_categories = []
    k = 5
    prediction = AgglomerativeClustering(n_clusters=k, linkage = linkopt).fit_predict(np.concatenate((train_matrix, test_matrix), axis=0))
    assignment = majority_vote(k, prediction[:train_matrix.shape[0]], train_truth)
    predicted_test_categories = [assignment[idx] for idx in prediction[train_matrix.shape[0]:]]
    
    return predicted_test_categories

def spectral(train_matrix,test_matrix, train_truth):
    predicted_test_categories = []
    k = 5
    prediction = SpectralClustering(n_clusters=k).fit_predict(np.concatenate((train_matrix, test_matrix), axis=0))
    assignment = majority_vote(k, prediction[:train_matrix.shape[0]], train_truth)
    predicted_test_categories = [assignment[idx] for idx in prediction[train_matrix.shape[0]:]]
    
    return predicted_test_categories



