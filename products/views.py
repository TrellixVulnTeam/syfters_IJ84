from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from .models import BlogLeft
from .models import LatestBlogLeft
from .models import LatestBlogRight
from django.shortcuts import render
from pyshop.form import contactForEmail
from django.core.mail import send_mail



def home(request):
    products = LatestBlogRight.objects.all()
    return render(request, 'index.html', {'products':products})

def lands(request):
    products = Product.objects.all()
    return render(request, 'properties.html', {'products':products})

def news(request):
    products = BlogLeft.objects.all()
    return render(request, 'news.html', {'products':products})

def contacts(request):
    products = LatestBlogLeft.objects.all()
    return render(request, 'contact.html', {'products':products})
    

#email

def contactSendMail(request):
    if request.method == "GET":
        form = contactForEmail()
    else:
        form = contactForEmail(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(name, email, message,['mahabojang110@gmail.com',name])
    return render(request,'contacts.html',{'form':form})






