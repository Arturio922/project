from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def new_user(request):
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    # if form.is_valid():
    #     form.save()
    #     email = form.cleaned_data.get('email')
    #     messages.success(request, 'Вы успешно зарегистрировались')
    #     return redirect('user')
    # else:
    #     form = UserCreationForm()

    return render(request, 'usersapp/new_user.html')


def user(request):
    return render(request, 'usersapp/user.html')
