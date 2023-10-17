from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

from course_app.models import Course
from users.models import User


@shared_task(name='send_mail')
def send_mail_task(email, course_title):
    """
    Запуск сразу: send_mail.delay()
    Отложенный запуск: send_mail.apply_async(args=(), countdown=15)
    """
    send_mail(
        subject=f'Уведомление об изменении курса {course_title}',
        message='Внимание! Изменился курс, на который Вы подписаны.',
        recipient_list=[email],
        from_email=settings.EMAIL_HOST_USER
    )


@shared_task
def notice_about_update(course_id):
    """
    1. Получает всех подписчиков на курс
    2. Отправляет каждому активному подписчику письмо
    """
    course = Course.objects.get(id=course_id)
    subscribers = User.objects.filter(subscriptions__course=course, subscriptions__is_active=True)
    for subscriber in subscribers:
        send_mail_task.delay(subscriber.email, course.title)


@shared_task(name='check_active_user')
def check_active_user():
    """
    Определяет неактивных пользователей.
    """
    limit_day = timezone.now() - timezone.timedelta(days=30)
    inactive_users = User.objects.filter(is_active=True, last_login__lt=limit_day)
    inactive_users.update(is_active=False)
