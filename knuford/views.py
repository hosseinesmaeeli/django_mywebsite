from django.shortcuts import render

# Create your views here.
def index_view(request) :
    context= {
    'name':'Hossein Esmaeeli',
    'description_0':'I am Hossein Esmaeeli',
    'about_me':'Im civil engineer but I like devlope my Idea and now I try to learn python and django framework with Mr.Bigdeli'
    }
    return render(request,"knuford/index.html",context)
