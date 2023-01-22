from django.db.models import Sum, QuerySet, Count
from django.db.models.functions import TruncWeek

from .models import OriginalUrl, LinkHit, ShortUrl


def get_number_of_hits_grouped_by_week_per_short_url(short_url: ShortUrl) -> QuerySet:
    return LinkHit.objects.filter(url=short_url).annotate(week=TruncWeek('created')).values('week').annotate(hit_count=Count('id')).values('week', 'hit_count')


def get_number_of_urls_per_long_url(long_url: str) -> int:
    """
    Returns an int representing the number of short_urls created for a long url
    """
    return ShortUrl.objects.filter(original_url=long_url).count()


def get_number_of_redirects_to_long_url(long_url: str) -> int:
    """
    Returns and in representing the number of redirects to long url
    """
    short_urls_by_long_url = ShortUrl.objects.filter(original_url=long_url).aggregate(Sum('hit_count'))
    return short_urls_by_long_url['hit_count__sum']


def get_number_of_different_users_entering_to_long_url(long_url: str) -> int:
    """
    Returns and int representing the number of distinct users redirected to long url from all short links
    """
    short_urls_by_long_url = ShortUrl.objects.filter(original_url=long_url).values('id')
    return LinkHit.objects.filter(url__id__in=short_urls_by_long_url).values('source').distinct().count()


def get_number_of_different_users_clicked_on_short_link(short_link: str) -> int:
    """
    Returns and int representing the number of distinct users redirected to from short link
    Note - we do not use "hit-count" directly because there could be several hits with the same "source"
    """
    return LinkHit.objects.filter(url__url=short_link).values('source').distinct().count()


def store_original_url(long_url: str) -> OriginalUrl:
    return OriginalUrl.objects.get_or_create(url=long_url)[0]


def store_short_url(short_url: str, long_url: OriginalUrl, is_permanent: bool) -> ShortUrl:
    return ShortUrl.objects.create(url=short_url, original_url=long_url, is_permanent=is_permanent)


def get_short_urls_of_long_url(long_url: str) -> QuerySet:
    return ShortUrl.objects.filter(original_url__url=long_url)
