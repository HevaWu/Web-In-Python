import re
import nltk
from nltk.util import ngrams
from nltk.tokenize import sent_tokenize
from nltk import load

#function that loads a lexicon of positive words to a set and returns the set
def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname)
    #add every word in the file to the set
    for sentence in lex_conn:
        newLex.add(sentence.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex


# return tagged_terms that include specific POS tags
def getPOSterms(tagged_terms,POStags):

        POSterms={}
        for tag in POStags:POSterms[tag]=set()

        #for each tagged term
        for pair in tagged_terms:
                for tag in POStags: # for each POS tag
                        if pair[1].startswith(tag): POSterms[tag].add(pair[0])

        return POSterms

# updates the frequency of each noun in the sentence
# returns a list of all the 'not <any word>  <pos/neg word>  <noun>' 4grams in the sentence

def processSentence(sentence,freq,posLex,negLex,tagger):

        matchedfgrams=[]

        sentence = re.sub('[^a-zA-Z\d]',' ',sentence)
        sentence=re.sub(' +',' ',sentence).strip()

        terms = nltk.word_tokenize(sentence.lower())

        tagged_terms=tagger.tag(terms)
        POStags = ['NN']
        NNterms = getPOSterms(tagged_terms,POStags)
        nouns=NNterms['NN']

        #print 'nn: ',NNterms
        fourgrams=ngrams(terms,4)

        for n in nouns:
                freq[n] = freq.get(n,0)+1

        print 'freq: ',freq

        for tg in fourgrams:
        #       print 'tg: ', tg
                if tg[0]=="not" and tg[2] in posLex and tg[3] in nouns:
                        matchedfgrams.append(tg)
                if tg[0]=="not" and tg[2] in negLex and tg[3] in nouns:
                        matchedfgrams.append(tg)

        #print 'tag: ', matchedfgrams

        return matchedfgrams


# gts the list with the 3 most frequent keys in a dictionary
def getTop3(D):

        result=[]

        sortedD = sorted(D.items(), key=itemgetter(1), reverse=True)

        for value in sortedD[0:3]:
                result.append(value[0])

        return result

        
def run(fpath):

        posLex=loadLexicon('positive-words.txt')
        negLex=loadLexicon('negative-words.txt')

        #make a new tagger
        _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
        tagger = load(_POS_TAGGER)

        #read the input
        f=open(fpath)
        text=f.read().strip()
        f.close()

        #split sentences
        sentences=sent_tokenize(text)

        freq={} # keep track of noun frequency  (number of sentences that include the noun)

        matched4gramsPerSent=[]# will hold all 4grams with the following structure: not <any word>  <pos/neg word>  <noun>

        # for each sentence
        for sentence in sentences:
                matched4grams=processSentence(sentence,freq,posLex,negLex,tagger)
                matched4gramsPerSent.append(matched4grams)

        freqNouns=getTop3(freq)  #atts=None#getAtts() #['bike','size']
        final4grams=set() # final result

        for fgrams in matched4gramsPerSent: # for each sentence
                for fg in fgrams: # for each matched 4gram in this sentence
                        if fg[3] in freqNouns: final4grams.add(' '.join(fg))

        return final4grams


if __name__=='__main__':
        print run('input.txt')
