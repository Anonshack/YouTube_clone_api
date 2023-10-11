from django.contrib import admin
from .models import YouTubeVideo, About, YouTubeCategory
# Register your models here.

a = [YouTubeVideo, About, YouTubeCategory]
for i in a:
    admin.site.register(i)