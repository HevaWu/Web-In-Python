from BeautifulSoup import BeautifulSoup
import re
import urllib2
from operator import itemgetter
import time
import sys
import requests


def getPage(url):
        html=None
        for i in range(5): # try 5 times
                try:
                        #use the browser to access the url
                        response=requests.get(url,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                        html=response.content # get the html\
                        break # we got the file, break the loop
                except Exception as e:# browser.open() threw an exception, the attempt to get the response failed
                        print 'failed attempt',i
                        time.sleep(2) # wait 2 secs, avoid you request too many times

        return html


def getCritic(review):  #get the reviews critics like "Jami Bernard"
        critic='NA'
        criticChunk=review.find('a',{'href':re.compile('/critic/')})
        if criticChunk: critic=criticChunk.text.encode('ascii','ignore') #if not ascii code, ignore it
        return critic


def getText(review): #get the text of review like "It's about time... "
        text='NA'
        textChunk=review.find('div',{'class':'the_review'})
        if textChunk: text=textChunk.text.encode('ascii','ignore')


def run(url):

        pageNum=2 # number of pages to collect

        fw=open('reviews.txt','w') # output file 'w' used for write the file

        for p in range(1,pageNum+1): # for each page (1,2

                if p==1: pageLink=url # url for page 1
                else: pageLink=url+'?page='+str(p)+'&sort=' # make the page url

                html=getPage(pageLink)

                if not html:continue # couldnt get the page, ignore

                soup = BeautifulSoup(html) # parse the html/website

                reviews=soup.findAll('div', {'class':re.compile('review_table_row')}) # get all the review divs

                for review in reviews:
                        critic=getCritic(review)
                        text=getText(review)
                        fw.write(critic+'\t'+text+'\n') # write to file

                time.sleep(2)   # wait 2 secs

        fw.close()


if __name__=='__main__':
        url='https://www.rottentomatoes.com/m/space_jam/reviews/'
        run(url)


