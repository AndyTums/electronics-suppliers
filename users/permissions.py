from rest_framework import permissions


class IsActive(permissions.BasePermission):
    """ Проверка является ли пользователь активным."""

    def has_permission(self, request, view):
        # Проверяем, является ли пользователь аутентифицированным и активным
        return request.user.is_authenticated and request.user.is_active

    def has_object_permission(self, request, view, obj):
        # Проверяем, является ли пользователь активным
        return request.user.is_active
