from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
class YouTubeVideo(models.Model):
    title = models.CharField(max_length=200)
    video_id = models.CharField(max_length=20, unique=True, validators=[MinLengthValidator(4)])
    description = models.TextField()
    published_date = models.DateTimeField()
    views = models.PositiveIntegerField()
    likes = models.PositiveIntegerField()
    channel_name = models.CharField(max_length=100)
    channel_id = models.CharField(max_length=20, validators=[MinLengthValidator(4)])
    video_url = models.URLField()

    def __str__(self):
        return self.title


class About(models.Model):
    image = models.ImageField(upload_to='about/')
    title = models.CharField(max_length=155)
    info = models.TextField()


class YouTubeCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name




