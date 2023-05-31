from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args,**kwargs):
    print(request.user)
    #return HttpResponse("<h1>hello</h1>")
    return render(request,"home.html",{})

def contact_view(request,*args,**kwargs):
    my_context = {
        "text":"±test text iz konteksta±",
        "lista":[1,2,3]
    }
    return render(request,"contact.html",my_context)