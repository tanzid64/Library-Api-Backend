from rest_framework.permissions import BasePermission
from .models import Book

class CanManageBooks(BasePermission):
    """
    Custom permission to allow users to see book details,
    publishers to add, edit, and delete their own books,
    and admins to do all actions.
    """

    def has_permission(self, request, view):
        # Allow all users to see book details
        if request.method == 'GET':
            return True
        
        # Check if the user is a publisher
        is_publisher = request.user.is_publisher
        
        # Allow publishers to add books
        if request.method == 'POST' and is_publisher:
            return True
        
        # Allow publishers to edit and delete their own books
        if is_publisher and request.method in ['PUT', 'PATCH', 'DELETE']:
            # Assuming your Book model has a field 'publisher' which stores the publisher's user object
            book_id = view.kwargs.get('pk')
            book = Book.objects.get(pk=book_id)
            if book.publisher == request.user:
                return True
        
        # Allow admins to do all actions
        if request.user.is_staff and request.method == 'DELETE':
            return True
        
        return False
