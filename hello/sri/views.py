from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Welcome To Vishnu's Project")

def index(request):
    return render(request,'index.html')
def demo(request):
    return render(request,'demo.html')
