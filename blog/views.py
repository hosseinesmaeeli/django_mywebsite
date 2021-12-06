from django.shortcuts import render, get_object_or_404
from blog.models import Post,Comment
from django.core.paginator import PageNotAnInteger, Paginator,EmptyPage,PageNotAnInteger
from blog.forms import CommentForm
from django.contrib import messages

# Create your views here.

# def blog_index(request,cat_name=None, author_username=None) :
#     posts= Post.objects.filter(status=1)
#     if cat_name :
#     # context={'content':'helooooo. My name is Hossein'}
#         posts= posts.filter(category__name= cat_name)
#     if author_username :
#         posts= posts.filter(author__username = author_username)   
#     context={'posts': posts}
#     return render(request,"blog/blog-home.html",context)

def blog_index(request,**kwargs) :
    posts= Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        posts= posts.filter(category__name= kwargs['cat_name'] )
    # context={'content':'helooooo. My name is Hossein'}

    if kwargs.get('author_username') != None:
        posts= posts.filter(author__username = kwargs['author_username'])  
    posts= Paginator(posts,3)   
    try:  
        page_number= request.GET.get('page')
        posts=posts.get_page(page_number)
    except PageNotAnInteger :
        posts=posts.get_page(1)   
    except EmptyPage :   
        posts=posts.get_page(1)   
    context={'posts': posts}
    return render(request,"blog/blog-home.html",context)




def blog_single(request,pid) :
    if request.method == 'POST' :
        form=CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your message submitted')
        else :
            messages.add_message(request,messages.ERROR,'your message didnt submitted')

    posts= Post.objects.filter(status=1)            
    post = get_object_or_404(Post, pk=pid, status=1)
    comments= Comment.objects.filter(post=post.id,approved=True).order_by('created_date')
    form= CommentForm()
    context={'post': post,'comments': comments,'form': form}
    return render(request,"blog/blog-single.html",context)    

def test(request) :
    posts= Post.objects.all()
    # # posts= Post.objects.filter(status=0)
    context={'posts': posts}
    return render(request,"blog/test.html",context)    


# def test(request, name,famili_name) :

#     context={'name': name, 'famili_name' : famili_name}
#     return render(request,"blog/test.html",context)

# def test(request, pid) :
#     # post= Post.objects.get(id=pid)
#     post = get_object_or_404(Post, pk=pid)
#     context={'post': post}
#     return render(request,"blog/test.html",context)

def blog_category(request,cat_name) :
    posts= Post.objects.filter(status=1)
    posts= posts.filter(category__name= cat_name)

    context={'posts': posts}
    return render(request,"blog/blog-home.html",context)    

def blog_search(request) :
    posts= Post.objects.filter(status=1)
    # if request.method == 'GET' :
    #     print(request.GET.get('s'))
    #     posts= posts.filter(content__contains= request.GET.get('s'))
    if request.method == 'GET' :
            if s:= request.GET.get('s') :
                posts= posts.filter(content__contains= s)

    context={'posts': posts}
    return render(request,"blog/blog-home.html",context)


          
