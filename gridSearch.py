"""
A simple script that demonstrates how we can use grid search to set the parameters of a classifier
"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from nltk.corpus import stopwords
from sklearn.model_selection import GridSearchCV

# read the reviews and their polarities from a given file


def loadData(fname):
    reviews = []
    labels = []
    f = open(fname)
    for line in f:
        review, rating = line.strip().split('\t')
        reviews.append(review.lower())
        labels.append(rating)
    f.close()
    return reviews, labels

rev_train, labels_train = loadData('reviews_train.txt')
rev_test, labels_test = loadData('reviews_test.txt')

# Build a counter based on the training dataset
counter = CountVectorizer(stop_words=stopwords.words('english'))
counter.fit(rev_train)

# count the number of times each term appears in a document and transform
# each doc into a count vector
counts_train = counter.transform(rev_train)  # transform the training data
counts_test = counter.transform(rev_test)  # transform the testing data

KNN = KNeighborsClassifier()
KNN.fit(counts_train, labels_train)

# use the classifier to predict
predicted = KNN.predict(counts_test)

# print the accuracy
print(accuracy_score(predicted, labels_test))

# build the parameter grid
param_grid = [
    {'n_neighbors': [1, 3, 5, 7, 9, 11, 13, 15, 17],
        'weights':['uniform', 'distance']}
]

# build a grid search to find the best parameters
clf = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5)

# run the grid search
clf.fit(counts_train, labels_train)

# print the best parameter setting
print("\nBest parameters", clf.best_params_)


KNN = KNeighborsClassifier(n_neighbors=clf.best_params_['n_neighbors'])
KNN.fit(counts_train, labels_train)

# use the classifier to predict
predicted = KNN.predict(counts_test)

# print the accuracy
print(accuracy_score(predicted, labels_test))
