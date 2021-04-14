import argparse
from os import getenv

from twitter import Twitter

from dotenv import load_dotenv

from downloads import download_from_tweet
from data import export_tweets
from data import import_tweets

keywords = { 
    "bookmarks": "https://twitter.com/i/bookmarks" 
}

def main():
    parser = argparse.ArgumentParser(
        description="Twitter Media Downloader",
        usage= "tmd [<options>] [url]",
    )

    parser.add_argument("url", help="File/link to extract tweets from")
    parser.add_argument("--export", action="store_true", help="Export tweet data in JSON format")
    parser.add_argument("--file", action="store_true", help="Import tweet data from JSON file")
    parser.add_argument("--no-image", action="store_true", help="Do not download images")
    parser.add_argument("--no-video", action="store_true", help="Do not download videos")
    parser.add_argument("--overwrite", action="store_true", help="If a file already exists, it will be overwritten")

    args = parser.parse_args()

    url = args.url


    load_dotenv()

    twitter = None
    tweets = []

    if(args.file):
        try:
            tweets = import_tweets(url)
            print(f"[✔] Retrieve tweets from {url}")
        except (PermissionError) as e:
            print(f"Unable to open file {url}: {str(e)}")
            return
    else:
        twitter = Twitter(True, getenv("auth_token"))

        if(url in keywords):
            url = keywords[url]

        tweets = twitter.get_from(url)
        print(f"[✔] Retrieve tweets from {url}")

    if(args.export):
        print("Export tweets")
        export_tweets(tweets)
        return

    for tweet in tweets:
        download_from_tweet(tweet, args)
    
    if(twitter):
        twitter.driver.quit()

if(__name__== "__main__"):
    main()