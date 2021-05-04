from django.urls import path #importation de la fonction path de Django
from . import views #importation de toutes les vues de l'application blog

urlpatterns = [
    path('', views.post_list, name='post_list'),
]