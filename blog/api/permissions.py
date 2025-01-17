from rest_framework import permissions


class ExampleComOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        email = getattr(request.user, 'email', '')
        return email.split("@")[-1] == 'example.com'


class AuthorModifyOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user == obj.author


class IsAdminUserForObject(permissions.IsAdminUser):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_staff)