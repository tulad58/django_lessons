from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones_object = Phone.objects.all()
    context = {'phone': phones_object}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    slug_url = get_object_or_404(Phone, slug=slug)
    context = {'slug': slug_url}
    return render(request, template, context)
