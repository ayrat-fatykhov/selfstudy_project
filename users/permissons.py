from rest_framework import permissions


class IsModer(permissions.BasePermission):
    """
    Вводит разрешения в контроллерах для группы'manager'.
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name='manager').exists()
