from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm
from .seguridad import Seguridad

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
            seg = Seguridad()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirmation = form.cleaned_data['password_confirmation']
            msg = seg.registrarUsuario(email, password, confirmation)
            return render(request, 'login/response.html', {'msg' : msg })

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserRegistrationForm()

    return render(request, 'login/index.html', {'form': form})

def response(request,mesage):
    return HttpResponse("")
