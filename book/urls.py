from django.urls import path
from . import views, models
from datetime import datetime, timedelta
start_data = datetime.today() - timedelta(days=10)

app_name = "books_url"
urlpatterns = [
    path('books/', views.BookListView.as_view(), name="books_all_url"),
    path('books/latest/', views.BookListView.as_view(
        queryset=models.Book.objects.filter(
            created_date__gt=start_data).order_by("-id")
    ), name="latest"),
    path('books/drama/', views.BookListView.as_view(
        queryset=models.Book.objects.filter(genre="Drama").order_by("-id")
    ), name="Drama"),
    path('books/fantasy/', views.BookListView.as_view(
        queryset=models.Book.objects.filter(genre="Fantasy").order_by("-id")
    ), name="Fantasy"),
    path('books/thriller/', views.BookListView.as_view(
        queryset=models.Book.objects.filter(genre="Thriller").order_by("-id")
    ), name="thriller"),
    path('books/romance/', views.BookListView.as_view(
        queryset=models.Book.objects.filter(genre="Romance").order_by("-id")
    ), name="Romance"),
    path('books/westerns/', views.BookListView.as_view(
        queryset=models.Book.objects.filter(genre="Westerns").order_by("-id")
    ), name="westerns"),
    path('books/literary_fiction/', views.BookListView.as_view(
        queryset=models.Book.objects.filter(genre="Literary Fiction").order_by("-id")
    ), name="Literary Fiction"),
    path('books/humor/', views.BookListView.as_view(
        queryset=models.Book.objects.filter(genre="Humor").order_by("-id")
    ), name="Humor"),
    path('books/motivational/', views.BookListView.as_view(
        queryset=models.Book.objects.filter(genre="Motivational").order_by("-id")
    ), name="Motivational"),
    path('books/historical_fiction/', views.BookListView.as_view(
        queryset=models.Book.objects.filter(genre="Historical Fiction").order_by("-id")
    ), name="Historical Fiction"),
    path('books/masnavyi/', views.BookListView.as_view(
        queryset=models.Book.objects.filter(genre="Masnavyi").order_by("-id")
    ), name="Masnavyi"),



    path('books/<int:id>/', views.BookDetailView.as_view(), name="books_url"),
    path('books/<int:id>/update/', views.BookUpdateView.as_view(), name="books_update"),
    path('books/<int:id>/delete/', views.BookDeleteView.as_view(), name="books_delete"),
    path('add-books/', views.BookCreateView.as_view(), name="add_books"),
]