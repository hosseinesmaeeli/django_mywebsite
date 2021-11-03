from django.shortcuts import render

# Create your views here.
def blog_index(request) :
    context={'content':'helooooo. My name is Hossein'}
    return render(request,"blog/blog-home.html",context)

def blog_single(request) :
    return render(request,"blog/blog-single.html")    
