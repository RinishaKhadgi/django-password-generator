from django.shortcuts import render
import random

def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 10))
    password = ''

    for x in range(length):
        if request.GET.get('uppercase'):
            characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        if request.GET.get('numbers'):
            characters.extend(list('0123456789'))
        if request.GET.get('special'):
            characters.extend(list("!#$%&*+,-./:;?@^_`~"))

        password += random.choice(characters)

    context = {
        'password': password
    }
    return render(request, 'generator/password.html', context)
