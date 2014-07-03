import sys
import json
import re

# def hw():
#     print 'Hello, world!'

# def lines(fp):
#     print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)
    

if __name__ == '__main__':
    # --- Dictionary File ---
    # This opens up the dictionary file & converts it into a dict of Term, #Score
    afinnfile = open("AFINN-111.txt")
    scores = {}                             # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")     # The file is tab-delimited.
        scores[term] = int(score)           # Convert the score to an integer
    # print scores.items()                  # Print each (term, score) pair in the dict
    
    
    # --- Tweets File ---
    # This loads up the file with the Tweets
    tweetFile = open("problem_1_submission.txt")
    
    
    # -- Query for File Analysis --
    # This question asks if the 'Analysis of File' step needs to be ran. This is not
    # necessary if Part 2 of Assignment 1 was already ran.
    fileAna = raw_input('Does the tweet_file need to be analyzed for sentiment? (Y/N): ')
    
    
    # --- Creation & Analysis of File ---
    # We convert each (JSON) line of the tweet file into a dict format. From there, 
    #   we run an if-statement to see if there is a tweet in a given line. If a tweet
    #   does not exist in the file, we go to line 63 & load up the next line.
    if fileAna == 'Y':
        scoreFile = open("scoreOutput.txt","wb")
        tweetScores = []
        lineCount = 0
        
        for line in tweetFile:
            tweetLine = json.loads(line)
            tweetScore = 0
            lineCount = lineCount + 1
            print lineCount
        
            # --- Saving of Tweet ---
            # If there is a tweet in the given file, we save the tweet as tweetLine.
            if 'text' in tweetLine:
                tweetLine = tweetLine['text']
                wordsLine = tweetLine.split()
            
                # --- Analysis of Tweet ---
                # We then compare the tweet with the dictionary file to see if any words in 
                #   said tweet, EXACTLY match with the dictionary file. If so, we assign the
                #   tweet a point value, based on what is mentioned in said dictionary file.
                for word in wordsLine:
                    termLine = '\\b' + term + '\\b'
                    searchObj = re.findall(termLine,tweetLine)
                    if searchObj:
                        tweetScore = tweetScore + scores[term];
                    else:
                        wordsNew = 
                    
                    # --- Save Tweet Score to File ---
                    print >> scoreFile, tweetScore      # Saves the tweetScore to a list
                
                    # --- Decomposition of Tweet ---
                    words = inLine.split()
                    searchObj = re.findall(termLine,tweetLine)
                    for word in words:
                        if word != term:
                            newDict[word] = tweetScore
                            termLine = '\\b' + term + '\\b'
                            searchObj = re.findall(termLine,tweetLine)
                        if searchObj:
        tweetScore = tweetScore + scores[term];
        else:
                        continue
    print words
        
            else:
                print >> scoreFile, tweetScore      # Saves the tweetScore to a list
    
        tweetFile.close()
        scoreFile.close()
    
    
    # --- Opening previous File & Analysis of File ---
#    else:
#        for line in tweetFile:
#            tweetLine = line
#            if 'text' in tweetLine:
#                tweetLine = tweetLine['text']
#                unknown(tweetLine,scores[term])  