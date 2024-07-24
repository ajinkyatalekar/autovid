# Autovid
Python package to automate and simplify video creation.

## What It Does
Autovid simplifies the text-to-speech video creation process by producing beautifully edited videos with minimal commands. :sparkles:

https://github.com/user-attachments/assets/ff08d7fc-5804-4ec7-930b-4a55bc38a834

## :rocket: Getting Started

### Prerequisites
1. Obtain a client key and secret from Reddit by creating an app [here](https://old.reddit.com/prefs/apps/).
2. Install autovid via pip
   
   ```sh
   pip install autovid
   ```
That's it!

### Usage
First, import autovid and update the Reddit API key and secret to let autovid access Reddit.
```py
import autovid as av

av.api_keys.client_id = "my_client_id"
av.api_keys.client_secret = "my_client_secret"
```

Autovid creates 'clips' that are combined to create the final video. Use the ```redditpostclip``` or ```redditcommentclip``` methods to create clips that can be passed to the ```makevideo``` method to generate the video.
```py
queue = [
  av.redditpostclip("")
]
```
