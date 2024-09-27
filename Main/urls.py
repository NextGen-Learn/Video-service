# your_app/urls.py
from django.urls import path
from .views import AllVideos  # Убедитесь, что это правильно

urlpatterns = [
    path('videos/', AllVideos.as_view(), name='all-videos'),
]
