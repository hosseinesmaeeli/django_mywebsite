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

@register.inclusion_tag('popularposts.html')
def popularposts():
    posts= Post.objects.filter(status=1).order_by('published_date')[:1] #for end post
    return {'posts':posts}