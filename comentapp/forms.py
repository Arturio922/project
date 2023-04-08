from .models import Coment
from django.forms import ModelForm, TextInput, Textarea, forms
from django.contrib.auth.models import User


class ComentForm(ModelForm):
    class Meta:
        model = Coment
        fields = ['title', 'full_text']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше имя'
            }),

            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш отзыв'

            })
        }

#
# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'email')
#
#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password'] != cd['password2']:
#             raise forms.ValidationError('Passwords don\'t match.')
#         return cd['password2']