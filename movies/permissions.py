from rest_framework import permissions


class AuthPermissionToUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated or request.user.is_superuser 
