from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):   
    return render(request, 'auth/login.html')

def register(request):   
    return render(request, 'auth/register.html')

def index_book(request):   
    return render(request, 'books/index.html')

def create_book(request):   
    return render(request, 'books/create.html')

def show_book(request):   
    return render(request, 'books/show.html')

def config(request):   
    return render(request, 'user/config.html')

def profile(request):   
    return render(request, 'user/profile.html')

def dark(request):   
    return render(request, 'dark.html')
