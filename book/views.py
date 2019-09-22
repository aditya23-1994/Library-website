from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book


# Create your views here.

class HomePageView(ListView):

    model = Book

    template_name = 'home.html'

class BookDetailView(DetailView):

    model = Book

    template_name = 'book_detail.html'

class BookCreateView(CreateView):

    model = Book

    template_name = 'book_new.html'

    fields = '__all__'

class BookUpdateView(UpdateView):

    model = Book

    template_name = 'book_edit.html'

    fields = ['title', 'body']

class BookDeleteView(DeleteView):

    model = Book

    template_name = 'book_delete.html'

    success_url = reverse_lazy('home')