import praw;
import config;
import time
import os
import markovify


def bot_login():
    bot = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = config.user_agent)
    print("Mohamed Mohamed is active.")

    return bot

def run_bot(bot, list):
    print("Obtaining 25 comments..")
    for comment in bot.subreddit('abatest').comments(limit=30) :
        if "?wisdom" in comment.body and comment.id not in comments_replied_to and not comment.author == bot.user.me():
            print("Ababoubian wisdom!")
            comment.reply(ababou())
            print(ababou())
            comments_replied_to.append(comment.id);
            with open("comments_replied_to.txt", "a") as file:
                file.write(comment.id + "\n")


    print("Sleeping for 10 seconds..")
    print(comments_replied_to)
    time.sleep(10)

def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = [];
    else:
        with open("comments_replied_to.txt", "r") as file:
            comments_replied_to = file.read();
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = list(filter(None, comments_replied_to))

    return comments_replied_to

def ababou():
    with open("wisdom.txt", encoding='utf8') as file:
        text = file.read()

    ababou = markovify.Text(text);

    sentence = ababou.make_short_sentence(140)

    return sentence;






bot = bot_login();
comments_replied_to = get_saved_comments()

while True:
    run_bot(bot, comments_replied_to)