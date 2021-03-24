##############################################
# Author:                                    #
# Edward Riley                               #
##############################################

import baseAPI
import json

resultPopular = (baseAPI.getResult("subreddits/popular/"))

# SAVE THIS FOR FUTURE GUIDANCE ON KEYWORDS - EDWARD RILEY
# for each in resultPopular['data']['children'][0]['data']:
#    print(each)

prettyJSON = json.dumps(resultPopular['data']['children'][0]['data']['title'], indent=2)
counter=0
array = []
try:
    while True:
        subArray = []
        name = resultPopular['data']['children'][counter]['data']['title']
        subscribers = resultPopular['data']['children'][counter]['data']['subscribers']
        
        subArray.append(name)
        subArray.append(subscribers)

        array.append(subArray)
        counter = counter + 1
except:
    print("\nTotal Subreddits: " + str(counter) + "\n")
    print(array)

# print(prettyJSON)