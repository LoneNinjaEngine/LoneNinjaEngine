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

def evaluate_features(feature_select):
    posFeatures = []
    negFeatures = []
    with open(RT_POLARITY_POS_FILE, 'r') as posSentences:
        for i in posSentences:
            posWords = re.findall(r"[\w']+|[.,!?;]", i.rstrip())
            posWords = [feature_select(posWords), 'pos']
            posFeatures.append(posWords)
    with open(RT_POLARITY_NEG_FILE, 'r') as negSentences:
        for i in negSentences:
            negWords = re.findall(r"[\w']+|[.,!?;]", i.rstrip())
            negWords = [feature_select(negWords), 'neg']
            negFeatures.append(negWords)

    trainFeatures = posFeatures + negFeatures
    
    #trains a Naive Bayes Classifier
    classifier = NaiveBayesClassifier.train(trainFeatures)    

    #initiates referenceSets and testSets
    referenceSets = collections.defaultdict(set)
    testSets = collections.defaultdict(set)   
    
    outputfile = open(OUTPUT_FILE, 'w')
    if not os.path.isfile(INPUT_FILE):
        print('File does not exist.')
    else:            
        with open(INPUT_FILE, 'r') as inputSentences:
            for sentence in inputSentences:
                wordsarray=re.findall(r"[\w']+|[.,!?;]", sentence.rstrip())
                testFeatures = []
                wordelement=[feature_select(wordsarray),'input']
                testFeatures.append(wordelement)
                for i, (features,label) in enumerate(testFeatures):
                    referenceSets[label].add(i)
                    predicted = classifier.classify(features)
                    if (predicted == 'pos'):
                        output='Positive'
                    else:
                        output='Negative'
                    outputfile.write(output+'\n')
                    testSets[predicted].add(i)
                testFeatures.clear()
    outputfile.close()

#creates a feature selection mechanism that uses all words
def make_full_dict(words):
    return dict([(word, True) for word in words])

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

#tries using all words as the feature selection mechanism
evaluate_features(make_full_dict)


