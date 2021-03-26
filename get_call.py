##############################################
# Author:                                    #
# Edward Riley                               #
##############################################

try:
    import baseAPI
except:
    print("baseAPI.py file not found. ")
    exit(1)

try:
    import baseSQL
except:
    print("baseSQL.py file not found.")
    exit(1)
try:
    import json
except:
    print("JSON package not found.")
    exit(1)

try:
    import mysql
except:
    print("MySQL package not found.")
    exit(1)

try:
    from datetime import datetime
    import time
except:
    print("Datetime or Time not found.")
    exit(1)

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