from django.shortcuts import render
from django.http import HttpResponse

def user_list(request):
    return render(request, 'index.html')

def producto(request):
    return render(request, 'producto.html')