from django.db import models

class Video(models.Model):
    id = models.AutoField(primary_key=True)  
    user = models.IntegerField(blank=False)
    views_count = models.IntegerField(default=0)
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/',blank=False)
    description = models.TextField(blank=True, null=True)  
    duration = models.PositiveIntegerField()  
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
