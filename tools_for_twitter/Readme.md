# Twitter tools

## Downloading tweets

To download the tweets, the command to be entered in the console is the following:

**python download_tweets.py**

Running that command will create a file named *tweets_ID.txt* in this folder. That file will contain all the tweets using the following format:
tweetID <TAB> text

**tweetID** is the unique tweet identifier.
**text** Is the text in that tweet.

## Preprocessing the texts

Once the tweets have been downloaded, then some preprocessing to remove numbers and perform other replacements. To preprocess the downloaded tweets the command to be entered in the console is the following:

**python preprocessSentences.py**

Running this script will create a folder named *"tweets"* containing all the text files (".txt").


## Loading text files with the tweets in Brat.
Then, you have to copy all the files located in the newly generated *"tweets"* folder to
*gold/twitter/* or to *gold_conflated/twitter/* folders. Doing so will allow you to see the annotations in Brat tool (http://brat.nlplab.org/).
