#!/usr/bin/env python

# Functions used in preprocessing steps

import sys
import re
import os
from PorterStemmer import *


# Reference: http://stackoverflow.com/questions/19790188/expanding-english-language-contractions-in-python
contractions = {
    "aren't": "are not",
    "can't": "cannot",
    "could've": "could have",
    "couldn't": "could not",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hasn't": "has not",
    "haven't": "have not",
    "he'd": "he had",
    "he'll": "he will",
    "how'd": "how did",
    "how'll": "how will",
    "I'd": "I had",
    "I'll": "I will",
    "I'm": "I am",
    "I've": "I have",
    "isn't": "is not",
    "it'll": "it will",
    "it's": "it is",
    "let's": "let us",
    "must've": "must have",
    "mustn't": "must not",
    "o'clock": "of the clock",
    "she'd": "she had",
    "she'll": "she will",
    "she's": "she is",
    "should've": "should have",
    "shouldn't": "should not",
    "that'd": "that had",
    "that's": "that is",
    "there's": "there is",
    "they'd": "they had",
    "they'll": "they will",
    "they're": "they are",
    "they've": "they have",
    "wasn't": "was not",
    "we'd": "we had",
    "we'll": "we will",
    "we're": "we are",
    "we've": "we have",
    "weren't": "were not",
    "what's": "what is",
    "where's": "where is",
    "where've": "where have",
    "who'll": "who will",
    "who's": "who is",
    "who've": "who have",
    "why's": "why is",
    "why've": "why have",
    "will've": "will have",
    "won't": "will not",
    "would've": "would have",
    "wouldn't": "would not",
    "y'all": "you all",
    "you'd": "you had",
    "you'll": "you will",
    "you're": "you are",
    "you've": "you have",
    "\'s": " \'s"
}


# Removes all tags in input using a regular expression
def removeSGML(input):

    # Regular expression used to match SGML
    # Used this reference: https://www.debuggex.com/cheatsheet/regex/python
    # matches tags in the form of <word>
    matchSGML = re.compile('<.*?>')
    text = re.sub(matchSGML, '', input)
    return text


# Returns a list of tokenized content in input
def tokenizeText(input):

    # Expand contractions
    pattern = re.compile('|'.join(re.escape(key) for key in contractions))
    input = pattern.sub(lambda x: contractions[x.group()], input)

    # Split on: comma, space, !, ?, :, ;, (, )
    list = filter(None, re.split("[ \!?:;()]+", input))

    # Remove single . elements
    list = filter(lambda x: x != '.', list)

    # Remove commas
    list = [word.replace(",", "") for word in list]

    # Remove / on either side of words
    # Do this last since we want to keep dates together
    for i, word in enumerate(list):
        if len(word) >= 2:
            if word[0] == '/' or word[len(word) - 1] == '/':
                list[i] = list[i].replace("/", "")

    return list


# Returns a list with removed stop words in input
def removeStopwords(input):
    stopWordsFile = open('stopwords', 'r')
    stopWords = [words.rstrip() for words in stopWordsFile.readlines()]

    list = [word for word in input if word not in stopWords]

    stopWordsFile.close()

    return list


# Uses PorterStemmer to stem words by removing common affixes
def stemWords(input):
    p = PorterStemmer()
    return [p.stem(word, 0, len(word) - 1) for word in input]


def main():
    folder = sys.argv[1]
    totalWords = 0
    wordSet = {}
    uniqueWords = 0

    # For all the files in the folder
    for filename in os.listdir(folder):

        file = open(folder + filename, 'r')
        for line in file:

            # trim leading and trailing whitespace
            line = line.strip()

            parsedContent = removeSGML(line)

            # skip empty lines
            if not parsedContent:
                continue

            parsedContentList = tokenizeText(parsedContent)

            withoutStopWords = removeStopwords(parsedContentList)

            tokens = stemWords(withoutStopWords)

            totalWords += len(tokens)

            # Keep track of frequencies
            for token in tokens:
                if token in wordSet:
                    wordSet[token] += 1
                else:
                    wordSet[token] = 1

        file.close()

    uniqueWords = len(wordSet)

    # Write to file
    outfile = open('preprocess.output', 'w')
    outfile.truncate()
    outfile.write('Words {}\n'.format(totalWords))
    outfile.write('Vocabulary {}\n'.format(uniqueWords))
    outfile.write('Top 50 words\n')

    # Sort based on key
    sortedFreq = sorted(wordSet, key=wordSet.get, reverse=True)

    # Only write top 50
    for word in sortedFreq[:50]:
        outfile.write("{} {}\n".format(word, wordSet[word]))

    # Get how many unique words account for 25% of vocab size
    numWords = totalWords * .25
    count = 1

    for word in sortedFreq:
        numWords -= (wordSet[word])
        if numWords < 0:
            break
        count += 1
    # print('Count for 25% of corpus: ' + str(count) + '\n')


if __name__ == '__main__':
        main()
