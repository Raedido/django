from django.db import models
from .forms import Registerform
# Create your models here

class RegisterModel(models.Model):
    fname= models.CharField(max_length=100)
    lname= models.CharField(max_length=100)
    country= models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    #message= models.CharField(label='Your Message', widget=models)
   
    class Meta:
        db_table = "register"