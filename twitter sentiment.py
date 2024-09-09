# sentiment analysis with twitter api

import tweepy  
from textblob import TextBlob

wiki = TextBlob("Kevin is exited about using Twitter's API for sentiment analysis")
print(wiki.words) 
print(wiki.sentiment.polarity)  

consumer_key = "42qRIsYEQtj0UMxB7UvQB2ijF"
consumer_secret = "B05FjESnQrLKFIil07j6ifvJrr0YeYgPmdRRv1pAeTqdTtoYlH"

access_token ="1767640796927287296-JL9wVyMvb4Prv7SL4lmtoWs4f0StE8"
access_token_secret ='aMbITpJljVVSUflTGbgjAX9RUKXN65vaawpndb78mg9U1' 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# search method looks for a specific arguments, in this case a specific topic
public_tweets = api.search_tweets('trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment.polarity)
    
    
    
    
# seems I don't have enough permissions for extracting the tweets from the twitter api