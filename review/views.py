from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookReviewSerializer, BookReviewGetSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import BookReview
from book.models import Book
from .paginations import ReviewPagination
# Create your views here.

class BookReviewView(ModelViewSet):
    queryset = BookReview.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]  # Ensure the user is authenticated
    pagination_class = ReviewPagination
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookReviewGetSerializer
        else: 
            return BookReviewSerializer
    def get_queryset(self):
        book_id = self.request.query_params.get('book')
        if book_id is None:
            return BookReview.objects.none()

        try:
            book_instance = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        
        queryset = BookReview.objects.filter(book=book_instance)
        return queryset
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Ensure user is authenticated
        if not request.user.is_authenticated:
            return Response({"message": "User not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
        
        # Fetch the book instance from the database
        book_id = self.request.query_params.get('book')
        print(self.kwargs.get('book'))
        try:
            book_instance = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Assign the book instance to the review
        serializer.validated_data['book'] = book_instance
        
        # Assign the reviewer
        serializer.validated_data['reviewer'] = request.user
        
        # Save the review
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)