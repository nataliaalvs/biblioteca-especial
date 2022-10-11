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
        form.save() 
        # book = Book.objects.get(path=form.cleaned_data['path'])
        # convert(str(form.cleaned_data['path']), request.user.id)
        # print('chamando convert(' + str(form.cleaned_data['path']) + ')')

        return redirect('book.index')
    return render(request, 'books/create.html', { 'form': form })



@login_required(login_url='auth.login')
def show_book(request, id, pg):
    book = Book.objects.get(pk=id)
    if str(book.user_id) == str(request.user.email):
        pdfFileObj = open(str(book.path), 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)    
        count = pdfReader.numPages
        if count >= pg:
            book.current_page = pg
            book.save()
            content_book = ('<h2> <label for="chapter" class="col-sm-10  col-lg-12 col-form-label">Pág. ' +str(pg)+ '</label> </h2> <div class="row"> <div class="col-xs-12 col-sm-12 col-md-12 col-lg-12"> <div class="text-justify">' + pdfReader.getPage(pg).extractText() + ' </div> </div> </div> <br>')
            pdfFileObj.close()
            return render(request, 'books/show.html', { 'content_book': content_book, 'book': book, 'pg': pg })

    return redirect('book.index')

@login_required(login_url='auth.login')
def update_books(request):
    pass

@login_required(login_url='auth.login')
def delete_books(request):
    return redirect('book.index')

@login_required(login_url='auth.login')
def config(request):   
    return render(request, 'user/config.html')

@login_required(login_url='auth.login')
def profile(request):   
    return render(request, 'user/profile.html')

def dark(request):   
    return render(request, 'dark.html')
