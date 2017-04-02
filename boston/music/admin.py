from django.contrib import admin

# Register your models here.
from .models import Album, Song  # fra denne mappen sin models fil importer
# klassen Album

admin.site.register(Album)
admin.site.register(Song)