#!/usr/bin/python3
'''
Queries the reddit api for number of subscribers
'''
import requests


def recurse(subreddit, param=None, hot_list=[]):
    '''
    Get the number of subscribers from a subreddit
    '''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {"User-Agent": "alx/1"}
    resp = requests.get(
                url,
                headers=header,
                allow_redirects=False,
                params=param
            )
    if resp.status_code == 200:
        json_resp = resp.json()
        count = len(json_resp['data']['children'])
        lst_post = {}
        for data in json_resp['data']['children']:
            title = data['data']['title']
            hot_list.append(title)
            lst_post = data['data']['name']
        else:
            param = {}
            param['count'] = param.get('count', 0) + count
            param['after'] = lst_post
            if json_resp['data']['after'] is None:
                return hot_list
            return hot_list + recurse(subreddit, param, hot_list)
    elif resp.status_code == 404:
        return hot_list
    else:
        return None
