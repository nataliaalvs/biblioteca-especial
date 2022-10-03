from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required(login_url='auth.login')
def index_book(request):   
    books = Book.objects.all()
    return render(request, 'books/index.html', { 'books': books })

@login_required(login_url='auth.login')
def create_book(request):   
    form = BookForm(request.POST, request.FILES)
    if form.is_valid():        
        # handle_uploaded_file(request.FILES['file'])
        form.save()        
        return redirect('book.index')
    return render(request, 'books/create.html')

@login_required(login_url='auth.login')
def show_book(request):   
    return render(request, 'books/show.html')

@login_required(login_url='auth.login')
def config(request):   
    return render(request, 'user/config.html')

@login_required(login_url='auth.login')
def profile(request):   
    return render(request, 'user/profile.html')

def dark(request):   
    return render(request, 'dark.html')
