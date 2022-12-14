"""bib URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bib.views import *

urlpatterns = [
    path('books/', index_book, name="book.index"),
    path('book/novo/', create_book, name="book.create"),
    path('book/<int:id>/<int:pg>', show_book, name='book.show'),
    path('book/<int:id>/', delete_book, name='book.delete'),
    path('perfil/<int:pk>', profile, name='user.profile'),
    path('contrast/', contrast, name='contrast'),
    path('dyslexic/', dyslexic, name='dyslexic'),
    path('font_plus/', font_plus, name='font_plus'),
    path('font_less/', font_less, name='font_less'),


]
