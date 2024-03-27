import requests
import redis

r = redis.Redis()


def count_calls(url: str):
    key = f"count:{url}"
    r.incr(key)


def cache_page(url: str, content: str):
    key = f"page:{url}"
    r.setex(key, 10, content)


def get_page(url: str) -> str:
    count_calls(url)
    page = r.get(f"page:{url}")
    if page is None:
        page = requests.get(url).text
        cache_page(url, page)
    return page


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
