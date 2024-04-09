#!/usr/bin/python3
'''
Queries the reddit api for number of subscribers
'''
import requests


def top_ten(subreddit):
    '''
    Get the number of subscribers from a subreddit
    '''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {"User-Agent": "alx/1"}
    resp = requests.get(url, headers=header, allow_redirects=False)
    if resp.status_code == 200:
        json_resp = resp.json()
        count = 0
        for data in json_resp['data']['children']:
            if count < 10:
                print(data['data']['title'])
                count = count + 1
    else:
        return None
