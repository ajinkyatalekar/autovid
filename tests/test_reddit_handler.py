import pytest

import autovid as av

def test_invalid_url():
    with pytest.raises(Exception):
        reddit = av.RedditEngine()
        reddit.fetch("https://www.invalid_url.com")