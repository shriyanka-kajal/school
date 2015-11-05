from django.conf.urls import include, url
from django.contrib import *
from views import *

urlpatterns = [
    url(r'^', IndexView.as_view(), name='index'),
]