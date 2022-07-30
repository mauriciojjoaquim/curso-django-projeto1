from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html')


def sobre(requerest):
    return HttpResponse('sobre')


def contato(requerest):
    return HttpResponse('contato')
