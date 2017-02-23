import praw
from datetime import datetime
from dateutil.relativedelta import relativedelta
import time

reddit = praw.Reddit('findareddit')

subreddit = reddit.subreddit('findareddit')

print("Going through submissions")
#Check if any submission is under the limit
for submission in subreddit.new(limit=100):
    if datetime.utcnow() > (datetime.utcfromtimestamp(submission.created_utc) + relativedelta(hours=24)):
        #Submission is more than 24 hours old, no need to look further
        continue
    elif submission.score <= -3:
        submission.report("Submission has a score of {}.".format(submission.score))
        print("-------------------")
        print("Found post with score of negative 3 or less.")
        print("Title: ", submission.title)
        print("-------------------")

print("Finished going through submissions, now sleeping before going through comments")
time.sleep(5)
print("Now going through comments")
for i, comment in subreddit.comments(limit=100):
    if datetime.utcnow() > (datetime.utcfromtimestamp(comment.created_utc) + relativedelta(hours=24)):
        #Comment is more than 24 hours old, no need to look further
        break
    if comment.score <= -3:
        comment.report("Comment has a score of {}.".format(comment.score))
        print("-------------------")
        print("Found comment with score of negative 3 or less.")
        print("Comment ID: ", comment.id)
        print("Comment body: ",comment.body)
        print("-------------------")
print("Finished going through all comments")


