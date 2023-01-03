from django.contrib import admin

# Register your models here.
from .models import OriginalUrl, LinkHit, ShortUrl

admin.site.register(OriginalUrl)
admin.site.register(ShortUrl)
admin.site.register(LinkHit)
