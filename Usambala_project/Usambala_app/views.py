from django.shortcuts import render,redirect


# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def project(request):
    return render(request,'project.html')

def gallery(request):
    return render(request,'gallery.html')

def donate(request):
    return render(request,'donate.html')

def contact(request):
    return render(request,'contact.html')

def home(request):
    return render(request,'home.html')