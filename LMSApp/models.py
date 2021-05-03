from django.db import models
from django.utils import timezone


# Create your models here.
class Register(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=255, blank=False)
    Roll = models.CharField(max_length=255, blank=False)
    Dob = models.DateField(blank=False, default=timezone.now)
    Class = models.CharField(max_length=255, blank=False)
    Department = models.CharField(max_length=255, blank=False)
    Email = models.CharField(max_length=255, blank=False)
    Phone = models.CharField(max_length=15, blank=False)
    Created = models.DateField(default=timezone.now)
    is_member = models.CharField(blank=False, default='NO', max_length=3)


class Book(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Book_Name = models.CharField(max_length=255, blank=False)
    Author = models.CharField(max_length=255, blank=False)
    Volume = models.CharField(max_length=255, blank=False)
    Update = models.DateField(default=timezone.now)

# class Membership(models.Model):
#     Id = models.BigAutoField(primary_key=True)
#     Member_Id = models.ForeignKey("LMSApp.Register", on_delete=models.CASCADE)
#     Membership_Date = models.DateField(default=timezone.now)
