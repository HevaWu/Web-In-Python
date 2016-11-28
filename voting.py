"""
A simple script that demonstrates how we classify textual data with sklearn.

"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


#read the reviews and their polarities from a given file
def loadData(fname):
    reviews=[]
    labels=[]
    f=open(fname)
    for line in f:
        review,rating=line.strip().split('\t')  
        reviews.append(review.lower())    
        labels.append(int(rating))
    f.close()
    return reviews,labels

#both training and test all need to do this operation
# for test, we need to make sure our result is true, it is a match
rev_train,labels_train=loadData('reviews_train.txt')
rev_test,labels_test=loadData('reviews_test.txt') 


#Build a counter based on the training dataset
counter = CountVectorizer()
#all unique words appear in strings
counter.fit(rev_train)


#count the number of times each term appears in a document and transform each doc into a count vector
#[play,5]  --- word, freq
counts_train = counter.transform(rev_train)#transform the training data
counts_test = counter.transform(rev_test)#transform the testing data

#pick 3 classifiers
clf1 = LogisticRegression()
clf2 = KNeighborsClassifier()
clf3 = MultinomialNB()

#build a voting classifer
eclf = VotingClassifier(estimators=[('lr', clf1), ('knn', clf2), ('mnb', clf3)], voting='hard')

#train all classifier on the same datasets
eclf.fit(counts_train,labels_train)

#use hard voting to predict (majority voting)
pred=eclf.predict(counts_test)

#print accuracy
print accuracy_score(pred,labels_test)


