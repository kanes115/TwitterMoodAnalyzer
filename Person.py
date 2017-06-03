from Text import Text
from TwitterDownloader import TwitterDownloader


class Person:

    amount_of_tweets = 100

    def __init__(self, name):
        self.twitter_id = id
        self.texts = []
        self.downloader = TwitterDownloader()
        self.downloader.check_authentication()
        self.downloader.set_twitterid(name)
        self.downloaded = False

    def get_texts(self):
        self._download_if_needed()
        return self.texts

    def all_text_as_one(self):
        self._download_if_needed()
        res = Text('')
        for t in self.texts:
            if t:
                res += t
        return res

    def _download_if_needed(self):
        if not self.downloaded:
            self.texts = self.downloader.download_all_tweets()
        print('length' + str(len(self.texts)))

