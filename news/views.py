from news.models import Feed
from news.serializers import FeedSerializer
from rest_framework import viewsets
from news.pagination import ResultsSetPagination


class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    pagination_class = ResultsSetPagination

