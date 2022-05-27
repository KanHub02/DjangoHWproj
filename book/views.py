from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from . import models, forms
from datetime import datetime, timedelta
from django.views import generic

start_data = datetime.today() - timedelta(days=10)


class BookListView(generic.ListView):
    template_name = "books.html"
    queryset = models.Book.objects.order_by("id")

    def get_queryset(self):
        return self.queryset


# def all_books(request):
#     queryset = models.Book.objects.order_by("-id")
#     return render(request, "books.html", {"books": queryset})
#
#
# def all_books_latest(request):
#     queryset = models.Book.objects.filter(created_date__gt=start_data).order_by("-id")
#     return render(request, "books.html", {"books": queryset})
#
#
# def all_books_drama(request):
#     queryset = models.Book.objects.filter(genre__in="Drama").order_by("-id")
#     return render(request, "books.html", {"books": queryset})
#
#
# def all_books_fantasy(request):
#     queryset = models.Book.objects.filter(genre__in="Fantasy").order_by("-id")
#     return render(request, "books.html", {"books": queryset})
#
#
# def all_books_thriller(request):
#     queryset = models.Book.objects.filter(genre__in="Thriller").order_by("-id")
#     return render(request, "books.html", {"books": queryset})
#
#
# def all_books_romance(request):
#     queryset = models.Book.objects.filter(genre__in="Romance").order_by("-id")
#     return render(request, "books.html", {"books": queryset})
#
#
# def all_books_westerns(request):
#     queryset = models.Book.objects.filter(genre__in="Westerns").order_by("-id")
#     return render(request, "books.html", {"books": queryset})
#
#
# def all_books_literary_fiction(request):
#     queryset = models.Book.objects.filter(genre__in="Literary Fiction").order_by("-id")
#     return render(request, "books.html", {"books": queryset})
#
#
# def all_books_humor(request):
#     queryset = models.Book.objects.filter(genre__in="Humor").order_by("-id")
#     return render(request, "books.html", {"books": queryset})
#
#
# def all_books_motivational(request):
#     queryset = models.Book.objects.filter(genre__in="Motivational").order_by("-id")
#     return render(request, "books.html", {"books": queryset})
#
#
# def all_books_historical_fiction(request):
#     queryset = models.Book.objects.filter(genre__in="Historical Fiction").order_by("-id")
#     return render(request, "books.html", {"books": queryset})
#
#
# def all_books_masnavyi(request):
#     queryset = models.Book.objects.filter(genre__in="Masnavyi").order_by("-id")
#     return render(request, "books.html", {"books": queryset})

class BookDetailView(generic.DetailView):
    template_name = "book_detail.html"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=book_id)


# def get_book_detail(request, id):
#     object = get_object_or_404(models.Book, id=id)
#     return render(request, "book_detail.html", {"book": object})

class BookCreateView(generic.CreateView):
    template_name = "add_books.html"
    form_class = forms.BookForm
    queryset = models.Book.objects.all()
    success_url = "/books/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookCreateView, self).form_valid(form=form)


# def add_books(request):
#     method = request.method
#     if method == "POST":
#         form = forms.BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # return HttpResponse("Books Created successfully")
#             return redirect(reverse("books_url:books_all_url"))
#     else:
#         form = forms.BookForm()
#     return render(request, "add_books.html", {"form": form})
class BookUpdateView(generic.UpdateView):
    template_name = "book_update.html"
    form_class = forms.BookForm
    success_url = "/books/"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=book_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookUpdateView, self).form_valid(form=form)


# def book_update(request, id):
#     book_object = get_object_or_404(models.Book, id=id)
#     if request.method == "POST":
#         form = forms.BookForm(instance=book_object, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("books_url:books_all_url"))
#     else:
#         form = forms.BookForm(instance=book_object)
#     return render(request, "book_update.html", {"form": form,
#                                                 "object": book_object})
class BookDeleteView(generic.DeleteView):
    success_url = "/books/"
    template_name = "confirm_delete_book.html"

    def get_object(self, **kwargs):
        books_id = self.kwargs.get("id")
        return get_object_or_404(models.Book,id=books_id)

# def book_delete(request, id):
#     book_object = get_object_or_404(models.Book, id=id)
#     book_object.delete()
#     return redirect(reverse("books_url:books_all_url"))