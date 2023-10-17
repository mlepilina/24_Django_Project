from course_app.models import Lesson, Subscription, Course
from users.models import User


def notice_about_update(course: Course):
    """
    1. Получает всех подписчиков на курс
    2. Отправляет каждому активному подписчику письмо
    """

    subscribers = User.objects.filter(subscriptions__course=course, subscriptions__is_active=True)
    for subscriber in subscribers:
        pass

