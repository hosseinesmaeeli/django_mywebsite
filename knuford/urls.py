from django.urls import path

from knuford.views import index_view
# from website.views import http_test , json_test , home

app_name = 'website'

urlpatterns = [

    path('',index_view, name='index'),
    
]