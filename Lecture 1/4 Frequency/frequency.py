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
    
    # --- Create List & Dictionary to track values ---
    # This creates a list & dictionary which will pair termHits per term
    termList = []
    termDict = {}
    wordCount = 0
    
    # --- Analysis of File ---
    # We convert each (JSON) line of the tweet file into a dict format.
    for line in tweetFile:
        tweetLine = json.loads(line)
        
        # --- For Line, If Text: Saving of Tweet ---
        # If there is a tweet in the given file, we save the tweet as tweetLine.
        if 'text' in tweetLine:
            tweetLine = tweetLine['text']
            tweetLine = tweetLine.encode('utf-8')
            tweetList = tweetLine.split()
        
            # --- For Line, If Text: Adding values to termDict & termList ---
            # We then see if the word is in termList (and thus, termDict). If so, we add
            # another mention of said word to termDict. If not, we add the new term to
            # both termDict & termList.
            for word in tweetList:
                wordCount = wordCount + 1
                termFreq = termList.count(word)
                if termFreq != 0:
                    termDict[word] = termDict[word] + 1
                else:
                    termDict[word] = 1
                    termList.append(word)
            
       
       # --- If No Text, Move to next Tweet ---
        else:
            continue
    
    # --- Closes TweetFile ---
    tweetFile.close()
    
    # --- Calculate Ratios in termDict & Prints Values ---
    for word in termDict:
        termDict[word] = termDict[word]/wordCount
        print word, termDict[word]