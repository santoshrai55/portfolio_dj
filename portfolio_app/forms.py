from django import forms
from . models import Project


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project

        fields = ('title', 'description', 'image',)
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'description': forms.Textarea(attrs={'class': 'form-control'}),
                   'image': forms.FileInput(attrs={'class': 'form-control'}),
                   }
