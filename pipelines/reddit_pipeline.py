from etls.reddit_etl import reddit_connect, extract_posts,transform_data,load_data_to_csv
from utils.constant import CLIENT_ID, SECRET_KEY,OUTPUT_PATH
import pandas as pd
def reddit_pipeline(file_name:str, subreddit:str, time_filter:'day', limit=None):
    # connecting to reddit instance
    reddit = reddit_connect(client_id=CLIENT_ID, secret_key=SECRET_KEY, user_agent='data-api')
    # subreddit='dataengineering'
    posts = extract_posts(reddit,subreddit,time_filter,limit)
    # transformation
    post_df=pd.DataFrame(posts)
    post_df=transform_data(post_df)
    print(post_df)
    # load to csv

    file_path=f'{OUTPUT_PATH}/{file_name}.csv'
    load_data_to_csv(post_df,file_path)


    return file_path
