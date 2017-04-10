# Require to include sklearn.svm in other script as well
# Quad kernel SVM, can exlpore other options(e.g. radial basis function kernel)
from __future__ import division
from sklearn.svm import SVC
from sklearn.utils import resample
import time
import numpy as np
import copy


def svm(train_matrix, test_matrix, train_truth):
    print("Training SVM ....")
    C_Quad = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
    R_Quad = [0.1, 1, 10]
    accuracy_mat = np.zeros([len(C_Quad),len(R_Quad)])
    
    # validation
    sep = round(train_matrix.shape[0]*0.8)
    validation_matrix = train_matrix[sep:,:]
    validation_label = train_truth[sep:]
    tp_train_matrix = train_matrix[:sep,:]
    tp_train_label = train_truth[:sep]
    """
    for i in range(len(C_Quad)):
        print("Parameter Tuning {} % complete".format(i*14.28))
        for j in range(len(R_Quad)):
            L2Quad = SVC(kernel='poly', C=C_Quad[i],
                         coef0=R_Quad[j], degree=2,
                         class_weight='balanced')

            L2Quad.fit(tp_train_matrix, tp_train_label)
            prediction = L2Quad.predict(validation_matrix)
            accuracy_mat[i,j] = np.sum(validation_label == prediction)

    C_idx, R_idx = np.where(accuracy_mat == np.max(accuracy_mat))
    L2Quad = SVC(kernel='poly', C=C_Quad[C_idx[0]],
                     coef0=R_Quad[R_idx[0]], degree=2,
                     class_weight='balanced')
    print(C_idx[0], R_idx[0])
    """
    L2Quad = SVC(kernel='poly', C=C_Quad[3],
                     coef0=R_Quad[2], degree=2,
                     class_weight='balanced')
    
    L2Quad.fit(train_matrix, train_truth)
    predicted_test_categories = L2Quad.predict(test_matrix)

    # Have to decide regularization and the cofficeint in quad function 
    return predicted_test_categories


def ensemble_svm(train_matrix, test_matrix, train_truth):
        num_classifier = 20 #More is better just takes more time to train
        num_train = train_matrix.shape[0]
        C_Quad = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
        R_Quad = [0.1, 1, 10]
        SVM_ls = []
        
        for i in range(num_classifier):
            idx = resample(list(range(num_train)), replace=1, n_samples=num_train, random_state=i)
            C_idx = np.random.randint(len(C_Quad), size=1)[0]
            R_idx = np.random.randint(len(R_Quad), size=1)[0]
            tp_train_matrix = train_matrix[idx,:]
            tp_train_label = []
            for j in idx:
                tp_train_label.append(train_truth[j])
            L2Quad = SVC(kernel='poly', C=C_Quad[C_idx],
                         coef0=R_Quad[R_idx], degree=2,
                         class_weight='balanced')
            L2Quad.fit(tp_train_matrix, tp_train_label)
            SVM_ls.append(L2Quad)
        
        predicted_test_categories = []
        for i in range(test_matrix.shape[0]):
            prediction = [L2Quad.predict(test_matrix[i,:])[0] for L2Quad in SVM_ls]
            predicted_test_categories.append(max(set(prediction), key=prediction.count))
    
        return predicted_test_categories
