from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
	phone_number=models.CharField("Phone Number",max_length=20,blank=False)
	country=models.CharField("Country",max_length=100,blank=False)
	about=models.TextField("About", default="write about yourself here",max_length=1000,blank=False)
	datetoday=models.DateTimeField(auto_now_add=True)
