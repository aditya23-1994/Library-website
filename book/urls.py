from django.urls import path
from .views import HomePageView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

from .models import Book


urlpatterns = [

    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),

    path('book/<int:pk>/edit/', BookUpdateView.as_view(), name='book_edit'),

    path('book/new/', BookCreateView.as_view(), name='book_new'),

    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),

    path('', HomePageView.as_view(), name='home'),

]