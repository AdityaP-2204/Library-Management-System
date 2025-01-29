from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)  # Changed from author_name
    dob = models.DateField()
    address = models.TextField()
    experience = models.IntegerField()

    def __str__(self):
        return self.name

class Book(models.Model):
    book_code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)  # Changed from book_name
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_of_purchase = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subject_code = models.CharField(max_length=100)
    rack_no = models.IntegerField()
    no_of_books = models.IntegerField()

    def __str__(self):
        return self.name