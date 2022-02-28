from django import forms
from .models import Solution


class SolutionForm(forms.ModelForm):
    class Meta:
        model = Solution
        exclude = ['created_by','date_created']
       
