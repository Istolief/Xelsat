from django.shortcuts import render
from .models import Product, Category, Brand
# from django.utils import timezone


def product_list(request, top_category='', category='', brand=''):
    # todo: Можно переписать понятнее формировать аргументы отдельно
    if category != '':
        # inner_qs = Category.objects.filter(slug__exact=filter_category)
        # products = Product.objects.filter(category__in=inner_qs)
        if brand == '':
            products = Product.objects.filter(category__slug__exact=category).order_by('title')
        else:
            products = Product.objects.filter(category__slug__exact=category,
                                              brand__slug__exact=brand).order_by('title')

    elif top_category != '':
        if brand == '':
            products = Product.objects.filter(category__owner__slug__exact=top_category).order_by('title')
        else:
            products = Product.objects.filter(category__owner__slug__exact=top_category,
                                              brand__slug__exact=brand).order_by('title')

    elif brand != '':
        products = Product.objects.filter(brand__slug__exact=brand).order_by('title')

    else:
        products = Product.objects.all().order_by('title')

    b = get_brands(products)
    return render(request, 'catalog/catalog_list.html', {
        'products': products,
        'catalog': get_catalog(),
        'brands': b,
    })


def get_catalog():
    # todo: Скорее всего не правильно, запросы в цикле, должна быть возможность получить дерево одним запросом
    qs = Category.objects.filter(owner__id__exact=None)
    category_list = []
    i = 0
    for e in qs:
        i += 1
        category_list.append({
            'iter': i,
            'owner': e.title,
            'items': Category.objects.filter(owner__exact=e).order_by('title'),
        })
    return category_list


def get_brands(products):
    return Brand.objects.filter(id__in=products.values('brand_id').distinct())

