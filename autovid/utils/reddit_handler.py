import praw
import os

from autovid import api_keys
from autovid import exceptions

__all__ = ['_fetch_post', '_fetch_comment']

def __getcredentials():
    
    # Testing ONLY
    if not api_keys.client_id:
        return praw.Reddit(
        client_id=os.getenv('REDDIT_CLIENT_ID'),
        client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
        user_agent="autovid 0.0.2"
        )

    return praw.Reddit(
        client_id=api_keys.client_id,
        client_secret=api_keys.client_secret,
        user_agent="autovid 0.0.2"
    )

def _fetch_post(url:str):
    reddit = __getcredentials()
    submission = reddit.submission(url=url)
    return submission

def _fetch_comment(url:str):
    reddit = __getcredentials()
    submission = reddit.comment(url=url)
    return submission