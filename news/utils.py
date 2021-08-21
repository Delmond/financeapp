from datetime import datetime
from time import mktime
from random import choice
import feedparser

URL_BASE = "https://feeds.finance.yahoo.com/rss/2.0"
URL_QUERY = "headline"
URL_DEFAULT_QUERY_PARAMS = {"region": "US", "lang": "en-US"}
# Set count to high number to fetch every entry
MAX_COUNT = 10000


def get_random_user_agent():
    user_agents = [
        # User agent for OS: Windows 10, Browser: Edge
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
        # User agent for OS: Windows 7, Browser: Chrome
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
        # User agent for OS: Mac OS X10, Browser: Safari
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
        # User agent for OS: Ubuntu, Browser: Firefox
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
        # User agent for OS: Chrome, Browser: Chrome
        "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36"
    ]
    return choice(user_agents)


def get_url(symbol, count=MAX_COUNT):
    url_additional_query_params = {
        "count": str(count),
        "s": symbol
    }

    url_query_params = {**URL_DEFAULT_QUERY_PARAMS, **url_additional_query_params}

    # Construct a single string with all the query parameters separated with the character '&'
    params = "&".join([name + "=" + value for name, value in url_query_params.items()])
    url = f"{URL_BASE}/{URL_QUERY}?{params}"
    return url


def fetch_results(url, user_agent):
    return feedparser.parse(url, agent=user_agent)


def filter_fields(item):
    title = item.title
    description = item.summary
    published_date = datetime.fromtimestamp(mktime(item.published_parsed))
    guid = item.id
    link = item.link
    return {'title': title, 'description': description, 'published_date': published_date, 'guid': guid, 'link': link }
