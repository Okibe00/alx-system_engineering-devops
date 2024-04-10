#!/usr/bin/python3
'''
Queries the reddit api for number of subscribers
'''
import requests


def top_ten(subreddit):
    '''
    Get the number of subscribers from a subreddit
    '''
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    header = {"User-Agent": "alx/1"}
    resp = requests.get(url, headers=header, allow_redirects=False)
    if resp.status_code == 200:
        try:
            json_resp = resp.json()
            for data in json_resp['data']['children']:
                print(data['data']['title'])
        except Exception as e:
            print(None)
    else:
        print(None)
