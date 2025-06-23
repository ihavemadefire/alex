from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from ..forms import BookForm, ISBNLookupForm
from ..models import Book
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class BookListView(ListView):
    model = Book
    template_name = "books.html"
    context_object_name = "books"


class BookDetailView(DetailView):
    model = Book
    template_name = "book.html"
    context_object_name = "book"


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = "delete_book.html"
    success_url = reverse_lazy("media:books")  # your actual route

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Book deleted successfully.")
        return super().delete(request, *args, **kwargs)


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = "add_book.html"
    success_url = reverse_lazy("media:books")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BookCreateFromISBNView(LoginRequiredMixin, View):
    template_name = "add_from_isbn.html"

    def get(self, request):
        form = ISBNLookupForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = ISBNLookupForm(request.POST)
        if form.is_valid():
            isbn = form.cleaned_data["isbn"]
            book_data = self.lookup_book_by_isbn(isbn)
            if book_data:
                book = Book.objects.create(
                    title=book_data.get("title", "Unknown Title"),
                    creator=book_data.get("author", "Unknown Author"),
                    year=book_data.get("year"),
                    isbn=isbn,
                    publisher=book_data.get("publisher", ""),
                    genre=book_data.get("genre", ""),
                    description=book_data.get("description", ""),
                    notes="Added via ISBN lookup",
                    user=request.user,
                )
                messages.success(request, f"Book '{book.title}' added successfully.")
                return redirect("media:book-detail", pk=book.pk)
            else:
                messages.error(
                    request,
                    "Could not fetch book data. Please check the ISBN or try again later.",
                )
        return render(request, self.template_name, {"form": form})

    def lookup_book_by_isbn(self, isbn):
        """
        Placeholder function to simulate an API call. Replace with a real API integration.
        """
        # Simulated data for demo
        return {
            "title": "Sample Book Title",
            "author": "Sample Author",
            "year": 1999,
            "publisher": "Sample Publisher",
            "genre": "Fiction",
            "description": "A sample description returned from a book lookup API.",
        }
