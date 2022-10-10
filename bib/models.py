from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Para utilizar a autenticação customizada:
from customauth.models import MyUser
# from django.contrib.auth.base_user import AbstractBaseUser

def user_directory_path(instance, name):
    # file will be uploaded to MEDIA_ROOT/books/user_<id>/<filename>
    return 'books/user_{0}/{1}'.format(instance.user_id.id, name)

class Genre(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    path = models.FileField(verbose_name='arquivo', upload_to=user_directory_path)
    current_page = models.IntegerField(validators=[MinValueValidator(0)])
    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)