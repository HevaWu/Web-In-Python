# cd week2  进入盘
# ls   显示当前盘内所有文件
# vi textfile   进入/create文件  press i to type      press esc to exit insert format
# shift + ":"  进入下面的命令   接着输入 “wq”  退出该文件
# Make sure only you can see your script: Type "chmod 700 counter.py"
# Test your script. Type 'testme' and press Enter     //run the code inside
# python counter.py   //run the file
"""
Step 1: Enter this week's directory. Type: cd week2     

Step 2: Create a new python script named counter.py inside the week2 folder: Type vi counter.py

Step 3: Define a function called run() inside counter.py. The function should accept as input the path to a text file and return a dictionary that includes the frequency of each word in the file. Make sure you ignore case. For example, house and House are the same word.

Step 4: When you are done, save your script and exit back to the terminal.  

Press the Esc button.
Hold Shift and press the : button.  
Type wq and press Enter.
Step 5: Make sure only you can see your script: Type chmod 700 counter.py

Step 6: Test your script. Type testme and press Enter. If the message "Success!!!" shows up on the screen, then you are done. If not, go back to your script, change it, and try Step 7 again.
"""


"""  多行注释
Week 2
The script defines a function run(). The function accepts as input the path to a text file and 2 words. It then returns the number of times that each
word appears in the file.
"""

#define a new function
def run(path,word1,word2):

        freq={} # new dictionary. Maps each word to each frequency
        #  key is word, value is freq

        #initialize the frequency of the two words to zero.
        freq[word1]=0
        freq[word2]=0

        fin=open(path) # open a connection to the file
        for line in fin: # read the file line by line
                # lower() converts all the letters in the string to lower-case
                # strip() removes blank space from the start and end of the string
                # split(c) splits the string on the character c and returns a list of the pieces. For example, "A1B1C1D".split('1')" returns [A,B,C,D]
                words=line.lower().strip().split(' ')

                # use for to go over all the words in the list
                for word in words: # for each word in the line
                        if word==word1:
                                freq[word1]=freq[word1]+1 # if the word is word1, then increase the count of word1 by 1
                        elif word==word2:
                                freq[word2]=freq[word2]+1 # if the word is word2, then increase the count of word2 by 1

        fin.close() #close the connection to the text file

        return freq[word1],freq[word2]


# use the function
print run('textfile','blue','yellow')
print run('textfile','the','house')

"""

EXPLANATION
==================

In the beginning, we have freq['blue']=0 and freq['yellow']=0

The first line of the file is:
My name is John and I live in the blue house

After we lower, strip, and split we get the following list of words:
                                                                                                                                                                           