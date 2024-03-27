#!/usr/bin/env python3
'''A module for using the Redis NoSQL data storage.
'''

import requests
import redis

r = redis.Redis()


def count_calls(url: str):
    """
    Decorator that counts the number of times a 3
    function is called with a specific URL.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: The decorated function.
    """
    key = f"count:{url}"
    r.incr(key)


def cache_page(url: str, content: str):
    """
    Decorator that caches the result of a 
    function call with a specific URL.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: The decorated function.
    """
    key = f"page:{url}"
    r.setex(key, 10, content)


def get_page(url: str) -> str:
    """
    Fetches the HTML content of a URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the URL.
    """
    count_calls(url)
    page = r.get(f"page:{url}")
    if page is None:
        page = requests.get(url).text
        cache_page(url, page)
    return page


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
