from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    file = models.FileField()
    image = models.ImageField()
    

    def __str__(self):
        return self.title

    
