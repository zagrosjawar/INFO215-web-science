from django.db import models

# Create your models here.
class Post(models.Model):
    post_title = models.TextField(max_length=50)
    post_content = models.TextField()

    def __str__(self):
        return self.post_title
