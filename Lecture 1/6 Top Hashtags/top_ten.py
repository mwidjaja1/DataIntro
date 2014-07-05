import sys
import json

""" -- Matthew Widjaja: Project 1, Part 6 --
    Looks at a series of tweets to determine which hashtags are the most popular.
"""   

if __name__ == '__main__':  
    # --- Input from Terminal ---
    # These variables represent the file inputs from the terminal
    tweet_file = open(sys.argv[1])
    
    # --- Tweets File ---
    # This loads up the file with the Tweets
    tweetFile = tweet_file
    tweetHT = {}
    
    # --- Loads Up File ---
    # This code saves all coordinates from tweets with said data.
    for line in tweetFile:
        tweetLine = json.loads(line)
        tweetScore = 0
        
        # --- Save Tweet Data ---
        if 'entities' in tweetLine:
            tweetHash = tweetLine['entities']['hashtags']
            for ht in tweetHash:
                if ht:                
                    if ht["text"].encode("utf-8") in tweetHT.keys():
                        tweetHT[ht["text"].encode("utf-8")] += 1
                    else:
                        tweetHT[ht["text"].encode("utf-8")] = 1
                            
    # --- Close TweetFile ---
    tweetFile.close()   
    
    # --- Sorting Dictionary for Top 10 Values ---
    for line in sorted(tweetHT, key=tweetHT.get, reverse=True)[:10]:
        print line, tweetHT[line]