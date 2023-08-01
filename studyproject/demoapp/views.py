from django.http import HttpResponse
from django.shortcuts import render
from .models import Places

# Create your views here.
def start(request):
    return render(request,"home.html")

def about(request):
    return render(request,'about.html')

def contact(request):
    return HttpResponse("this is contact")

def addition(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    result = x+y
    mul = x*y
    return render(request ,'result.html',{'obj':result,'obj1':mul})

def develop(request):
    obj = Places.objects.all()
    return render(request,'index.html',{'res':obj})
