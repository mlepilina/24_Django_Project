from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from course_app.models import Course, Lesson, Payment, Subscription
from course_app.paginators import LessonPaginator
from course_app.permissions import IsOwner, IsModerator, IsNotModerator
from course_app.serializers import CourseSerializer, LessonSerializer, PaymentSerializer, SubscriptionSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        default = super().get_permissions()
        if self.action == 'create':
            default.append(
                IsNotModerator()
            )
        if self.action == 'destroy':
            default.append(
                IsOwner()
            )
        if self.action in ('retrieve', 'update', 'partial_update'):
            if self.request.user.is_authenticated and not self.request.user.is_moderator:
                default.append(
                    IsOwner()
                )

        return default

    def get_queryset(self):
        query = super().get_queryset()
        if self.request.user.is_moderator:
            return query

        return query.filter(owner=self.request.user).prefetch_related('subscription_set')


class SubscriptionCreateAPIView(APIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        course_name = request.data.get('course', None)
        is_active = request.data.get('is_active', False)

        course = get_object_or_404(Course.objects, title=course_name)

        new_subscription = Subscription(
            course=course,
            subscriber=request.user,
            is_active=is_active
        )

        new_subscription.save()

        return Response()


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsNotModerator]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = LessonPaginator

    def get_queryset(self):
        query = super().get_queryset()
        if self.request.user.is_moderator:
            return query
        return query.filter(owner=self.request.user)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'method',)
    ordering_fields = ('date',)


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
