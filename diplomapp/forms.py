from .models import User
from django.forms import ModelForm, EmailInput, PasswordInput


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

        widgets = {
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваш e-mail'
            }),

            'password': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш пароль'

            })
        }
