from django.shortcuts import render
from django.http import HttpResponse

from .models import Director, Film

# Create your views here.
def hola(request):
    return "Hi from FilmCatalogue"

def index(request):
    num_films = Film.objects.all().count()
    num_directors = Director.objects.all().count()
    
    return render(
        request,
        "index.html",
        context={
            "num_films": num_films,
            "num_directors": num_directors,
        }
    )

def films(request):
    film = Film.objects.all()
    
    return render(
        request,
        "films.html",
        context={'film': film}
        )

def directors(request):
    director = Director.objects.all()

    return render(
        request,
        "directors.html",
        context={'director': director}
    )
