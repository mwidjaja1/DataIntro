import sys
import json

""" -- Matthew Widjaja: Project 1, Part 2 --
    Calculates the sentiment score of an output.txt file with a series of Tweets, using
    the score values assigned in AFINN-111.txt.
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
                    print termFreq, scores[term]
                    tweetScore = (termFreq * scores[term]) + tweetScore

            # --- For Line, If Text: Print Tweet Score ---
            print tweetScore
       
       # --- If No Text, Print Tweet Score ---
        else:
            print tweetScore
    
    tweetFile.close()