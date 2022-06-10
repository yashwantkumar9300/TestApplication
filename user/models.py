from django.db import models

# Create your models here.

class User(models.Model):
    idno = models.AutoField(primary_key=True)
    mobile = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    image = models.ImageField(default='images/user.png',upload_to='user_image/')
    models.DateField(auto_now_add=True)

class Contact(models.Model):
    idno = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    email = models.EmailField()
    meaasge = models.TextField()

class SmsModel(models.Model):
    idno = models.AutoField(primary_key = True)
    fromm = models.CharField(max_length=10)
    to = models.CharField(max_length=16)
    text = models.TextField(max_length=120)