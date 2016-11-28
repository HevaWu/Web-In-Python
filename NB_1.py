"""
A simple script that demonstrates how we classify textual data with sklearn.
"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
#read the reviews and their polarities from a given file

def loadData(fname):
    reviews=[]
    labels=[]
    f=open(fname)
    for line in f:
        review,rating=line.strip().split('\t')  
        reviews.append(review.lower())    
        labels.append(rating)
    f.close()
    return reviews,labels

rev_train,labels_train=loadData('reviews_train.txt')
rev_test,labels_test=loadData('reviews_test.txt')

#Build a counter based on the training dataset
counter = CountVectorizer(stop_words=stopwords.words('english'))
counter.fit(rev_train)

#count the number of times each term appears in a document and transform each doc into a count vector
counts_train = counter.transform(rev_train)#transform the training data
counts_test = counter.transform(rev_test)#transform the testing data

LR = Pipeline([('tfidf', TfidfTransformer()),
               ('clf',SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, n_iter=5, random_state=42))])
#build a Logistic Regression classifier on the training data
#LR=MultinomialNB()
LR.fit(counts_train,labels_train)

#use the classifier to predict
predicted=LR.predict(counts_test)

#print the accuracy
print accuracy_score(predicted,labels_test)
fw = open('out.txt','w')
for i in predicted:
    fw.write(i+'\n')
fw.close()
