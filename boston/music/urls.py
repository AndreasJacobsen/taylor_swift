from django.conf.urls import url
# from . betyr "hent fra denne mappen", altså . betyr denne mappen.
from . import views
# dette er altså index for music. Hver trenger/bør ha en index

urlpatterns = [
    # ingenting betyr at dette er default for music,
    # /music
    url(r'^$', views.index, name='index'),
    # /music/712/, gruppe () kan se etter *alle* album IDene, så kjører vi det-
    # - inn som variable, regexen kjøre for hvert tall, og sjekker om 0-9
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]
