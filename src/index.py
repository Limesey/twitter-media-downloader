from os import  getenv

from dotenv import load_dotenv
import dotenv

from twitter import Twitter

if(__name__ == "__main__"):
    load_dotenv()

    twitter = Twitter(getenv("auth_token"))
    twitter.get_bookmarks()