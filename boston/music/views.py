from django.http import Http404
from django.shortcuts import render
from .models import Album


def index(request):
    # all albums lagrer albumene fra databasen i en variabel
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums})


def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist: 
        raise Http404("Album not found, it does not exist in our database.")
    return render(request, 'music/detail.html', {'album': album})