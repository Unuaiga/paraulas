from django.urls import include, path
from django.conf.urls import url
from . import views


urlpatterns = [
    url('^grops/lista/?$', views.ListGroup, name="liste_groupes"),
]
