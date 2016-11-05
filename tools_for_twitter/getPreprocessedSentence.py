# -*- coding: utf8 -*-
#!/usr/bin/python
"""
Methods used to preprocess the tweets
Created by nestoralvaro
"""
from collections import defaultdict
from nltk.corpus import sentiwordnet as swn
from nltk import word_tokenize
import re
import string

try:
  HIGHPOINTS = re.compile(u'[\U00010000-\U0010ffff]')
except re.error:
  # UCS-2 build
  HIGHPOINTS = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')

# Strings that we use to convert matched strings
USERNAME_STRING = "__username__"
URL_STRING = "__url__"
EMAIL_STRING = "__email__"
# In this case I put blanks at both sides because the numbers tend to be glued to words
NUMERIC_STRING = " __number__ "

# When in doubt about a regexp use this site: https://regex101.com/
# '[,.:;\'\" \?\(\)\[\]!\n]+'
# Matches twitter usernames. I have to indicate the start as well to prevent matching e-mail addresses
twitter_username_re = re.compile(r'(^|[^@\w])@(\w*)')
# Matches e-mails
email_string_re = re.compile(r'([\w\.-]+)@([\w\.-]+)')
# Matches strings duplicated more than 2 times
duplicated_char_re = re.compile(r'(.)\1\1+')
# Matches any numeric string
numeric_string_re = re.compile(r'-?[0-9]+')
# This regexp is to remove duplicated appearances of NUMERIC_STRING
numeric_string_duplicates_re = re.compile(ur'(__number__ )+')

# FLAGS used in "cleanString" method
NORMALIZE_USERNAMES = True
NORMALIZE_EMAIL = True
NORMALIZE_ELONGATIONS = True
NORMALIZE_NUMBERS = True

def cleanString(s, dic):
  """
  Cleans the input string and outputs it.
    - replaces USERNAME strings
    - replaces EMAIL strings
    - reduce elongated words
    - replaces NUMERIC strings
  """
  output = s
  # Twitter usernames are replaced with USERNAME_STRING (the "\\1" is used to keep the blank in case there's any
  if NORMALIZE_USERNAMES:
    out_tmp = re.sub(twitter_username_re, '\\1' + USERNAME_STRING, output)
    output = out_tmp
  # The EMAILS are replaced with EMAIL_STRING
  if NORMALIZE_EMAIL:
    out_tmp = re.sub(email_string_re, EMAIL_STRING, output)
    output = out_tmp
  # Reduce the length of some words (if the same letter is repeated more than twice we discarded extra copies) -> "adddderalllllll" would become "adderall"
  if NORMALIZE_ELONGATIONS:
    out_tmp = re.sub(duplicated_char_re, '\\1\\1', output)
    output = out_tmp
  # The NUMBERS are replaced with NUMERIC_STRING
  if NORMALIZE_NUMBERS:
    out_tmp = re.sub(numeric_string_re, NUMERIC_STRING, output)
    output = out_tmp
  # Remove extra blanks
  out_tmp = ' '.join(output.split())
  output = out_tmp
  # Discard "NUMERIC_STRING" duplications
  if NORMALIZE_NUMBERS:
    out_tmp = re.sub(numeric_string_duplicates_re, NUMERIC_STRING.lstrip(), output)
    pattern = NUMERIC_STRING.strip() + " . " + NUMERIC_STRING.strip()
    out_tmp = out_tmp.replace(pattern, NUMERIC_STRING)
    output = out_tmp
  return output

def preprocessText(rawText, dic):
  """
  Preprocess one tweet
    - remove non-ascii characters (e.g. emoji)
    - usernames, e-mails, NUMBERS are replaced (see "cleanString" method) + elongated
  """
  # Remove non-ascii characters
  rawText = rawText.decode('ascii','ignore')
  # lowercase the string
  # Apply strings replacemens + dictionary
  rawText = cleanString(rawText, dic)
  preprocessedText = rawText
  return preprocessedText

def countAstralCharacters(sentence):
  """
  This function counts the total number of astral characters in the sentence
  """
  # Try to convert it to UTF-8. Otherwise the regexp may not work well
  try:
    sentence = sentence.decode('utf8')
  except UnicodeError:
    pass
  return ((len(re.findall(HIGHPOINTS, sentence))) / (len(word_tokenize(sentence)) * 1.0) )

def loadDict(fileToRead, keyField, valueField):
  """
  Creates a dictionary using the required elements as
    key and the corresponding value for such key
  """
  ftr = open(fileToRead, 'r')
  fileLines = ftr.readlines()
  valuesSet = defaultdict(list)
  # Iterate over all sentences
  for line in fileLines:
    parts = line.split("\t")
    key = (parts[keyField]).decode('utf-8').strip()
    valuesSet[key] = (parts[valueField]).strip()
  ftr.close()
  return valuesSet

def prepareEmojiStrReplacement(emojiStr):
  """
  This method prepares the string replacement for the emojis
  """
  replacement = emojiStr.lower().replace(" ", "_")
  return " ***" + replacement + "*** "

def transformEmojisInString(sentence, emoji_StringReplacementDictionary):
  """
  Receives a sentence and performs the required replacement for the emojis
  """
  other_emoji_str = "Other Emoji character"
  transformedSentence = sentence
  transformedSentence = unicode(sentence, 'utf-8')
  # Only perform the transformation if there is an astral character
  if countAstralCharacters(sentence) > 0:
    # Iterate over the whole dictionary of emojis
    for k,v in emoji_StringReplacementDictionary.items():
      # If the current emoji is in the string, replace it
      if k in transformedSentence:
        transformedSentence = transformedSentence.replace(k, prepareEmojiStrReplacement(emoji_StringReplacementDictionary[k]))
    # JUST IN CASE: At this point the common emojis should be transformed, so I transform the rest to a custom string
    transformedSentence = re.sub(HIGHPOINTS, prepareEmojiStrReplacement(other_emoji_str), transformedSentence)
    # This exception should NEVER HAPPEN
    if countAstralCharacters(transformedSentence) > 0:
      raise Exception
  return transformedSentence
