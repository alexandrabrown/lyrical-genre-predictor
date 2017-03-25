# Import Library of Gaussian Naive Bayes model
# sudo pip3 install -U scikit-learn
# sudo pip3 install -U numpy
# sudo pip3 install -U scipy
# http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import datasets
from sklearn.pipeline import Pipeline
import sys


def main():
    # iris = datasets.load_iris()
    # print(iris)
    # gnb = GaussianNB()
    # y_pred = gnb.fit(iris.data, iris.target).predict(iris.data)
    # print(y_pred)


    text_clf = Pipeline([('vect', CountVectorizer()),
                         ('tfidf', TfidfTransformer()),
                         ('clf', MultinomialNB()) ])
    


if __name__ == '__main__':
    sys.exit(int(main() or 0))
