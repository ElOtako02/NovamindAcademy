from django.shortcuts import render
from django.views.generic import CreateView
from .forms import FormularioRegistroConCorreo
from django.urls import reverse_lazy
from django import forms

#Create your views here
class Registro(CreateView):
    form_class = FormularioRegistroConCorreo
    template_name = 'registration/registro.html'

    def get_success_url(self) -> str:
        return reverse_lazy('login') + "?registroOK"
    
    def get_form(self, form_class=None):#
        form = super(Registro, self).get_form()

        #modificar campos
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2','placeholder':'Correo'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Confirmar Contraseña'})

        for fieldname in ['username','email','password1','password2']:
            form.fields[fieldname].label = ''
    
        return form