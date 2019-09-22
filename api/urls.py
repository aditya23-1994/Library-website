from django.urls import path

from .views import ListApiView, BookRetriveView, BookCreateView, BookUpdateApiView, BookDeleteView


urlpatterns = [

    path('delete/<int:pk>/', BookDeleteView.as_view(), name='api_delete'),

    path('update/<int:pk>/', BookUpdateApiView.as_view(), name='api_edit'),

    path('create/', BookCreateView.as_view(), name='api_create'),

    path('<int:pk>/detail/', BookRetriveView.as_view(), name='api_detail'),

    path('', ListApiView.as_view(), name='api_list'),

]