from django.db import models

class Feed(models.Model):
    # Hyphenated guid;s have a string length of 36
    guid = models.CharField(unique=True, max_length=36, null=False, blank=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    published_date = models.DateTimeField(null=False, blank=False)
    link = models.URLField(null=False, blank=False)
    symbol = models.CharField(max_length=50, null=False, blank=False)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
