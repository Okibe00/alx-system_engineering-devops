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
    header = {"User-Agent": "alx/1"}
    resp = requests.get(url, headers=header, allow_redirects=False)
    if resp.status_code == 200:
        json_resp = resp.json()
        return (json_resp['data']['subscribers'])
    else:
        return 0
