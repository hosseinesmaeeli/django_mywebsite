from django import template
from blog.models import Post

register = template.Library()

# @register.simple_tag
# def function(a):
#     return a+2

# @register.simple_tag(name='totalposts')   
# def function():
#     # posts=Post.objects.filter(status=1)
#     posts=Post.objects.filter(status=1).count()
#     return posts

@register.simple_tag(name='totalposts')   
def function():
    # posts=Post.objects.filter(status=1)
    posts=Post.objects.filter(status=1).count()
    return posts

@register.filter
def snippet(value,arg=50) :
    return value[:arg]
