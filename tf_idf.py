import sys
from sklearn.feature_extraction.text import TfidfVectorizer

def main():
    corpus = [
    'This is the first document.',
    'This is the second second document.',
    'And the third one.',
    'Is this the first document?',
    ]

    vectorizer = TfidfVectorizer(min_df=1)
    vectorizer.fit_transform(corpus)

    print vectorizer.fit_transform(corpus).toarray()



if __name__ == "__main__":
    sys.exit(int(main() or 0))