from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def cadastro(request):
    return HttpResponse("Você está na página de cadastro.")
