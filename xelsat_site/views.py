from django.shortcuts import render


def main_page(request):
    return render(request, 'xelsat_site/main.html', {})
