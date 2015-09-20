import tweepy

consumer_key = ''
consumer_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

twitterUser = tweepy.api.get_user('ZakDoesGaming')
print(twitterUser.followers_count)

