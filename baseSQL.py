##############################################
# Author:                                    #
# Edward Riley                               #
##############################################

import psycopg2

try:
    databaseVar = psycopg2.connect("dbname=subreddit_db")
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
    mycursor.execute("SELECT abbreviation FROM lookup")
    myresult = mycursor.fetchall()
    return myresult

def insertRowInformation(id, date, subscribers, activeSubscribers, submission, comment):
    mycursor = databaseVar.cursor()
    mycursor.execute("INSERT INTO information (subreddit_id, date, subscribers, active_subscribers, submission, comments) VALUES ('" + str(id) + "', '"+ str(date) + "', '" + str(subscribers) + "', '" + str(activeSubscribers) + "', '" + str(submission) + "', '" + str(comment) + "');")

