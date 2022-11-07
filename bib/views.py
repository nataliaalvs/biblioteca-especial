from django.shortcuts import render, redirect
from customauth.forms import UserChangeForm
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
import PyPDF2
import os

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required(login_url='auth.login')
def index_book(request):   
    books = Book.objects.filter(user=request.user)
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
    if book.user.id == request.user.id:
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
    if book.user.id == request.user.id:
        os.remove(str(book.path)) 
        book.delete()
    return redirect('book.index')

@login_required(login_url='auth.login')
def profile(request, pk):   
    user = MyUser.objects.get(pk=pk)
    if user.id == request.user.id:
        form = UserChangeForm(request.POST or None, instance=user)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('./' + str(request.user.id))

        return render(request, 'user/profile.html', {"form":form})

    return redirect('home')
    
@login_required(login_url='auth.login')
def dyslexic(request):  
    user = MyUser.objects.get(pk=request.user.id)
    if user.dyslexic:
        user.dyslexic = False
    else: 
        user.dyslexic = True
    user.save()
    next = request.POST.get('next', '/')    
    return redirect(next)

@login_required(login_url='auth.login')
def contrast(request):  
    user = MyUser.objects.get(pk=request.user.id)
    if user.contrast:
        user.contrast = False
    else: 
        user.contrast = True
    user.save()
    next = request.POST.get('next', '/')    
    return redirect(next)

@login_required(login_url='auth.login')
def font_plus(request):
    user = MyUser.objects.get(pk=request.user.id)
    if user.font_size < 1.7:
        user.font_size = round(user.font_size + 0.1, 2)
        user.save()
    next = request.POST.get('next', '/')    
    return redirect(next)

@login_required(login_url='auth.login')
def font_less(request):
    user = MyUser.objects.get(pk=request.user.id)
    if user.font_size > 0.5:
        user.font_size = round(user.font_size - 0.1, 2)
        user.save()
    next = request.POST.get('next', '/')    
    return redirect(next)