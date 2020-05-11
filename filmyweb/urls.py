from django.urls import path, include
from filmyweb.views import all_movies, nowy_film, edytuj_film, usun_film

urlpatterns = [
    path('all/', all_movies, name="all_movies"),
    path('new/', nowy_film, name="nowy_film"),
    path('edit/<int:id>/', edytuj_film, name="edytuj_film"),
    path('del/<int:id>/', usun_film, name="usun_film"),
]
