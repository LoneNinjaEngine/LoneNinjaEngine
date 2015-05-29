import sys,re, math, collections, itertools, os
import nltk, nltk.classify.util, nltk.metrics
from nltk.classify import NaiveBayesClassifier
from nltk.metrics import BigramAssocMeasures
from nltk.probability import FreqDist, ConditionalFreqDist

'''
Created on May 28, 2015

@author: Prasanth Mathew
'''
POLARITY_DATA_DIR = os.path.join('rt-polaritydata', 'rt-polaritydata')
RT_POLARITY_POS_FILE = os.path.join(POLARITY_DATA_DIR, 'rt-polarity.pos')
RT_POLARITY_NEG_FILE = os.path.join(POLARITY_DATA_DIR, 'rt-polarity.neg')
INPUT_FILE = os.path.join('inputfile.txt')
OUTPUT_FILE = os.path.join('outputfile.txt')  

if not os.path.isfile(INPUT_FILE):
        print('Input File does not exist.')
        sys.exit()
if not os.path.isfile(OUTPUT_FILE):
        print('Output File does not exist.')
        sys.exit()
if not os.path.isfile(RT_POLARITY_POS_FILE):
        print('Input File does not exist.')
        sys.exit()
if not os.path.isfile(RT_POLARITY_NEG_FILE):
        print('Output File does not exist.')
        sys.exit()
        
inputfile = open(INPUT_FILE,'r')
outputfile = open(OUTPUT_FILE,'r')
posdic = open (RT_POLARITY_POS_FILE,'a')
negdic = open (RT_POLARITY_NEG_FILE,'a')

for inputline in inputfile:
    feedback=outputfile.readline().strip()
    if(feedback=='Positive'):
        posdic.write(inputline)
    elif(feedback=='Negative'):
        negdic.write(inputline)        
inputfile.close()
outputfile.close()
posdic.close()
negdic.close()