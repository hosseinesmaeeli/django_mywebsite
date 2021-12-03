from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from website.models import Contact
from django.http import HttpResponse,JsonResponse
from website.forms import NameForm,ContactForm,NewsletterForm
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
    if request.method =='POST' :
        form= ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form=ContactForm()
    return render(request,"website/contact.html",{'form':form})    

def about_view(request) :
    return render(request,"website/about.html")

# def test_view(request) :
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


# def test_view(request) :
#     if request.method=='POST' :
#         form=NameForm(request.POST)
#         if form.is_valid() :
#             name=form.cleaned_data['name']
#             subject=form.cleaned_data['subject']
#             email=form.cleaned_data['email']
#             message=form.cleaned_data['message']
#             print(name,subject,email,message)
#             return HttpResponse('done')
#         else :
#             return HttpResponse ('not valid')  
#     form= NameForm()
#     return render(request,'test.html',{'form': form})    

def test_view(request) :
    if request.method=='POST' :
        form=ContactForm(request.POST)
        if form.is_valid() :
            # name=form.cleaned_data['name']
            # subject=form.cleaned_data['subject']
            # email=form.cleaned_data['email']
            # message=form.cleaned_data['message']
            # print(name,subject,email,message)
            form.save()
            return HttpResponse('done')
        else :
            return HttpResponse ('not valid')  
    form= ContactForm()
    return render(request,'test.html',{'form': form})        

def newsletter_view(request) :
    if request.method=='POST' :
        form=NewsletterForm(request.POST)
        if form.is_valid() :
            form.save()
            return HttpResponseRedirect  ('/')  
        else :
            return HttpResponseRedirect  ('/')  
