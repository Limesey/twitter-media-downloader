from os.path import isfile

from argparse import Namespace
import urllib.request

def download_image(url):
    try:
        headers = {}
        headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0"

        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req)

        return urllib.request.urlopen(req).read()

    except Exception as exception:
        print("Error downloading image:\n", str(exception))

def download_from_tweet(tweet: list, options: Namespace):
    download_videos = options.no_video == False 
    download_images = options.no_image == False

    if(download_videos):
        if(tweet["contains_video"]):
            print("Do youtube-dl thing")

    if(download_images):
        images = tweet["images"]

        if(len(images) > 0):
            for img in images:
                image_url = img["src"]

                parsed_url = urllib.parse.urlparse(image_url)

                path = parsed_url.path
                query = parsed_url.query

                path_start = path.split("/")[1]

                if(path_start != "media"):
                    return

                name = path.split("/")[2]

                format = query[len("format=") : len(query)] \
                .split("&")
                format.pop()
                format = format[0]

                if(isfile(f"./images/{name}.{format}") and options.overwrite == False):
                    print(f"Skipping {image_url}: File already exists. To overwrite existing files use --overwrite")
                    return

                try:
                    with open(f"./images/{name}.{format}", "wb") as file:
                        file.write(download_image(image_url))
                        file.close()

                except PermissionError as err:
                    print("Unable to create file: ", str(err))