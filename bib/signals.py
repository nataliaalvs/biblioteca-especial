from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book
from .books.convert import convert

@receiver(post_save, sender=Book)
def create_book(sender, instance, created, **kwargs):
    if created:
        print('criado')
        convert(str(instance.path))
    else:
        print('não criado')