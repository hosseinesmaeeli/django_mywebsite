from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.
def blog_index(request) :
    posts= Post.objects.filter(status=0)
    # context={'content':'helooooo. My name is Hossein'}
    context={'posts': posts}
    return render(request,"blog/blog-home.html",context)

def blog_single(request) :
    return render(request,"blog/blog-single.html")    

# def test(request) :
#     posts= Post.objects.all()
#     # posts= Post.objects.filter(status=0)
#     context={'posts': posts}
#     return render(request,"blog/test.html",context)    


# def test(request, name,famili_name) :

#     context={'name': name, 'famili_name' : famili_name}
#     return render(request,"blog/test.html",context)

def test(request, pid) :
    # post= Post.objects.get(id=pid)
    post = get_object_or_404(Post, pk=pid)
    context={'post': post}
    return render(request,"blog/test.html",context)