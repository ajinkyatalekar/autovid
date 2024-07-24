from autovid.utils import reddit_handler
from autovid.utils.clip import Clip

__all__ = ['redditpostclip','redditcommentclip']

def redditpostclip(url):
    submission = reddit_handler._fetch_post(url)
    audio_str = submission.title + submission.selftext
    clip = Clip(audio_str)
    clip._selenium_wrapper = {'type':'post','url':'https://www.reddit.com/'+submission.id}
    return clip

def redditcommentclip(url):
    submission = reddit_handler._fetch_comment(url)
    audio_str = submission.body
    clip = Clip(audio_str)
    clip._selenium_wrapper = {'type':'comment','url':'https://www.reddit.com'+submission.permalink}
    return clip

def textclip(text):
    return Clip(text)