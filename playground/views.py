from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    Dict = {'name': 'Anuj'}
    return render(request, 'hello.html', Dict)