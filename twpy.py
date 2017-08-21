#!/usr/bin/env python3
from requests_oauthlib import OAuth1Session
import json
import argparse


USAGE = '''
[-tw text]  tweet text
[-tl]       show timeline'''
DESCR = '''With this, you can tweet from the terminal.'''
def prep_args():
    parser = argparse.ArgumentParser(description=DESCR,
                                     usage=USAGE)
    parser.add_argument('-tw', '--tweet', help='tweet text', required=False)
    parser.add_argument('-tl', '--timeline',
                        action='store_true', help='view TL', required=False)
    args = parser.parse_args()
    return args


def get_timeline():
    '''get timeline'''
    BLUF = '\x1b[34m'
    REDF = '\x1b[31m'
    GRYB = '\x1b[40m'
    ENDC = '\033[0m'

    url = 'https://api.twitter.com/1.1/statuses/home_timeline.json'
    params = {'count': 200}
    req = twitter.get(url, params=params)
    if req.status_code == 200:
        # api limit info
        limit = req.headers['x-rate-limit-remaining']
        reset = req.headers['x-rate-limit-reset']
        print('API remain:', limit)
        print('API reset:', reset)
        print('=====================')
        # timeline
        timeline = json.loads(req.text)
        counter = 0
        for tweet in timeline:
            if tweet['retweet_count']>5 or tweet['favorite_count']>10:
                LC = GRYB if counter % 2 == 0 else ''
                print(BLUF+str(tweet['retweet_count'])+ENDC,
                      REDF+str(tweet['favorite_count'])+ENDC,
                      LC+tweet['text'].replace('\n', '\\n')+ENDC)
                counter += 1
                if counter > 14:
                    break
    else:
        print('Error: %d' % req.status_code)


def post_tweet(text):
    '''post a tweet'''
    url = 'https://api.twitter.com/1.1/statuses/update.json'
    params = {'status': text}
    req = twitter.post(url, params=params)
    if req.status_code == 200:
        print('Success')
    else:
        print('Error: %d' % req.status_code)


if __name__ == '__main__':
    with open('secrets.json', 'r') as f:
        _tokens = json.load(f)
    twitter = OAuth1Session(*_tokens)
    args = prep_args()
    if args.tweet:
        print('=== tweet ===')
        text = args.tweet
        post_tweet(text)
    elif args.timeline:
        print('=== timeline ===')
        get_timeline()
    else:
        print(USAGE)
