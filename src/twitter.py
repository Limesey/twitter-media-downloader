from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

class Twitter:
    def __init__(self, headless: bool = None, auth_token: str = None):
        options = webdriver.FirefoxOptions()

        if(headless):
            options.add_argument("--headless")

        self.driver = webdriver.Firefox(options=options)

        if(auth_token):
            self.auth_cookie = auth_token
            self.driver.get("https://twitter.com")
            self.driver.add_cookie({"name": "auth_token", "value": self.auth_cookie})

    def _get_articles(self):
        return self.driver.find_elements_by_tag_name("article")

    def _get_videos(self, article):
        video = article.find_elements_by_tag_name("video")

        if(len(video) > 0):
            return True
        else:
            return False

    def _get_images(self, article):
        images = []
        imgs = article.find_elements_by_tag_name("img")

        imgs.pop(0)

        for img in imgs:
            image = {
                "src": img.get_attribute("src"),
                "text": img.get_attribute("alt")
            }

            images.append(image)
        
        return images


    def _create_tweet(self, article):
        """
        Create a tweet object using web scrapped data
        """
        tweet = {
            "link": self.get_link(article),
            "author": self.get_author(article),
            "content": self.get_text_content(article),
            "images": self._get_images(article),
            "contains_video": self._get_videos(article),
        }

        self._get_images(article)

        return tweet

    def _create_tweets(self, articles):
        """
        Create tweet objects using web scrapped data
        """
        tweets = []

        for article in articles:
            tweets.append(self._create_tweet(article))

        return tweets

    def get_text_content(self, article):
        # css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0

        # TO DO:
        # Figure why this doesn't work
        # span = article.find_elements_by_css_selector(".css-901oao .css-16my406 .r-poiln3 .r-bcqeeo .r-qvutc0")

        elements = article.find_elements_by_css_selector(".r-poiln3")

        if(len(elements) > 3):
            # span[1] => username
            # span[2] => @username
            # span[3] => .

            # TO DO:
            # Fix elements[4] sometimes returning a number or @ handle
            span = elements[4]

            return span.text

    def get_author(self, article):
        a = article.find_elements_by_tag_name("a")

        if(len(a) > 0 and a[1].get_attribute("href")):
            return a[1].get_attribute("href")

    def get_link(self, article):
        a = article.find_elements_by_tag_name("a")

        if(len(a) > 1 and a[2].get_attribute("href")):
            return a[2].get_attribute("href")

    # TO DO:
    # Look into missing tweets (seems to be a low number)
    # Finds 43/51 tweets
    def _fetch_new_tweets(self, existing_tweets: list = None):
        driver = self.driver
        new_tweets_added = False

        if(existing_tweets is None):
            print("No previous tweets. Getting them now!")
            existing_tweets = self._create_tweets( self._get_articles() )
        else:
            # TO DO:
            # Check if there are any new tweets before scrolling

            print("We're checking this.. right?")
            t = self._create_tweets( self._get_articles() )

            for t1 in t:
                if(not t1 in existing_tweets):
                    print(t1["url"], "was loaded after the last check")
            pass

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/.6);")
        time.sleep(5)

        for tweet in self._create_tweets( self._get_articles() ):
            if(not tweet in existing_tweets):
                new_tweets_added = True
                existing_tweets.append(tweet)

        if(new_tweets_added):
            self._fetch_new_tweets(existing_tweets)

        return existing_tweets

    def get_bookmars(self):
        driver = self.driver

        driver.get("https://twitter.com/i/bookmarks")

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "article"))
        )

        return self._fetch_new_tweets()