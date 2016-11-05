# -*- coding: utf8 -*-
#!/usr/bin/python
"""
Script to preprocess the RAW tweets and prepare the textual files to be used in Brat
Created by nestoralvaro
"""
from collections import defaultdict
import getPreprocessedSentence as gps
import os

def loadFileWithTweetIds(path):
  """
  Creates a list with the tweet identifiers
  """
  f= open(path, 'r')
  tweets = []
  for line in f.xreadlines():
    tweets.append((line).strip())
  f.close()
  return tweets

def getPreprocessedSentence(rawSentence, emoji_StringReplacementDictionary):
  """
  Preprocess the sentence performing some string replacements like emojis or numbers
  """
  rawSentence = rawSentence.replace("&amp;", "&")
  rawSentence = rawSentence.replace("&lt;", "<")
  rawSentence = rawSentence.replace("&gt;", ">")
  # Replace the emojis (This could be Optional)
  sentence = gps.transformEmojisInString(rawSentence, emoji_StringReplacementDictionary)
  sentence = sentence.encode("utf8")
  # Replace numbers, usernames and some other strings
  sentence = gps.preprocessText(sentence, {})
  return sentence

def storeToFile(sentenceId, rawSentence, targetFolder, emoji_StringReplacementDictionary):
  """
  Store all extracted sentences to a file
  """
  fileName = "{0}{1}{2}".format(targetFolder, sentenceId, ".txt")
  #print fileName
  #print rawSentence
  preprocessedSentence = getPreprocessedSentence(rawSentence, emoji_StringReplacementDictionary)
  #print sentenceId, fileName, preprocessedSentence
  f = open(fileName,'w')
  f.write(preprocessedSentence)
  f.close()

def getExtraSentencesTwitter(fileWithTargetSentences, folderToStoreFiles, emoji_StringReplacementDictionary):
  """
  Creates the files that will be stored in Brat.
  """
  listTweetsAndIds = loadFileWithTweetIds(fileWithTargetSentences)
  # Pick the sentences of interest
  for ltai in listTweetsAndIds:
    information = ltai.split("\t")
    sentenceId = information[0]
    rawSentence = information[1]
    storeToFile(sentenceId, rawSentence, folderToStoreFiles, emoji_StringReplacementDictionary)

if __name__ == '__main__':
  # File with the IDs and the sentences that I want to prepare for BRAT
  fileWithTargetSentences = "tweets_ID.txt"
  # TODO
  # I will stored the sentences here (Then, I just need to compress and upload this folder to BRAT)
  folderToStoreFiles = "tweets/"
  if not os.path.exists(folderToStoreFiles):
    os.makedirs(folderToStoreFiles)
  # Dictionary with the replacements
  emoji_StringReplacementDictionary = gps.loadDict("Emoji_Strings.txt", 0, 1)
  getExtraSentencesTwitter(fileWithTargetSentences, folderToStoreFiles, emoji_StringReplacementDictionary)
