from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    mail_key = models.CharField(max_length=30, default='', verbose_name='key', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []