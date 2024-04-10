#!/usr/bin/python3
"""Query Reddit API to determine subreddit sub count
"""

import requests


def count_words(subreddit, word_list, count_list=[], next_page=None):
    """Request subreddit recursively using pagination
    """
    # convert word_list to dict with count
    if not count_list:
        for word in word_list:
            count_list.append(dict({'keyword': word,
                                    'count': 0}))

    # NETWORKING
    # set custom user-agent
    user_agent = '0x16-api_advanced-jmajetich'
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    # if page specified, pass as parameter
    if next_page:
        url += '?after={}'.format(next_page)

    headers = {'User-Agent': user_agent}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return
