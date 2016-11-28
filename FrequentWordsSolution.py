import os,sys,re
from nltk.corpus import stopwords
from operator import itemgetter

#function that loads a lexicon of positive words to a set and returns the set
def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname)
    #add every word in the file to the set
    for sentence in lex_conn:
        newLex.add(sentence.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex


def run(path):

	freq={}

	#load lexicons
	posLex=loadLexicon('positive-words.txt')
	negLex=loadLexicon('negative-words.txt')
	stopLex=set(stopwords.words('english'))

	#read input
	fin=open(path)
	text=fin.read().lower()
	fin.close()

	sentences=text.split('.')	
	
	#for each sentence
	for sentence in sentences:

		sentence=sentence.lower().strip()
		
		sentence=re.sub('[^a-z]',' ',sentence) # clean

		words=sentence.split(' ') # split

		hasSentiment=False

		unique=set() # remember unique words that are not empty,stopwords,pos or neg in this sentence
		for word in words:

			if word=='' or word in stopLex:continue # ignore these words

			elif word in negLex or word in posLex: # this is a senti-sentence
				hasSentiment=True
			else:
				unique.add(word) # add the word to the set
				
			 
		if hasSentiment: # if this is a senti-sent
			for word in unique: # for each word in the set
				freq[word]=freq.get(word,0)+1# increment frequency	

	fin.close()
	
	#find and return set of words with a freq at least 4
	top=set()
	for word in freq:
		if freq[word]>=4:top.add(word)

	return top



