from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = 'Вы не являетесь создателем курса/урока'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class IsModerator(BasePermission):
    message = 'Вы не являетесь модератором/владельцем'

    def has_permission(self, request, view):
        return request.user.is_moderator


class IsNotModerator(BasePermission):
    message = 'Для модераторов доступ запрещен'

    def has_permission(self, request, view):
        return not request.user.is_moderator
