from .models import OriginalUrl, LinkHit, ShortUrl


def get_number_of_urls_per_long_url(long_url: str) -> int:
    """
    Returns an int representing the number of short_urls created for a long url
    """
    return ShortUrl.objects.filter(original_url=long_url).count()


def get_number_of_redirects_to_long_url(long_url: str) -> int:
    """
    Returns and in representing the number of redirects to long url
    """
    short_urls_by_long_url = ShortUrl.objects.filter(original_url=long_url).values('hit_count')
    return sum(short_urls_by_long_url)


def get_number_of_different_users_entering_to_long_url(long_url: str) -> int:
    """
    Returns and int representing the number of distinct users redirected to long url from all short links
    """
    short_urls_by_long_url = ShortUrl.objects.filter(original_url=long_url).values('id')
    return LinkHit.objects.filter(id__in=short_urls_by_long_url).values('source').distinct().count()


def get_number_of_different_users_clicked_on_short_link(short_link: str) -> int:
    """
    Returns and int representing the number of distinct users redirected to from short link
    """
    short_urls_by_long_url = ShortUrl.objects.filter(url=short_link).values('id')
    return LinkHit.objects.filter(id__in=short_urls_by_long_url).values('source').distinct().count()


def store_original_url(long_url: str) -> OriginalUrl:
    return OriginalUrl.objects.get_or_create(url=long_url)[0]


def store_short_url(short_url: str, long_url: OriginalUrl) -> ShortUrl:
    short_url = ShortUrl.objects.create(url=short_url, original_url=long_url)
    return short_url
