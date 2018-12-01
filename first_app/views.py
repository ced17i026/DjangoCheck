from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(req):
    return HttpResponse("Hello World, this is my first Django page")