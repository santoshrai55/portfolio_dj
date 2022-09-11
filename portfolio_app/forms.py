from django import forms
from . models import Project


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project

        fields = "__all__"

        # we can also exclude fields
        # exclude = ['title']
