from rest_framework import serializers

from course_app.models import Course, Lesson, Payment, Subscription
from course_app.validators import LinkValidator

from course_app.tasks import notice_about_update


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = [
            'id',
            'title',
            'preview',
            'description',
            'video_link',
            'course',
            'owner',
        ]
        validators = [
            LinkValidator(fields=['video_link', 'description']),
        ]

    def save(self, **kwargs):
        lesson = super().save(**kwargs)
        notice_about_update.delay(lesson.course.id)

        return lesson


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = [
            'subscriber',
            'course',
            'is_active',
        ]


class CourseSerializer(serializers.ModelSerializer):

    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)
    number_of_lessons = serializers.IntegerField(source='lesson_set.all.count', read_only=True)
    is_subscribed = serializers.SerializerMethodField(method_name='qwe')

    class Meta:
        model = Course
        fields = [
            'title',
            'preview',
            'description',
            'number_of_lessons',
            'lessons',
            'owner',
            'is_subscribed'
        ]
        # validators = [LinkValidator(field='description')]

    def qwe(self, obj):
        return obj.subscription_set.filter(subscriber=self._context['view'].request.user, is_active=True).exists()


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = [
            'date',
            'course',
            'method',
            'amount',
            'client',
        ]
