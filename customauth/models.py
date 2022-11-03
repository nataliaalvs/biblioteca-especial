from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, password):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Usuário deve ter um endereço de email.')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(
        verbose_name='Endereço de e-mail',
        max_length=255,
        unique=True,
    )
    font_size = models.FloatField(default=1, validators=[MinValueValidator(0)])
    contrast = models.BooleanField(default=False)
    dyslexic = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    date_joined = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'theme']
    class Meta:
        verbose_name = _('usuário')
        verbose_name_plural = _('usuários')