from django.contrib import admin

from course_app.models import Course, Lesson, Payment


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'course',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('course', 'user', 'date')
