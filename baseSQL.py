from sqlalchemy import create_engine
import sqlalchemy

username = "root"
password = "students"
hostname = "localhost"
database = "subreddit_db"

engine = create_engine("mysql://" + username + ":" + password + "@" + hostname + "/" + database)

def insertRowInformation(id, date, subscribers, activeSubscribers, submission, comment):
    print("Executing insert statement for SubredditID#" + str(id))
    insertStatement = "INSERT INTO `subreddit_db`.`information` (`subreddit_id`, `date`, `subscribers`, `active_subscribers`, `submission`, `comments`) VALUES ('" + str(id) + "', '"+ str(date) + "', '" + str(subscribers) + "', '" + str(activeSubscribers) + "', '" + str(submission) + "', '" + str(comment) + "');"
    result = engine.execute(insertStatement)
    result.close()

def selectAllInformation():
    print("Fetching results!")
    result = engine.execute('SELECT * FROM information')
    for row in result:
        print(row)
    result.close()

