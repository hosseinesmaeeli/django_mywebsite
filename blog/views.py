from django.shortcuts import render
from blog.models import Post

# Create your views here.
def blog_index(request) :
    posts= Post.objects.filter(status=0)
    # context={'content':'helooooo. My name is Hossein'}
    context={'posts': posts}
    return render(request,"blog/blog-home.html",context)

def blog_single(request) :
    return render(request,"blog/blog-single.html")    

def test(request) :
    posts= Post.objects.all()
    # posts= Post.objects.filter(status=0)
    context={'posts': posts}
    return render(request,"blog/test.html",context)    
