from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer
from sklearn.decomposition import TruncatedSVD


def lsa_vectorize(train_lyrics, test_lyrics, output_matrix, n_components = 10):
    corpus = train_lyrics + test_lyrics
    vectorizer = TfidfVectorizer(min_df=1)
    dmatrix = vectorizer.fit_transform(corpus)

    svd = TruncatedSVD(n_components)
    normalizer = Normalizer(copy=False)
    lsa = make_pipeline(svd, normalizer)
    dmatrix = lsa.fit_transform(dmatrix)
    assert(len(dmatrix) == len(train_lyrics) + len(test_lyrics))
    return dmatrix[:len(train_lyrics)], dmatrix[-len(test_lyrics):]
