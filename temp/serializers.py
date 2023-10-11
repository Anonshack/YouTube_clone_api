from rest_framework import serializers
from .models import YouTubeCategory


class YouTubeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = YouTubeCategory
        fields = ['id', 'name']

