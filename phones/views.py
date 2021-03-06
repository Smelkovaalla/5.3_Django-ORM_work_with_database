from django.shortcuts import render, redirect
from phones.models import Phone
from pprint import pprint

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get("sort")
    phones = Phone.objects.all()
    if sort == 'name':
        phones = Phone.objects.order_by('name')
    elif sort == 'min_price':
        phones = Phone.objects.order_by('price')
    elif sort == 'max_price':
        phones = Phone.objects.order_by('-price')
    context = {
        'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)
    context = {
        'phone': phone[0],
    }
    return render(request, template, context)




