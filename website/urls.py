from django.urls import path
from website.views import http_test , json_test , home


urlpatterns = [
    path('http_test',http_test),
    path('json_test',json_test),
    path('',home)
]