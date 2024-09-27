from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer

class AllVideos(APIView):
    def get(self, request):
        videos = Video.objects.all()
        video_serializer = VideoSerializer(videos, many=True)

        return Response({
            'videos': video_serializer.data,
        })
