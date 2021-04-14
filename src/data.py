import json

def export_tweets(tweets: list):
    with open("./tweets.json", "w") as json_file:
        json.dump(tweets, json_file, indent=4, ensure_ascii=True)

        json_file.close()

def import_tweets(file):
    with open(file, "r") as json_file:
        return json.load(json_file)