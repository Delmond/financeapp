from celery import shared_task
from news.utils import get_url, get_random_user_agent, fetch_results, filter_fields
from news.models import Feed
from news.serializers import FeedSerializer

@shared_task
def scrape_yahoo_finance_rss(symbol):

    user_agent = get_random_user_agent()
    url = get_url(symbol)
    results = fetch_results(url, user_agent)

    filtered = [filter_fields(item) for item in results.entries]

    feeds = Feed.objects.filter(symbol=symbol)
    guid_lookup = set(feed.guid for feed in feeds)
    new_entries = [{**item, "symbol": symbol} for item in filtered if item['guid'] not in guid_lookup]

    if len(new_entries) == 0:
        return f"Symbol {symbol}: No new items where added in the database"

    serialized = FeedSerializer(data=new_entries, many=True)
    if not serialized.is_valid():
        print(serialized.errors)
        return f"Symbol {symbol}: Retrieved data is not valid"

    serialized.save()


    # Feed.objects.bulk_create(new_entries)
    return f"Symbol {symbol}: successfully added {len(new_entries)} to the database"