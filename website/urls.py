from django.urls import path

from website.views import about_view, contacts_viw, index_view
# from website.views import http_test , json_test , home


urlpatterns = [
    path('contacts',contacts_viw),
    path('about',about_view),
    path('',index_view)
]