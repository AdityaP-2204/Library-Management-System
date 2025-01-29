from django.db import models
from django.contrib.auth.models import User  # Integrate Django auth

class Staff(models.Model):
    name = models.CharField(max_length=255)  # Changed from staff_name
    dob = models.DateField()
    address = models.TextField()
    designation = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_joining = models.DateField()

    def __str__(self):
        return self.name

class Librarian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Replaces admin_login/password
    # Add librarian-specific fields here (if needed)

    def __str__(self):
        return self.user.username