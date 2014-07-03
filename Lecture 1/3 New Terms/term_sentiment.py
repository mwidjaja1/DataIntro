import sys
import json
import re

""" -- Matthew Widjaja: Project 1, Part 3 --
    Calculates the sentiment score of terms in a tweet JSON file which do not currently
    exist on a sentiment file. We derive its values from the tweet score previously
    obtained in part 2.
"""   

if __name__ == '__main__':  
    # --- Input from Terminal ---
    # These variables represent the file inputs from the terminal
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    # --- Dictionary File ---
    # This opens up the dictionary file & converts it into a dict of Term, #Score
    afinnfile = sent_file
    scores = {}                             # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")     # The file is tab-delimited.
        scores[term] = int(score)           # Convert the score to an integer

    # --- Tweets File ---
    # This loads up the file with the Tweets
    tweetFile = tweet_file
    tweetScores = []

    # --- New Dictionary File ---
    # This loads up a list which will create a new dictionary file
    newList = []
    newDict = {}
    
    # --- Analysis of File ---
    # We convert each (JSON) line of the tweet file into a dict format. From there, 
    #   we run an if-statement to see if there is a tweet in a given line. If a tweet
    #   does not exist in the file, we go to line 63 & load up the next line.
    for line in tweetFile:
        tweetLine = json.loads(line)
        tweetScore = 0
        
        # --- For Line, If Text: Saving of Tweet ---
        # If there is a tweet in the given file, we save the tweet as tweetLine.
        if 'text' in tweetLine:
            tweetLine = tweetLine['text']
            tweetLine = tweetLine.encode('utf-8')
            tweetList = tweetLine.split()
        
          # --- For Line, If Text: Analysis of Tweet ---
            # We then compare the tweet with the dictionary file to see if any words in 
            #   said tweet, EXACTLY match with the dictionary file. If so, we assign the
            #   tweet a point value, based on what is mentioned in said dictionary file.
            for term in scores:
                termFreq = tweetList.count(term)
                if termFreq != 0:
                    tweetScore = (termFreq * scores[term]) + tweetScore
                    for i in range(0,termFreq):
                        tweetList.remove(term)
            
            # --- For Line, If Text: Computing Unmatched Values ---
            # We then take the list of words which were not caught (and removed) from the
            # tweet, and assign the previous tweetScore to it for the newDict. If a word
            # is already in the newDict, we average the tweetScores thus far.
            for new in tweetList:
                if new in newDict:
                    newDict[new] = (tweetScore + newDict[new])/2
                else:
                    newDict[new] = tweetScore
            
       
       # --- If No Text, Print Tweet Score ---
        else:
            print tweetScore
    
    # --- Closes TweetFile ---
    tweetFile.close()
    
    # --- Prints newDict as a List ---
    for i in newDict:
        print i, newDict[i]