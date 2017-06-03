import twitter
from requests_oauthlib import OAuth1
import APIs

from Text import Text


class TwitterDownloader:

    passwords = APIs.tweeter

    def __init__(self):
        # seeting passwords for manual requests
        self.auth = OAuth1(*self.passwords)
        # setting passwords for library requests
        self.api = twitter.Api(*self.passwords)
        self.userid = -1
        self.userid_set = False

    def check_authentication(self):
        print(self.api.VerifyCredentials())

    def set_twitterid(self, name):
        [user] = self.api.GetUsersSearch(term=name, page=1, count=1, include_entities=None)
        self.userid = user.id
        self.userid_set = True

    def download_all_tweets(self):
        try:
            alltweets = []
            new_tweets = self.api.GetUserTimeline(user_id=self.userid, count=200)
            alltweets.extend(new_tweets)
            oldest = alltweets[-1].id - 1
            while len(new_tweets) > 0:
                new_tweets = self.api.GetUserTimeline(user_id=self.userid, count=200, max_id=oldest)
                alltweets.extend(new_tweets)
                oldest = alltweets[-1].id - 1
        except:
            raise TwitterDownloaderException('Error while downloading')
        return list(map(lambda e: self._make_text_with_id(e), alltweets))


    @staticmethod
    def _make_text_with_id(tweet):
        links = list(map(lambda e: e.expanded_url, tweet.urls))
        hashs = list(map(lambda e: e.text, tweet.hashtags))
        return Text(tweet.text, hashs, links)

class TwitterDownloaderException(Exception):
    pass