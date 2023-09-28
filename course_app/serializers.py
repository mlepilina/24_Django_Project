from rest_framework import serializers

from course_app.models import Course, Lesson, Payment


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
        ]


class CourseSerializer(serializers.ModelSerializer):

    lessons = LessonSerializer(source='lesson_set', many=True)
    number_of_lessons = serializers.IntegerField(source='lesson_set.all.count')


    class Meta:
        model = Course
        fields = [
            'title',
            'preview',
            'description',
            'number_of_lessons',
            'lessons',
        ]


class PaymentSerializer(serializers.ModelSerializer):
    lesson_title = serializers.SerializerMethodField()

    def get_lesson_title(self, obj):
        if obj.lesson is None:
            return 'все уроки'
        return obj.lesson.title

    class Meta:
        model = Payment
        fields = [
            'date',
            'lesson_title',
            'course',
            'method',
            'amount',
            'user',
        ]
