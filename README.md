# FindARedditBot
Bot that reports posts and comments in /r/FindAReddit if they have a score of -3 or less.

## Setup
If you would like to use this bot for your own subreddit then all you need to do is clone
this repository and create a praw.ini file with the following contents:

```ini
[<config id>]
username=username
password=password
client_id=client_id
client_secret=client_secret
user_agent=user_agent
```

Open bot.py and replace reddit = praw.Reddit('findareddit') with reddit = praw.Reddit('<config id>') 
and subreddit = reddit.subreddit('findareddit') with the subreddit of your choice.

Change the global threshold variable to create a custom threshold for your posts.

Please do not use this bot without the permission from that subreddit's moderators.

## Usage
I recommend using cronjobs to make this bot run as frequently as you would like. 

If you are on Linux, open bash and type

```bash
crontab -e
```

This opens up a file where you can create a cronjob to be run every so often
f.x. if you want it to be run every 30 minutes you would put

```
30 * * * * * cd /FilePath/FindARedditBot; ./bot.py
```

## License

MIT: see the [LICENSE](https://github.com/Unnar/FindARedditBot/blob/master/LICENSE) file.
