from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ReportType(models.Model):
    title = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = True, auto_now=False)
    def __str__(self):
        return str(self.title)

class SubUnitReport(models.Model):
    report_type = models.ForeignKey(ReportType, on_delete=models.CASCADE)
    introductions = models.TextField(null=True)
    achievement = models.TextField(null=True)
    challenge =  models.TextField(null=True)
    conclusion =  models.TextField(null=True)
    date_from = models.DateField(auto_now_add = False, auto_now=False)
    date_to = models.DateField(auto_now_add = False, auto_now=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add = True, auto_now=False)

    def __str__(self):
        return str(self.report_type)

class UpdatedSubUnitReport(models.Model):
    subUnitReport = models.ForeignKey(SubUnitReport, on_delete=models.CASCADE)
    report_type = models.ForeignKey(ReportType, on_delete=models.CASCADE)
    introductions = models.TextField(null=True)
    achievement = models.TextField(null=True)
    challenge =  models.TextField(null=True)
    conclusion =  models.TextField(null=True)
    edited_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now_add = True, auto_now=False)

    def __str__(self):
        return str(self.report_type)
