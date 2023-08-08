import pandas as pd
import json
import re
import seaborn
import datetime
import demoji
import snscrape.modules.twitter as twitterScraper


def scrape_keywords(query):
    tweets = []
    limit = 100

    for tweet in twitterScraper.TwitterSearchScraper(query, top=True).get_items():
        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.url, tweet.date, tweet.content, tweet.renderedContent, tweet.id, tweet.user.username,
                           tweet.user.id, tweet.user.displayname, tweet.user.description, tweet.user.verified, tweet.user.created,
                           tweet.user.followersCount, tweet.user.friendsCount, tweet.user.statusesCount, tweet.user.favouritesCount,
                           tweet.user.listedCount, tweet.user.mediaCount, tweet.user.location, tweet.user.linkUrl,
                           tweet.user.profileImageUrl, tweet.retweetCount, tweet.likeCount,
                           tweet.lang, tweet.replyCount])

    df = pd.DataFrame(tweets, columns=["url", "date", "Content", "renderedContent", "id", "username", "userID", "displayname", "description",
                                       "verified", "datetime", "followers", "following", "statusCount", "favouriteCount", "listedCount",
                                       "mediaCount", "Location", "linkURL", "profileImageUrl", "retweetCount", "likesCount",
                                       "language", "replyCount"])
    print(df.head(2))
    print(df.info())
    print(df.head())

    print(df['Content'])

    new_emojies = []
    for i in df['Content']:
        new = demoji.findall_list(i)
        new_emojies.append(new)

    new_emojies
    df['new_text_emojies'] = new_emojies

    print(df)

    # Eliminating all the emojies present in the Content

    new_User = []
    for i, j in enumerate(df["Content"]):
        ome = j
        emoji_pattern = re.compile("["u"\U0001F600-\U0001F64F"  # emoticons
                                   u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                   u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                   u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                   u"\U00002500-\U00002BEF"  # chinese char
                                   u"\U00002702-\U000027B0"
                                   u"\U00002702-\U000027B0"
                                   u"\U000024C2-\U0001F251"
                                   u"\U0001f926-\U0001f937"
                                   u"\U00010000-\U0010ffff"
                                   u"\u2640-\u2642"
                                   u"\u2600-\u2B55"
                                   u"\u200d"
                                   u"\u23cf"
                                   u"\u23e9"
                                   u"\u231a"
                                   u"\ufe0f"  # dingbats
                                   u"\u092d]+", flags=re.UNICODE)
        pattern = emoji_pattern.sub(r'', ome)
        pattern = pattern.lower()
        emoji = re.compile('[!@#$%^&*<>?]|[\n]')
        emoji_done = emoji.sub('', pattern)
        final_result = re.sub(
            r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', "", emoji_done)
        new_User.append(final_result)

    df["Cleaned_Content"] = new_User

    print(df.head(2))

    # Converting dtype: datetime64[ns, UTC] to string or bytes-like object

    df["date"] = df["date"].apply(lambda x: str(x))

    # Extracting Date
    new_datetime = []
    for i in df["date"]:
        n1 = datetime.datetime.strptime(i[:10], "%Y-%m-%d").date()
        new_datetime.append(n1)

    df["Date"] = new_datetime

    # Extracting time
    new_time = []
    for i in df["date"]:
        n1 = datetime.datetime.strptime(i[11:-6], "%H:%M:%S").time()
        new_time.append(n1)

    df["Time"] = new_time

    print(df.head(5))
    df['tweet_date'] = pd.to_datetime(df.datetime).dt.tz_localize(None)
    df.drop("datetime", axis=1, inplace=True)

    print(df.head())

    try:
        twitter_table = df["Content"]
        twitter_table.reset_index(drop=True, inplace=True)
        print(twitter_table.head())
        file_name = "keyword_tweets.xlsx"
        twitter_table.to_excel(file_name)
        print("\nRecords sucessfully scraped and stored ")
    except Exception as e:
        print(e)
