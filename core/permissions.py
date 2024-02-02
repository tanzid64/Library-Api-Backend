from rest_framework.permissions import BasePermission

class IsModOrPublisherOrUser(BasePermission):
    """
    Custom permission to allow different access levels:
    - Read access for any user (GET).
    - Create access for publishers (is_publisher=True) and moderators (is_mod=True).
    - Edit and delete access for moderators only (is_mod=True).
    """

    def has_permission(self, request, view):
        # Allow read-only access for all users (GET, HEAD, OPTIONS)
        if request.method == 'GET':
            return True

        # Allow creation for publishers and moderators
        if request.method == 'POST' and (request.user.is_publisher or request.user.is_mod):
            return True

        # Allow edit and delete access for moderators only
        return request.user.is_mod
