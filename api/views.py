from django.shortcuts import render


def menu(request):
    return render(request=request, template_name="menu.html")


def beers(request):
    return render(request=request, template_name="beers.html")
