from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Film, ExtraInfo, Review
from .forms import FilmForm, ExtraInfoForm, ReviewForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, FilmSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FilmView(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

# Create your views here.


def all_films(request):
    #filmy = ['Avatar', 'Titanic']

    wszystkie = Film.objects.all()
    return render(request, 'filmy.html', {'filmy': wszystkie})

@login_required
def new_movie(request):
    if_new = True
    form_film = FilmForm(request.POST or None, request.FILES or None)
    form_extra = ExtraInfoForm(request.POST or None)


    if all((form_film.is_valid(), form_extra.is_valid())):
        film = form_film.save(commit=False)
        extra = form_extra.save()
        film.extra = extra
        film.save()
        return redirect(all_films)

    return render(request, 'film_form.html', {'form': form_film,'form_extra': form_extra,'reviews': None, 'form_review': None, 'new': True})

@login_required
def edit_movie(request, id):
    if_new = False
    film = get_object_or_404(Film, pk=id)

    reviews = Review.objects.filter(film=film)


    try:
        extra = ExtraInfo.objects.get(film=film.id)
    except ExtraInfo.DoesNotExist:
        extra = None

    form_film = FilmForm(request.POST or None, request.FILES or None, instance=film)
    form_extra = ExtraInfoForm(request.POST or None, instance=extra)

    form_review = ReviewForm(request.POST or None)

    if request.method == 'POST':
        if 'stars' in request.POST:
            review = form_review.save(commit=True)
            review.film = film
            review.save()

    if all((form_film.is_valid(), form_extra.is_valid())):
        film = form_film.save(commit=False)
        extra = form_extra.save()
        film.extra = extra
        film.save()
        return redirect(all_films)

    return render(request, 'film_form.html', {'form': form_film, 'form_extra': form_extra, 'reviews': reviews, 'form_review': form_review, 'new': False})

@login_required
def delete_movie(request, id):
    film = get_object_or_404(Film, pk=id)

    if request.method == "POST":
        film.delete()
        return redirect(all_films)

    return render(request, 'confirm.html', {'film': film})
