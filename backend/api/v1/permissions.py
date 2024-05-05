from rest_framework.permissions import BasePermission


class IsAdminAuthorOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        return (request.method in ('GET',)
                or obj.author == request.user
                or request.user.is_staff)
