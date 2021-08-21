from celery import shared_task
from news.utils import get_url, get_random_user_agent, fetch_results, filter_fields
from news.models import Feed
from news.serializers import FeedSerializer

@shared_task
def scrape_yahoo_finance_rss(symbol):

    user_agent = get_random_user_agent()
    url = get_url(symbol)
    results = fetch_results(url, user_agent)
    if results.status != 200:
        return f"Symbol {symbol}: Failed to retrieve the items from the API"
    filtered = [filter_fields(item) for item in results.entries]

    feeds = Feed.objects.filter(symbol=symbol)
    guid_lookup = set(feed.guid for feed in feeds)
    new_entries = [{**item, "symbol": symbol} for item in filtered if item['guid'] not in guid_lookup]

    if len(new_entries) == 0:
        return f"Symbol {symbol}: No new items where added in the database"

    saved_entries = 0
    for entry in new_entries:
        serialized = FeedSerializer(data=entry)
        if serialized.is_valid():
            serialized.save()
            saved_entries += 1

    if saved_entries == 0:
        return f"Symbol {symbol}: None of the retrieved entries were valid"

    # Feed.objects.bulk_create(new_entries)
    return f"Symbol {symbol}: successfully added {len(new_entries)} to the database"