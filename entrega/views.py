from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from basedata.models import Contacto

def index(request):
        return render(request, 'index.html')

def contacto(request):
        contacto = Contacto.objects.all()
        context = {'contacto': contacto         }
        return render(request, 'contacto.html', context = context)

# def search_product_view(request):
#     print(request.GET)
#     #product = Products.objects.get()
#     products = Products.objects.filter(name__contains = request.GET['search'])
#     context = {'products':products}
#     return render(request, 'search_product.html', context = context)