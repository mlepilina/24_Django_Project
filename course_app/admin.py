from django.contrib import admin

from course_app.models import Course, Lesson, Payment, Subscription


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'course',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('course', 'client', 'date')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('subscriber', 'course', 'is_active')
