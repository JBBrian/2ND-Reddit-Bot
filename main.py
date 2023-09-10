import praw
import os
import time

reddit = praw.Reddit(
    client_id=os.environ.get('client_id'),
    client_secret=os.environ.get('client_secret'),
    user_agent='JEEP-BOT:v1.2',
    username='Chad-Jeeper-Bot',
    password=os.environ.get('pass'),
)

subreddit = reddit.subreddit('Jeep')
reply_comment = "It's a Jeep thing"

for post in subreddit.new(limit=40):
    try:
        existing_comment = None
        for comment in post.comments:
            if comment.author == reddit.user.me() and comment.body == reply_comment:
                existing_comment = comment
                break
        if existing_comment is None:
            post.reply(reply_comment)
            print('Bot commented')
            time.sleep(10)
    except Exception as e:
        print(f'An error has occurred: {e}')
