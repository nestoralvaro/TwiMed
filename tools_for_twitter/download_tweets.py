# -*- coding: utf8 -*-
#!/usr/bin/python
"""
Script to download RAW tweets (including non-ascii characters like emojis)
Created by nestoralvaro
"""
from bs4 import BeautifulSoup
from collections import defaultdict
import requests

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

def retrieveTweet(tweetId, tweetUser=None):
  """
  Given the tweet ID get the tweet with such ID
  """
  if not tweetUser:
    tweetUser = "twitter"
  tweetUrl = "http://twitter.com/{0}/status/{1}".format(tweetUser, tweetId)
  r  = requests.get(tweetUrl)
  data = r.text
  soup = BeautifulSoup(data, 'lxml')
  aa = soup.find("meta", {"property":"og:description"})
  text = ""
  if aa:
    text = aa['content']
    text = text.strip()
    # remove the quotes
    text = text[1:-1]
    text = text.strip()
  return text

def storeTweetIdAndText(file_to_write, tweetsDictionary):
  """
  Receives a dictionary containing the tweetIds as key and the text as the value.
  Stores to a file that information, separating the fields with a <TAB>
  """
  ftw = open(file_to_write, 'w')
  for key, val in tweetsDictionary.items():
    line = "{0}\t{1}".format(key,val.encode('utf-8'))
    lines = line.split("\n")
    oneline = ""
    for l in lines:
      if l:
        oneline += l.strip() + " "
    oneline = oneline.strip()
    ftw.write(oneline)
    ftw.write("\n")
    print oneline
  ftw.close()

if __name__ == '__main__':
  tweetsFile = "tweets.txt"
  file_to_write = "tweets_ID.txt"
  tweets = loadFileWithTweetIds(tweetsFile)
  tweetsDictionary = defaultdict()
  for tweet in tweets:
    text = retrieveTweet(tweet)
    if text:
      #print text
      tweetsDictionary[tweet] = text
    else:
      print "Not found: " + tweet
  storeTweetIdAndText(file_to_write, tweetsDictionary)
