from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    msg = "<h1>Hello, It's My First Project</h1>"
    return HttpResponse(msg)

def fun():
    msg = "<li>list 1</li>"
    return HttpResponse(msg)

# def current_datetime(request):
#     now = datetime.now()
#     html = "<html><body>It is now %s.</body></html>"
#     return HttpResponse(html)
# Create your views here.
from datetime import datetime
def home(request):
    msg="<h1>welcome to website</h1>"
    return HttpResponse(msg)
def current_datetime(request):
    now = datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now   
    # // we can use %s or %now
    return HttpResponse(html)

def add(request):
    a = 10
    b = 15
    c = a+b
    return HttpResponse(c)

def temp(request):
    return render(request, "index.html")