from requests_oauthlib import OAuth1Session
import json
import argparse
import os
from math import log10 as log
from datetime import datetime as dt


def prep_args():
    parser = argparse.ArgumentParser(
        description='''This command help you tweet
        or view timeline from commandline''')
    parser.add_argument('tweet',
                        help='''Pass a string to tweet.
                        If none is given, will get timeline''',
                        nargs='?')
    args = parser.parse_args()
    return args


TWITTER_USER_NAME = ''
TWITTER_ENVS = [
    'TWITTER_CONSUMER_KEY',
    'TWITTER_CONSUMER_SECRET',
    'TWITTER_ACCESS_TOKEN',
    'TWITTER_ACCESS_TOKEN_SECRET',
]


class Twitter:

    def __init__(self):
        # Prepare API keys
        if set(os.environ) >= set(TWITTER_ENVS):
            self.twitter = OAuth1Session(
                *[os.environ[token] for token in TWITTER_ENVS]
            )
        else:
            print('Please set up your env values with Twitter tokens')

    def _print_error(self, req):
        print(f'Error: {req.status_code} {req.reason}')
        print('Details: ')
        for e in req.json()['errors']:
            for k, v in e.items():
                print(f'{k}: {v}')

    def get_timeline(self):
        '''Get timeline'''

        url = 'https://api.twitter.com/1.1/statuses/home_timeline.json'
        params = {'count': 200}
        req = self.twitter.get(url, params=params)

        def C(n): return '\033[%sm' % str(n)
        BLUF = C(32)
        REDF = C(31)
        ENDC = C(0)
        if req.status_code == 200:
            # api limit info
            limit = int(req.headers['x-rate-limit-remaining'])
            reset = int(req.headers['x-rate-limit-reset'])
            print('===== timeline =====')
            print('lmt:', '*'*limit + '.'*(15-limit))
            print('rst:', dt.fromtimestamp(reset).strftime('%m/%d %H:%M'))
            print('====================')
            # timeline
            timeline = json.loads(req.text)
            counter = 0
            for tweet in timeline:
                if tweet['retweet_count'] > 5 or tweet['favorite_count'] > 10:
                    LC = C('48;5;236') if counter % 2 == 0 else C('48;5;232')
                    SC = C('38;5;255') if counter % 2 == 0 else C('38;5;252')
                    rt, fv = tweet['retweet_count'], tweet['favorite_count']
                    print(LC+BLUF + '%1.1f' % log(rt + 1) + ' '+ENDC,
                          LC+REDF + '%1.1f' % log(fv + 1) + ' '+ENDC,
                          LC+SC+tweet['text'].replace('\n', '\u21a9 '),
                          sep='', end='\n'+C(49))
                    counter += 1
                    if counter > 14:
                        break
        else:
            self._print_error(req)

    def post_tweet(self, text):
        '''Post a tweet'''

        url = 'https://api.twitter.com/1.1/statuses/update.json'
        params = {'status': text}
        req = self.twitter.post(url, params=params)

        if req.status_code == 200:
            print('=== tweet ===')
            print('Success')
        else:
            self._print_error(req)


def main():
    args = prep_args()
    if args.tweet:
        # post a tweet.
        text = args.tweet
        Twitter().post_tweet(text)
    else:
        # get timeline.
        Twitter().get_timeline()
