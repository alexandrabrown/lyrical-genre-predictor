# Require to include sklearn.svm in other script as well
# Quad kernel SVM, can exlpore other options(e.g. radial basis function kernel)
from sklearn.svm import SVC


def svm(vector_rep, label):
    C_Quad = [0.001, 0.001, 10**(-0.5)]
    R_Quad = [0.01, 0.01, 10**3]
    model = []
    for i in range(len(C_Quad)):
        for j in range(len(R_Quad)):
            L2Quad = SVC(kernel='poly', C=C_Quad[i],
                         coef0=R_Quad[ij], degree=2,
                         class_weight='balanced')

            L2Quad.fit(vector_rep, label)
            model.append(L2Quad)
    # Have to decide regularization and the cofficeint in quad function 
    return model
