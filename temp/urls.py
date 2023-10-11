from django.urls import path
from .views import YouTube, AboutViewAPI, YouTubeCategoryList

urlpatterns = [
    path('about/', AboutViewAPI.as_view(), name='about'),
    path('category/', YouTubeCategoryList.as_view(), name='youtube-categories'),
    path('api/', YouTube.as_view(), name='api'),
]