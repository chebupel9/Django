from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return HttpResponse("<h4>Это страничка о нас</h4>")

