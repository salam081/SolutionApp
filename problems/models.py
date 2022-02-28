from django.db import models
from django.contrib.auth.models import User



class ProblemType(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title

class ProblemLocation(models.Model):
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.location    

class Problem(models.Model):
    app = models.ForeignKey('App', on_delete=models.CASCADE, blank=True, null=True)
    Problem_type = models.ForeignKey(ProblemType, on_delete=models.CASCADE, blank=True, null=True)
    title        = models.ForeignKey('Title', on_delete=models.CASCADE)
    description  = models.TextField(null=True,blank=True)
    attempted     = models.BooleanField(default=False)
    adopted     = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    created_by   = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    location     = models.ForeignKey(ProblemLocation, on_delete=models.CASCADE, blank=True, null=True) 

    def __str__(self):
        return self.title.title
        

class Cause(models.Model):
    Problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    cause = models.TextField(max_length=100)


    def __str__(self):
        return self.cause



class App(models.Model):
    app_name = models.CharField(max_length=50)

    def __str__(self):
        return self.app_name       


class Title(models.Model):
    app   = models.ForeignKey(App, on_delete=models.CASCADE) 
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


        
     