from rest_framework import generics

from book.models import Book
from .serializers import BookSerializer, BookRetriveSerializer, BookUpdateSerializer, BookDeleteSerializer

# Create your views here.

class ListApiView(generics.ListAPIView):

    lookup_field = 'pk'

    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetriveView(generics.RetrieveAPIView):

   lookup_field = 'pk'
   serializer_class = BookRetriveSerializer

   def get_queryset(self):
       return Book.objects.all()

class BookCreateView(generics.CreateAPIView):

   lookup_field = 'pk'
   serializer_class = BookSerializer

   def post_queryset(self):
       return Book.objects.all()

class BookUpdateApiView(generics.UpdateAPIView):
    lookup_field = 'pk'
    serializer_class = BookUpdateSerializer

    def post_queryset(self):
       return Book.objects.all()

class BookDeleteView(generics.DestroyAPIView):

   lookup_field = 'pk'
   serializer_class = BookDeleteSerializer

   def post_queryset(self):
       return Book.objects.all()
