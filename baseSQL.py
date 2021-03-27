##############################################
# Author:                                    #
# Edward Riley                               #
##############################################

username = "root"
password = "students"
hostname = "localhost"
database = "subreddit_db"

import mysql.connector

try:
    databaseVar = mysql.connector.connect(
        host=hostname,
        user=username,
        password=password,
        database=database
    )
except:
    print("Database Connection Failed")
    exit(2)


def selectAllInformation():
    mycursor = databaseVar.cursor()
    mycursor.execute("SELECT * FROM information")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)


def insertRowInformation(id, date, subscribers, activeSubscribers, submission, comment):
    mycursor = databaseVar.cursor()
    mycursor.execute("INSERT INTO `subreddit_db`.`information` (`subreddit_id`, `date`, `subscribers`, `active_subscribers`, `submission`, `comments`) VALUES ('" + str(id) + "', '"+ str(date) + "', '" + str(subscribers) + "', '" + str(activeSubscribers) + "', '" + str(submission) + "', '" + str(comment) + "');")

