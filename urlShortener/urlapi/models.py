from django.db import models


class OriginalUrl(models.Model):
    """A model of an original url"""
    url = models.CharField(max_length=200, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)


class ShortUrl(models.Model):
    """A model of a rock band member."""
    # add unique constraint
    url = models.CharField("Short URL", max_length=200, unique=True)
    original_url = models.ForeignKey("OriginalUrl", on_delete=models.CASCADE, to_field="url")
    created = models.DateTimeField(auto_now_add=True)


class LinkHit(models.Model):
    url = models.ForeignKey("ShortUrl", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    source = models.CharField("IP of user", max_length=200)
