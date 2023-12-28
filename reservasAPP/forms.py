from django import forms
from django.contrib.auth.models import User
from .models import Reserva

class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre', 'telefono', 'fecha_reserva', 'hora_reserva', 'cantidad_personas', 'estado', 'observacion']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_reserva': forms.DateInput(attrs={'class': 'form-control'}),
            'hora_reserva': forms.TimeInput(attrs={'class': 'form-control'}),
            'cantidad_personas': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'observacion': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_cantidad_personas(self):
        cantidad_personas = self.cleaned_data['cantidad_personas']
        if not 1 <= cantidad_personas <= 15:
            raise forms.ValidationError('La cantidad de personas debe estar entre 1 y 15.')
        return cantidad_personas
