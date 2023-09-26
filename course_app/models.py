from rest_framework import serializers
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=250, verbose_name='название курса', unique=True)
    preview = models.ImageField(upload_to='course_app/', verbose_name='превью (картинка)', **NULLABLE)
    description = models.TextField(verbose_name='описание курса', **NULLABLE)

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

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


