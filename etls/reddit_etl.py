import praw
from praw import Reddit
from utils.constant import POST_FIELDS
import pandas as pd
import numpy as np


def reddit_connect(client_id: str, secret_key: str, user_agent: str) -> Reddit:
    try:
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=secret_key,
            user_agent=user_agent
        )
        return reddit
    except Exception as e:
        print(e)
def extract_posts(reddit:Reddit, subreddit:str,time_filter:str, limit=None):
    sub_reddit = reddit.subreddit(subreddit)
    posts = sub_reddit.top(time_filter, limit)
    post_lst = []
    for post in posts:
        # print("Title:- ",post.title)
        post_dict=vars(post)
        post = {key:post_dict[key] for key in POST_FIELDS}
        post_lst.append(post)
        # print(post)
    return post_lst

def transform_data(post_df: pd.DataFrame):
    post_df['created_utc'] = pd.to_datetime(post_df['created_utc'], unit='s')
    post_df['over_18'] = np.where((post_df['over_18'] == True), True, False)
    post_df['author'] = post_df['author'].astype(str)
    edited_mode = post_df['edited'].mode()
    post_df['edited'] = np.where(post_df['edited'].isin([True, False]),post_df['edited'], edited_mode).astype(bool)
    post_df['num_comments'] = post_df['num_comments'].astype(int)
    post_df['score'] = post_df['score'].astype(int)
    post_df['title'] = post_df['title'].astype(str)

    return post_df

def load_data_to_csv(data: pd.DataFrame, path: str):
    data.to_csv(path, index=False)

