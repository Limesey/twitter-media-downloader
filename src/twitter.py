from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Twitter:
    def __init__(self, auth: str = None, headless: bool = None):
        self.auth_cookie = auth
        options = webdriver.FirefoxOptions()

        if(headless):
            options.add_argument("--headless")

        self.browser = webdriver.Firefox(options=options)
        self.browser.get("https://twitter.com")

        if(self.auth_cookie):
            self.browser.add_cookie({"name": "auth_token", "value": self.auth_cookie})

    def get_author(self, tweet):
        """
        Returns the URL to the tweet's author
        """

        a = tweet.find_elements_by_tag_name("a")

        if(len(a) > 0 and a[1].get_attribute("href")):
            return a[1].get_attribute("href")

    def get_link(self, tweet):
        """
        Get a tweet's link
        """
        a = tweet.find_elements_by_tag_name("a")

        if(len(a) > 0 and a[2].get_attribute("href")):
            return a[2].get_attribute("href")

    def get_bookmarks(self):
        """
        Returns an authenticated user's bookmarks
        """
        driver = self.browser

        driver.get("https://twitter.com/i/bookmarks")

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "article"))
        )

        # TO DO:
        # Fetch all bookmarked tweets (scrolling down to load them)
        # Handle Twitter's random errors

        return self._get_articles()

    def get_video_tweets(self):
        pass

if(__name__ == "__main__"):
    Twitter().get_bookmarks()