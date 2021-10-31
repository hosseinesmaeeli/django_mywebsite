from django.shortcuts import render

# from django.http import HttpResponse , JsonResponse

# def http_test(request) :
#     return HttpResponse ('<h1>salam</h1>')

# def json_test(request) :
#     return JsonResponse ({"name":"hossein"})  
# # Create your views here.

# def home(request) :
#     return HttpResponse ('<h1>this is home page</h1>')

def index_view(request) :
    return render(request,"website/index.html")

def contacts_viw(request) :
    return render(request,"website/contact.html")    

def about_view(request) :
    return render(request,"website/about.html")