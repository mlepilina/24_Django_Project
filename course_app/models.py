from rest_framework import serializers
from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=250, verbose_name='название курса', unique=True)
    preview = models.ImageField(upload_to='course_app/', verbose_name='превью (картинка)', **NULLABLE)
    description = models.TextField(verbose_name='описание курса', **NULLABLE)

    owner = models.ForeignKey(User, to_field='email', db_column="owner", on_delete=models.CASCADE,
                              verbose_name='создатель курса', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=250, verbose_name='название урока')
    preview = models.ImageField(upload_to='course_app/', verbose_name='превью (картинка)', **NULLABLE)
    description = models.TextField(verbose_name='описание урока', **NULLABLE)
    video_link = models.TextField(verbose_name='ссылка на видео', **NULLABLE)

    course = models.ForeignKey(Course, to_field='title', db_column="course", on_delete=models.CASCADE, verbose_name='из курса')
    owner = models.ForeignKey(User, to_field='email', db_column="owner", on_delete=models.CASCADE,
                              verbose_name='создатель урока', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Payment(models.Model):

    class METHOD_CHOICES(models.TextChoices):
        CASH = ('наличные', 'наличные')
        TRANSFER = ('перевод на счет', 'перевод на счет')

    method = models.CharField(max_length=50, choices=METHOD_CHOICES.choices, verbose_name='способ оплаты')
    date = models.DateField(auto_now_add=True, verbose_name='дата оплаты')
    amount = models.FloatField(verbose_name='сумма оплаты')

    course = models.ForeignKey(Course, to_field='title', db_column="course", on_delete=models.CASCADE, verbose_name='оплаченный курс', **NULLABLE)
    client = models.ForeignKey(User, to_field='email', db_column="client", on_delete=models.CASCADE, verbose_name='клиент-плательщик', **NULLABLE)

    def __str__(self):
        return f'{self.id} {self.method} {self.date}'

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплата'


class Subscription(models.Model):

    subscriber = models.ForeignKey(User, to_field='email', db_column="subscriber", on_delete=models.CASCADE, verbose_name='подписчик')
    course = models.ForeignKey(Course, to_field='title', db_column="course", on_delete=models.CASCADE, verbose_name='курс подписки')
    is_active = models.BooleanField(default=False, verbose_name='подписан')

    def __str__(self):
        return f'{self.subscriber} {self.course} {self.is_active}'

    class Meta:
        verbose_name = 'подписка на курс'
        verbose_name_plural = 'подписки на курсы'


