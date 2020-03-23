from django.db import models
import datetime
# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=100, blank=False, null=False, verbose_name='email')
    FullName = models.CharField(max_length=100, blank=False, null=False, verbose_name='Full Name')
    BirthDate = models.DateField(blank=False, null=False, verbose_name='Birth date')
    Phone = models.IntegerField(blank=False, null=False, verbose_name='Phone number')
    City = models.CharField(blank=False, null=False,max_length=100, verbose_name='City')
    password = models.CharField(blank=False,max_length=100, null=False, verbose_name='password')
    date_joined = models.DateTimeField(auto_now=True)