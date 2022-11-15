from api.views import menu, beers
from django.urls import path

urlpatterns = [
    path("", menu),
    path("beers.html", beers)
]
