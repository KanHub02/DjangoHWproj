from django.db import models


class Book(models.Model):
    GENRE_CHOICE = (
        ("Drama", "Drama"),
        ("Fantasy", "Fantasy"),
        ("Thriller", "Thriller"),
        ("Romance", "Romance"),
        ("Westerns", "Westerns"),
        ("Literary Fiction", "Literary Fiction"),
        ("Humor", "Humor"),
        ("Motivational", "Motivational"),
        ("Historical Fiction", "Historical Fiction"),
        ("Masnavyi", "Masnavyi")

    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="")
    author = models.CharField(max_length=30)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICE)
    year_of_issue = models.PositiveIntegerField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    age_control = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class BookUser(models.Model):
    username = models.CharField(max_length=200)
    def __str__(self):
        return self.username

class BookComment(models.Model):
    books = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="books_comment")
    user = models.ForeignKey(BookUser,
                             on_delete=models.CASCADE,
                             related_name="books_comment",
                             null=True)
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.books.title