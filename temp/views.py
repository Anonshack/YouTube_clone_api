from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import YouTubeVideo, About, YouTubeCategory
from .serializers import YouTubeCategorySerializer


class YouTube(APIView):
    def get(self, request):
        try:
            clay = request.GET.get('temp')
            print("clay:", clay)
            if clay:
                add = YouTubeVideo.objects.filter(title__icontains=clay).values()
            else:
                add = YouTubeVideo.objects.all().values()
        except Exception as e:
            print("Error:", e)
            add = YouTubeVideo.objects.all().values()
        return Response({'YouTube': list(add)})

    def delete(self, request, youtube):
        try:
            video = YouTubeVideo.objects.get(pk=youtube)
            video.delete()
            return Response({'res': 'success'})
        except YouTubeVideo.DoesNotExist:
            return Response({'res': 'error', 'message': 'Video not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'res': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'queryset' in self.request.GET:
            q = self.request.GET['queryset']
            sat_q = Q(Q(title__icontains=q) | Q(channel_name__icontains=q) | Q(description__icontains=q))
            queryset = queryset.filter(sat_q)
        return queryset


class AboutViewAPI(APIView):
    def get(self, request):
        try:
            pass_score = request.GET['temp']
            add = About.objects.filter(info__gte=pass_score).values()
        except:
            add = About.objects.all().values()
        return Response({'About': list(add)})

    def delete(self, request):
        try:
            about_id = request.data['about'];
            About.objects.filter(pk=about_id).delete();
            return Response({'res': 'success'})
        except:
            return Response({'res': 'error'})


class YouTubeCategoryList(generics.ListAPIView):
    queryset = YouTubeCategory.objects.all()
    serializer_class = YouTubeCategorySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        # print(serializer.data)
        return Response({'Category': serializer.data})

    def delete(self, request):
        try:
            category = request.data['category'];
            YouTubeCategory.objects.filter(pk=category).delete();
            return Response({'res': 'success'})
        except:
            return Response({'res': 'error'})


