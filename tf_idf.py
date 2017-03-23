import sys
from sklearn.feature_extraction.text import TfidfVectorizer

def tf_idf_vectorize():
    corpus = [
    'This is the first document.',
    'This is the second second document.',
    'And the third one.',
    'Is this the first document?',
    ]

    vectorizer = TfidfVectorizer(min_df=1)
    vectorizer.fit_transform(corpus)

    return vectorizer.fit_transform(corpus).toarray()
