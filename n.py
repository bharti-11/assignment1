import tweepy
consumer_key='qHEq5rqTrMjhdgjkjkjb7WM'
consumer_secret='zS8AC5K3FOjAMohigjgjk878t8er24u8abFmKmCUwmqKLR4qwW'
access_token='1011137913722195968-MO97DVghuhumSodRg8TYjz2W6ub'
access_token_secret='U9zhBtTwG6WVlhhPhgdhffhySgBaZX2lZAQUJKLHS'
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
tweets=api.search('#jobs',lang="en",count=3,tweet_mode="extended")
for tweet in tweets:
    print(".............")
    print(tweet.full_text)
    print(".............")