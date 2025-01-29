from django.db import models
from catalogue.models import Book
from users.models import Student

class IssuedByStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)  # Allow null for unreturned books

    def __str__(self):
        return f"{self.student} → {self.book}"