import sys
import json

""" -- Matthew Widjaja: Project 1, Part 4 --
    Looks at a series of tweets in order to determine which state is the happiest.
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
    tweetLocation = []
    tweetScores = []
    
    # --- Keeping Tweets with Location Data ---
    # This code keeps the tweets with location data that places it in USA. All other
    # tweets are removed from tweetLibrary. This removes deleted tweets as a result.
    for line in tweetFile:
        tweetLine = json.loads(line)
        
        if 'coordinates' in tweetLine:
            
    
    
# Paste in Analysis of File, and all sections below
    
    tweetFile.close()