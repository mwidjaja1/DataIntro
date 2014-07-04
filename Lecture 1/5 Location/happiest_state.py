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
    stateNames = states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }
    tweetScores = {
        'AK': 1,
        'AL': 1,
        'AR': 1,
        'AS': 1,
        'AZ': 1,
        'CA': 1,
        'CO': 1,
        'CT': 1,
        'DC': 1,
        'DE': 1,
        'FL': 1,
        'GA': 1,
        'GU': 1,
        'HI': 1,
        'IA': 1,
        'ID': 1,
        'IL': 1,
        'IN': 1,
        'KS': 1,
        'KY': 1,
        'LA': 1,
        'MA': 1,
        'MD': 1,
        'ME': 1,
        'MI': 1,
        'MN': 1,
        'MO': 1,
        'MP': 1,
        'MS': 1,
        'MT': 1,
        'NC': 1,
        'ND': 1,
        'NE': 1,
        'NH': 1,
        'NJ': 1,
        'NM': 1,
        'NV': 1,
        'NY': 1,
        'OH': 1,
        'OK': 1,
        'OR': 1,
        'PA': 1,
        'PR': 1,
        'RI': 1,
        'SC': 1,
        'SD': 1,
        'TN': 1,
        'TX': 1,
        'UT': 1,
        'VA': 1,
        'VI': 1,
        'VT': 1,
        'WA': 1,
        'WI': 1,
        'WV': 1,
        'WY': 1
    }
    tweetSTs = {
        'AK': 1,
        'AL': 1,
        'AR': 1,
        'AS': 1,
        'AZ': 1,
        'CA': 1,
        'CO': 1,
        'CT': 1,
        'DC': 1,
        'DE': 1,
        'FL': 1,
        'GA': 1,
        'GU': 1,
        'HI': 1,
        'IA': 1,
        'ID': 1,
        'IL': 1,
        'IN': 1,
        'KS': 1,
        'KY': 1,
        'LA': 1,
        'MA': 1,
        'MD': 1,
        'ME': 1,
        'MI': 1,
        'MN': 1,
        'MO': 1,
        'MP': 1,
        'MS': 1,
        'MT': 1,
        'NC': 1,
        'ND': 1,
        'NE': 1,
        'NH': 1,
        'NJ': 1,
        'NM': 1,
        'NV': 1,
        'NY': 1,
        'OH': 1,
        'OK': 1,
        'OR': 1,
        'PA': 1,
        'PR': 1,
        'RI': 1,
        'SC': 1,
        'SD': 1,
        'TN': 1,
        'TX': 1,
        'UT': 1,
        'VA': 1,
        'VI': 1,
        'VT': 1,
        'WA': 1,
        'WI': 1,
        'WV': 1,
        'WY': 1
    }
    
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
        
            # --- Save State > Only if its present & in US ---
            if 'place' in tweetLine:
                place = tweetLine['place']
                if place:
                    if place['country_code'] == 'US':
                        tweetST = place['full_name']
                        tweetST = tweetST[-2:]
                        if tweetST in tweetScores:
                            if 'tweetST' in tweetSTs:
                                tweetSTs['tweetST'] = tweetSTs['tweetST'] + 1
                            else:
                                tweetSTs['tweetST'] = 1
                
                            # --- Analysis of Tweet ---
                            for term in scores:
                                termFreq = tweetText.count(term)
                                if termFreq != 0:
                                    tweetScore = (termFreq * scores[term]) + tweetScore
                            
                            # --- Saving of Tweet Score ---
                            tweetScores[tweetST] = tweetScores[tweetST] + tweetScore
    
    # --- Close TweetFile ---
    tweetFile.close()                            
    
    # --- Averaging of Sentiment Scores per State ---
    for state in tweetScores:
        tweetScores[state] = tweetScores[state] / tweetSTs[state]
    
    # --- Calculating Best State 
    bestState = max(tweetScores, key=tweetScores.get)
    print stateNames[bestState]
