from django.shortcuts import get_object_or_404, render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from anime.models import AnimeCategory, Anime
from .serializers import AnimeCategorySerializer, AnimeSerializer


@api_view(["GET", "POST"])
def anime_categories(request):

    query = AnimeCategory.objects.all()
    serializer = AnimeCategorySerializer(query, many=True)
    if serializer.is_valid:
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    


@api_view(["GET", "POST"])
def anime_category(request, slug, pk):
    query = AnimeCategory.objects.filter(pk=pk).filter(slug=slug)
    print(query)
    serializer = AnimeCategorySerializer(query, many=False)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


@api_view(["GET", "POST"])
def anime(request, pk ):
    item = get_object_or_404(Anime, pk=pk)
    serializer = AnimeSerializer(item)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)