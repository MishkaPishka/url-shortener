import random
import string
from django.db import IntegrityError

from .models import OriginalUrl
from .url_queries import store_original_url, store_short_url

MAX_SUFFIX_LENGTH = 7
MAX_NUMBER_OF_ATTEMPTS = 1000
VALID_CHARACTERS = string.ascii_uppercase + string.digits


def generate_short_url() -> str:
    return ''.join(random.choices(VALID_CHARACTERS, k=MAX_SUFFIX_LENGTH))


def generate_unique_short_url_and_update_db(request, long_url: str) -> bool:
    """
    create short url for original url
    adds long_url to db if it does not exist
    adds short link to db
    returns true if actions is successful false otherwise
    """
    original_url: OriginalUrl
    for i in range(MAX_NUMBER_OF_ATTEMPTS):
        short_url = build_complete_url(request, generate_short_url())
        try:
            # add long url to db
            original_url = store_original_url(long_url)
            # add short url to db
            return store_short_url(short_url, original_url)

        except IntegrityError as e:
            print(e.args)
            if i >= MAX_NUMBER_OF_ATTEMPTS:
                raise Exception(f"COULD NOT GENERATE RANDOM URL, failed after {MAX_NUMBER_OF_ATTEMPTS} attempts.")


def build_complete_url(request, url):
    """
    returns the completed parsed url
    """
    return request.get_host() + "/s/" + url
