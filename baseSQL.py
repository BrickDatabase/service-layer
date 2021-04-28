##############################################
# Author:                                    #
# Edward Riley                               #
##############################################

import os
import psycopg2
import time
from dotenv import load_dotenv

load_dotenv()
host = os.getenv('DB_HOST')
database = os.getenv('DB')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
port = os.getenv('DB_PORT')

# print("host='" + host + "' dbname='" + database + "' user='" + user + "' password='" + password + "' port='" + port + "'")

try:
    databaseVar = psycopg2.connect("host='" + host + "' dbname='" + database + "' user='" + user + "' password='" + password + "' port='" + port + "'")
    databaseVar.autocommit = True
    databaseVar.set_session(autocommit=True)

except:
    print("Database Connection Failed")
    exit(2)


def selectAllInformation():
    mycursor = databaseVar.cursor()
    mycursor.execute("SELECT * FROM information")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def returnSelectAllAbbreviation():
    mycursor = databaseVar.cursor()
    mycursor.execute("SELECT * FROM lookup")
    myresult = mycursor.fetchall()
    return myresult

def insertRowInformation(id, date, subscribers, activeSubscribers, submission, comment):
    mycursor = databaseVar.cursor()
    mycursor.execute("INSERT INTO information (subreddit_id, date, subscribers, active_subscribers, submission, comments) VALUES ('" + str(id) + "', '"+ str(date) + "', '" + str(subscribers) + "', '" + str(activeSubscribers) + "', '" + str(submission) + "', '" + str(comment) + "');")

def insertSubreddit(fullname, subreddit):
    tupleVar = (fullname, subreddit)
    mycursor = databaseVar.cursor()
    mycursor.execute("INSERT INTO lookup (name, abbreviation) VALUES(%s, %s)", tupleVar)

def deleteSubreddit(id):
    mycursor = databaseVar.cursor()
    mycursor.execute("DELETE from lookup WHERE id = " + str(id) + ";")
    mycursor.execute("DELETE from information WHERE subreddit_id = " + str(id) + ";")

def returnUpdateCount(id):
    mycursor = databaseVar.cursor()
    mycursor.execute("SELECT comments, submission, subscribers, active_subscribers from information WHERE subreddit_id = " + id + " ORDER BY date DESC LIMIT 1;")
    myresult = mycursor.fetchall()
    return myresult

def insertCalculation(date, comment, submission, subscribers, activeSubscriber, subreddit_id):
    time.sleep(1)
    mycursor = databaseVar.cursor()
    mycursor.execute('INSERT INTO schedule (posted, new_subscriber, new_comment, new_submission, new_active_subs, subreddit_id) VALUES ("' + str(date) + '",  "' + str(subscribers) + '",  "' + str(comment) + '",  "' + str(submission) + '",  "' + str(activeSubscriber) + '",  "' + str(subreddit_id) + '");')
    myresult = mycursor.fetchall()
    print(myresult)