# Lyrical Genre Predictor
EECS 486 project to predict song genres based on their lyrics.
Contributors: Alexandra Brown  (alexbro), Gabriel Hodge (gdhodge), Noriyuki Kojima (kojimano), Harry Zhang (zharry)

The genres in consideration are country, rock, rap, blues, and pop.

All of our data is from the Million Song Dataset. https://labrosa.ee.columbia.edu/millionsong/. We are using the lyrical data provided by musiXmatch and genre annotations provided by tagtraum.

**lyrics**:
http://labrosa.ee.columbia.edu/millionsong/sites/default/files/AdditionalFiles/mxm_dataset.db

**genre annotations**:
http://www.tagtraum.com/genres/msd_tagtraum_cd2c.cls.zip

**ID to title mapping**: 
http://labrosa.ee.columbia.edu/millionsong/sites/default/files/AdditionalFiles/mxm_779k_matches.txt.zip

**requirements**:
scikit-learn
tensorflow
numpy
scipy

**setup**:
```
sh setup.sh
```
or download and unzip the three files listed at the top of the readme and run dataformat.py

**usage**:
```
python3 main.py [tf_idf | count | binary | lsa] [naive_bayes | rocchio | knn | svm | kmeans | agglomerative | spectral | neural_network] <optional_filename>
```

**description**:
The program first vectorizes each training document (bag-of-words model) using the specified vectorization scheme, and then it classifies the testing documents using the specified algorithm. After training on 5000 testing documents evenly split between the five genres, if the optional_filename is not specified, it tests on another 500 documents and outputs micro/macro precision/accuracy and F-score; if it is specified, the program reads in the specified file and classifies the lyrics line by line.
