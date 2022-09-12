from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.


class Blog_item(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    # blog_content = models.TextField(max_length=2000)
    blog_content = RichTextField(blank=True, null=True)
    blog_image = models.ImageField(
        upload_to='blog_app/images/')
    published_date = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=True)

    def __str__(self):
        return self.title + ' by ' + str(self.author.first_name)
