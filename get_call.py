##############################################
# Author:                                    #
# Edward Riley                               #
##############################################

import baseAPI
import baseSQL
import json
import mysql
from datetime import datetime
import time

subredditArray = ['rit', 'minecraft', 'bitcoin', 'wallstreetbets', 'robinhood', 'gamestop', 'playstation', 'xbox', 'nintendo', 'gaming']

subredditID = 1

for subreddit in subredditArray:
    
    # API endpoint will crash if you go too fast, after some tests, 1 second is the optimal speed. 
    time.sleep(1)
    print(subredditID)
    
    url = "/r/" + subreddit + "/about/"
    
    result = (baseAPI.getResult(url))
    submission = baseAPI.getSubmissionResult(subreddit)['metadata']['total_results']
    comment = baseAPI.getCommentResult(subreddit)['metadata']['total_results']

    #print(subreddit.capitalize() + " Subscribers:\t" + str(result['data']['subscribers']))
    #print(subreddit.capitalize() + " Active Users Count:\t" + str(result['data']['active_user_count']))
    #print(subreddit.capitalize() + " Submission:\t" + str(submission))
    #print(subreddit.capitalize() + " Comment:\t" + str(comment))

    subscribers = result['data']['subscribers']
    activeSubscribers = result['data']['active_user_count']
    date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    baseSQL.insertRowInformation(subredditID, date, subscribers, activeSubscribers, submission, comment)
    subredditID = subredditID + 1

baseSQL.selectAllInformation()