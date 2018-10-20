from django import forms


class UserRegistrationForm(forms.Form):
    email = forms.CharField(
        label = 'Correo Eléctronico',
    )
    password = forms.CharField(
        label = 'Clave',
        widget = forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        label = 'Confirmación',
        widget = forms.PasswordInput()
    )
