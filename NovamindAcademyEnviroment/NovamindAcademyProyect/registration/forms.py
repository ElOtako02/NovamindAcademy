from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioRegistroConCorreo(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Obligatorio, 254 caracteres máximo y valido')

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def clean_email(self):
        correo = self.cleaned_data.get('email')
        if User.objects.filter(email=correo).exists():
            raise forms.ValidationError("El correo ya esta registrado")
        return correo
        