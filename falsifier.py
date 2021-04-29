import requests
import random

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

counter = 0
currentMonth = 4
currentDay = 29

# Subscribers
redditOneSubscribers = 20572
redditTwoSubscribers = 5118986
redditThreeSubscribers = 2786986
redditFourSubscribers = 9970617
redditFiveSubscribers = 732977
redditSixSubscribers = 74629
redditSevenSubscribers = 507490
redditEightSubscribers = 275714
redditNineSubscribers = 2079704
redditTenSubscribers = 1066693

# Active Subscribers
redditOneActiveSubscribers = 301
redditTwoActiveSubscribers = 28724
redditThreeActiveSubscribers = 9968
redditFourActiveSubscribers = 224025
redditFiveActiveSubscribers = 2021
redditSixActiveSubscribers = 320
redditSevenActiveSubscribers =1774
redditEightActiveSubscribers =1221
redditNineActiveSubscribers = 2005
redditTenActiveSubscribers = 7334



# Submission
redditOneSubmission = 35330
redditTwoSubmission = 2177169
redditThreeSubmission = 963083
redditFourSubmission = 1518235
redditFiveSubmission = 90990
redditSixSubmission = 71435
redditSevenSubmission = 197966 
redditEightSubmission = 110042
redditNineSubmission = 213519
redditTenSubmission = 375125


# Comments
redditOneComments = 328339
redditTwoComments = 18695819
redditThreeComments = 11303160
redditFourComments = 39908289
redditFiveComments = 592727
redditSixComments = 669154
redditSevenComments = 1170266
redditEightComments = 635837
redditNineComments =  3681233
redditTenComments = 2066560


while counter <= 30:
    date = "2021-" + str(currentMonth) + "-" + str(currentDay) + " 12:00:35"
    calcDate = "2021-" + str(currentMonth) + "-" + str(currentDay)
    print(counter)

    # 1 
    randomSubscriber   = random.randrange(35, 50)
    randomActiveSubscriber   = random.randrange(1, 5) - random.randrange(1, 3)
    randomComments = random.randrange(300, 400)
    randomSubmission  = random.randrange(200, 300)

    redditOneSubscribers = redditOneSubscribers - randomSubscriber
    redditOneActiveSubscribers = redditOneActiveSubscribers - randomActiveSubscriber
    redditOneSubmission = redditOneSubmission - randomComments
    redditOneComments = redditOneComments - randomSubmission
    
    baseSQL.insertRowInformation(1, date, redditOneSubscribers, redditOneActiveSubscribers, redditOneSubmission, redditOneComments)
    baseSQL.insertCalculation(calcDate, randomComments, randomSubmission, randomSubscriber, randomActiveSubscriber, 1, redditOneComments, redditOneSubmission, redditOneSubscribers, redditOneActiveSubscribers)
    
    # 2
    randomSubscriber   = random.randrange(35, 50)
    randomActiveSubscriber   = random.randrange(1, 5) - random.randrange(1, 3)
    randomComments = random.randrange(300, 400)
    randomSubmission  = random.randrange(200, 300)

    redditTwoSubscribers = redditTwoSubscribers - randomSubscriber
    redditTwoActiveSubscribers = redditTwoActiveSubscribers - randomActiveSubscriber
    redditTwoSubmission = redditTwoSubmission - randomComments
    redditTwoComments = redditTwoComments - randomSubmission

    baseSQL.insertRowInformation(2, date, redditTwoSubscribers, redditTwoActiveSubscribers, redditTwoSubmission, redditTwoComments)
    baseSQL.insertCalculation(calcDate, randomComments, randomSubmission, randomSubscriber, randomActiveSubscriber, 2, redditTwoComments, redditTwoSubmission, redditTwoSubscribers, redditTwoActiveSubscribers)

    # 3
    randomSubscriber   = random.randrange(35, 50)
    randomActiveSubscriber   = random.randrange(1, 5) - random.randrange(1, 3)
    randomComments = random.randrange(300, 400)
    randomSubmission  = random.randrange(200, 300)

    redditThreeSubscribers = redditThreeSubscribers - randomSubscriber
    redditThreeActiveSubscribers = redditThreeActiveSubscribers - randomActiveSubscriber
    redditThreeSubmission = redditThreeSubmission - randomComments
    redditThreeComments = redditThreeComments - randomSubmission
    
    baseSQL.insertRowInformation(3, date, redditThreeSubscribers, redditThreeActiveSubscribers, redditThreeSubmission, redditThreeComments)
    baseSQL.insertCalculation(calcDate, randomComments, randomSubmission, randomSubscriber, randomActiveSubscriber, 3, redditThreeComments, redditThreeSubmission, redditThreeSubscribers, redditThreeActiveSubscribers)

    # 4
    randomSubscriber   = random.randrange(35, 50)
    randomActiveSubscriber   = random.randrange(1, 5) - random.randrange(1, 3)
    randomComments = random.randrange(300, 400)
    randomSubmission  = random.randrange(200, 300)

    redditFourSubscribers = redditFourSubscribers - randomSubscriber
    redditFourActiveSubscribers = redditFourActiveSubscribers - randomActiveSubscriber
    redditFourSubmission = redditFourSubmission - randomComments
    redditFourComments = redditFourComments - randomSubmission
    
    baseSQL.insertRowInformation(4, date, redditFourSubscribers, redditFourActiveSubscribers, redditFourSubmission, redditFourComments)
    baseSQL.insertCalculation(calcDate, randomComments, randomSubmission, randomSubscriber, randomActiveSubscriber, 4, redditFourComments, redditFourSubmission, redditFourSubscribers, redditFourActiveSubscribers)
    
    # 5
    randomSubscriber   = random.randrange(35, 50)
    randomActiveSubscriber   = random.randrange(1, 5) - random.randrange(1, 3)
    randomComments = random.randrange(300, 400)
    randomSubmission  = random.randrange(200, 300)

    redditFiveSubscribers = redditFiveSubscribers - randomSubscriber
    redditFiveActiveSubscribers = redditFiveActiveSubscribers - randomActiveSubscriber
    redditFiveSubmission = redditFiveSubmission - randomComments
    redditFiveComments = redditFiveComments - randomSubmission
    
    baseSQL.insertRowInformation(5, date, redditFiveSubscribers, redditFiveActiveSubscribers, redditFiveSubmission, redditFiveComments)
    baseSQL.insertCalculation(calcDate, randomComments, randomSubmission, randomSubscriber, randomActiveSubscriber, 5, redditFiveComments, redditFiveSubmission, redditFiveSubscribers, redditFiveActiveSubscribers)
    
    # 6
    randomSubscriber   = random.randrange(35, 50)
    randomActiveSubscriber   = random.randrange(1, 5) - random.randrange(1, 3)
    randomComments = random.randrange(300, 400)
    randomSubmission  = random.randrange(200, 300)

    redditSixSubscribers = redditSixSubscribers - randomSubscriber
    redditSixActiveSubscribers = redditSixActiveSubscribers - randomActiveSubscriber
    redditSixSubmission = redditSixSubmission - randomComments
    redditSixComments = redditSixComments - randomSubmission
    
    baseSQL.insertRowInformation(6, date, redditSixSubscribers, redditSixActiveSubscribers, redditSixSubmission, redditSixComments)
    baseSQL.insertCalculation(calcDate, randomComments, randomSubmission, randomSubscriber, randomActiveSubscriber, 6, redditSixComments, redditSixSubmission, redditSixSubscribers, redditSixActiveSubscribers)
    
    # 7
    randomSubscriber   = random.randrange(35, 50)
    randomActiveSubscriber   = random.randrange(1, 5) - random.randrange(1, 3)
    randomComments = random.randrange(300, 400)
    randomSubmission  = random.randrange(200, 300)

    redditSevenSubscribers = redditSevenSubscribers - randomSubscriber
    redditSevenActiveSubscribers = redditSevenActiveSubscribers - randomActiveSubscriber
    redditSevenSubmission = redditSevenSubmission - randomComments
    redditSevenComments = redditSevenComments - randomSubmission
    
    baseSQL.insertRowInformation(7, date, redditSevenSubscribers, redditSevenActiveSubscribers, redditSevenSubmission, redditSevenComments)
    baseSQL.insertCalculation(calcDate, randomComments, randomSubmission, randomSubscriber, randomActiveSubscriber, 7, redditSevenComments, redditSevenSubmission, redditSevenSubscribers, redditSevenActiveSubscribers)
    
    # 8
    randomSubscriber   = random.randrange(35, 50)
    randomActiveSubscriber   = random.randrange(1, 5) - random.randrange(1, 3)
    randomComments = random.randrange(300, 400)
    randomSubmission  = random.randrange(200, 300)

    redditEightSubscribers = redditEightSubscribers - randomSubscriber
    redditEightActiveSubscribers = redditEightActiveSubscribers - randomActiveSubscriber
    redditEightSubmission = redditEightSubmission - randomComments
    redditEightComments = redditEightComments - randomSubmission
    
    baseSQL.insertRowInformation(8, date, redditEightSubscribers, redditEightActiveSubscribers, redditEightSubmission, redditEightComments)
    baseSQL.insertCalculation(calcDate, randomComments, randomSubmission, randomSubscriber, randomActiveSubscriber, 8, redditEightComments, redditEightSubmission, redditEightSubscribers, redditEightActiveSubscribers)

    
    # 9
    randomSubscriber   = random.randrange(35, 50)
    randomActiveSubscriber   = random.randrange(1, 5) - random.randrange(1, 3)
    randomComments = random.randrange(300, 400)
    randomSubmission  = random.randrange(200, 300)

    redditNineSubscribers = redditNineSubscribers - randomSubscriber
    redditNineActiveSubscribers = redditNineActiveSubscribers - randomActiveSubscriber
    redditNineSubmission = redditNineSubmission - randomComments
    redditNineComments = redditNineComments - randomSubmission
    
    baseSQL.insertRowInformation(9, date, redditNineSubscribers, redditNineActiveSubscribers, redditNineSubmission, redditNineComments)
    baseSQL.insertCalculation(calcDate, randomComments, randomSubmission, randomSubscriber, randomActiveSubscriber, 9, redditNineComments, redditNineSubmission, redditNineSubscribers, redditNineActiveSubscribers)

    # 10
    randomSubscriber   = random.randrange(35, 50)
    randomActiveSubscriber   = random.randrange(1, 5) - random.randrange(1, 3)
    randomComments = random.randrange(300, 400)
    randomSubmission  = random.randrange(200, 300)

    redditTenSubscribers = redditTenSubscribers - randomSubscriber
    redditTenActiveSubscribers = redditTenActiveSubscribers - randomActiveSubscriber
    redditTenSubmission = redditTenSubmission - randomComments
    redditTenComments = redditTenComments - randomSubmission
    
    baseSQL.insertRowInformation(10, date, redditTenSubscribers, redditTenActiveSubscribers, redditTenSubmission, redditTenComments)
    baseSQL.insertCalculation(calcDate, randomComments, randomSubmission, randomSubscriber, randomActiveSubscriber, 10, redditTenComments, redditTenSubmission, redditTenSubscribers, redditTenActiveSubscribers)
     
    


    currentDay = currentDay - 1
    if currentDay == 0:
        currentMonth = 3
        currentDay = 31


    counter = 1 + counter