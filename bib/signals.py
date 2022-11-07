from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book
from .books.convert import convert
import asyncio
import threading

@receiver(post_save, sender=Book)
def create_book(sender, instance, created, **kwargs):
    thread = threading.Thread(target=prepare_create_book, args=(instance, created,  ))
    thread.start()

def prepare_create_book(instance, created):
    if created:
        print('criado')
        convert(str(instance.path))
    else:
        print('não criado')