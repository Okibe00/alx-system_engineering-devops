#!/usr/bin/python3
'''
Queries the reddit api for number of subscribers
'''
import requests


def number_of_subscribers(subreddit):
    '''
    Get the number of subscribers from a subreddit
    '''
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/102.0.0.0 Safari/537.36'
        }
    resp = requests.get(url, headers=header, allow_redirects=False)
    if resp.status_code == 200:
        json_resp = resp.json()
        return (json_resp['data']['subscribers'])
    else:
        return 0
