#Q.1- What is an access token? Generate your access token for any API.(for example Twitter,Spotify etc).

# An access token is an object that describes the security context of a process or thread.
 #The information in a token includes the identity and privileges of the user account associated with the process or thread. ... 
 #The security identifier (SID) for the user's account. SIDs for the groups of which the user is a member.
 
#acess token   1011137913722195968-MOpQNI7It09dghlpiubdRg8TYjz2W6ub
#access_token_secret    U9zhBtTwG6WVlhhPhgdhffhySgBaZX2lZAQUJKLHS




#Q.2- Get the IP address of some common sites like Google, Facebook by using DNS lookup.

#ip address of google
 nslookup google.com
Non-authoritative answer:
Server:  UnKnown
Address:  2405:200:800::1

Name:    google.com
Addresses:  2404:6800:4002:807::200e
          172.217.161.14


#ip address of facebook
 nslookup facebook.com
Non-authoritative answer:
Server:  UnKnown
Address:  2405:200:800::1

Name:    facebook.com
Addresses:  2a03:2880:f12f:83:face:b00c:0:25de
          157.240.16.35



#Q.3- Using Tweepy library try to extract tweets from Twitter.
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



#Q.4- What is a difference between library and API . Figure it out with examples.
#A library is a collection of software that IMPLEMENTS an API.

#The “API” is a description of the interface between an application program and a library.

#So, for example, OpenGL is a “library” - and the API for it is defined in the OpenGL specification.
# The API comprises a bunch of named constants and a list of function calls specifications.

#The OpenGL library is the actual software that implements those function calls.

#The term “API” has also come to be used in Web design - indicating the interfaces to a web server that can be employed to access it from some other web server or web client.
# In that case, there may or may not be a “library” involved.







