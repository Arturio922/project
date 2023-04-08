from django.shortcuts import render, redirect
from .models import Coment
from .forms import ComentForm


def comhome(request):
    coments = Coment.objects.all()
    return render(request, 'comentapp/comentadd.html', {'coments': coments})


def create(request):
    error = ''
    if request.method == 'POST':
        form = ComentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comhome')
        else:
            error = 'Ошибка'

    form = ComentForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'comentapp/create.html', data)
