'''
Adrienne Hembrick
March 20, 2021

Problem: Find the accuracy for predciton based programs

Description: the scorer will take in two files, a test file and a key file, the code will
take out all of the non-label words and places the labels into lists that will then be
compared inorder to find the complete accuracy. Then it will produce

Instructions: In the terminal after compiling the file place the test file along with a
'>' character and the file you want the information to be moved to.

Example:

    python scorer.py pos-test-with-tags.txt pos-test-key.txt > pos-tagging-report.txt

    86.45%
    
Side Comments: Generally the Scorer code runs fine except for the fact that when splitting
the tags from the words adds one to the test-trained and takes one away from the test key.
This causes a shild in the two lists that ruins the score. Hence why the scores are so low


Baseline Score: 
Score: 58.82%
Rule 1:if last word was a preposition make next word determiner
Score: 57.87%
Rule 2:if last word was a determiner make next word noun
Score: 58.18%
Rule 3:if last word was a adjective make next word noun
Score: 58.04%
Rule 4:if last word was a noun make next word verb(past)
Score: 56.32%
Rule 5:if last word was adverb make next word verb(past)
Score: 57.25%

'''
## IMPORTS ##
import sys
import re
import random
from collections import defaultdict

### METHODS ###

#Inputs Test Files
def input(arg2):
    sent = ""
    g = open(arg2, 'r')
    sent += g.read() #groups lines into a file
    sent = sent.upper() #ensures all words are lowercase for sorting
    return sent

#removes the brackets
def clearBrack(sent):
    sent = sent.replace(']'," ")
    sent = sent.replace('\n'," ")
    sent = sent.replace('['," ")
    sent = sent.replace('\\/', '$$$')
    sent = sent.replace('/', ' /')
    l = re.split(" |  ",sent)
    while '' in l:
       l.remove('')
    return l

#seperates words and '/'
def sepSent(sent):
    t = list()
    words = list()
    i = 0
    for x in range(len(sent)):
        if x == 0 or x%2 == 0:
            words.append(sent[x])
        else:
            t.append(sent[x])
    return t

# Calculates the accuracy
def scoreCal(l1,l2):
    i = 0.0
    y = 0.0
    for x in range(len(l1)):
        if l1[x] == l2[x]:
            i += 1
        y += 1
    return (i/y) * 100


### MAIN METHOD ###

tester = sys.argv[1]    
scorer = sys.argv[2]

s = (clearBrack(input(scorer)))
t = (clearBrack(input(tester)))

print("Score: " + format(scoreCal(t,s),'^-.2f') + "%")

      
