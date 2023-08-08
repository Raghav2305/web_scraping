import tweepy
from tweepy import OAuthHandler
import pandas as pd
import time


def scrape_username(username):

    consumer_key = "LlD25Y2bvaoKZcOZO9pJkICDq"
    consumer_secret = "QLPVNJSuieVyxZ5CLyTy6iJs3LU4AhYCgDbYAoLno33qGU3n5n"
    access_token_key = "1512426760092102658-6pjoIzx2joOJl4LxkvwUlFzfVieK8i"
    access_token_secret = "JhRMJlvzOs1AUxUTZYlOeEwyqaEz9ILRUTRVmcl0Unnz4"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    count = 10

    df_user_tweets = pd.DataFrame()
    # Creation of query method using appropriate parameters
    tweets = tweepy.Cursor(
        api.user_timeline, id=username, lang="en").items(count)

    for tweet in tweets:
        df_user_tweets = df_user_tweets.append(
            {'Created at': tweet._json['created_at'],
             'User ID': tweet._json['id'],
             'User Name': tweet.user._json['name'],
             #          'follower': tweet.user._json['following_count'],
             'listed count': tweet.user._json['listed_count'],
             #          'media count': tweet.user._json['media_count'],
             'retweet count': tweet._json['retweet_count'],
             #          'profile type': tweet._json['profile_type'],
             'Text': tweet._json['text'],
             'Description': tweet.user._json['description'],
             'Location': tweet.user._json['location'],
             'Followers Count': tweet.user._json['followers_count'],
             'Friends Count': tweet.user._json['friends_count'],
             'Statuses Count': tweet.user._json['statuses_count'],
             'Profile Image Url': tweet.user._json['profile_image_url'],
             #          'likes': tweet._json['like_count'],
             }, ignore_index=True)

    print(df_user_tweets)
    print(df_user_tweets['Text'])

    try:
        twitter_table = df_user_tweets['Text']
        twitter_table.reset_index(drop=True, inplace=True)
        print(twitter_table.head())
        file_name = "username_tweets.xlsx"
        twitter_table.to_excel(file_name)
        print("\nRecords sucessfully scraped and stored ")
    except Exception as e:
        print(e)
