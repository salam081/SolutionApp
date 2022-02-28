from django.db import models
from problems.models import Problem
from django.contrib.auth.models import User

class Solution(models.Model):
    problem       = models.ForeignKey(Problem, on_delete=models.CASCADE)
    solution      =    models.TextField(max_length=100, null=False, blank=False)
    data_created =       models.DateTimeField(auto_now_add=True, auto_now=False)
    created_by   = models.ForeignKey(User, on_delete=models.CASCADE)
     
    def __str__(self):
        
        return self.solution



