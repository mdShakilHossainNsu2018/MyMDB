from django.shortcuts import render
from django.views.generic import (ListView, DetailView)
from .models import Movie, Person

# Create your views here.


class MovieList(ListView):
    model = Movie
    paginate_by = 5


class MovieDetail(DetailView):
    queryset = (Movie.objects.all_with_related_with_person())
    # template_name = 'core/movie_detail.html'


class PersonDetail(DetailView):
    queryset = Person.objects.all_with_prefetch_movie()

