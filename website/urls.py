from django.urls import path

from website.views import about_view, contacts_viw, index_view,test_view,newsletter_view
# from website.views import http_test , json_test , home

app_name = 'website'

urlpatterns = [
    path('contacts',contacts_viw, name='contact'),
    path('about',about_view, name='about'),
    path('',index_view, name='index'),
    path('test',test_view, name='test'),
    path('newsletter',newsletter_view, name='newsletter'),
]