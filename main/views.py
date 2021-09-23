from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Contact


def index(request):
    return render(request,'index.html', {})

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email= request.POST.get('email')
        phoneno= request.POST.get('phoneno')
        message= request.POST.get('message')
        contact=Contact(name=name,email=email,phoneno=phoneno,message=message)
        contact.save()
        
        return HttpResponse("<h1>Thank you for contacting us</h1>")
        


        return render(request,'contact.html',{})
    else:
        return render(request,'contact.html',{})

   
        
def about(request):
    return render(request,'about.html', {})


def gallery(request):
    return render(request,'gallery.html', {})


