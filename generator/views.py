from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    passwordLength = int(request.GET.get('length', 12)) #12 is the default value

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!"#$%&\'()*+,-./:;<=>?@[]^_`{|}~'))
    if request.GET.get('special'):
        characters.extend(list('0123456789'))

    userpassword = ''
    for x in range(passwordLength):
        userpassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': userpassword})

def about(request):
    return render(request, 'generator/about.html')