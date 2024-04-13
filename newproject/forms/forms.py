# myapp/ forms.py
from django import forms



class Registerform(forms.Form):
    fname= forms.CharField(label='first Name', max_length=100)
    lname= forms.CharField(label='last Name', max_length=100)
    country= forms.CharField(label='country Name', max_length=100)
    email= forms.EmailField(label='Your Email')
    #message= forms.CharField(label='Your Message', widget=forms)
