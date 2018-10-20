from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm

# Create your views here.
def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserRegistrationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
        # return HttpResponseRedirect("/response/")
            return render(request, 'login/response.html', {'email' : email,
                'password' : password })

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserRegistrationForm()

    return render(request, 'login/index.html', {'form': form})

def response(request,mesage):
    return HttpResponse("aso")
