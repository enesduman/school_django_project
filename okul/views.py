from django.shortcuts import render,HttpResponse
from .models import Okul
# Create your views here.

def index(request,id=None):
    cx={}
    cx['tek']= Okul.objects.all()
    return render(request,"index.html",cx)