from . import api_keys

class RedditEngine:
    def __init__(self):
        self.reddit = Reddit(
            client_id=api_keys.client_id,
            client_secret=api_keys.client_secret,
            user_agent="autovid 0.0.1"
        )

    def fetch(self,url):
        pass