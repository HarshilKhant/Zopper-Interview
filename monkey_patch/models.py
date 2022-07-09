from django.db import models

class User_Details(models.Model):
    username = models.CharField(db_column="username", primary_key=True)
    contact = models.IntegerField(db_column="contact", primary_key=True)
    address_line1 = models.TextField(max_length=30, null=True)
    address_line2 = models.TextField(max_length=30, null=True)
    address_line3 = models.TextField(max_length=22, null=True)
    city = models.CharField(null=True)
    state = models.CharField(null=True)
    pincode = models.IntegerField(null=True)