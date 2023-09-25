from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones_object = Phone.objects.all()
    if request.GET:
        if request.GET.get('sort') == 'name':
            phones_object = Phone.objects.order_by('name').all()
        if request.GET.get('sort') == 'min_price':
            phones_object = Phone.objects.order_by('price').all()
        if request.GET.get('sort') == 'max_price':
            phones_object = Phone.objects.order_by('-price').all()
    context = {'phones': phones_object}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones_object = Phone.objects.get(slug=slug)
    context = {'phone': phones_object}
    return render(request, template, context)
