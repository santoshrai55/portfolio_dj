from django.db import models
from ckeditor.fields import RichTextField


class Project(models.Model):
    title = models.CharField(max_length=100)
    # description = models.CharField(max_length=250)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(
        upload_to='portfolio/images/')  # this requires pillow
    url = models.URLField(blank=True)
