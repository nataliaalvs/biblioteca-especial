from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from .books.convert import convert
import PyPDF2
import os

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
        form.instance.user = request.user
        form.save() 
        return redirect('book.index')
    return render(request, 'books/create.html', { 'form': form })



@login_required(login_url='auth.login')
def show_book(request, id, pg):
    book = Book.objects.get(pk=id)
    if str(book.user) == str(request.user.email):
        pdfFileObj = open(str(book.path), 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)    
        count = pdfReader.numPages
        if count > pg:
            book.current_page = pg
            book.save()
            if (count - 1) == pg:
                content_book = (pdfReader.getPage(pg).extractText() +'<br> <h3 class="text-center">FIM</h3>')
            else:
                content_book = (pdfReader.getPage(pg).extractText() +'<br>')

            pdfFileObj.close()
            return render(request, 'books/show.html', { 'content_book': content_book, 'book': book, 'pg': pg })

    return redirect('book.index')

@login_required(login_url='auth.login')
def update_book(request):
    pass

@login_required(login_url='auth.login')
def delete_book(request, id):
    book = Book.objects.get(pk=id)
    os.remove(str(book.path)) 
    book.delete()
    return redirect('book.index')

@login_required(login_url='auth.login')
def config(request):   
    return render(request, 'user/config.html')

@login_required(login_url='auth.login')
def profile(request):   
    return render(request, 'user/profile.html')

def dark(request):   
    return render(request, 'dark.html')
