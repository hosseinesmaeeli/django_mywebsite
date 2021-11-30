from django.shortcuts import render
from website.models import Contact
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

def test_view(request) :
    if request.method == "POST" :
    #     print(request.POST.get('name')) 
    #     print ("post")
    # elif request.method == "GET" :
    # print ("get")  
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        messege = request.POST.get('messege')
        print(name,email,subject,messege)

        c=Contact() 
        c.name= name
        c.email= email
        c.subject= subject
        c.message= messege
        c.save()

  
    return render(request,"test.html",{})    