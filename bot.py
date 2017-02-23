import praw
from datetime import datetime
from dateutil.relativedelta import relativedelta
import time

reddit = praw.Reddit('findareddit')

subreddit = reddit.subreddit('findareddit')

#List of reported submissions
reported_submissions = []
#List of reported comments
reported_comments = []

try:
    with open('reported_submissions.txt', 'r') as f:
        for line in f:
            reported_submissions.append(line.strip())
except FileNotFoundError:
    with open('reported_submissions.txt', 'w') as f:
        pass

try:
    with open('reported_comments.txt', 'r') as f:
        for line in f:
            reported_comments.append(line.strip())
except FileNotFoundError:
    with open('reported_comments.txt', 'w') as f:
        pass

print("Going through submissions")
#Check if any submission is under the limit
for submission in subreddit.new(limit=100):
    if datetime.utcnow() > (datetime.utcfromtimestamp(submission.created_utc) + relativedelta(hours=24)):
        #Submission is more than 24 hours old, no need to look further
        continue
    elif submission.score <= -3:
        print("-------------------")
        print("Found post with score of negative 3 or less.")
        print("Title: ", submission.title)
        print("-------------------")
        if submission.id in reported_submissions:
            print("Submission has already been reported, continuing.")
            continue    
        submission.report("Submission has a score of {}.".format(submission.score))
        with open('reported_submissions.txt', 'a') as f:
            f.write(submission.id+'\n')
        print("Submission has been reported and written to file.")


print("Finished going through submissions, now sleeping before going through comments")
time.sleep(5)
print("Now going through comments")
for comment in subreddit.comments(limit=100):
    if datetime.utcnow() > (datetime.utcfromtimestamp(comment.created_utc) + relativedelta(hours=24)):
        #Comment is more than 24 hours old, no need to look further
        break
    if comment.score <= -3:
        print("-------------------")
        print("Found comment with score of negative 3 or less.")
        print("Comment ID: ", comment.id)
        print("Comment body: ",comment.body)
        print("-------------------")
        if comment.id in reported_comments:
            print("Comment has already been reported, continuing.")
            continue
        comment.report("Comment has a score of {}.".format(comment.score))
        with open('reported_comments.txt', 'a') as f:
            f.write(comment.id+'\n')
        print("Comment has been reported and written to file.")
print("Finished going through all comments")


