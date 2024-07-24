import pytest
import os

import autovid as av

def test_no_api_keys():
    with pytest.raises(Exception):
        av.api_keys.client_id = ""
        clip = av.redditpostclip("https://www.reddit.com/r/reddit.com/comments/87/the_downing_street_memo/")

def test_valid_post_url():
    try:
        av.api_keys.client_id = os.getenv('REDDIT_CLIENT_ID')
        av.api_keys.client_secret = os.getenv('REDDIT_CLIENT_SECRET')
        clip = av.redditpostclip("https://www.reddit.com/r/reddit.com/comments/87/the_downing_street_memo/")
    except Exception:
        pytest.fail("Unexcepted exception thrown")

def test_invalid_post_url():
    with pytest.raises(Exception):
        clip = av.redditpostclip("https://www.invalid_url.com")