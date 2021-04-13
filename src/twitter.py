from selenium import webdriver

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

    def get_link(tweet):
        """
        Get a tweet's link
        """
        a = tweet.find_elements_by_tag_name("a")

        if(len(a) > 0 and a[1].get_attribute("href")):
            return a[1].get_attribute("href")

    def get_bookmarks(self):
        """
        Returns an authenticated user's bookmarks
        """

        browser = self.browser

        browser.get("https://twitter.com/i/bookmarks")

    def get_video_tweets(self):
        pass

if(__name__ == "__main__"):
    Twitter().get_bookmarks()