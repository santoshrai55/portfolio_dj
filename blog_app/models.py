from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    blog_content = models.TextField(max_length=2000)
    blog_image = models.ImageField(
        upload_to='blog_app/images/')
    published_date = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=True)
