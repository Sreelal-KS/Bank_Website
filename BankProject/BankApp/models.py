from django.db import models

gender_choices = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
)

account_choices = (
    ('savings', 'Savings Account'),
    ('current', 'Current Account'),
)


# Create your models here.

class UserDetails(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=20, choices=gender_choices, default=None)
    phone_number = models.IntegerField(unique=True, default=None)
    Email = models.EmailField(max_length=100, unique=True, default=None)
    address = models.TextField(max_length=250, default=None)
    account_type = models.CharField(max_length=50, choices=account_choices, default=None)
    materials = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
