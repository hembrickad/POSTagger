"""
Adrienne Hembrick
March 20, 2021

Problem: Through the use of a training file tagger.py, trys to predict the types of words in in a text file
         with the use of tagging each word.

Description: The tagger code first takes in both files that the user gives through ther terminal and and places them as
text and capitolizes all of the character. The clearBrack() method takes out all of the brackets and unneeded characters
from the text and the sepSent() separates the words into tags and words. The test files is then separated and run through
association to find the closest tag match to the word or symbol placing all results into a list. A different list
of the test file's words will be combined together inoder to creates a string with tags included.

Instructions: In the terminal after compiling the file place the test file along with a
'>' character and the file you want the information to be moved to.

    python tagger.py pos-test.txt pos-train.txt > pos-test-train.txt

Side Comments:The rules are tested one at a time not compunded

Baseline: 58.82%

Rule 1: 57.87%

Rule 2: 58.18%

Rule 3: 58.04%

Rule 4: 56.32%

Rule 5: 57.25%
"""

####### Imports #######
import sys
import re
import random
from collections import defaultdict

######## Universal Variables #######
predict = defaultdict(int) # finds most likely label with word
label = defaultdict(int) # finds most likely label with pattern
total = defaultdict(int) # total count of words
totallab = list()# extended list of labels
words = list()#extended list of words

###### Methods #######
#Inputs Train Files
def input(arg2):
    sent = " "
    g = open(arg2, 'r')
    sent += g.read() #groups lines into a file
    sent = sent.upper() #ensures all words are lowercase for sorting
    return sent
# Secondary input for test file
def input2(arg2):
    sent = " "
    g = open(arg2, 'r')
    sent += g.read() #groups lines into a file
    return sent

#removes the brackets
def clearBrack(sent):
    sent = sent.replace(']',"")
    sent = sent.replace('\n',"")
    sent = sent.replace('[',"")
    sent = sent.replace('\\/', '$$$')
    sent = sent.replace('/', ' /')
    return sent

#seperates words and '/'
def sepSent(sent):
    l = re.split(" |  ",sent)
    while '' in l:
       l.remove('')
    for x in range(len(l)):
        if x == 0 or x%2 == 0:
            words.append(l[x])
        else:
            totallab.append(l[x])
    return l

#seperates words and '/' for the test file
def sep(sent):
    l = re.split(" |  ",sent)
    while '' in l:
       l.remove('')
    return l

#Creates total dictionary
def tot(l):
    tol = defaultdict(int)
    for x in l:
        tol[x] += 1
    return tol    
            
#Creates the predictive table
def pred(l1, l2):
    g2 = [(l1[i], l2[i]) for i in range(len(l1))]
    predict = tot(g2)
    return predict

#Creates the label table
def lab(li):
     g2 = [(li[i-1], li[i]) for i in range(len(li))]
     label = tot(g2)
     return label

#Assigns labels to words
def association(test):
    associ = list()
    f = False
    s = False
    i = 0
    for x in range(len(test)):
        f = False
        s = False
        for k in predict.keys(): # Tries to frind a word equivilant
            if k[0] == test[x] and f == False:
                associ.append(k[1])
                f = True
        if f == False:
            for y in label.keys():# if cannot find word equilivant tries to estimate
                if y[0] == associ[i-1] and s == False:
                    associ.append(y[1])
                    i += 1
                    s = True
    return associ

#combines the words into text
def combo(text, li):
    comb = ' '
    for x in range(len(text)):
            text[x] += li[x]
    comb = comb.join(text)#[' '.join(text[0 : len(text)])] # combines everything
    comb = comb.replace('$$$','\\/' )
    return comb
            
#Uses rules based on boolean input
def rules(r1,r2,r3,r4,r5,li):
    for x in range(len(li)):
        if(r1 == True): #if last word was a preposition make next word determiner
            if(x > 0 and li[x-1] == '/IN'):
                li[x] = '/DT'
        if(r2 == True): #if last word was a determiner make next word noun
            if(x > 0 and li[x-1] == '/DT'):
                li[x] = '/NN'
        if(r3 == True): #if last word was a adjective make next word noun
            if( x > 0 and li[x-1] == '/JJ'):
                li[x] = '/NN'
        if(r4 == True): #if last word was a noun make next word verb(past)
            if(x > 0 and li[x-1] == '/NN'):
                li[x] = '/VBD'
        if(r5 == True):#if last word was adverb make next word verb(past)
            if(x > 0 and li[x-1] == '/RB'):
                li[x] = '/VBD'




######## MAIN METHOD ########

train = sys.argv[1]    
test = sys.argv[2]

te = sep(clearBrack(input(test)))
te2 = sep(clearBrack(input2(test)))
tr = sepSent(clearBrack(input(train)))

predict = pred(words, totallab)
label = lab(totallab)

g = open(test, 'r')
hh= association(te)
h2 = rules(False,False,False,False,False,hh)

print(combo(te2,hh))






