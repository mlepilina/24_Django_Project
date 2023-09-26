from rest_framework import serializers

from course_app.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = [
            'title',
            'preview',
            'description',
        ]


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
