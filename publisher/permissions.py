from rest_framework.permissions import BasePermission


class IsAdminOrOwner(BasePermission):
    """
    Custom permission to allow only admins to create, update, or delete,
    and allow owners to perform actions on their own shop.
    """

    def has_permission(self, request, view):
        # Allow all GET requests (read-only)
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Allow admins to create, update, or delete
        if request.user and request.user.is_superuser:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        # Allow admins to perform actions on any shop
        if request.user and request.user.is_superuser:
            return True

        # Allow shop owners to perform actions on their own shop
        if obj.owner == request.user:
            return True

        return False
