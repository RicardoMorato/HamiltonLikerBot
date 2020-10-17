import tweepy
from env import *

auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
user = api.me()

keyword = 'Python'
numbers_of_tweets = 5

for tweet in tweepy.Cursor(api.search, keyword).items(numbers_of_tweets):
    try:
        print(tweet.text)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
