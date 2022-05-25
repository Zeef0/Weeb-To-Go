from django.urls import path
from .serializers import AnimeCategorySerializer

from . import views

urlpatterns = [
    path('categories/', views.anime_categories, name="anime_categories"),
    path('category/<slug:slug>/<int:pk>', views.anime_category, name="category_anime"),
    path("anime/<int:pk>", views.anime, name="anime")
    ]


import os