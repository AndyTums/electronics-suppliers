from rest_framework import permissions


class IsActive(permissions.BasePermission):
    """ Проверка является ли пользователь активным."""

    def has_object_permission(self, request, view, obj):
        if request.user.is_active == "True":
            return True
        return False
