##############################################
# Author:                                    #
# Edward Riley                               #
##############################################
import requests

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
    import apscheduler
except: 
    print("apscheduler package not found.")
    exit(1)

try:
    import numpy
except:
    print("numpy package not found")
    exit(1)
    
try:
    import json
except:
    print("JSON package not found.")
    exit(1)

try:
    from datetime import datetime
    import time
except:
    print("Datetime or Time not found.")
    exit(1)

def convertTuple(tup):
    str =  ''.join(tup)
    return str

subredditArray = baseSQL.returnSelectAllAbbreviation()

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

# Every 11:00 AM 

#@sched.scheduled_job('cron', hour=11)

# Every 15 minutes
@sched.scheduled_job('interval', minutes=15)
def scheduled_job():
    subredditArray = baseSQL.returnSelectAllAbbreviation()

    subredditID = 1
    print(subredditArray)

    for subreddit in subredditArray:
        subreddit = numpy.asarray(subreddit)

        subredditID = subreddit[0] 
        # API endpoint will crash if you go too fast, after some tests, 2 second is the optimal speed on Heroku. 
        time.sleep(2)
        print(subredditID)
        
        url = "/r/" + subreddit[2] + "/about/"
        
        result = (baseAPI.getResult(url))
        submission = baseAPI.getSubmissionResult(subreddit[2])['metadata']['total_results']
        comment = baseAPI.getCommentResult(subreddit[2])['metadata']['total_results']
        subscribers = result['data']['subscribers']
        activeSubscribers = result['data']['active_user_count']
        date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        oldArray = baseSQL.returnUpdateCount(subreddit[0])
        for oldArrayVal in oldArray:
            oldComment          = oldArrayVal[0]
            oldSubmission       = oldArrayVal[1]
            oldSubscriber       = oldArrayVal[2]
            oldActiveSubscriber = oldArrayVal[3]

            commentChange = comment - oldComment
            submissionChange = submission - oldSubmission
            subscriberChange = subscribers - oldSubscriber
            activeSubChange = activeSubscribers - oldActiveSubscriber

            baseSQL.insertCalculation(date, commentChange, submissionChange, subscriberChange, activeSubChange, subredditID, comment, submission, subscribers, activeSubscribers)

        baseSQL.insertRowInformation(subredditID, date, subscribers, activeSubscribers, submission, comment)

    baseSQL.selectAllInformation()

sched.start()
