from tabnanny import verbose
from rest_framework import serializers

from anime.models import AnimeCategory, Anime

class AnimeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model  = AnimeCategory
        exclude = ["user", "slug"]

        slug = serializers.SlugField(read_only=True, required=False)

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = "__all__"

