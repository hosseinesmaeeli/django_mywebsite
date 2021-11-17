from django.urls import path

from blog.views import blog_index,blog_single,test
# from website.views import http_test , json_test , home

app_name = 'blog'

urlpatterns = [
    path('blog/blog_index',blog_index, name='index'),
    path('blog/blog_single',blog_single, name='single'),
    path('blog/test',test, name='test'),
   ]