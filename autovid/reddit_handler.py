import praw

from . import api_keys
from . import exceptions

class RedditEngine:

    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=api_keys.client_id,
            client_secret=api_keys.client_secret,
            user_agent="autovid 0.0.1"
        )

        try:
            submission = self.reddit.submission(url="https://www.reddit.com/r/reddit.com/comments/87/the_downing_street_memo/")
            submission.title
        except:
            raise Exception(exceptions.INVALID_CREDENTIALS)

    def fetch(self,url):
        try:
            submission = self.reddit.submission(url=url)
        except:
            raise Exception(exceptions.INVALID_URL)
        
        print(submission.title)