from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_no = models.CharField(max_length=15)

    class Meta:
        abstract = True  # Reusable template

class Student(Person):
    student_id = models.AutoField(primary_key=True)
    branch = models.CharField(max_length=100)
    fine = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    # Removed issue_date/expiry_date (moved to transactions)

    def __str__(self):
        return self.name

class Faculty(Person):
    f_id = models.AutoField(primary_key=True)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name