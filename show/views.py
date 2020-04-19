from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from show.models import MovieInfo
import datetime

from show.reptile import get_top100


def index(request):
    # return HttpResponse(u"欢迎光临!")
    return render(request, 'index.html')


def chart(request):
    # return HttpResponse(u"欢迎光临!")
    return render(request, 'chart.html')


def demo(request):
    # return HttpResponse(u"欢迎光临!")
    return render(request, 'demo.html')


def datatable(request):
    # return HttpResponse(u"欢迎光临!")
    dataset = MovieInfo.objects.all()
    for data in dataset:
        directors_str = data.directors.replace('\'', '').replace('[', '').replace(']', '')
        data.directors_str = directors_str
        actors_str = data.actors.replace('\'', '').replace('[', '').replace(']', '')
        data.actors_str = actors_str
        types_str = data.types.replace('\'', '').replace('[', '').replace(']', '')
        data.types_str = types_str
    return render(request, 'datatable.html', {'dataset': dataset})


def refresh_movie_info(request):
    results = get_top100()
    MovieInfo.objects.all().delete()
    for movie in results:
        m = MovieInfo(movie_id=movie['movie_id'], title=movie['title'], rate=movie['rate'],
                      movie_url=movie['movie_url'], cover_url=movie['cover_url'], cover_x=movie['cover_x'],
                      cover_y=movie['cover_y'], directors=movie['directors'], actors=movie['actors'],
                      duration=movie['duration'], region=movie['region'], types=movie['types'],
                      release_year=movie['release_year'], create_time=datetime.datetime.now())
        m.save()
    return HttpResponse(u"成功!")
