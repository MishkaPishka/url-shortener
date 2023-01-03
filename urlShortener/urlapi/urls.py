from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('create/', csrf_exempt(views.create_short_url), name="create"),
    path('s/<str:short_url_suffix>/', views.short_url_redirect, name="short"),
    path('get_data_long/', csrf_exempt(views.get_long_url_data), name="long_data"),
    path('get_data_short/', csrf_exempt(views.get_short_url_data), name="short_data"),
]
