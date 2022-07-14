from rest_framework import permissions

class CustomAdminPermission(permissions.BasePermission):
    def has_permission(self, request, _):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser