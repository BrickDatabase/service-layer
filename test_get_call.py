import requests
import pytest

try:
    import baseAPI
except:
    print("baseAPI.py file not found. ")
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
def scheduled_job():
    subredditArray = ['rit','minecraft','bitcoin',
    'wallstreetbets','robinhood','gamestop',
    'playstation','xbox','nintendo',
    'gaming','lsrs']
    subredditID = 1
    print(subredditArray)
    for subreddit in subredditArray:
        # API endpoint will crash if you go too fast, after some tests, 1 second is the optimal speed. 
        time.sleep(1)
        print(subredditID)
        url = "/r/" + subreddit + "/about/"
        result = (baseAPI.getResult(url))
        submission = baseAPI.getSubmissionResult(subreddit)['metadata']['total_results']
        comment = baseAPI.getCommentResult(subreddit)['metadata']['total_results']
        subscribers = result['data']['subscribers']
        activeSubscribers = result['data']['active_user_count']
        date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        res = requests.post('https://brick-subreddit.herokuapp.com/info', 
        data={'subreddit_id':subredditID,
        'submission':submission,
        'comment':comment,
        'subscribers':subscribers,
        'active_subscribers':activeSubscribers,
        'date':date})
        print(res)
        if res.status_code == 200:
            print('Success!')
        elif res.status_code == 404:
            print('Not Found.')
        subredditID = subredditID + 1
def testing_op():
    try:
        scheduled_job()
    except:
        print('Dumping data gone wrong.')
        raise SystemExit(0)
def test_mytest():
        testing_op()
