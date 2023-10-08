from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):

    username = None

    email = models.EmailField(verbose_name='контактный email', unique=True)
    surname = models.CharField(max_length=100, verbose_name='фамилия')
    name = models.CharField(max_length=100, verbose_name='имя')
    phone = models.PositiveBigIntegerField(verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='город', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    @property
    def is_moderator(self):
        return self.groups.filter(name='moderator').exists()
