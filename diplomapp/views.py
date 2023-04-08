from django.shortcuts import render, redirect
# from django.urls import reverse_lazy
# from django.views.generic import CreateView
#
# from .models import User
from .forms import UserForm


def index(request):
    data = {
        'title': 'Чистюля',
    }
    return render(request, 'diplomapp/diplom.html', data)


def contact(request):
    return render(request, 'diplomapp/contact.html')


def service(request):
    return render(request, 'diplomapp/service.html')


def new_user(request):

    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user')
        else:
            error = 'Ошибка'

    form = UserForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'diplomapp/new_user.html', data)


def user(request):
    return render(request, 'diplomapp/user.html')


