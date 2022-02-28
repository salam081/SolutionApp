from django import forms
from .models import Problem


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        #fields = '__all__'
        exclude = ['adopted','attempted','created_by', 'date_created']

