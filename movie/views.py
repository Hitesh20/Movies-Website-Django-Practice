from django.shortcuts import render
from django.http import *
from . models import Movie
from django.shortcuts import render,get_object_or_404
from django.template import loader
def index(request):

    all_movies = Movie.objects.all()
    template = loader.get_template('movie/index.html')
    context = {'all_movies' : all_movies}
    return HttpResponse(template.render(context,request))
    '''
    return HttpResponse("This is the list of all movies")
    '''
def detail(request,movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    context = {'movies' : movie}
    return render(request, 'movie/detail.html', context)
def about(request):
    return render(request, 'movie/about.html')