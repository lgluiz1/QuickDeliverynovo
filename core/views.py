from django.shortcuts import render, redirect
# Create your views here.

def index(request):
    return render(request, 'core/home.html')

def empresa(request):
    return render(request, 'core/empresa.html')

def unidades(request):
    return render(request, 'core/unidades.html')

def certificados(request):
    return render(request, 'core/certificados.html')

def cod_etica(request):
    return render(request, 'core/cod_etica.html')

def contato(request):
    return render(request, 'core/contato.html')

def servicos(request):
    return render(request, 'core/servicos.html')

