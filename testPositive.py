from textblob import TextBlob

def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname)
    #add every word in the file to the set
    for sentence in lex_conn:
        newLex.add(sentence.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex

def run(path): {
	posLex=loadLexicon('positive-words.txt')
	negLex=loadLexicon('negative-words.txt')

	f = open(path)
	text = f.read().strip()
	f.close()

	sentences=sent_tokenize(text)
	for sentence in sentences:
		print(sentence.sentiment.polarity)

}

if __name__=='__main__':
	print run('input.txt')