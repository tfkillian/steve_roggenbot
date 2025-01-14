## Stevenrogganbot Twitter bot version 1.1

'''
This is a Python bot to automate shitposting on Twitter. First, the script reads
a CSV file of images and tweets (past and present) as a Pandas dataframe and
selects the first unposted entry of an image and tweet. The script then reads a
YAML file containing the user app credentials, Tweepy client using these
credentials and posts the image and the tweet. If successful, the original CSV 
is edited to show that image and tweet pair has already been posted.
'''

import pandas as pd
import yaml
import tweepy
from datetime import datetime

# 1. Load the CSV into a Pandas DataFrame
csv_file = "tweet_list.csv"
df = pd.read_csv(csv_file)

# 2. Find the first row where posting_status is blank or NaN
# We consider a row valid for posting if 'posting_status' is empty ("") or NaN (missing value).
mask = (df["posting_status"].isna()) | (df["posting_status"] == "")
rows_to_post = df[mask]

# If there are no rows left to post, we can exit
# NOTE: this is unlikely to happen because we have a near-limitless amount of things to post
if rows_to_post.empty:
    print("No tweets left to post.")
    exit()

# Get the first row matching the condition
row_to_post = rows_to_post.iloc[0]

# Extract the image path and tweet text
image_path = row_to_post["image_path"]
tweet_text = row_to_post["tweet"]

# 3. Load Twitter Credentials from YAML file 
with open("credentials.yaml", "r") as file:
    config = yaml.safe_load(file)

# Extract Twitter credentials from the YAML config file
twitter_creds = config.get("twitter", {})
bearer_token = twitter_creds.get("bearer_token")
api_key = twitter_creds.get("api_key")
api_secret = twitter_creds.get("api_secret")
access_token = twitter_creds.get("access_token")
access_token_secret = twitter_creds.get("access_token_secret")

# 4. Initialize Tweepy for Twitter API v2 (Client) and v1.1 (for media)
# OAuth1 for media upload (v1.1)
auth = tweepy.OAuth1UserHandler(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)
api_v1 = tweepy.API(auth)

# Create a Tweepy client using the credentials
# Tweepy Client for Twitter API v2 actions (tweet posting)
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# 5. Upload Media (v1.1) and Post Tweet (v2)
try:
    # 5a. Upload image via API v1.1
    media = api_v1.media_upload(image_path)
    media_id = media.media_id_string

    # 5b. Create tweet with attached media via API v2
    response = client.create_tweet(text=tweet_text, media_ids=[media_id])
    print("Tweet posted successfully!")
    print("Response details:", response)

    # 6. Update posting_status for the posted row in the CSV
    posted_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df.loc[df["image_path"] == image_path, "posting_status"] = f"posted {posted_time}"

    # Save the DataFrame back to CSV
    df.to_csv(csv_file, index=False)
    print(f"CSV updated. Row with image_path '{image_path}' marked as posted.")

except Exception as e:
    print("Error posting tweet:", e)

print("yolo swag")
