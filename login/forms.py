from django import forms


class UserRegistrationForm(forms.Form):
    email = forms.CharField(
        label = 'Email',
    )
    password = forms.CharField(
        label = 'Clave',
        widget = forms.PasswordInput()
    )
