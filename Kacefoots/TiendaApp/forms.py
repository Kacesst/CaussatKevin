from django import forms
from .models import Producto
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


from .models import Producto
class SignInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        
class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto 
        fields = ['nombre', 'categoria', 'precio']

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 5:
            raise forms.ValidationError("El nombre es demasiado corto")
        return nombre

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        categoria = cleaned_data.get('categoria')
        if not nombre and not categoria:
            raise forms.ValidationError("Nombre y categoría son obligatorios")
        return cleaned_data

class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_password2(self):

        print(self.cleaned_data)

        password2 = self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2
    
