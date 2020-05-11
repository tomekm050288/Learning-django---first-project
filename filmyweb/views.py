from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from filmyweb.models import Film
from .forms import FilmForm


def all_movies(request):
    all_movies = Film.objects.all()
    return render(request, 'filmy.html', {'filmy': all_movies})


def nowy_film(request):
    form = FilmForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(all_movies)

    return render(request, 'film_form.html', {'form': form})


def edytuj_film(request, id):
    film = get_object_or_404(Film, pk=id)
    form = FilmForm(request.POST or None, request.FILES or None, instance=film)

    if form.is_valid():
        form.save()
        return redirect(all_movies)

    return render(request, 'film_form.html', {'form': form})


def usun_film(request, id):
    film = get_object_or_404(Film, pk=id)

    if request.method == "POST":
        film.delete()
        return redirect(all_movies)

    return render(request, 'confirm.html', {'film': film})





