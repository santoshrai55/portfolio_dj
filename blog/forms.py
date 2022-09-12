from django import forms
from . models import Blog_item


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog_item
        fields = ('title', 'author', 'blog_content',
                  'blog_image', 'published_date', 'featured')
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'author': forms.Select(attrs={'class': 'form-control'}),
                   'blog_content': forms.Textarea(attrs={'class': 'form-control'}),
                   'blog_image': forms.FileInput(attrs={'class': 'form-control'}),
                   'published_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
                   'featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                   }
