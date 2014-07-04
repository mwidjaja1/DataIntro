import sys
import json

""" -- Matthew Widjaja: Project 1, Part 5 --
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
    tweetSTs = {}
    tweetScores = {}
    
    # --- Loads Up File ---
    # This code saves all coordinates from tweets with said data.
    for line in tweetFile:
        tweetLine = json.loads(line)
        tweetScore = 0
        
        # --- Save Tweet Data ---
        if 'text' in tweetLine:
            tweetText = tweetLine['text']
            tweetText = tweetText.encode('utf-8')
            tweetText = tweetText.split()
        
            # --- Save Place Data ---
            if 'place' in tweetLine:
                place = tweetLine['place']
                if place:
                    if place['country_code'] == 'US':
                        tweetST = place['full_name']
                        tweetST = tweetST[-2:]
                        if tweetST != 'SA':
                            if 'tweetST' in tweetSTs:
                                tweetSTs['tweetST'] = tweetSTs['tweetST'] + 1
                            else:
                                tweetSTs['tweetST'] = 1
                    
                 # --- Analysis of Tweet ---
                        for term in scores:
                            termFreq = tweetText.count(term)
                            if termFreq != 0:
                                tweetScore = (termFreq * scores[term]) + tweetScore
                                if tweetScores[tweetST]:
                                    tweetScores[tweetST] = tweetScores[tweetST] + tweetScore
                                else:
                                    tweetScores[tweetST] = 0        
                   


    # Paste in Analysis of File, and all sections below
    tweetFile.close()