import tweepy
import logging
import os


auth = tweepy.OAuthHandler("consumer_key", "consumer_sercret")
auth.set_access_token("token", "secret")

#Create API object
api = tweepy.API(auth)
logger = logging.getLogger()
file = None

final_tweet = None
max_likes = 0

try:
    api.verify_credentials()
    logger.info("API created")
except:
    logger.error("Error creating API", exe_info=True)

if(os.stat("tweetnum.txt").st_size == 0):
    pass
else:
    file = open("tweetnum.txt", "r")

    #find the most favorited tweet within the previous tweets
    fread = file.readlines()
    for line in fread:
        update_tweet = api.get_status(line)
        if (update_tweet.favorite_count >= max_likes):
            final_tweet = update_tweet
            max_likes = update_tweet.favorite_count
    api.update_status(final_tweet.text)

#find the new tweets to add to the file
file = open("tweetnum.txt", "w+")
for tweet in api.search(q="phrase", lang="en", rpp=1):
    if("@" in tweet.text):
        pass
    else:
        file.write(tweet.id_str + "\n")
file.close()
