from django.http import HttpResponse , JsonResponse

def http_test(request) :
    return HttpResponse ('<h1>salam</h1>')

def json_test(request) :
    return HttpResponse ('{name:"hossein"}')    