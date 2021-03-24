##############################################
# Author:                                    #
# Edward Riley                               #
##############################################

# Note To Self for Edward: Take a look at active_user_count, accounts_active for {/r/[subreddit]/about/}


import baseAPI
import json

subredditArray = ['rit', 'minecraft', 'bitcoin', 'wallstreetbets', 'robinhood', 'gamestop', 'playstation', 'xbox', 'nintendo', 'gaming']


for subreddit in subredditArray:
    url = "/r/" + subreddit + "/about/"
    
    result = (baseAPI.getResult(url))
    print(subreddit.capitalize() + ": \t" + str(result['data']['subscribers']))

url = "/r/rit/api/info"
result = (baseAPI.getResult(url))
print(result['data'])