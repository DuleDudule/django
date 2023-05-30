from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(*args,**kwargs):
    return HttpResponse("<h1>hello</h1>")

def contact_view(*args,**kwargs):
    return HttpResponse("<h1>contact</h1>")