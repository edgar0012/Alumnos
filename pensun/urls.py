from django.conf.urls import url
from . import views


urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^pensun/nueva/$', views.pensun_nueva, name='pensun_nueva'),
    ]
