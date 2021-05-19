import praw
import os

#enter credentials to user PRAW: The Python Reddit API Wrapper
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='')
#scapping function
def scrapeSubreddit(subreddit_name, file_directory):
    '''Scrape target subreddit and save as txt file in target directory.
    
    Keyword arguments:
    subreddit_name -- the subreddit name (e.g. 'funny')
    file_directory -- name of directory to save files to
    '''
    if not os.path.isdir(file_directory):
        os.mkdir(file_directory)
    
    count = 0
    authors = {}
    for submission in reddit.subreddit(subreddit_name).top(limit=100000):
        if 0 < len(submission.selftext) < 201 and count < 100 and "https" not in submission.selftext:
            file_name = file_directory + subreddit_name + "_" + str(count) + ".txt"
            file = open(file_name, "w")
            title = submission.title + "\n"
            author = str(submission.author) + "\n"
            if (author in authors):
                freq = authors[author]
                authors[author] = freq + 1
            else:
                authors[author] = 1
            text = submission.selftext + "\n"
            file.writelines([title, author, text])
            count = count + 1
    print('# of posts collected from '+subreddit_name + ":" + str(count))

