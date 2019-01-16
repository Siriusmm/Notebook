from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path(r'^$', index_views),
    path('login/',login_views),
    path('register/',register_views),
    path('check/',check_views),
    path("test/",test_views),
]
