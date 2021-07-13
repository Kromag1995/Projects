from django import forms
from .models import Project,Chore

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["tittle"]

class ChoreForm(forms.ModelForm):
    class Meta:
        model = Chore
        fields = ["tittle", "text", "done"]