import json

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F, Count
from django.db.models.functions import TruncMonth, TruncWeek
from django.http import HttpResponse, JsonResponse, HttpResponseServerError
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
from .models import ShortUrl, LinkHit
from .url_generator import generate_unique_short_url_and_update_db, build_complete_url
from .url_queries import get_number_of_redirects_to_long_url, get_number_of_urls_per_long_url, \
    get_number_of_different_users_entering_to_long_url, get_number_of_different_users_clicked_on_short_link, \
    get_short_urls_of_long_url, get_number_of_hits_grouped_by_week_per_short_url


@require_http_methods(["GET"])
def short_url_redirect(request, short_url_suffix: str):
    """
    if short_url exists in db - redirects to db and also increment count by 1
    otherwise - redirects to 404
    """
    try:
        short_url_suffix = build_complete_url(request, short_url_suffix)
        short_url = ShortUrl.objects.get(url=short_url_suffix)
        # on update increase hit count
        ShortUrl.objects.filter(url=short_url_suffix).update(hit_count=F('hit_count') + 1)
        # adds data to LinkHit table
        user_ip = get_client_ip(request)
        LinkHit.objects.create(url=short_url, source=user_ip)
        redirect_url = short_url.original_url
        return redirect(redirect_url.url)

    except ObjectDoesNotExist as e:
        print(e.args)
        return HttpResponse(f"<h1>Error</h1>")


@require_http_methods(["POST"])
def create_short_url(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    long_url = body.get('url')
    is_permanent = body.get('permanent', True)
    short_url: ShortUrl
    short_url = generate_unique_short_url_and_update_db(request, long_url, is_permanent)
    return HttpResponse(short_url.url, content_type="text/plain")


@require_http_methods(["GET"])
def get_short_url_data(request):
    """
    creates LinkData object from short url
    data contains info about - number of hits, number of different users, last_hit timestamp
    :param request:
    :param short_url:
    """
    try:
        short_url_value = request.GET['URL']
        short_url = ShortUrl.objects.get(url=short_url_value)
        hits_count_grouped_by_week = get_number_of_hits_grouped_by_week_per_short_url(short_url)
        results = short_url.to_dict()
        link_hits_by_week = [hit_count_per_week for hit_count_per_week in hits_count_grouped_by_week]
        results['timestamps'] = link_hits_by_week
        return JsonResponse(results)
    except KeyError:
        print("URL NOT FOUND IN REQUEST ARGUMENTS")
        return HttpResponseServerError("Bad Request - URL does not exist.")
    except ObjectDoesNotExist:
        print("URL NOT FOUND DB")
        return HttpResponseServerError("Bad Request - URL not Found in DB.")


@require_http_methods(["GET"])
def get_long_url_data(request):
    """
    created LinkData object for original url
    data contains info about - number of short links, total number of hits of all links, total number of different users
    """
    try:
        original_url = request.GET['URL']
        number_of_short_urls = get_number_of_urls_per_long_url(original_url)
        number_of_hits = get_number_of_redirects_to_long_url(original_url)
        number_of_different_users = get_number_of_different_users_entering_to_long_url(original_url)
        short_urls = [short_url.to_dict() for short_url in get_short_urls_of_long_url(original_url)]
        return JsonResponse({'link': original_url, 'numberOfHits': number_of_hits,
                             'numberOfDifferentUsers': number_of_different_users,
                             'number_of_links': number_of_short_urls, 'short_urls': short_urls})
    except KeyError:
        print("URL NOT FOUND IN REQUEST ARGUMENTS")
        return HttpResponseServerError("Bad Request - URL does not exist.")
    except ObjectDoesNotExist as e:
        print(e.args)
        return HttpResponseServerError("Bad Request - URL not Found in DB.")


def get_client_ip(request):
    """
    returns the ip of the user making the request
    used for linkHit data
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
