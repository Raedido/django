from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import Registerform
from .models import RegisterModel 
def register(request):
    if request.method == 'POST':
        form = Registerform(request.POST)
       
        if form.is_valid():
            # Process the data here, for example, save it to the database
            print(form.cleaned_data)
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            country = form.cleaned_data['country']
            email = form.cleaned_data['email']
            print("fname:", fname)
            print("lname:", lname)
            print("country:", country)
            print("email:", email)
            register = RegisterModel.objects.create(fname=fname, lname=lname, country=country, email=email)
            register.save()
            #message = form.cleaned_data['message']
            # Redirect to a success page or do something else
            return HttpResponse("Thank you for adding your data")
    else:
        form = Registerform()
    return render(request, 'forms/register.html', {'form': form})
 
def success_view(request):
    return render(request, 'forms/success.html')