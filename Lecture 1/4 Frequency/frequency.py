import sys
import json
import re

""" -- Matthew Widjaja: Project 1, Part 4 --
    Calculates the frequency ratio of each term in a series of tweets
"""   

if __name__ == '__main__':  
    # --- Input from Terminal ---
    # These variables represent the file inputs from the terminal
    tweetFile = open(sys.argv[1])
    
    # --- Create Dictionary to track values ---
    # This creates a dictionary which will pair termHits per term
    
    
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
        
            
            
            
            # --- For Line, If Text: Computing Unmatched Values ---
            # We then take the list of words which were not caught (and removed) from the
            # tweet, and assign the previous tweetScore to it for the newDict. If a word
            # is already in the newDict, we average the tweetScores thus far.
            for word in tweetList:
                termFreq = tweetList.count(word)
                if termFreq != 0:
                    newDict[new] = (tweetScore + newDict[new])/2
                else:
                    newDict[new] = tweetScore
            
       
       # --- If No Text, Print Tweet Score ---
        else:
            print tweetScore
    
    # --- Closes TweetFile ---
    tweetFile.close()