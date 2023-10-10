from rest_framework import status
from rest_framework.test import APITestCase

from course_app.models import Course
from users.models import User


class CourseTestCase(APITestCase):

    fixtures = [
        'users/fixtures/test_user.json'
    ]

    def setUp(self) -> None:
        self.user = User.objects.get()
        self.client.force_authenticate(user=self.user)

    def test_create_course(self):
        """Тестирование создания курса"""
        data = {
            'title': 'Course_test',
        }

        response = self.client.post(
            '/courses/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )


class LessonTestCase(APITestCase):

    fixtures = [
        'users/fixtures/test_user.json',
        'course_app/fixtures/test_courses.json'
    ]

    def setUp(self) -> None:
        self.user = User.objects.get()
        self.client.force_authenticate(user=self.user)

    def test_create_lesson(self):
        """Тестирование создания урока"""

        random_course = Course.objects.all().first()
        data = {
            'title': 'Title_test',
            'course': random_course.title
        }

        response = self.client.post(
            '/lesson/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

