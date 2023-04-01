from datetime import datetime
from os import listdir

from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('dir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    template_name = 'app/time.html'
    current_time = datetime.now().time()
    msg = f'Текущее время: {current_time.strftime("%H:%M:%S")}'
    context = {
        'msg': msg
    }
    return render(request, template_name, context)


def workdir_view(request):
    template_name = 'app/dir.html'
    workdir = listdir(path='.')
    context = {
        'workdir': workdir
    }
    return render(request, template_name, context)
