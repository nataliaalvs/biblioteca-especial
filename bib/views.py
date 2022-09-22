from django.shortcuts import render

# Create your views here.

def index(request):
    return render (request, 'index.html')

def login(request):   
    return render (request, 'login.html')

def cadastro(request):   
    return render (request, 'cadastro.html')

def biblioteca(request):   
    return render (request, 'biblioteca.html')

def addLivro(request):   
    return render (request, 'addLivro.html')

def config(request):   
    return render (request, 'config.html')

def perfil(request):   
    return render (request, 'perfil.html')

def livro(request):   
    return render (request, 'pagLeitura.html')

def dark(request):   
    return render (request, 'dark.html')
